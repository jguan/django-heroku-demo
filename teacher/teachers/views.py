from django.shortcuts import render_to_response, get_object_or_404
from teachers.models import Teacher, Student

def index(request):
    teacher_list = Teacher.objects.all()
    return render_to_response('teachers/index.html', {'teacher_list': teacher_list})

def detail(request, teacher_id):
    t = get_object_or_404(Teacher, pk=teacher_id)
    return render_to_response('teachers/detail.html', {'teacher': t})

def student_list(request):
    student_list = Student.objects.all()
    return render_to_response('teachers/student_list.html', {'student_list': student_list})

def student_detail(request, student_id):
    s = get_object_or_404(Student, pk=student_id)
    return render_to_response('teachers/student_detail.html', {'student': s})

