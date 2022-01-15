from frontend.models import Teachers
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer , TeacherSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework import status

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
    

@api_view(['POST','PATCH'])
def teacher_details(request):
    if request.method == 'POST':
        teacher_serializer = TeacherSerializer(data = request.data)
        if teacher_serializer.is_valid():
            teacher_serializer.save()
            return JsonResponse(teacher_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(teacher_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    if request.method == 'PATCH':
        email = request.data.get('email')
        teacher = Teachers.objects.get(email = email)
        teacher_serializer = TeacherSerializer(teacher,data = request.data)
        if teacher_serializer.is_valid():
            teacher_serializer.save()
            return JsonResponse(teacher_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(teacher_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        