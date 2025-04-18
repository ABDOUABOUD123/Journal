from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'volumes', views.VolumeViewSet)
router.register(r'issues', views.IssueViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'keywords', views.KeywordViewSet)
router.register(r'articles', views.ArticleViewSet)
router.register(r'article-authors', views.ArticleAuthorViewSet)
router.register(r'article-keywords', views.ArticleKeywordViewSet)
router.register(r'files', views.FileViewSet)
router.register(r'citations', views.CitationViewSet)
router.register(r'favorites', views.UserFavoriteViewSet, basename='favorite')
router.register(r'saved-searches', views.SavedSearchViewSet, basename='savedsearch')

urlpatterns = [
    path('', include(router.urls)),
]