import user.models
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Work(models.Model):
    wrk_id = models.AutoField("作品ID", primary_key=True)
    wrk_name = models.CharField("名字", max_length=40, default="Null")
    description = models.TextField("介绍", max_length=400, default="无")
    mark = models.TextField("备注", max_length=400, default="默认标注")
    created_id = models.ForeignKey(to=user.models.Designer, on_delete=models.CASCADE)
    created_at = models.DateTimeField("添加日期", auto_now_add=True)

    def __str__(self):
        return self.wrk_name

    class Meta:
        ordering = ['-created_at']
        verbose_name = '作品信息表'
        verbose_name_plural = '作品信息表'