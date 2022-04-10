from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from .views import GroupViewSet, PostViewSet, CommentViewSet


router = SimpleRouter()
router.register('groups', GroupViewSet)
router.register('posts', PostViewSet)
router.register('posts/(?P<post_id>\d+)/comments', CommentViewSet)

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
]
