from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
User = settings.AUTH_USER_MODEL


class Question(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class QuestionReply(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='reply')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.question.title}"




