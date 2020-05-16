from TestUtils.models import BaseTestCase
from PlacesStats.models import PlaceStats, AcceptStats, RatingStats


class PlacesStatsListTestCase(BaseTestCase):
    """
    Тесты для /places/
    """
    def setUp(self):
        super().setUp()
        self.token.set_role(self.token.ROLES.SUPERUSER)
        self.path = self.url_prefix + 'places/'
        self.stat = PlaceStats.objects.create(place_id=1, user_id=1, action=PlaceStats.OPENED,
                                              action_dt='2020-03-01T12:12:12Z')
        self.data_201_1 = {
            'action': 'CREATED',
            'user_id': 1,
            'place_id': 1,
            'action_dt': '2020-03-12T13:00:01Z',
        }
        self.data_201_2 = {
            'action': 'OPENED',
            'user_id': None,
            'place_id': 1,
            'action_dt': '2020-03-12T13:00:01Z',
        }
        self.data_400_1 = {
            'action': 'CREATED',
        }
        self.data_400_2 = {
            'action': 'wrong',
            'user_id': 1,
            'place_id': 1,
            'action_dt': '2020-03-12T13:00:01Z',
        }
        self.data_400_3 = {
            'action': 'CREATED',
            'user_id': None,
            'place_id': 1,
            'action_dt': '2020-03-12T13:00:01Z',
        }
        self.data_400_4 = {
            'action': 'CREATED',
            'user_id': 1,
            'place_id': 1,
            'action_dt': '2020/03/12 13:00:01',
        }

    def testGet200_OK(self):
        response = self.get_response_and_check_status(url=self.path)
        self.list_test(response, PlaceStats)

    def testGet200_WithQueryParams(self):
        response = self.get_response_and_check_status(url=self.path +
                                                      f'?user_id={self.stat.user_id}&place_id={self.stat.place_id}')
        self.assertEqual(len(response), 1, msg='No instance in response')

    def testGet200_EmptyWithQueryParams(self):
        response = self.get_response_and_check_status(url=self.path + f'?user_id={self.stat.user_id+1000}')
        self.assertEqual(len(response), 0, msg='Instance in response')
        response = self.get_response_and_check_status(url=self.path + f'?place_id={self.stat.place_id+1000}')
        self.assertEqual(len(response), 0, msg='Instance in response')

    def testGet401_403_NotSuperuser(self):
        self.token.set_role(self.token.ROLES.USER)
        _ = self.get_response_and_check_status(url=self.path, expected_status_code=[401, 403])

    def testPost201_OKWithUserId(self):
        _ = self.post_response_and_check_status(url=self.path, data=self.data_201_1)

    def testPost201_WithoutUserId(self):
        _ = self.post_response_and_check_status(url=self.path, data=self.data_201_2)

    def testPost400_WrongJSON(self):
        _ = self.post_response_and_check_status(url=self.path, data=self.data_400_1, expected_status_code=400)

    def testPost400_WrongAction(self):
        _ = self.post_response_and_check_status(url=self.path, data=self.data_400_2, expected_status_code=400)

    def testPost400_NoUserId(self):
        _ = self.post_response_and_check_status(url=self.path, data=self.data_400_3, expected_status_code=400)

    def testPost400_WrongDTFormat(self):
        _ = self.post_response_and_check_status(url=self.path, data=self.data_400_4, expected_status_code=400)

    def testPost401_403_WrongAppToken(self):
        self.token.set_error(self.token.ERRORS_KEYS.APP_AUTH, self.token.ERRORS.BAD_CODE_403_TOKEN)
        _ = self.post_response_and_check_status(url=self.path, data=self.data_201_1, expected_status_code=[401, 403])

    def testPost401_403_ErrorOnAuthService(self):
        self.token.set_error(self.token.ERRORS_KEYS.APP_AUTH, self.token.ERRORS.BAD_CODE_403_TOKEN)
        _ = self.post_response_and_check_status(url=self.path, data=self.data_201_1, expected_status_code=[401, 403])


class PlaceStatsTestCase(BaseTestCase):
    """
    Тесты для /places/<pk>/
    """
    def setUp(self):
        super().setUp()
        self.token.set_role(self.token.ROLES.SUPERUSER)
        self.stat = PlaceStats.objects.create(place_id=1, user_id=1, action=PlaceStats.OPENED,
                                              action_dt='2020-03-01T12:12:12Z')
        self.path = self.url_prefix + f'places/{self.stat.id}/'
        self.path_404 = self.url_prefix + f'places/{self.stat.id + 1000}/'

    def testGet200_OK(self):
        _ = self.get_response_and_check_status(url=self.path)

    def testGet401_403_NotSuperuser(self):
        self.token.set_role(self.token.ROLES.USER)
        _ = self.get_response_and_check_status(url=self.path, expected_status_code=[401, 403])

    def testGet404_WrongId(self):
        _ = self.get_response_and_check_status(url=self.path_404, expected_status_code=404)


class AcceptStatsListTestCase(BaseTestCase):
    """
    Тесты для /accepts/
    """
    def setUp(self):
        super().setUp()
        self.token.set_role(self.token.ROLES.SUPERUSER)
        self.path = self.url_prefix + 'accepts/'
        self.stat = AcceptStats.objects.create(place_id=1, user_id=1, action=AcceptStats.ACCEPTED,
                                               action_dt='2020-03-01T12:12:12Z')
        self.data_201 = {
            'action': 'ACCEPTED',
            'user_id': 1,
            'place_id': 1,
            'action_dt': '2020-03-12T13:00:01Z',
        }
        self.data_400_1 = {
            'action': 'ACCEPTED',
        }
        self.data_400_2 = {
            'action': 'wrong',
            'user_id': 1,
            'place_id': 1,
            'action_dt': '2020-03-12T13:00:01Z',
        }
        self.data_400_3 = {
            'action': 'ACCEPTED',
            'user_id': 1,
            'place_id': 1,
            'action_dt': '2020/03/12 13:00:01',
        }

    def testGet200_OK(self):
        response = self.get_response_and_check_status(url=self.path)
        self.list_test(response, AcceptStats)

    def testGet200_WithQueryParams(self):
        response = self.get_response_and_check_status(url=self.path +
                                                      f'?user_id={self.stat.user_id}&place_id={self.stat.place_id}')
        self.assertEqual(len(response), 1, msg='No instance in response')

    def testGet200_EmptyWithQueryParams(self):
        response = self.get_response_and_check_status(url=self.path + f'?user_id={self.stat.user_id+1000}')
        self.assertEqual(len(response), 0, msg='Instance in response')
        response = self.get_response_and_check_status(url=self.path + f'?place_id={self.stat.place_id+1000}')
        self.assertEqual(len(response), 0, msg='Instance in response')

    def testGet401_403_NotSuperuser(self):
        self.token.set_role(self.token.ROLES.USER)
        _ = self.get_response_and_check_status(url=self.path, expected_status_code=[401, 403])

    def testPost201_OK(self):
        _ = self.post_response_and_check_status(url=self.path, data=self.data_201)

    def testPost400_WrongJSON(self):
        _ = self.post_response_and_check_status(url=self.path, data=self.data_400_1, expected_status_code=400)

    def testPost400_WrongAction(self):
        _ = self.post_response_and_check_status(url=self.path, data=self.data_400_2, expected_status_code=400)

    def testPost400_WrongDTFormat(self):
        _ = self.post_response_and_check_status(url=self.path, data=self.data_400_3, expected_status_code=400)

    def testPost401_403_WrongAppToken(self):
        self.token.set_error(self.token.ERRORS_KEYS.APP_AUTH, self.token.ERRORS.BAD_CODE_403_TOKEN)
        _ = self.post_response_and_check_status(url=self.path, data=self.data_201, expected_status_code=[401, 403])

    def testPost401_403_ErrorOnAuthService(self):
        self.token.set_error(self.token.ERRORS_KEYS.APP_AUTH, self.token.ERRORS.BAD_CODE_403_TOKEN)
        _ = self.post_response_and_check_status(url=self.path, data=self.data_201, expected_status_code=[401, 403])


class AcceptStatsTestCase(BaseTestCase):
    """
    Тесты для /accepts/<pk>/
    """
    def setUp(self):
        super().setUp()
        self.token.set_role(self.token.ROLES.SUPERUSER)
        self.stat = AcceptStats.objects.create(place_id=1, user_id=1, action=AcceptStats.ACCEPTED,
                                               action_dt='2020-03-01T12:12:12Z')
        self.path = self.url_prefix + f'accepts/{self.stat.id}/'
        self.path_404 = self.url_prefix + f'accepts/{self.stat.id + 1000}/'

    def testGet200_OK(self):
        _ = self.get_response_and_check_status(url=self.path)

    def testGet401_403_NotSuperuser(self):
        self.token.set_role(self.token.ROLES.USER)
        _ = self.get_response_and_check_status(url=self.path, expected_status_code=[401, 403])

    def testGet404_WrongId(self):
        _ = self.get_response_and_check_status(url=self.path_404, expected_status_code=404)


class RatingStatsListTestCase(BaseTestCase):
    """
    Тесты для /ratings/
    """
    def setUp(self):
        super().setUp()
        self.token.set_role(self.token.ROLES.SUPERUSER)
        self.path = self.url_prefix + 'ratings/'
        self.stat = RatingStats.objects.create(place_id=1, user_id=1, old_rating=1, new_rating=5,
                                               action_dt='2020-03-01T12:12:12Z')
        self.data_201 = {
            'old_rating': 1,
            'new_rating': 5,
            'user_id': 1,
            'place_id': 1,
            'action_dt': '2020-03-12T13:00:01Z',
        }
        self.data_400_1 = {
        }
        self.data_400_2 = {
            'old_rating': 6,
            'new_rating': 6,
            'user_id': 1,
            'place_id': 1,
            'action_dt': '2020-03-12T13:00:01Z',
        }
        self.data_400_3 = {
            'old_rating': 3,
            'new_rating': 5,
            'user_id': 1,
            'place_id': 1,
            'action_dt': '2020/03/12 13:00:01',
        }

    def testGet200_OK(self):
        response = self.get_response_and_check_status(url=self.path)
        self.list_test(response, RatingStats)

    def testGet200_WithQueryParams(self):
        response = self.get_response_and_check_status(url=self.path +
                                                      f'?user_id={self.stat.user_id}&place_id={self.stat.place_id}')
        self.assertEqual(len(response), 1, msg='No instance in response')

    def testGet200_EmptyWithQueryParams(self):
        response = self.get_response_and_check_status(url=self.path + f'?user_id={self.stat.user_id+1000}')
        self.assertEqual(len(response), 0, msg='Instance in response')
        response = self.get_response_and_check_status(url=self.path + f'?place_id={self.stat.place_id+1000}')
        self.assertEqual(len(response), 0, msg='Instance in response')

    def testGet401_403_NotSuperuser(self):
        self.token.set_role(self.token.ROLES.USER)
        _ = self.get_response_and_check_status(url=self.path, expected_status_code=[401, 403])

    def testPost201_OK(self):
        _ = self.post_response_and_check_status(url=self.path, data=self.data_201)

    def testPost400_WrongJSON(self):
        _ = self.post_response_and_check_status(url=self.path, data=self.data_400_1, expected_status_code=400)

    def testPost400_WrongRatings(self):
        _ = self.post_response_and_check_status(url=self.path, data=self.data_400_2, expected_status_code=400)

    def testPost400_WrongDTFormat(self):
        _ = self.post_response_and_check_status(url=self.path, data=self.data_400_3, expected_status_code=400)

    def testPost401_403_WrongAppToken(self):
        self.token.set_error(self.token.ERRORS_KEYS.APP_AUTH, self.token.ERRORS.BAD_CODE_403_TOKEN)
        _ = self.post_response_and_check_status(url=self.path, data=self.data_201, expected_status_code=[401, 403])

    def testPost401_403_ErrorOnAuthService(self):
        self.token.set_error(self.token.ERRORS_KEYS.APP_AUTH, self.token.ERRORS.BAD_CODE_403_TOKEN)
        _ = self.post_response_and_check_status(url=self.path, data=self.data_201, expected_status_code=[401, 403])


class RatingStatsTestCase(BaseTestCase):
    """
    Тесты для /ratings/<pk>/
    """
    def setUp(self):
        super().setUp()
        self.token.set_role(self.token.ROLES.SUPERUSER)
        self.stat = RatingStats.objects.create(place_id=1, user_id=1, old_rating=2, new_rating=5,
                                               action_dt='2020-03-01T12:12:12Z')
        self.path = self.url_prefix + f'ratings/{self.stat.id}/'
        self.path_404 = self.url_prefix + f'ratings/{self.stat.id + 1000}/'

    def testGet200_OK(self):
        _ = self.get_response_and_check_status(url=self.path)

    def testGet401_403_NotSuperuser(self):
        self.token.set_role(self.token.ROLES.USER)
        _ = self.get_response_and_check_status(url=self.path, expected_status_code=[401, 403])

    def testGet404_WrongId(self):
        _ = self.get_response_and_check_status(url=self.path_404, expected_status_code=404)
