from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Student, Teacher, Review
from .forms import StudentForm, TeacherForm, ReviewForm, LoginForm
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_staff:  # Check if the user is an admin
                    return redirect('admin_dashboard')  # Redirect admin to admin dashboard
                else:
                    return redirect('student_dashboard')  # Redirect student to student dashboard
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user_role = request.POST.get('user_role')  # Get the selected user role from the form
            if user_role == 'student':
                user.save()  # Save the user
                Student.objects.create(user=user)  # Create a student profile for the user
            elif user_role == 'staff':
                user.is_staff = True  # Mark the user as staff
                user.save()  # Save the user
            login(request, user)
            return redirect('homepage')  # Redirect to homepage after signup
    else:
        form = StudentForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def create_review(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.teacher = teacher
            review.student = request.user.student
            review.save()
            return redirect('teacher_detail', pk=teacher_id)
    else:
        form = ReviewForm()

    return render(request, 'create_review.html', {'form': form, 'teacher': teacher})

@login_required
def create_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_manage')  # Redirect to teacher management page after creating teacher
    else:
        form = TeacherForm()
    return render(request, 'create_teacher.html', {'form': form})

@login_required
def delete_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    teacher.delete()
    return redirect('teacher_manage')  # Redirect to teacher management page after deleting teacher

@login_required
def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_manage')  # Redirect to student management page after creating student
    else:
        form = StudentForm()
    return render(request, 'create_student.html', {'form': form})

@login_required
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_manage')  # Redirect to student management page after deleting student

@login_required
def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'review_list.html', {'reviews': reviews})

def teacher_manage(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_manage.html', {'teachers': teachers})

def student_manage(request):
    students = Student.objects.all()
    return render(request, 'student_manage.html', {'students': students})

def student_reviews(request):
    student = request.user.student
    reviews = Review.objects.filter(student=student)
    return render(request, 'student_reviews.html', {'reviews': reviews})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

def homepage(request):
    return render(request, 'index.html')