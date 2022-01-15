import keyword
# to avoid param and method name collision with python keywords
paramKeywordConversion = {kw: f'{kw}Param' for kw in keyword.kwlist}
methodKeyWordConversion = {kw: f'{kw}Method' for kw in keyword.kwlist}
