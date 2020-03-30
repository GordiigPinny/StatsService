from TestUtils.models import BaseTestCase
from AwardsStats.models import AchievementStats, PinPurchaseStats


class PinPurchasesStatsListTestCase(BaseTestCase):
    """
    Тесты для /pin_purchases/
    """
    def setUp(self):
        super().setUp()
        self.path = self.url_prefix + 'pin_purchases/'
        self.stat = PinPurchaseStats.objects.create(pin_id=1, user_id=1, purchase_dt='2020-03-01T12:12:12Z')
        self.data_201 = {
            'user_id': 1,
            'pin_id': 1,
            'purchase_dt': '2020-03-12T13:00:01Z',
        }
        self.data_400_1 = {
            'user_id': 1,
        }
        self.data_400_2 = {
            'user_id': 1,
            'pin_id': 1,
            'purchase_dt': '2020/03/12 13:00:01',
        }

    def testGet200_OK(self):
        response = self.get_response_and_check_status(url=self.path)
        self.list_test(response, PinPurchaseStats)

    def testGet200_WithQueryParams(self):
        response = self.get_response_and_check_status(url=self.path +
                                                      f'?user_id={self.stat.user_id}&pin_id={self.stat.pin_id}')
        self.assertEqual(len(response), 1, msg='No instance in response')

    def testGet200_EmptyWithQueryParams(self):
        response = self.get_response_and_check_status(url=self.path + f'?user_id={self.stat.user_id+1000}')
        self.assertEqual(len(response), 0, msg='Instance in response')
        response = self.get_response_and_check_status(url=self.path + f'?pin_id={self.stat.pin_id+1000}')
        self.assertEqual(len(response), 0, msg='Instance in response')

    def testPost201_OK(self):
        _ = self.post_response_and_check_status(url=self.path, data=self.data_201)

    def testPost400_WrongJSON(self):
        _ = self.post_response_and_check_status(url=self.path, data=self.data_400_1, expected_status_code=400)

    def testPost400_WrongDTFormat(self):
        _ = self.post_response_and_check_status(url=self.path, data=self.data_400_2, expected_status_code=400)


class PinPurchasesStatsTestCase(BaseTestCase):
    """
    Тесты для /pin_purchases/<pk>/
    """
    def setUp(self):
        super().setUp()
        self.stat = PinPurchaseStats.objects.create(pin_id=1, user_id=1, purchase_dt='2020-03-01T12:12:12Z')
        self.path = self.url_prefix + f'pin_purchases/{self.stat.id}/'
        self.path_404 = self.url_prefix + f'pin_purchases/{self.stat.id + 1000}/'

    def testGet200_OK(self):
        _ = self.get_response_and_check_status(url=self.path)

    def testGet404_WrongId(self):
        _ = self.get_response_and_check_status(url=self.path_404, expected_status_code=404)


class AchievementsStatsListTestCase(BaseTestCase):
    """
    Тесты для /achievements/
    """
    def setUp(self):
        super().setUp()
        self.path = self.url_prefix + 'achievements/'
        self.stat = AchievementStats.objects.create(achievement_id=1, user_id=1, achievement_dt='2020-03-01T12:12:12Z')
        self.data_201 = {
            'user_id': 1,
            'achievement_id': 1,
            'achievement_dt': '2020-03-12T13:00:01Z',
        }
        self.data_400_1 = {
            'user_id': 1,
        }
        self.data_400_2 = {
            'user_id': 1,
            'achievement_id': 1,
            'achievement_dt': '2020/03/12 13:00:01',
        }

    def testGet200_OK(self):
        response = self.get_response_and_check_status(url=self.path)
        self.list_test(response, AchievementStats)

    def testGet200_WithQueryParams(self):
        response = self.get_response_and_check_status(url=self.path +
                                                      f'?user_id={self.stat.user_id}&achievement_id={self.stat.achievement_id}')
        self.assertEqual(len(response), 1, msg='No instance in response')

    def testGet200_EmptyWithQueryParams(self):
        response = self.get_response_and_check_status(url=self.path + f'?user_id={self.stat.user_id+1000}')
        self.assertEqual(len(response), 0, msg='Instance in response')
        response = self.get_response_and_check_status(url=self.path + f'?achievement_id={self.stat.achievement_id+1000}')
        self.assertEqual(len(response), 0, msg='Instance in response')

    def testPost201_OK(self):
        _ = self.post_response_and_check_status(url=self.path, data=self.data_201)

    def testPost400_WrongJSON(self):
        _ = self.post_response_and_check_status(url=self.path, data=self.data_400_1, expected_status_code=400)

    def testPost400_WrongDTFormat(self):
        _ = self.post_response_and_check_status(url=self.path, data=self.data_400_2, expected_status_code=400)


class AchievementStatsTestCase(BaseTestCase):
    """
    Тесты для /achievements/<pk>/
    """
    def setUp(self):
        super().setUp()
        self.stat = AchievementStats.objects.create(achievement_id=1, user_id=1, achievement_dt='2020-03-01T12:12:12Z')
        self.path = self.url_prefix + f'achievements/{self.stat.id}/'
        self.path_404 = self.url_prefix + f'achievements/{self.stat.id + 1000}/'

    def testGet200_OK(self):
        _ = self.get_response_and_check_status(url=self.path)

    def testGet404_WrongId(self):
        _ = self.get_response_and_check_status(url=self.path_404, expected_status_code=404)

