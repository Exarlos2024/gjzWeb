from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Contact
from .serializers import ContactSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]  # 需要用户认证

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            # 检查用户是否有添加、更新或删除联系人的权限
            if not self.request.user.has_perm('app_name.can_add_contact'):
                self.permission_denied(self.request)
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save()  # 保存联系人
