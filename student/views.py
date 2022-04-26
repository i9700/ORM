from django.shortcuts import render, HttpResponse
from .models import Student
import datetime


# Create your views here.


def add_student(request):
    # 添加记录

    # （1） 方式：实例化+save()  模型类对象映射表记录
    # birth = datetime.date(2012, 12, 12)
    # Student(name="张三", age=22, sex=1, birthday=birth)

    # stu = Student(name="张三", age=22, sex=1, birthday="2012-12-12")
    # stu.save()  # 创建对应的sql语句并执行
    # print(stu.id)
    # print(stu.name)
    # print(stu.age)

    # 方式2：creat返回了创建的模型类对象
    stu = Student.objects.create(name="李海", age=26, sex=1, birthday="1995-12-12")
    print(stu.id)
    print(stu.name)
    print(stu.age)

    return HttpResponse("添加记录成功!")
