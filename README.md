# libsimba.py-platform

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/SIMBAChain/libsimba.py-platform/main?filepath=notebooks%2Fexamples.ipynb)


libsimba.py-platform is a library simplifying the use of SIMBAChain SEP APIs. 

We aim to abstract away the various blockchain concepts, reducing the necessary time needed to get to working code.

### [🏠 Homepage](https://github.com/SIMBAChain/libsimba.py-platform)
### [📝 Documentation](https://simbachain.github.io/libsimba.py-platform/)

## Install

Just needs python >=3.7

The rest can be installed into a virtualenv with :

### Install - from PyPI

	pip install libsimba.py-platform

## Usage

The main imports required are `from libsimba.simba import Simba`:

and can be used similar to:

```python
from libsimba.simba import Simba
import logging
log = logging.getLogger(__name__)

BASE_API_URL = '<https://your.SEP.install.url.com>'
TEST_APP = '<Your App Name>'
TEST_CONTRACT = '<Your Contract Name>'

TEST_METHOD = '<Contract Method Name'

TEST_INPUTS = {
    'A_METHOD_PARAMETER': 'A parameter value'
}

simba = Simba(BASE_API_URL)
contract = simba.get_contract(TEST_APP, TEST_CONTRACT)
log.info('{} :: {} :: {}'.format(BASE_API_URL, TEST_APP, TEST_CONTRACT))

r = contract.submit_method(TEST_METHOD, TEST_INPUTS)
log.info(r.text)
assert (r.status_code >= 200 and r.status_code <= 299)
log.info(r.json())

r = contract.query_method(TEST_METHOD)
assert (r.status_code >= 200 and r.status_code <= 299)
log.info(r.json())
```

## Examples

See [here](https://github.com/SIMBAChain/PyLibSIMBA/blob/master/tests/examples.py)

## Contributing

Contributions, issues and feature requests are welcome!

Feel free to check [issues page](https://github.com/SIMBAChain/PyLibSIMBA/issues).

## License

Copyright © 2021 [SIMBAChain Inc](https://simbachain.com/).

This project is [MIT](https://github.com/SIMBAChain/PyLibSIMBA/blob/master/LICENSE) licensed.

## Appendix

### Makefile

Calling *make github* puts the Sphinx documentation into ./docs so the github pages can find it.

		
### Install - from package

	pip install dist/libsimba.py-platform-0.1.1.dev6.tar.gz

### Install - for development

    poetry install
    poetry update
   
    
## Change log

### v0.1.4
* Enable local_settings to override settings

### v0.1.3
* Fix for file submission

### v0.1.2
* Public release

### v0.1.0 - v0.1.6
* Initial release and bugfixes

