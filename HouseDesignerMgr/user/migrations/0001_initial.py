# Generated by Django 4.1.2 on 2022-10-30 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Designer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='设计者ID')),
                ('name', models.CharField(default='Null', max_length=40, verbose_name='名字')),
                ('description', models.TextField(default='无', max_length=400, verbose_name='介绍')),
                ('mark', models.TextField(default='默认标注', max_length=400, verbose_name='备注')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='添加日期')),
            ],
            options={
                'verbose_name': '设计者信息表',
                'verbose_name_plural': '设计者信息表',
                'ordering': ['-created_at'],
            },
        ),
    ]
