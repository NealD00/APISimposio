from rest_framework import routers
from .api import EstudianteViewSet

router = routers.DefaultRouter()
router.register('api/simposio', EstudianteViewSet, 'simposio')

urlpatterns = router.urls