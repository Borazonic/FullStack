"""
URL configuration for SWEBackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from StudentFeedbackApp.views import CSRFTokenView,StudentReviewCreate,TeacherListCreate,TeacherDetail,StudentDetail,StudentListCreate,ReviewList,ReviewDetail,UserLogin,UserSignup
from django.urls import path

urlpatterns = [
<<<<<<< HEAD
    path('', views.homepage, name='homepage'),
    path('students', views.student_manage, name='student-manage'),  # Redirect to student management page by default
    path('students/<int:pk>/', views.delete_student, name='delete-student'),
    path('teachers/', views.teacher_manage, name='teacher-manage'),
    path('teachers/create/', views.create_teacher, name='create-teacher'),
    path('teachers/<int:pk>/delete/', views.delete_teacher, name='delete-teacher'),
    path('students/create/', views.create_student, name='create-student'),
    path('reviews/', views.review_list, name='review-list'),
    path('reviews/student/', views.student_reviews, name='student-reviews'),
    path('reviews/create/<int:teacher_id>/', views.create_review, name='create-review'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('students/<int:pk>/delete/', views.delete_student, name='delete_student'),  # Define URL pattern for deleting a student
=======
    path('admin/', admin.site.urls),
    path('student-review/', StudentReviewCreate.as_view(), name='student-review-create'),
    path('teachers/', TeacherListCreate.as_view(), name='teacher-list-create'),
    path('teachers/<int:pk>/', TeacherDetail.as_view(), name='teacher-detail'),
    path('students/<int:pk>/', StudentDetail.as_view(), name='student-detail'),
    path('students/', StudentListCreate.as_view(), name='student-list-create'),
    path('reviews/', ReviewList.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    path('login/', UserLogin.as_view(), name='user-login'),
    path('signup/', UserSignup.as_view(), name='user-signup'),
    path('get-csrf-token/', CSRFTokenView.as_view(), name='get_csrf_token'),
>>>>>>> 51c909ada6ff0ba4f73337b943b67ca149b3ea87
]

