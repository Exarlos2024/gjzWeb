from django.db import models
from django.conf import settings

class Contact(models.Model):
    LEVEL_CHOICES = [
        ('局长', '局长'),
        ('副局长', '副局长'),
        ('科长', '科长'),
        ('科员', '科员'),
    ]

    name = models.CharField(max_length=100, verbose_name='姓名')
    position = models.CharField(max_length=100, verbose_name='职位')
    department = models.CharField(max_length=100, verbose_name='科室')
    office = models.CharField(max_length=100, verbose_name='办公室')
    office_phone = models.CharField(max_length=15, blank=True, verbose_name='办公电话')
    mobile_phone = models.CharField(max_length=15, blank=True, verbose_name='手机')
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES, verbose_name='级别')
    leader = models.CharField(max_length=100, blank=True, verbose_name='分管领导')  # 可以为空
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '联系人'
        verbose_name_plural = '联系人'
    
    def __str__(self):
        return self.name
