from django.conf.urls.defaults import *

urlpatterns = patterns('teachers.views',
    (r'^$', 'index'),
    (r'^(?P<teacher_id>\d+)/$', 'detail'),
    #(r'^(?P<poll_id>\d+)/results/$', 'results'),
    #(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
    (r'^students/$', 'student_list'),
    (r'^students/(?P<student_id>\d+)/$', 'student_detail'),
    (r'^new/$', 'new'),
    (r'^add/$', 'add'),
    (r'^(?P<teacher_id>\d+)/new/$', 'new_student'),
    (r'^(?P<teacher_id>\d+)/add/$', 'add_student'),
    (r'^delete/(?P<teacher_id>\d+)/$', 'delete'),
    (r'^students/delete/(?P<student_id>\d+)/$', 'delete_student'),
)
