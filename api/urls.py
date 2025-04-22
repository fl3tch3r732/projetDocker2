from django.urls import path, include

from api.manager.controllers import GroupViewSet, PersonneViewSet
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('personnes', PersonneViewSet, basename='personne')
router.register('groups', GroupViewSet, basename='groups')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('', include(router.urls)),
]