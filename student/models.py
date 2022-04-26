from django.db import models
import django.utils.timezone as timezone


# Create your models here.


class Student(models.Model):
    SEX_CHOICES = (
        (0, "女"),
        (1, "男"),
        (2, "保密"),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True, verbose_name="姓名")
    age = models.SmallIntegerField(default=18, verbose_name="年龄")
    sex = models.SmallIntegerField(choices=SEX_CHOICES)
    birthday = models.DateField()

    classmate = models.CharField(db_column="class", max_length=5, db_index=True, verbose_name="班级", default="")
    description = models.TextField(default="", verbose_name="个性签名")
    created_time = models.DateTimeField(default=timezone.now)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "db_student"
