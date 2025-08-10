from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# from django.shortcuts import HttpResponse

# def home(request): # http request
#     return HttpResponse("Welcome Home Page") # for testing

# def about(request):
#     return HttpResponse("About Page")

def home(request):
    # courses = Courses.objects.all() # get all courses
    # ORM select * where active
    # Lists
    products = [
        {
            'id':1,
            'title':'Shoes',
            'price':120
        }
    ]
    students = [
        {
            'id':1,
            'name':'Farid',
            'age':35,
            'grade':'1st',
            'active':True
        },
        {
            'id':2,
            'name':'Mohamed',
            'age':25,
            'grade':'2nd',
            'active':True
        },
        {
            'id':3,
            'name':'Reham',
            'age':20,
            'grade':'4th',
            'active':False
        },
        {
            'id':4,
            'name':'Asser',
            'age':25,
            'grade':'1st',
            'active':False
        },
    ]
    print(students)
    context = {
        'name':'Ahmed',
        'age':30,
        'address':'Cairo',
        'active':True,
        'students':students,
        'phone':'01099354656',
        'products':products,

        'page_title':'Home Page',
    }
    # DTL - jijna templates
    return render(request, 'home.html', context)

def about(request):
    context = {
        'page_title':'About Us',
    }
    return render(request, 'about.html', context)


def contact(request):
    context = {
        'page_title':'Contact Us',
    }
    
    return render(request, 'contact.html', context)

def cats(request):
    cats = Category.objects.all()
    context = {
        'page_title' : 'Categories',
        'name' : 'Omar',
        'cats':cats
    }
    return render(request, "cats.html", context)

# List Courses
def courses(request):
    courses = Course.objects.all()
    context = {
        'page_title':'Courses',
        'courses':courses
    }
    return render(request, 'courses.html', context)

# Single Course # 
def course(request, course_id):
    course = get_object_or_404(Course, id=course_id) # single object
    context = {
        'page_title':course.title,
        'course':course
    }
    return render(request, 'course_details.html', context)
    
# Create Course
def create_course(request):
    cats = Category.objects.all()

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data.items)
            form.save()
        return redirect('courses')
    else:
        form = CourseForm()
    
    context = {
        'page_title':'Create Course',
        'cats':cats,
        'form':form
    }
    return render(request, 'create_course.html', context)

# Update Course

# Delete Course


def faqs(request):
    context = {
        'page_title':'FAQ',
    }
    return render(request, 'faqs.html', context)