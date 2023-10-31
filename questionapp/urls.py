
from django.urls import path
from .views import (
    user_registration,
    user_login,
    QuestionListCreateView,
    QuestionDetailView,
    QuestionReplyListCreateView,
    QuestionReplyDetailView,
)

urlpatterns = [
    path('register/', user_registration, name='user-registration'),
    path('login/', user_login, name='user-login'),
    path('questions/', QuestionListCreateView.as_view(), name='question-list-create'),
    path('questions/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
    path('replies/', QuestionReplyListCreateView.as_view(), name='reply-list-create'),
    path('replies/<int:pk>/', QuestionReplyDetailView.as_view(), name='reply-detail'),
]
