import pytest
import pydantic

from vkf.auth import parse_auth_response


def test_parse_success():
    path = "/?access_token=vk1.a.XXXX&expires_in=86400&user_id=1"
    data = parse_auth_response(path)

    assert data.access_token == "vk1.a.XXXX"
    assert data.expires_in == 86400
    assert data.user_id == 1


def test_parse_no_access_token():
    path = "/?expires_in=86400&user_id=1"

    with pytest.raises(pydantic.ValidationError):
        parse_auth_response(path)
