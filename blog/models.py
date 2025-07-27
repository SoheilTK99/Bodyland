from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):

    CATEGORY_TYPE = (
        ('sport', 'ورزشی'),
        ('Diet', 'رژیم غذایی'),
        ('tools', 'ابزار ورزشی'),
    )

    STATUS = (
        ("draft",'Draft'),
        ("published",'Published'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    slug = models.SlugField(max_length=250, unique_for_date="published_at")
    title = models.CharField(max_length=250)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS,default='draft')
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    video = models.FileField(upload_to='video/', null=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_TYPE,default='sport')


    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('published_at',)
