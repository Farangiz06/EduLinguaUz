from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Language, Lesson, Story
from .serializers import LessonSerializer, StorySerializer, LanguageSerializer
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO
from django.db.models import Q

@api_view(["GET"])
def languages(request):
    langs = Language.objects.all().order_by("code")
    return Response(LanguageSerializer(langs, many=True).data)

@api_view(["GET"])
def lessons_by(request):
    code = request.GET.get("lang","es")
    level = request.GET.get("level","A1")
    lessons = Lesson.objects.filter(language__code=code, level=level, is_published=True).order_by("order")
    return Response(LessonSerializer(lessons, many=True).data)

@api_view(["GET"])
def stories_by(request):
    code = request.GET.get("lang","es")
    level = request.GET.get("level","A1")
    stories = Story.objects.filter(language__code=code, level=level)
    return Response(StorySerializer(stories, many=True).data)

@api_view(["GET"])
def search(request):
    q = request.GET.get("q","").strip()
    if not q: return Response([])
    lessons = Lesson.objects.filter(Q(title__icontains=q) | Q(content__icontains=q))
    return Response(LessonSerializer(lessons, many=True).data)

@api_view(["POST"])
def certificate(request):
    username = request.data.get("username","Student")
    lang = request.data.get("lang","es").upper()
    level = request.data.get("level","A1")
    buf = BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)
    c.setFont("Helvetica-Bold", 22); c.drawCentredString(300, 770, "EduLinguaUz Certificate")
    c.setFont("Helvetica", 14)
    c.drawCentredString(300, 730, f"This certifies that {username}")
    c.drawCentredString(300, 710, f"completed {lang} {level} level.")
    c.drawString(50, 660, "Signed: EduLinguaUz")
    c.showPage(); c.save()
    pdf = buf.getvalue(); buf.close()
    resp = HttpResponse(pdf, content_type="application/pdf")
    resp["Content-Disposition"] = 'attachment; filename="certificate.pdf"'
    return resp