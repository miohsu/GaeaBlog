from django.conf.urls import url

from .views import PostListView
from .views import PostDetailView

urlpatterns = [
    # url(r'^home/$', PostListView.as_view(), name='home'),
    url(r'^(?P<pk>[0-9]+)/$', PostDetailView.as_view(), name='detail'),
]
