from django.db import models
from django.contrib.auth.models import User

class Language(models.Model):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=50)
    def __str__(self): return self.name

class Lesson(models.Model):
    LEVELS = [("A1","A1"),("A2","A2"),("B1","B1"),("B2","B2")]
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name="lessons")
    level = models.CharField(max_length=2, choices=LEVELS, default="A1")
    order = models.IntegerField()
    title = models.CharField(max_length=200)
    content = models.TextField()
    audio_url = models.URLField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    is_published = models.BooleanField(default=True)
    class Meta:
        unique_together = ("language","level","order")
        ordering = ["language__code","level","order"]

class Story(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    level = models.CharField(max_length=2, default="A1")
    title = models.CharField(max_length=200)
    text = models.TextField()
    audio_url = models.URLField(blank=True, null=True)

class Badge(models.Model):
    key = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)

class CertificateRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    level = models.CharField(max_length=2, default="A1")
    created_at = models.DateTimeField(auto_now_add=True)