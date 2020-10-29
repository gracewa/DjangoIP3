from django.conf.urls import url


from .views import ProjectPostRudView, ProjectPostAPIView

urlpatterns = [
    url(r'^$', ProjectPostAPIView.as_view(), name='post-listcreate'),
    url(r'^(?P<pk>\d+)/$', ProjectPostRudView.as_view(), name='post-rud')
]