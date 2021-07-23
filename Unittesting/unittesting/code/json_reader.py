import json


class JsonError(Exception):
    pass


class JsonReader(object):

    def __init__(self, path):
        self._path = path

    def get(self):
        return_value = self._get_json()
        if return_value is not None:
            return return_value
        else:
            raise JsonError()

    def _get_json(self):
        with open(self._path, "r") as json_file:
            return json.load(json_file)
