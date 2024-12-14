from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.settings import api_settings
from .models import CustomUser
from .serializers import CustomUserSerializer, RegisterSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
import logging
import traceback
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

logger = logging.getLogger(__name__)

# 注册视图
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]  # 允许任何人访问

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 自定义用户列表视图
class CustomUserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

# 登录视图
class CustomAuthToken(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            print("Received login request data:", request.data)
            
            username = request.data.get('username')
            password = request.data.get('password')
            
            if not username or not password:
                return Response({
                    "error": "Missing credentials",
                    "detail": "Both username and password are required"
                }, status=status.HTTP_400_BAD_REQUEST)
            
            username = str(username)
            
            print(f"Attempting login with username: {username}")
            
            user = authenticate(request=request, username=username, password=password)
            print(f"Authentication result: {user}")

            if user is None:
                return Response({
                    "error": "Invalid credentials",
                    "detail": "Username or password is incorrect"
                }, status=status.HTTP_400_BAD_REQUEST)

            # 删除旧的 token（如果存在）
            Token.objects.filter(user=user).delete()
            
            # 创建新的 token
            token = Token.objects.create(user=user)
            
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'email': user.email
            })
            
        except Exception as e:
            logger.error(f"Login error: {str(e)}\n{traceback.format_exc()}")
            return Response({
                "error": "Server error",
                "detail": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserPermissionsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(f"User: {request.user.username} is requesting permissions.")  # 打印用户信息
        permissions = {
            'can_add_contact': request.user.has_perm('Directory.add_contact'),  # 确保使用正确的权限名称
            'can_view_contact': request.user.has_perm('Directory.view_contact'),
            'can_change_contact': request.user.has_perm('Directory.change_contact'),
            'can_delete_contact': request.user.has_perm('Directory.delete_contact'),
            # 添加其他权限检查
        }
        print(f"Permissions: {permissions}")  # 打印权限信息
        return Response(permissions)
