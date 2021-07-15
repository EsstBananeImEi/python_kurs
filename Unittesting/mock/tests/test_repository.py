from unittest.mock import patch

import mock

from Unittesting.mock.code.repository import Repository

mock_db_connection = mock.Mock()


class TestRepository(object):

    def connect_db_mock(self):
        self._connection = MockConnection()

    def test__init__(self):
        repo = Repository("$test$")
        rtv = repo._connection_str
        assert rtv == "$test$"

    def test__enter__called__connect_db(self):
        # arrange
        with patch.object(Repository, "_connect_db") as mock_connect_db, \
                patch.object(Repository, "_disconnect_db"):
            # act
            repo = Repository
            repo._connection = mock.Mock()

            # assert
            with Repository("$test$"):
                mock_connect_db.assert_called()

    def test__enter__called__return(self):
        # arrange
        with patch.object(Repository, "_connect_db"), \
                patch.object(Repository, "_disconnect_db"):
            # act
            repo = Repository("$test$")
            repo._connection = mock.Mock()

            # assert
            with repo as test_repo:
                rtv = test_repo
                assert rtv == repo

    def test__exit__called__disconnect_db(self):
        # arrange
        with patch.object(Repository, "_connect_db"), \
                patch.object(Repository, "_disconnect_db") as mock_disconnect:
            # act
            repo = Repository
            with repo("$test$"):
                pass

            # assert
            mock_disconnect.assert_called()

    def test__exit__(self):
        # arrange
        with patch.object(Repository, "_connect_db"), \
                patch.object(Repository, "_close_connection") as pyodbc_close:
            # act
            repo = Repository
            with repo("$test$"):
                pass

            # assert
            pyodbc_close.assert_called()

    @patch('Unittesting.mock.code.repository.SqlRepository._connect_db', side_effect=connect_db_mock)
    def test_execute_query(self, connect_db_mock):
        with patch("Unittesting.mock.code.repository.SqlRepository._connect_db.execute"):
            repo = Repository("$conn_strin$g")
            repo._connect_db(repo)

            query_result = ('', '')
            repo._connection.set_query_result(query_result)
            result = repo.get_data("$test_query$")

            assert result.fetchone() == query_result


class MockConnection():
    execute_was_called = False
    sql_query = ''
    params = None
    commit_was_called = False

    def __init__(self):
        self.result = None

    def set_query_result(self, result):
        self.result = result

    def cursor(self):
        return MockCursor(self.result)

    def execute(self, query, *args):
        return None

    def commit(self):
        self.commit_was_called = True


class MockCursor():
    def __init__(self, result):
        self.result_query = result

    def execute(self, query, *args):
        return None

    def fetchone(self):
        return self.result_query

    def fetchall(self):
        return self.result_query
