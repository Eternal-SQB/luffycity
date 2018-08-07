


from django.conf.urls import url
from api.views import course

urlpatterns = [


    url(r'courses/$', course.CoursesView.as_view()),
    url(r'coursesdetail/(?P<pk>\d+)/$', course.CoursesDetailView.as_view()),

    url(r'degreecourses_teacher/$', course.DegreeCourseTeacherView.as_view()),
    url(r'degreecourses_scholarship/$', course.DegreeCourseScholarshipView.as_view()),

    url(r'degree_courses/(?P<pk>\d+)/$', course.DegreeCourseModuleView.as_view()),

    url(r'a/(?P<pk>\d+)/$', course.CourseOneView.as_view()),
    url(r'b/(?P<pk>\d+)/$', course.CourseTwoView.as_view()),
    url(r'c/(?P<pk>\d+)/$', course.CourseThereView.as_view()),
    url(r'd/(?P<pk>\d+)/$', course.CourseFourView.as_view()),


]
