from rest_framework import serializers
from .models import (
    User, Volume, Issue, Author, Keyword, 
    Article, ArticleAuthor, ArticleKeyword,
    File, Citation, UserFavorite, SavedSearch
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'last_login', 'is_active']

class VolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volume
        fields = '__all__'

class IssueSerializer(serializers.ModelSerializer):
    volume = VolumeSerializer(read_only=True)
    
    class Meta:
        model = Issue
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = '__all__'

class ArticleAuthorSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    
    class Meta:
        model = ArticleAuthor
        fields = '__all__'

class ArticleKeywordSerializer(serializers.ModelSerializer):
    keyword = KeywordSerializer(read_only=True)
    
    class Meta:
        model = ArticleKeyword
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

class CitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citation
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    issue = IssueSerializer(read_only=True)
    authors = ArticleAuthorSerializer(source='articleauthor_set', many=True, read_only=True)
    keywords = ArticleKeywordSerializer(source='articlekeyword_set', many=True, read_only=True)
    files = FileSerializer(source='file_set', many=True, read_only=True)
    citations = CitationSerializer(source='citation_set', many=True, read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'

class UserFavoriteSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=True)
    
    class Meta:
        model = UserFavorite
        fields = '__all__'

class SavedSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedSearch
        fields = '__all__'