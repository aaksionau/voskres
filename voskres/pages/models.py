from django.db import models
from django.urls import reverse


class BlogPost(models.Model):
    BLOGPOST_TYPES = (
        ('S', 'Проповедь'),
        ('A', 'Статья'),
        ('P', 'Стих'),
    )
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    post_type = models.CharField(max_length=1, choices=BLOGPOST_TYPES)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    seo_keywords = models.CharField(max_length=250, blank=True, null=True)
    seo_description = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogpost-detail', kwargs={'id': self.id})


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    cc_myself = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created']
