from django.conf.urls import url
from PlacesStats import views


urlpatterns = [
    url(r'^places/$', views.PlaceStatsListView.as_view()),
    url(r'^places/(?P<pk>\d+)/$', views.PlaceStatsDetailView.as_view()),

    url(r'^accepts/$', views.AcceptStatsListView.as_view()),
    url(r'^accepts/(?P<pk>\d+)/$', views.AcceptStatsDetailView.as_view()),

    url(r'^ratings/$', views.RatingStatsListView.as_view()),
    url(r'^ratings/(?P<pk>\d+)/$', views.RatingStatsDetailView.as_view()),
]
