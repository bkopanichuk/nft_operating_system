from rest_framework import routers

from . import viewsets

router = routers.DefaultRouter()
router.register(r'basetoken', viewsets.BaseTokenViewSet)
router.register(r'metadata', viewsets.MetadataViewSet)