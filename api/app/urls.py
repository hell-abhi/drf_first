from django.conf.urls import url
from rest_framework import routers
from .views import UserViewSet, UserList

# router = routers.DefaultRouter()
# router.register(r'user', UserViewSet)
# #router.register(r'show', UserList)
#
# urlpatterns = router.urls

urlpatterns = [
    url(r'^user/$', UserViewSet),
]