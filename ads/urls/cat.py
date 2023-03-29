from rest_framework.routers import SimpleRouter

from ads.views import CatViewSet

cat_router = SimpleRouter()
cat_router.register("", CatViewSet)
urlpatterns = cat_router.urls

