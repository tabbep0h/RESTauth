from django.urls import path
from . import views

urlpatterns = [
    path('students', views.StudentListViews.as_view(), name='student_list'),
    path('students/<int:pk>', views.StudentCRUDApiViews.as_view(), name='student_detail'),
    path('subjects', views.SubjectListViews.as_view(), name='subject_list'),
    path('subjects/<int:pk>', views.SubjectCRUDApiViews.as_view(), name='subject_detail'),
    path('grades', views.GradeListViews.as_view(), name='grade_list'),
    path('grades/<int:pk>', views.GradeCRUDApiViews.as_view(), name='grade_detail'),
]
