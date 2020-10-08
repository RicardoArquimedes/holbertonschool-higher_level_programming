#!/usr/bin/python3
"""Module that coverte a str-JSON form
   jsonfile to object-python
Returns:
    [type]: object-python
"""


import json


def load_from_json_file(filename):
        """Function that load from joson file
        Args:
            filename ([type]): [description]
        """

        with open(filename,) as aJsonFile:
                return json.load(aJsonFile)
