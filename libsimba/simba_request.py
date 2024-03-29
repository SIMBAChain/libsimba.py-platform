import httpx
import json
from typing import Optional
import requests
from httpx import InvalidURL, ConnectError, ProtocolError, RequestError, Response
from libsimba.utils import build_url
from libsimba.settings import BASE_API_URL
from libsimba.decorators import auth_required
from libsimba.exceptions import (
    SimbaRequestException,
    SimbaInvalidURLException,
    LibSimbaException,
)


class SimbaRequest:
    base_api_url = BASE_API_URL

    def __init__(self, endpoint: str, query_params: dict, method: str = "get"):
        self.endpoint = endpoint
        self.query_params = query_params or {}
        self.method = method.lower()
        self._response = None
        self._json_response = None

    @property
    def url(self):
        if self.endpoint is None:
            raise SimbaInvalidURLException(
                message="SimbaRequest object has no target endpoint"
            )
        else:
            return build_url(
                SimbaRequest.base_api_url, self.endpoint, self.query_params
            )

    @property
    def response(self):
        return self._response

    @property
    def json_response(self):
        return self._json_response

    @auth_required
    def send_sync(
        self,
        headers: dict,
        json_payload: Optional[dict] = None,
        files: dict = None,
        fetch_all: Optional[bool] = True,
    ):
        if self.method == "get":
            response = httpx.get(self.url, headers=headers, follow_redirects=True)
            return self._process_response_sync(response, headers, fetch_all)
        elif self.method == "post":
            json_payload = json_payload or {}
            # data = {key: json.dumps(json_payload[key]) for key in json_payload}
            if files is not None:
                data = {key: json.dumps(json_payload[key]) for key in json_payload}
                response = requests.post(
                    self.url,
                    headers=headers,
                    data=data,
                    files=files,
                    allow_redirects=True,
                )
            else:
                headers.update({"content-type": "application/json"})
                response = httpx.post(
                    self.url,
                    headers=headers,
                    data=json_payload,
                    follow_redirects=True,
                )
            return self._process_response_sync(response, headers)

    @auth_required
    async def send(
        self,
        headers: dict,
        json_payload: Optional[dict] = None,
        files: dict = None,
        fetch_all: Optional[bool] = True,
    ):
        async with httpx.AsyncClient() as async_client:
            if self.method == "get":
                response = await async_client.get(
                    self.url, headers=headers, follow_redirects=True
                )
                return await self._process_response(
                    async_client, response, headers, fetch_all
                )
            elif self.method == "post":
                json_payload = json_payload or {}
                if files is not None:
                    data = {key: json.dumps(json_payload[key]) for key in json_payload}
                    response = await async_client.post(
                        self.url,
                        headers=headers,
                        data=data,
                        follow_redirects=True,
                        files=files,
                    )
                else:
                    headers.update({"content-type": "application/json"})
                    response = await async_client.post(
                        self.url,
                        headers=headers,
                        data=json_payload,
                        follow_redirects=True,
                    )
                return await self._process_response(
                    async_client, response, headers
                )

    def _process_response_sync(
        self, response: Response, headers: dict, fetch_all: Optional[bool] = False
    ):
        json_response = self._json_response_or_raise(response)
        if fetch_all:
            json_response = self._fetch_all_sync(json_response, headers)
        self._json_response = json_response
        return json_response

    async def _process_response(
        self,
        client: httpx.AsyncClient,
        response: Response,
        headers: dict,
        fetch_all: Optional[bool] = False,
    ):
        json_response = self._json_response_or_raise(response)
        if fetch_all:
            json_response = await self._fetch_all(json_response, headers, client)
        self._json_response = json_response
        return json_response

    def _json_response_or_raise(self, response: Response):
        try:
            self._response = response
            response.raise_for_status()
            json_response = response.json()
        except (InvalidURL, ConnectError, ProtocolError, ValueError) as e:
            raise SimbaInvalidURLException(str(e))
        except (RequestError) as e:
            raise SimbaRequestException(str(e))
        except Exception as e:
            raise LibSimbaException(message=str(e))
        return json_response

    def _fetch_all_sync(self, json_response: dict, headers: dict):
        if not json_response.get("results"):
            return json_response

        results = json_response.get("results")
        next_page_url = json_response.get("next")

        while next_page_url is not None:
            r = requests.get(next_page_url, headers=headers, allow_redirects=True)
            json_response = r.json()
            results += json_response.get("results")
            next_page_url = json_response.get("next")

        return results

    async def _fetch_all(
        self, json_response: dict, headers: dict, client: httpx.AsyncClient
    ):
        if not json_response.get("results"):
            return json_response

        results = json_response.get("results")
        next_page_url = json_response.get("next")

        while next_page_url is not None:
            r = await client.get(next_page_url, headers=headers, follow_redirects=True)
            json_response = r.json()
            results += json_response.get("results")
            next_page_url = json_response.get("next")

        return results
