from TestUtils.models import BaseTestCase
from RequestStats.models import RequestsStats


class RequestsStatsListTestCase(BaseTestCase):
    """
    Тесты для /requests/
    """
    def setUp(self):
        super().setUp()
        self.token.set_role(self.token.ROLES.SUPERUSER)
        self.path = self.url_prefix + 'requests/'
        self.request_stat = RequestsStats.objects.create(method='GET', endpoint='ee', user_id=1, process_time=10,
                                                         status_code=200, request_dt='2020-03-12T14:15Z')
        self.data_201_1 = {
            'method': 'GET',
            'user_id': 1,
            'endpoint': '/places/',
            'status_code': 200,
            'process_time': 100,
            'request_dt': '2020-03-12T14:15Z',
        }
        self.data_201_2 = {
            'method': 'GET',
            'user_id': None,
            'endpoint': '/places/',
            'status_code': 200,
            'process_time': 100,
            'request_dt': '2020-03-12T14:15Z',
        }
        self.data_400_1 = {
            'method': 'GET',
        }
        self.data_400_2 = {
            'method': 'WRONG',
            'user_id': 1,
            'endpoint': '/places/',
            'status_code': 200,
            'process_time': 100,
            'request_dt': '2020-03-12T14:15Z',
        }
        self.data_400_3 = {
            'method': 'GET',
            'user_id': 1,
            'endpoint': '/places/',
            'status_code': 200,
            'process_time': 100,
            'request_dt': '2020-03-12 14:15 ',
        }

    def testGet200_OK(self):
        response = self.get_response_and_check_status(url=self.path)
        self.list_test(response, RequestsStats)

    def testGet200_WithUserIdQueryParam(self):
        response = self.get_response_and_check_status(url=self.path + f'?user_id={self.request_stat.user_id}')
        self.assertEqual(len(response), 1, msg='No instance in response')

    def testGet200_EmptyWithUserIdQueryParam(self):
        response = self.get_response_and_check_status(url=self.path + f'?user_id={self.request_stat.user_id+1000}')
        self.assertEqual(len(response), 0, msg='Instance in response')

    def testGet401_403_NotSuperuser(self):
        self.token.set_role(self.token.ROLES.USER)
        response = self.get_response_and_check_status(url=self.path, expected_status_code=[401, 403])

    def testPost201_OKRegistered(self):
        _ = self.post_response_and_check_status(url=self.path, data=self.data_201_1)

    def testPost201_OKAnon(self):
        _ = self.post_response_and_check_status(url=self.path, data=self.data_201_2)

    def testPost400_WrongJSON(self):
        _ = self.post_response_and_check_status(url=self.path, data=self.data_400_1, expected_status_code=400)

    def testPost400_WrongMethod(self):
        _ = self.post_response_and_check_status(url=self.path, data=self.data_400_2, expected_status_code=400)

    def testPost400_WrongDTFormat(self):
        _ = self.post_response_and_check_status(url=self.path, data=self.data_400_3, expected_status_code=400)

    def testPost401_403_WrongAppToken(self):
        self.token.set_error(self.token.ERRORS_KEYS.APP_AUTH, self.token.ERRORS.BAD_CODE_403_TOKEN)
        _ = self.post_response_and_check_status(url=self.path, data=self.data_201_1, expected_status_code=[401, 403])

    def testPost401_403_ErrorOnAuthService(self):
        self.token.set_error(self.token.ERRORS_KEYS.APP_AUTH, self.token.ERRORS.ERROR_TOKEN)
        _ = self.post_response_and_check_status(url=self.path, data=self.data_201_1, expected_status_code=[401, 403])


class RequestsStatsTestCase(BaseTestCase):
    """
    Тесты для /requests/<pk>/
    """
    def setUp(self):
        super().setUp()
        self.token.set_role(self.token.ROLES.SUPERUSER)
        self.request_stat = RequestsStats.objects.create(method='GET', endpoint='ee', user_id=1, process_time=10,
                                                         status_code=200, request_dt='2020-03-12T14:15Z')
        self.path = self.url_prefix + f'requests/{self.request_stat.id}/'
        self.path_404 = self.url_prefix + f'requests/{self.request_stat.id+10000}/'

    def testGet200_OK(self):
        _ = self.get_response_and_check_status(url=self.path)

    def testGet401_403_NotSuperuser(self):
        self.token.set_role(self.token.ROLES.USER)
        response = self.get_response_and_check_status(url=self.path, expected_status_code=[401, 403])

    def testGet404_WrongId(self):
        _ = self.get_response_and_check_status(url=self.path_404, expected_status_code=404)
