from rest_framework.routers import SimpleRouter

from ads.views import SelectionViewSet

router = SimpleRouter()
router.register("", SelectionViewSet)
urlpatterns = router.urls
