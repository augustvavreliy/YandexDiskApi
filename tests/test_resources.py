import pytest


class TestGetRecourses():

    def test_get_resources(self, resources_api):
        response = resources_api.get_resources(path='/', fields='_embedded.items.name, _embedded.items.type')
        assert response.status_code_should_be(200)
        print(response.response.json().get('_embedded').get('items'))
