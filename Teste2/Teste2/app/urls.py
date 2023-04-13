from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('school_detail/<int:school_id>/', views.school_detail, name='school_detail'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
    path('test_detail/', views.test_detail, name='test_detail'),
    path('test_detail/<int:test_id>', views.test_detail, name='test_detail'),
    path('take_test/<int:test_id>/', views.take_test, name='take_test'),
    path('results/', views.results, name='results'),
    path('Escola/', views.escola_view, name='escola_view'),
    path('create_student/', views.create_student_view, name='create_student'),
    path('Aluno/', views.aluno_view, name='aluno_view'),
    path('create_school/', views.create_school_view, name='create_school'),
    path('student/<int:student_id>/delete/', views.delete_student_view, name='delete_student'),
    path('school/', views.schools_list, name='schools_list'),
    path('school/<int:school_id>/delete/', views.delete_school_view, name='delete_school')
]