from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# 自定义用户模型，继承自Django的AbstractUser
class CustomUser(AbstractUser):
    # 添加自定义字段：组织名称
    organization = models.CharField('Organization', max_length=128, blank=True)
    # 添加自定义字段：电话号码
    telephone = models.CharField('Telephone', max_length=50, blank=True)
    # 自动记录最后修改时间
    modified_date = models.DateTimeField('Last modified', auto_now=True)
    # 解除注释并保持默认的related_name（除非有特定需求要更改）
    groups = models.ManyToManyField(
        Group,
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    # 添加 related_name 参数以避免冲突
    # groups = models.ManyToManyField(
    #     Group,
    #     related_name='customuser_set',  # 修改为自定义的 related_name
    #     blank=True,
    #     help_text='The groups this user belongs to.',
    #     verbose_name='groups',
    # )
    # user_permissions = models.ManyToManyField(
    #     Permission,
    #     related_name='customuser_set',  # 修改为自定义的 related_name
    #     blank=True,
    #     help_text='Specific permissions for this user.',
    #     verbose_name='user permissions',
    # )

    class Meta:
        # 设置模型的单数和复数名称
        app_label = 'UserProfit'
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'

        # permissions = [
        #     ("can_add_contact", "Directory | 联系人 | Can add 联系人"),
        #     ("can_view_contact", "Directory | 联系人 | Can view 联系人"),
        #     ("can_change_contact", "Directory | 联系人 | Can change 联系人"),
        #     ("can_delete_contact", "Directory | 联系人 | Can delete 联系人"),
        # ]
    def __str__(self):
        # 返回用户的用户名作为字符串表示
        return self.username

