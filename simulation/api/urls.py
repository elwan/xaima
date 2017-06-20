from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet,Societe_TransfertList ,TarifList


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    url(r'^sta/', Societe_TransfertList.as_view()),
    url(r'^tarif/',TarifList.as_view()),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    ]
