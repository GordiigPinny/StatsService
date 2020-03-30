from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.pagination import LimitOffsetPagination
from AwardsStats.models import AchievementStats, PinPurchaseStats
from AwardsStats.serializers import AchievementStatSerializer, PinPurchaseStatSerializer
from StatsService.utils import RetrieveQueryParamsMixin


class PinStatsListView(ListCreateAPIView, RetrieveQueryParamsMixin):
    """
    Вьюха для списка статы по покупкам пинов
    """
    serializer_class = PinPurchaseStatSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return PinPurchaseStats.objects.filter(**self.get_lookup_fields(['user_id', 'pin_id']))


class PinStatsDetailView(RetrieveAPIView):
    """
    Вьюха для статы по покупке пина
    """
    serializer_class = PinPurchaseStatSerializer

    def get_queryset(self):
        return PinPurchaseStats.objects.all()


class AchievementStatsListView(ListCreateAPIView, RetrieveQueryParamsMixin):
    """
    Вьюха для списка статы по получению достижений
    """
    serializer_class = AchievementStatSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return AchievementStats.objects.filter(**self.get_lookup_fields(['user_id', 'achievement_id']))


class AchievementStatsDetailView(RetrieveAPIView):
    """
    Вьюха для статы по получению достижения
    """
    serializer_class = AchievementStatSerializer

    def get_queryset(self):
        return AchievementStats.objects.all()
