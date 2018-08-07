from rest_framework import serializers
from api import models


class CourseModelSerializer(serializers.ModelSerializer):
    level_name = serializers.CharField(source='get_level_display')
    hours = serializers.CharField(source='coursedetail.hours')
    course_slogan = serializers.CharField(source='coursedetail.course_slogan')

    recommd_courses = serializers.SerializerMethodField()

    class Meta:
        model = models.Course
        fields = ['id', 'name', 'level_name', 'hours', 'course_slogan', 'recommd_courses']

    def get_recommd_courses(self, row):
        recommend_list = row.coursedetail.recommend_courses.all()
        return [{'id': item.id, 'name': item.name} for item in recommend_list]


class DegreeCourseTeacherModelSerializer(serializers.ModelSerializer):
    """
    # a.查看所有学位课并打印学位课名称以及授课老师
    """
    teacher_name=serializers.SerializerMethodField()

    class Meta:
        model=models.DegreeCourse
        fields=['id','name','teacher_name']

    def get_teacher_name(self,t):
        teacher_list=t.teachers.all()
        return [{'name':tt.name} for tt in teacher_list ]



class DegreeCourseScholarshipModelSerializer(serializers.ModelSerializer):
    """
    # b.查看所有学位课并打印学位课名称以及学位课的奖学金
    """
    scholarship = serializers.SerializerMethodField()
    class Meta:
        model = models.DegreeCourse
        fields = ['id', 'name', 'scholarship']

    def get_scholarship(self,s):
        scholarship_list=s.scholarship_set.all()
        return [{'value':ss.value} for ss in scholarship_list]


class DegreeCourseModuleModelSerializer(serializers.ModelSerializer):
    """
   # d. 查看id=1的学位课对应的所有模块名称
    """
    degree_course = serializers.SerializerMethodField()
    class Meta:
        model = models.DegreeCourse
        fields = ['id', 'name', 'degree_course']

    def get_degree_course(self,s):
        degree_course_list=s.course_set.all()
        return [{'degree_course':ss.name} for ss in degree_course_list]


class CourseOneSerializer(serializers.ModelSerializer):
    """
    # e.获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
    """
    level_name = serializers.CharField(source='get_level_display')
    why_study=serializers.CharField(source='coursedetail.why_study')
    what_to_study_brief=serializers.CharField(source='coursedetail.what_to_study_brief')
    recommd_courses = serializers.SerializerMethodField()
    class Meta:
        model=models.Course
        fields=['name','level_name','why_study','what_to_study_brief','recommd_courses']

    def get_recommd_courses(self, row):
        recommend_list = row.coursedetail.recommend_courses.all()
        return [{'id': item.id, 'name': item.name} for item in recommend_list]



class CourseTwoSerializer(serializers.ModelSerializer):
    """
    # f.获取id = 1的专题课，并打印该课程相关的所有常见问题
    """
    question=serializers.SerializerMethodField()
    class Meta:
        model=models.Course
        fields=['name','question']

    def get_question(self, b):
        question_list = b.asked_question.all()
        return [{'question': item.question} for item in question_list]


class CourseThereSerializer(serializers.ModelSerializer):
    """
    # g.获取id = 1的专题课，并打印该课程相关的课程大纲

    """
    content=serializers.SerializerMethodField()
    class Meta:
        model = models.Course
        fields = ['name', 'content']

    def get_content(self, b):
        content_list = b.coursedetail.courseoutline_set.all()
        return [{'content': item.content} for item in content_list]



class CourseFourSerializer(serializers.ModelSerializer):
    """
    # h.获取id = 1的专题课，并打印该课程相关的所有章节
    """
    chapter=serializers.SerializerMethodField()
    class Meta:
        model = models.Course
        fields = ['name', 'chapter']

    def get_chapter(self, b):
        chapter_list = b.coursechapters.all()
        return [{'chapter': item.name} for item in chapter_list]