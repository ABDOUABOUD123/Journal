from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    # Remove username field and use email instead
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='custom_user_set',  # Changed from default
        related_query_name='user'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_set',  # Changed from default
        related_query_name='user'
    )

    class Meta:
        db_table = 'user'

class Volume(models.Model):
    volume_number = models.IntegerField()
    year = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"Volume {self.volume_number} ({self.year})"

class Issue(models.Model):
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE)
    issue_number = models.IntegerField()
    publication_date = models.DateField()
    special_issue = models.BooleanField(default=False)
    social_issue_title = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Issue {self.issue_number} of Volume {self.volume.volume_number}"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    affiliation = models.CharField(max_length=255, blank=True, null=True)
    orcid = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Keyword(models.Model):
    term = models.CharField(max_length=100, unique=True)
    frequency = models.IntegerField(default=0)
    is_controlled = models.BooleanField(default=False)

    def __str__(self):
        return self.term

class Article(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    abstract = models.TextField()
    doi = models.CharField(max_length=100, blank=True, null=True)
    page_start = models.IntegerField(blank=True, null=True)
    page_end = models.IntegerField(blank=True, null=True)
    publication_date = models.DateField()
    file_path = models.CharField(max_length=255, blank=True, null=True)
    citation_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class ArticleAuthor(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    author_order = models.IntegerField()

    class Meta:
        unique_together = ('article', 'author')
        ordering = ['author_order']

    def __str__(self):
        return f"{self.author} in {self.article} (order: {self.author_order})"

class ArticleKeyword(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    relevance_score = models.FloatField(default=1.0)

    class Meta:
        unique_together = ('article', 'keyword')

    def __str__(self):
        return f"{self.keyword} for {self.article} (score: {self.relevance_score})"

class File(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=255)
    file_type = models.CharField(max_length=50)

    def __str__(self):
        return self.file_name

class Citation(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    cited_doi = models.CharField(max_length=100, blank=True, null=True)
    cited_title = models.CharField(max_length=255)
    cited_authors = models.TextField()

    def __str__(self):
        return f"Citation from {self.article} to {self.cited_title}"

class UserFavorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'article')

    def __str__(self):
        return f"{self.user} favorited {self.article}"

class SavedSearch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query_string = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Search by {self.user}: {self.query_string[:50]}..."