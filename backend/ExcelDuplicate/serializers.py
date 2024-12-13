from rest_framework import serializers
from .models import ExcelFile, DuplicateResult

class ExcelFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExcelFile
        fields = ['id', 'original_filename', 'rows', 'columns', 'headers']

class DuplicateResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = DuplicateResult
        fields = ['id', 'duplicate_groups', 'duplicate_rows']