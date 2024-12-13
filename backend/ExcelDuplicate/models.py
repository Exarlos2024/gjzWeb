from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ExcelFile(models.Model):
    file = models.FileField(upload_to='excel_files/')
    original_filename = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rows = models.IntegerField()
    columns = models.IntegerField()
    headers = models.JSONField()

    class Meta:
        ordering = ['-uploaded_at']

class DuplicateResult(models.Model):
    excel_file = models.ForeignKey(ExcelFile, on_delete=models.CASCADE)
    result_file = models.FileField(upload_to='duplicate_results/')
    checked_columns = models.JSONField()
    duplicate_groups = models.IntegerField()
    duplicate_rows = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
