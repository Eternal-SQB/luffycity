from django.shortcuts import render, HttpResponse
from api import models


# Create your views here.
def index(request):


    # a.查看所有学位课并打印学位课名称以及授课老师

    # obj=models.DegreeCourse.objects.all().values_list('name','teachers__name')
    # print(obj)

    # b.查看所有学位课并打印学位课名称以及学位课的奖学金

    # obj=models.Scholarship.objects.all().values_list('degree_course__name','value')
    # print(obj)

    # c.展示所有的专题课

    # obj=models.Course.objects.filter(degree_course__isnull=True)
    # print(obj)

    # d.查看id = 1
    # 的学位课对应的所有模块名称
    # obj=models.DegreeCourse.objects.filter(id=1).values_list('name','course__name')
    # print(obj)
    # e.获取id = 1
    # 的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
    # obj = models.Course.objects.filter(id=1,degree_course__isnull=True).first()
    # level = obj.get_level_display()
    # print(obj.name,level,obj.coursedetail.why_study,obj.coursedetail.what_to_study_brief,obj.coursedetail.recommend_courses.all())

    # f.获取id = 1
    # 的专题课，并打印该课程相关的所有常见问题
    # obj=models.Course.objects.filter(id=1).values_list('name','asked_question__question')
    # print(obj)
    #
    # g.获取id = 1
    # 的专题课，并打印该课程相关的课程大纲
    # obj= models.Course.objects.filter(id=1).values_list('name','coursedetail__courseoutline__content')
    #     # print(obj)

    # h.获取id = 1
    # 的专题课，并打印该课程相关的所有章节
    # obj=models.Course.objects.filter(id=1).values_list('name','coursechapters__name')
    # print(obj)
    # i.获取id = 1
    # 的专题课，并打印该课程相关的所有课时
    # obj = models.Course.objects.filter(id=1, degree_course__isnull=True).first()
    # obj2 = obj.coursechapters.all()
    # print(obj)
    # for item in obj2:
    #     print(item.name)
    #     for i in item.coursesections.all():
    #         print(i.name)

    # 第1章·Python
    # 介绍、基础语法、流程控制
    # 01 - 课程介绍（一）
    # 01 - 课程介绍（一）
    # 01 - 课程介绍（一）
    # 01 - 课程介绍（一）
    # 01 - 课程介绍（一）
    # 第1章·Python
    # 介绍、基础语法、流程控制
    # 01 - 课程介绍（一）
    # 01 - 课程介绍（一）
    # 01 - 课程介绍（一）
    # 01 - 课程介绍（一）
    # 01 - 课程介绍（一）
    # i.获取id = 1
    # 的专题课，并打印该课程相关的所有的价格策略
    # obj = models.Course.objects.filter(id=1).first()
    #
    # price_list = models.PricePolicy.objects.filter(object_id=1,content_type__model='course')
    # print(price_list)


    return HttpResponse('OK')
