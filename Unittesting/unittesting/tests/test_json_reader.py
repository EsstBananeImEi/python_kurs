import nose
from mock import patch

from Unittesting.unittesting.code.json_reader import JsonReader, JsonError


class TestJsonMock(object):

    def test__init__(self):
        # Arrange
        json_mock = JsonReader
        path = "$test_path$"

        # Act
        rtv = json_mock(path)

        # Assert
        assert rtv._path == path

    def test_get_return(self):
        # Arrange
        json_mock = JsonReader
        path = "$test_path$"
        expected_result = {"key", "value"}

        # Act
        with patch.object(JsonReader, "_get_json", return_value=expected_result):
            rtv = json_mock(path).get()

            # Assert
            assert rtv == expected_result

    def test_get_exception(self):
        # Arrange
        json_mock = JsonReader
        path = "$test_path$"
        expected_result = {"key", "value"}

        # Act
        # Assert
        with patch.object(JsonReader, "_get_json", return_value=None):
            with nose.tools.assert_raises(JsonError):
                json_mock(path).get()
