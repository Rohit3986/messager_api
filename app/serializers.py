from rest_framework import serializers
from .models import Messages,Likes

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only = True)
    class Meta:
        model = Likes
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(read_only = True)
    total_likes = serializers.SerializerMethodField()
    class Meta:
        model = Messages
        fields = '__all__'
    
    def get_total_likes(self,obj):
        return Likes.objects.filter(message=obj).filter(like_status = 1).count()
    
    


