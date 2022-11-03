import user.models
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ReleaseCopyRight(models.Model):
    rcp_id = models.AutoField("版本ID", primary_key=True)
    rcp_name = models.CharField("版本名字", max_length=40, default="CopyRight 1.0")
    rcp_content = models.TextField("版本号", max_length=400, default="0.0.0")
    description = models.TextField("介绍", max_length=400, default="无")
    mark = models.TextField("备注", max_length=400, default="默认标注")
    updated_at = models.DateTimeField("更新日期", auto_now=True)
    created_at = models.DateTimeField("添加日期", auto_now_add=True)

    def __str__(self):
        return self.rcp_name

    class Meta:
        ordering = ['-created_at']
        verbose_name = '发布版本信息表'
        verbose_name_plural = '发布版本信息表'


class AssetBundles(models.Model):
    ab_id = models.AutoField("ab包ID", primary_key=True)
    ab_name = models.CharField("名字", max_length=40, default="Null")
    ab_md5 = models.TextField("ab包的md5", max_length=400, default="md5")
    ab_cp = models.ForeignKey(to=ReleaseCopyRight, on_delete=models.CASCADE)
    description = models.TextField("介绍", max_length=400, default="无")
    mark = models.TextField("备注", max_length=400, default="默认标注")
    updated_at = models.DateTimeField("更新日期", auto_now=True)
    created_at = models.DateTimeField("添加日期", auto_now_add=True)

    def __str__(self):
        return self.ab_name

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'ab包信息表'
        verbose_name_plural = 'ab包信息表'