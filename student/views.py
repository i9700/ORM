from django.shortcuts import render, HttpResponse
from .models import Student
import datetime
import json


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
    stu = Student.objects.create(name="小茜", age=26, sex=1, birthday="1995-6-12")
    print(stu.id)
    print(stu.name)
    print(stu.age)

    return HttpResponse("添加记录成功!")


def select_student(request):
    # (1) all函数：返回的一个 查询集 Queryset
    # about Queryset: Queryset是一个类似于list的数据类型，里面的元素是统一类型，比如模型类对象或者字典

    # 查询所有学生
    # student_list = Student.objects.all()
    # print("student_list:", student_list)

    # (2) first() last() 返回模型类对象
    # 查询第一个学生
    # stu = Student.objects.all()[0]
    # print(stu.name)
    # print(stu.age)

    # stu = Student.objects.first()
    # print(stu.name, stu.age)
    # stu = Student.objects.last()
    # print(stu.name, stu.age)

    # (3) filter方法: where语句 返回Queryset对象
    # 查询所有女生
    # stu = Student.objects.filter(sex=0)
    # stu = Student.objects.filter(sex=1, age=22)  # 逻辑与
    # print(stu)

    # (4) exclude: 排除符合条件的记录 返回Queryset对象
    # stu = Student.objects.exclude(sex=1)
    # print(stu)

    # (5) get方法: 查询结果必须是有且只有一条符合条件的记录:返回一个查询到的模型类对象
    # stu = Student.objects.get(sex=0)
    # stu = Student.objects.get(age=22)
    # print(stu)

    # (6)order_by():是queryset类型的一个内置方法 返回Queryset对象
    # 将所有学生年龄从高到低排序
    # stu = Student.objects.all().order_by("-age", "-id")
    # print(stu)

    # (7) count(): 是queryset类型的一个内置方法 返回int对象
    # 查询学生个数
    # count = Student.objects.all().count()
    # print(count)
    # 查询女学生个数
    # sex_count = Student.objects.filter(sex=0).count()
    # print(sex_count)

    # (8) exist: 是queryset类型的一个内置方法,判断是否存在记录，返回一个布尔值
    # 查询学生表中是否存在记录
    print(Student.objects.exists())

    # (9) values 和 values_list: 翻译的是select语句 返回Queryset对象
    student_list = Student.objects.all().values("name", "age")
    # print(student_list)
    print(json.dumps(list(student_list), ensure_ascii=False), type(json.dumps(list(student_list), ensure_ascii=False)))

    # student_list = Student.objects.all().values_list("name", "age")
    # print(student_list)
    # 查询所有男生的姓名和年龄
    male_student = Student.objects.all().values("name", "age").filter(sex=1)
    print(male_student)
    # male_student = Student.objects.all().filter(sex=1).values("name", "age")
    # print(male_student)

    # (10)distinct: 去重 是queryset类型的一个内置方法 返回Queryset对象
    student_list = Student.objects.all().values("age").distinct()
    print(student_list)
    return HttpResponse("查询成功！")
