from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages

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
    if request.method == 'POST':
        # legacy way - html
        # username = request.POST.get('username')
        # email = request.POST.get('email')
        # message = request.POST.get('message')

        # if username is None:
        #     return HttpResponse("username cannot be empty")
        
        # Contact.objects.create(
        #     username=username,
        #     email=email,
        #     message=message,
        # )

        # return redirect('home')

        # django forms way

        form = ContactForm(request.POST)
        if form.is_valid(): 
            form.save()
            messages.success(request, 'Yout request submitted successfully!') # tags = success
            return redirect('home')
        else:
            messages.error(request, 'Failed to submit!') # bootstrap class = danger
            return redirect('contact')

    else:
        form = ContactForm()


    context = {
        'page_title':'Contact Us',
        'form':form
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
            messages.success(request, 'New Course Created Successully')
            form.save()
            return redirect('courses')
        else:
            messages.error(request, "Failed to create new course")
    else:
        form = CourseForm()
    
    context = {
        'page_title':'Create Course',
        'cats':cats,
        'form':form
    }
    return render(request, 'course_form.html', context)


# Update Course
def update_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, f'{course.title} Updated Successfully')
            return redirect('course', course_id)
        else:
            messages.error(request, 'Failed to update')
    else:
        form = CourseForm(instance=course)

    context = {
        'form':form,
        'course':course
    }

    return render(request, 'course_form.html', context)

# Delete Course
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        course.delete()
        messages.info(request, 'Course Delete Succesfully')
        return redirect('courses')
    
    context = {
        'course':course,
    }
    
    return render(request, 'confirm_delete.html', context)


def faqs(request):
    context = {
        'page_title':'FAQ',
    }
    return render(request, 'faqs.html', context)