from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, api_view
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from .models import Question, QuestionReply
from .serializers import UserSerializer, QuestionSerializer, QuestionReplySerializer,QuestionDetailSerializer

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def user_registration(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    print(user)
    if user:
        login(request, user)
        return Response({'message': 'User logged in successfully'})
    return Response({'message': 'Invalid login credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class QuestionListCreateView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class QuestionReplyListCreateView(generics.ListCreateAPIView):
    queryset = QuestionReply.objects.all()
    serializer_class = QuestionReplySerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Set the user of the newly created instance to the current authenticated user
        serializer.save(user=self.request.user)

class QuestionReplyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuestionReply.objects.all()
    serializer_class = QuestionReplySerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
