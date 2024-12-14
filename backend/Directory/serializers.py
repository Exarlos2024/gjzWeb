from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'position', 'department', 'office', 'office_phone', 'mobile_phone', 'level', 'leader', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
