from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.pagination import LimitOffsetPagination
from PlacesStats.models import PlaceStats, AcceptStats, RatingStats
from PlacesStats.serializers import PlaceStatsSerializer, AcceptStatsSerializer, RatingStatsSerializer
from StatsService.utils import RetrieveQueryParamsMixin


class PlaceStatsListView(ListCreateAPIView, RetrieveQueryParamsMixin):
    """
    Вьюха для спискового представления статы по местам
    """
    serializer_class = PlaceStatsSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return PlaceStats.objects.filter(**self.get_lookup_fields())


class PlaceStatsDetailView(RetrieveAPIView):
    """
    Вьюха для детального представления статы по месту
    """
    serializer_class = PlaceStatsSerializer

    def get_queryset(self):
        return PlaceStats.objects.all()


class AcceptStatsListView(ListCreateAPIView, RetrieveQueryParamsMixin):
    """
    Вьюха для спискового представления статы по подтверждениям
    """
    serializer_class = AcceptStatsSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return AcceptStats.objects.filter(**self.get_lookup_fields())


class AcceptStatsDetailView(RetrieveAPIView):
    """
    Вьюха для детального представления статы по подтверждению
    """
    serializer_class = AcceptStatsSerializer

    def get_queryset(self):
        return AcceptStats.objects.all()


class RatingStatsListView(ListCreateAPIView, RetrieveQueryParamsMixin):
    """
    Вьюха для спискового представления статы по рейтингам
    """
    serializer_class = RatingStatsSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return RatingStats.objects.filter(**self.get_lookup_fields())


class RatingStatsDetailView(RetrieveAPIView):
    """
    Вьюха для детального представления статы по рейтингу
    """
    serializer_class = RatingStatsSerializer

    def get_queryset(self):
        return RatingStats.objects.all()
