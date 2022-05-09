from django.urls import path, include
from .views import ArticleAPIView, DetailAPIView, GenericAPIViews, ArticleModelViewSet, article_detail, article_list, \
    ArticleViewSet, ArticleGenericViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')
router.register('mod_article', ArticleModelViewSet, basename='model_viewset')
router.register('gen_article', ArticleGenericViewSet, basename='generic_viewset')
urlpatterns = [
    path('viewset/', include(router.urls)),
    path('mod_viewset/', include(router.urls)),
    path('generic_viewset/', include(router.urls)),
    path('generic_viewset/<int:pk>/', include(router.urls)),
    path('mod_viewset/<int:pk>/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),

    # path('article/', article_list),
    path('article/', ArticleAPIView.as_view()),
    path('generic/article/', GenericAPIViews.as_view()),
    path('generic/article/<int:id>/', GenericAPIViews.as_view()),

    # path('detail/<int:pk>/', article_detail),
    path('detail/<int:id>/', DetailAPIView.as_view()),
    # path('article/', article_list),
]
