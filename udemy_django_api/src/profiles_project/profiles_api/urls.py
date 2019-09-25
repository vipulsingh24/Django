from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, base_name='hello-viewset')
router.register('profile', UserProfileViewSet) # No base name because of model viewset
router.register('login', LoginViewSet, base_name='login')
router.register('feed', UserProfileFeedViewSet) # No base name because of model viewset

urlpatterns =  [
    url(r'^hello-view/', HelloApiView.as_view()),
    url(r'', include(router.urls))
]