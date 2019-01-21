from django.conf.urls import url

from .views import PostListView

urlpatterns = [
    url(r'^post/$', PostListView.as_view(), name='post'),
]
