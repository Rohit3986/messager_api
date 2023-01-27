from rest_framework.generics import ListCreateAPIView
from .serializers import MessageSerializer,LikeSerializer
from .models import Messages,Likes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
class MessageAPIView(ListCreateAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessageSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['sender']=request.user
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

class LikeAPIView(ListCreateAPIView):
    queryset = Likes.objects.all()
    serializer_class = LikeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['user']=request.user
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
