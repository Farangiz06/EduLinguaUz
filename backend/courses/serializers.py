from rest_framework import serializers
from .models import Language, Lesson, Story
class LanguageSerializer(serializers.ModelSerializer):
    class Meta: model = Language; fields = ["id","code","name"]
class LessonSerializer(serializers.ModelSerializer):
    language = LanguageSerializer()
    class Meta: model = Lesson; fields = ["id","language","level","order","title","content","audio_url","video_url","is_published"]
class StorySerializer(serializers.ModelSerializer):
    language = LanguageSerializer()
    class Meta: model = Story; fields = ["id","language","level","title","text","audio_url"]