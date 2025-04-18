from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import (
    User, Volume, Issue, Author, Keyword, 
    Article, ArticleAuthor, ArticleKeyword,
    File, Citation, UserFavorite, SavedSearch
)
from .serializers import (
    UserSerializer, VolumeSerializer, IssueSerializer,
    AuthorSerializer, KeywordSerializer, ArticleSerializer,
    ArticleAuthorSerializer, ArticleKeywordSerializer,
    FileSerializer, CitationSerializer, UserFavoriteSerializer,
    SavedSearchSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class VolumeViewSet(viewsets.ModelViewSet):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer

class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class KeywordViewSet(viewsets.ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleAuthorViewSet(viewsets.ModelViewSet):
    queryset = ArticleAuthor.objects.all()
    serializer_class = ArticleAuthorSerializer

class ArticleKeywordViewSet(viewsets.ModelViewSet):
    queryset = ArticleKeyword.objects.all()
    serializer_class = ArticleKeywordSerializer

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class CitationViewSet(viewsets.ModelViewSet):
    queryset = Citation.objects.all()
    serializer_class = CitationSerializer

class UserFavoriteViewSet(viewsets.ModelViewSet):
    queryset = UserFavorite.objects.all()
    serializer_class = UserFavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class SavedSearchViewSet(viewsets.ModelViewSet):
    queryset = SavedSearch.objects.all()
    serializer_class = SavedSearchSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)