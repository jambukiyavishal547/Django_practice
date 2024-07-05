from django.shortcuts import render
from .models import Student, Teacher
from django.db import connection
from django.db.models import Q

# Create your views here.


# def student_list(request):
#     posts = Student.objects.filter(Q(surname__startswith='austin') 
#                                    | Q(surname__startswith='baldwin') 
#                                    | Q(surname__startswith='avery-parker'))

#     print(posts)
#     print(connection.queries)

#     return render(request, 'output.html',{'posts':posts})

# def student_list_(request):
#     posts = Student.objects.filter(classroom=1) & Student.objects.filter(age=20)
#     return render(request, 'output.html',{'posts':posts})


def student_list_(request):
    posts = Student.objects.filter(Q(surname__startswith='baldwin')& 
                                   Q(firstname__startswith='lakisha'))
    return render(request, 'output.html',{'posts':posts})


def student_list_(request):
    posts = Student.objects.all().values_list('firstname').union(Teacher.objects.all().values('firstname'))
    print(posts)
    print(connection.queries)
    return render(request, 'output.html',{'posts':posts})

#using Exclude
def student_list_(request):
    posts = Student.objects.exclude(age__gt=19)
    print(posts)
    print(connection.queries)
    return render(request, 'output.html',{'posts':posts})

def student_list_(request):
    posts = Student.objects.filter(~Q(age__gt=20) & ~Q(surname__contains='baldwin'))
    print(posts)
    print(connection.queries)
    return render(request, 'output.html',{'posts':posts})

def student_list_(request):
    posts = Student.objects.filter(classroom=1).only('firstname', 'age')
    print(posts)
    print(connection.queries)
    return render(request, 'output.html',{'data':posts})

# RAW Queries
def student_list_(request):
    # posts = Student.objects,all()
    posts = Student.objects.raw('select * from student_student ')[:2]

    print(posts)
    print(connection.queries)
    return render(request, 'output.html',{'data':posts})

#bypass orm

def dictfetchall(cursor):
    desc = cursor.description
    return [
            dict(zip([col[0] for col in desc],row))
            for row in cursor.fetchall()
    ]
def student_list(request):
    cursor = connection.cursor()
    cursor.execute('select * from student_student where age >20')
    r= dictfetchall(cursor)
    print(r)
    print(connection.queries)
    return render(request, 'output.html',{'data':r})
