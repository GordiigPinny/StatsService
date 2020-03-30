from django.conf.urls import url
from AwardsStats import views


urlpatterns = [
    url(r'^pin_purchases/$', views.PinStatsListView.as_view()),
    url(r'^pin_purchases/(?P<pk>\d+)/$', views.PinStatsDetailView.as_view()),

    url(r'^achievements/$', views.AchievementStatsListView.as_view()),
    url(r'^achievements/(?P<pk>\d+)/$', views.AchievementStatsDetailView.as_view()),
]
