from TestUtils.models import BaseTestCase
from Stats.models import RequestsStats


class RequestsStatsListTestCase(BaseTestCase):
    """
    Тесты для /requests/
    """
    def setUp(self):
        super().setUp()
        self.path = self.url_prefix + 'requests/'
        self.request_stat = RequestsStats.objects.create(method='GET', endpoint='ee', user_id=1, gateway_process_time=10,
                                                         status_code=200, cb_end_state='CLOSED', cb_start_state='CLOSED',
                                                         is_fully_processed=True, queue_length=True)
        self.data_201_1 = {
            'method': 'GET',
            'user_id': 1,
            'endpoint': '/places/',
            'gateway_process_time': 10,
            'status_code': 200,
            'is_fully_processed': True,
            'cb_start_state': 'CLOSED',
            'cb_end_state': 'CLOSED',
            'queue_length': 0,
        }
        self.data_201_2 = {
            'method': 'GET',
            'user_id': 1,
            'endpoint': '/places/',
            'gateway_process_time': 10,
            'status_code': 200,
            'is_fully_processed': True,
            'cb_start_state': 'CLOSED',
            'cb_end_state': 'CLOSED',
            'queue_length': 0,
        }
        self.data_400_1 = {
            'method': 'GET',
        }
        self.data_400_2 = {
            'method': 'WRONG',
            'user_id': 1,
            'endpoint': '/places/',
            'gateway_process_time': 10,
            'status_code': 200,
            'is_fully_processed': True,
            'cb_start_state': 'CLOSED',
            'cb_end_state': 'CLOSED',
            'queue_length': 0,
        }
        self.data_400_3 = {
            'method': 'GET',
            'user_id': 1,
            'endpoint': '/places/',
            'gateway_process_time': 10,
            'status_code': 200,
            'is_fully_processed': True,
            'cb_start_state': 'WRONG',
            'cb_end_state': 'WRONG',
            'queue_length': 0,
        }

    def testGet200_OK(self):
        response = self.get_response_and_check_status(url=self.path)
        self.list_test(response, RequestsStats)

    def testPost201_OKRegistered(self):
        _ = self.post_response_and_check_status(url=self.path, data=self.data_201_1)

    def testPost201_OKAnon(self):
        _ = self.post_response_and_check_status(url=self.path, data=self.data_201_1)

    def testPost400_WrongJSON(self):
        _ = self.post_response_and_check_status(url=self.path, data=self.data_400_1, expected_status_code=400)

    def testPost400_WrongMethod(self):
        _ = self.post_response_and_check_status(url=self.path, data=self.data_400_2, expected_status_code=400)

    def testPost400_WrongCBState(self):
        _ = self.post_response_and_check_status(url=self.path, data=self.data_400_3, expected_status_code=400)


class RequestsStatsTestCase(BaseTestCase):
    """
    Тесты для /requests/<pk>/
    """
    def setUp(self):
        super().setUp()
        self.request_stat = RequestsStats.objects.create(method='GET', endpoint='ee', user_id=1, gateway_process_time=10,
                                                         status_code=200, cb_end_state='CLOSED', cb_start_state='CLOSED',
                                                         is_fully_processed=True, queue_length=True)
        self.path = self.url_prefix + f'requests/{self.request_stat.id}/'
        self.path_404 = self.url_prefix + f'requests/{self.request_stat.id+10000}/'

    def testGet200_OK(self):
        _ = self.get_response_and_check_status(url=self.path)

    def testGet404_WrongId(self):
        _ = self.get_response_and_check_status(url=self.path_404, expected_status_code=404)
