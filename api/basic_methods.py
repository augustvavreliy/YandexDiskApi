import requests

class Api:

    _HEADERS = {
        'Content-Type': 'application/json',
        'Authorization': 'y0_AgAAAABwPgDVAADLWwAAAADq1--KHehQUwmFTfyyrfteNuEn4VmYf7I'
    }
    token = {'trainer_token':'9bd189a8403bc75b51d64f3e84e73754'}

    def __init__(self):
        '''
        Initialization
        '''
        self.response = None
        self.url = 'https://cloud-api.yandex.net'

    def get(self, url: str, params: dict = None):
        '''
        Basic GET-request
            :param url:
            :param params:
            :return:
        '''
        

        self.response = requests.get(url=url,
                                     params=params,
                                     headers=self._HEADERS)
        return self

    def status_code_should_be(self, expected_code: int):

        """
        Checking the status code
            :param expected_code:
            :return:
        """

        actual_code = self.response.status_code
        assert expected_code == actual_code, f'\nОжидаемый статус-код: {expected_code} ' \
                                             f'\nФактический статус-код: {actual_code}'
        return self

