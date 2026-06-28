from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

@login_required
def student_list(request):
    query = request.GET.get('q', '')
    if request.user.is_superuser:
        students = Student.objects.all()
    else:
        students = Student.objects.filter(created_by=request.user)
    if query:
        students = students.filter(name__icontains=query)
    return render(request, 'students/student_list.html', {'students': students, 'query': query})

@login_required
def student_create(request):
    if not request.user.is_superuser:
        if Student.objects.filter(created_by=request.user).exists():
            return redirect('student_list')
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        course = request.POST['course']
        if Student.objects.filter(email=email).exists():
            return render(request, 'students/student_form.html', {
                'error': 'A student with this email already exists.'
            })
        Student.objects.create(
            name=name, email=email,
            phone=phone, course=course,
            created_by=request.user
        )
        return redirect('student_list')
    return render(request, 'students/student_form.html')

@login_required
def student_update(request, pk):
    if request.user.is_superuser:
        student = get_object_or_404(Student, pk=pk)
    else:
        student = get_object_or_404(Student, pk=pk, created_by=request.user)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.phone = request.POST['phone']
        student.course = request.POST['course']
        student.save()
        return redirect('student_list')
    return render(request, 'students/student_form.html', {'student': student})

@login_required
def student_delete(request, pk):
    if not request.user.is_superuser:
        return redirect('student_list')
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_list')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('student_list')
    else:
        form = UserCreationForm()
    return render(request, 'students/signup.html', {'form': form})