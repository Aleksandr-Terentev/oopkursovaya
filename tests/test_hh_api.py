from src.hh_api import HH


def test_head_hunter_api_requests():
    obj_api = HH()
    assert type(obj_api) is HH
