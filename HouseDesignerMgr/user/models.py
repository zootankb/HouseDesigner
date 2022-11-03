from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Designer(models.Model):
    des_id = models.AutoField("设计者ID", primary_key=True)
    des_name = models.CharField("名字", max_length=40, default="Null")
    des_password = models.TextField("密码", max_length=64, default="123456")
    description = models.TextField("介绍", max_length=400, default="无")
    mark = models.TextField("备注", max_length=400, default="默认标注")
    created_at = models.DateTimeField("添加日期", auto_now_add=True)

    def __str__(self):
        return self.des_name

    class Meta:
        ordering = ['-created_at']
        verbose_name = '设计者信息表'
        verbose_name_plural = '设计者信息表'