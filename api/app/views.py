from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'user_list.html'

    def get(self, request):
        queryset = User.objects.all()
        return Response({'users': queryset})
