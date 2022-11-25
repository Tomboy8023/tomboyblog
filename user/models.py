from django.db import models


class Users(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="自增ID")
    uname = models.CharField(max_length=20, verbose_name="用户名")
    userid = models.CharField(max_length=12, verbose_name="用户ID")
    pwd = models.CharField(max_length=20, verbose_name="用户密码")
    sex = models.SmallIntegerField(choices=((1, '男'), (2, '女')), null=True, blank=True, verbose_name="用户性别")
    age = models.SmallIntegerField(null=True, blank=True, verbose_name="用户年龄")
    user_introduction = models.CharField(max_length=50, null=True, blank=True, verbose_name="用户简介")

