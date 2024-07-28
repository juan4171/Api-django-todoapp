from rest_framework import routers
from .views import TodoViewSet

router = routers.DefaultRouter()

router.register('api/todos', TodoViewSet, 'todos') #aqui se registra la ruta de la api

urlpatterns = router.urls