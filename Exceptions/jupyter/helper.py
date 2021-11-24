class DataObject():
    is_valid = False


class SqlConnection:

    def connect(self):
        raise ConnectionAbortedError

    def get_data(self):
        return {"name": "Sarah", "surname": "Müller"}


def im_running():
    print("Wohoo i am running")


def get_backend_json_data():
    return {}
