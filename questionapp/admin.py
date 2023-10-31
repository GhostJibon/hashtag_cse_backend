from django.contrib import admin
from .models import Question, QuestionReply

# Register your models here.
admin.site.register(Question)
admin.site.register(QuestionReply)