from lib.time_error import TimeError
from unittest.mock import Mock

def test_get_server_time_calls_to_api_to_provide_unixtime_then_error_returns_difference_in_time():
    requester_mock = Mock(name='requester')
    response_mock = Mock(name='response')
    time_mock = Mock()

    time_mock.time.return_value = 1690968962
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"unixtime":1690921762,}
    
    time_error = TimeError(requester_mock, time_mock)
    result = time_error._get_server_time()
    assert result == 1690921762

    result = time_error.error()
    assert result == (1690921762 - 1690968962)