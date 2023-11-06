from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    brief = models.TextField(max_length=250, blank=True, null=True)
    link = models.CharField(max_length=100, blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})


class Books(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    brief = models.TextField(max_length=250, blank=True, null=True)
    file = models.FileField(blank=True, null=True, upload_to='documents')
    author = models.CharField(max_length=100, blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})


class Videos(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    brief = models.TextField(max_length=250, blank=True, null=True)
    link = models.CharField(max_length=100, blank=True, null=True)
    channel = models.CharField(max_length=100, blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('video-detail', kwargs={'pk': self.pk})
