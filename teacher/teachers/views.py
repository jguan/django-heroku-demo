from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from teachers.models import Teacher, Student

def index(request, message = ""):
    teacher_list = Teacher.objects.all()
    return render_to_response('teachers/index.html', {'teacher_list': teacher_list, 'message': message})

def detail(request, teacher_id):
    t = get_object_or_404(Teacher, pk=teacher_id)
    return render_to_response('teachers/detail.html', {'teacher': t})

def student_list(request):
    student_list = Student.objects.all()
    return render_to_response('teachers/student_list.html', {'student_list': student_list})

def student_detail(request, student_id):
    s = get_object_or_404(Student, pk=student_id)
    return render_to_response('teachers/student_detail.html', {'student': s})

def new(request):
    return render_to_response('teachers/new_teacher.html', {'action': 'add', 'button': 'Add'}, context_instance=RequestContext(request))

def add(request):
    name = request.POST["name"]
    t = Teacher( name = name )
    t.save()
    return HttpResponseRedirect(reverse('teachers.views.index'))

def new_student(request, teacher_id):
    t = get_object_or_404(Teacher, pk=teacher_id)
    return render_to_response('teachers/new_student.html', {'teacher': t, 'action': 'add', 'button': 'Add'}, context_instance=RequestContext(request))

def add_student(request, teacher_id):
    name = request.POST["name"]
    t = get_object_or_404(Teacher, pk=teacher_id)
    s = Student( name = name, teacher = t )
    s.save()
    return HttpResponseRedirect(reverse('teachers.views.index'))

def delete(request, teacher_id):
    get_object_or_404(Teacher, pk=teacher_id).delete()
    return HttpResponseRedirect(reverse('teachers.views.index'))

def delete_student(request, student_id):
    get_object_or_404(Student, pk=student_id).delete()
    return HttpResponseRedirect(reverse('teachers.views.student_list'))

