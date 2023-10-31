
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Question, QuestionReply

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        read_only_fields =('id',)  

class QuestionSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username',read_only=True)
    class Meta:
        model = Question
        fields = '__all__' 
        read_only_fields =('id','user_name')  


class QuestionReplySerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username',read_only=True)

    class Meta:
        model = QuestionReply
        fields =['question','content','user_name']
        #exclude = ('user')
        read_only_fields =('id','created_at','update_at')  


class QuestionDetailSerializer(serializers.ModelSerializer):
    reply=QuestionReplySerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = '__all__' 
        read_only_fields =('id','reply')