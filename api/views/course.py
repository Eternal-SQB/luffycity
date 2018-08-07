from django.shortcuts import HttpResponse

from rest_framework.views import APIView
from rest_framework.versioning import URLPathVersioning
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from api.serializer.course import CourseModelSerializer,DegreeCourseTeacherModelSerializer,DegreeCourseScholarshipModelSerializer,\
    DegreeCourseModuleModelSerializer,CourseOneSerializer,CourseTwoSerializer,CourseThereSerializer,CourseFourSerializer
from api.utils.response import BaseResonse

from api import models


class CoursesView(APIView):
    """
    # c.展示所有的专题课
    """

    def get(self, request, *args, **kwargs):
        ret = BaseResonse()
        try:
            queryset = models.Course.objects.all()
            # 分页
            # page = PageNumberPagination()
            # course_list = page.paginate_queryset(queryset, request, self)

            ser = CourseModelSerializer(instance=queryset, many=True)
            ret.data = ser.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'

        return Response(ret.dict)


class CoursesDetailView(APIView):
    """
    课程详情接口
    """

    def get(self, request, pk, *args, **kwargs):
        ret = BaseResonse()
        try:
            course = models.Course.objects.get(id=pk)
            ser = CourseModelSerializer(instance=course)
            ret.data = ser.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'
        return Response(ret.dict)


class DegreeCourseTeacherView(APIView):
    """
    # a.查看所有学位课并打印学位课名称以及授课老师
    """
    def get(self,request,*args,**kwargs):
        ret=BaseResonse()
        try:
            course_teacher_list=models.DegreeCourse.objects.all()
            ser=DegreeCourseTeacherModelSerializer(instance=course_teacher_list,many=True)
            ret.data=ser.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'
        return Response(ret.dict)

class DegreeCourseScholarshipView(APIView):
    """
    # b.查看所有学位课并打印学位课名称以及学位课的奖学金
    """
    def get(self,request,*args,**kwargs):
        ret=BaseResonse()
        try:
            course_scholarship=models.DegreeCourse.objects.all()
            ser=DegreeCourseScholarshipModelSerializer(instance=course_scholarship,many=True)
            ret.data=ser.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'
        return Response(ret.dict)




class DegreeCourseModuleView(APIView):
    """
    # d. 查看id=1的学位课对应的所有模块名称
    """
    def get(self, request, pk,*args, **kwargs):
        ret = BaseResonse()
        try:
            degree_course = models.DegreeCourse.objects.filter(id=pk)
            ser = DegreeCourseModuleModelSerializer(instance=degree_course, many=True)
            ret.data = ser.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'
        return Response(ret.dict)

class CourseOneView(APIView):
    """
# e.获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
    """
    def get(self, request,pk,*args, **kwargs):
        ret = BaseResonse()
        try:
            course = models.Course.objects.filter(id=pk)
            ser = CourseOneSerializer(instance=course, many=True)
            ret.data = ser.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'
        return Response(ret.dict)

class CourseTwoView(APIView):
    """
# f.获取id = 1的专题课，并打印该课程相关的所有常见问题
    """
    def get(self, request,pk,*args, **kwargs):
        ret = BaseResonse()
        try:
            course = models.Course.objects.filter(id=pk)
            ser = CourseTwoSerializer(instance=course, many=True)
            ret.data = ser.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'
        return Response(ret.dict)


class CourseThereView(APIView):
    """
# g.获取id = 1的专题课，并打印该课程相关的课程大纲
    """
    def get(self, request,pk,*args, **kwargs):
        ret = BaseResonse()
        # try:
        course = models.Course.objects.filter(id=pk)
        ser = CourseThereSerializer(instance=course, many=True)
        ret.data = ser.data
        # except Exception as e:
        #     ret.code = 500
        #     ret.error = '获取数据失败'
        return Response(ret.dict)

class CourseFourView(APIView):
    """
# h.获取id = 1的专题课，并打印该课程相关的所有章节
    """
    def get(self, request,pk,*args, **kwargs):
        ret = BaseResonse()
        # try:
        course = models.Course.objects.filter(id=pk)
        ser = CourseFourSerializer(instance=course, many=True)
        ret.data = ser.data
        # except Exception as e:
        #     ret.code = 500
        #     ret.error = '获取数据失败'
        return Response(ret.dict)