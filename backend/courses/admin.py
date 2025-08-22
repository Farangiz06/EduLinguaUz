from django.contrib import admin
from .models import Language, Lesson, Story, Badge, UserProgress, CertificateRequest
for m in [Language,Lesson,Story,Badge,UserProgress,CertificateRequest]: admin.site.register(m)
