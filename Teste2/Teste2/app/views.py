from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import School, Student, Test, Question, Answer, TestResult
from django.template import loader
from django.contrib.auth.models import User

def index(request):
    schools = School.objects.all()
    return render(request, 'app/index.html', {'schools': schools})

def school_detail(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    return render(request, 'app/school_detail.html', {'school': school})


def schools_list(request):
    schools = School.objects.all()
    return render(request, 'schools_list.html', {'schools': schools})

def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'app/student_detail.html', {'student': student})

def students(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'app/students.html', context)

def create_student_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        school_id = request.POST.get('school_id')
        sex = request.POST.get('sex')
        year = request.POST.get('year')
        student = Student(first_name=first_name, last_name=last_name, date_of_birth=date_of_birth, school_id=school_id, sex=sex, year=year)
        student.save()
        return redirect('index')
    schools = School.objects.all()
    return render(request, 'app/create_student.html', {'schools': schools})

def create_school_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        contact_number = request.POST.get('contact_number')
        new_school = School(name=name, address=address, contact_number=contact_number)
        new_school.save()
        return redirect('index')
    return render(request, 'app/create_school.html')

def escola_view(request):
    schools = School.objects.all()
    context = {'schools': schools}
    return render(request, 'app/Escola.html', context)

def aluno_view(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'app/Aluno.html', context)

def test_detail(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    questions = Question.objects.filter(test=test)
    return render(request, 'app/test_detail.html', {'test': test, 'questions': questions})

def take_test(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    questions = Question.objects.filter(test=test)
    if request.method == 'POST':
        score = 0
        for question in questions:
            selected_answer_id = request.POST.get(f'question_{question.id}', None)
            if selected_answer_id is not None:
                selected_answer = get_object_or_404(Answer, pk=selected_answer_id)
                if selected_answer.is_correct:
                    score += 1
        total_questions = questions.count()
        student_id = request.user.student.id
        TestResult.objects.create(student_id=student_id, test=test, score=score, total_questions=total_questions)
        return HttpResponseRedirect('/results/')
    return render(request, 'app/take_test.html', {'test': test, 'questions': questions})

def delete_student_view(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('index')

def delete_school_view(request, school_id):
    school = get_object_or_404(School, id=school_id)
    if request.method == 'POST':
        school.delete()
        return redirect('index')
    return render(request, 'index')

def results(request):
    student_id = request.user.student.id
    results = TestResult.objects.filter(student_id=student_id)
    return render(request, 'app/results.html', {'results': results})