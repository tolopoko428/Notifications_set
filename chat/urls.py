from rest_framework import routers
from views import NotificatioViewnSet

router = routers.DefaultRouter()
router.register(r'notifications', NotificatioViewnSet)


urlpatterns = router.urls
