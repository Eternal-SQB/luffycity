from api import models
from rest_framework import serializers


class CourseListSerializer(serializers.ModelSerializer):
    level = serializers.CharField(source="get_level_display", read_only=True)
    course_type = serializers.CharField(source="get_course_type_display", read_only=True)
    status = serializers.CharField(source="get_status_display", read_only=True)

    class Meta:
        model=models.Course
        fields="__all__"
        depth=2



class CourseDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.CourseDetail
        fields="__all__"
