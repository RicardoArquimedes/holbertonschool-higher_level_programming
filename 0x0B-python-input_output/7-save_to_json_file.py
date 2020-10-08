#!/usr/bin/python3
"""Module that coverte a object-python to str-JSON in a
   jsonfile
"""


import json


def save_to_json_file(my_obj, filename):
        """Function that save to json file
        Args:
            my_obj ([type]): object-python
            filename ([type]): name of jsonfile
        """
        with open(filename, mode='w') as my_fileJSON:
                json.dump(my_obj, my_fileJSON)
