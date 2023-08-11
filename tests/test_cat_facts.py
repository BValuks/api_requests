from lib.cat_facts import CatFacts
from unittest.mock import Mock

def test_provide_mothod_returns_formatted_string_using_info_from_api():
    mock_requester = Mock()
    # mock_response = Mock()
    # mock_requester.get.return_value = mock_response
    # mock_response.json.return_value = {"fact":"The ancestor of all domestic cats is the African Wild Cat which still exists today."}
    mock_requester.get.return_value.json.return_value = {"fact":"The ancestor of all domestic cats is the African Wild Cat which still exists today."}

    cat_fact = CatFacts(mock_requester)
    result = cat_fact.provide()
    assert result == "Cat fact: The ancestor of all domestic cats is the African Wild Cat which still exists today."