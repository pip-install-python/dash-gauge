import os as _os
import json as _json
import dash as _dash
import sys as _sys
from ._imports_ import *
from ._imports_ import __all__

from typing import Any, Dict, List, Tuple, Union

_basepath = _os.path.dirname(__file__)
_filepath = _os.path.abspath(_os.path.join(_basepath, 'package-info.json'))
with open(_filepath) as file:
    package = _json.load(file)

package_name = package['name'].replace(' ', '_').replace('-', '_')
__version__ = package['version']

# Get the paths for the component bundles
_current_path = _os.path.dirname(_os.path.abspath(__file__))
_this_module = _sys.modules[__name__]

_js_dist = [
    {
        "relative_package_path": "dash_gauge.min.js",
        "external_url": f"https://unpkg.com/{package_name}@{__version__}/dash_gauge/dash_gauge.min.js",
        "namespace": package_name
    },
    {
        "relative_package_path": "dash_gauge.min.js.map",
        "external_url": f"https://unpkg.com/{package_name}@{__version__}/dash_gauge/dash_gauge.min.js.map",
        "namespace": package_name,
        "dynamic": True
    },
    {
        "relative_package_path": "proptypes.js",
        "namespace": package_name,
        "dev_package_path": "proptypes.js"
    }
]

_css_dist: List = []

for _component in __all__:
    setattr(locals()[_component], '_js_dist', _js_dist)
    setattr(locals()[_component], '_css_dist', _css_dist)