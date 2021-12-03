from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views import AuthViewSet, AmocrmRequest

router = DefaultRouter()
router.register(r'auth', AuthViewSet, basename='auth')
urlpatterns = [
    path('update_or_create/', AmocrmRequest.as_view({'get': 'list'})),
]

urlpatterns += router.urls
