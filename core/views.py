from django.shortcuts import render

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

def courses(request):
    courses = [
        {
            'id':1,
            'title':'Python for begginers',
            'description': 'Some description for python courses ',
            'price':220,
            'featured':True
        },
        {
            'id':2,
            'title':'OOP using Java',
            'description': 'Some description for Java programming language courses ',
            'price':120,
            'featured':False,
        },
    ]
    context = {
        'page_title':'Courses',
        'courses':courses
    }
    return render(request, 'courses.html', context)


def faqs(request):
    context = {
        'page_title':'FAQ',
    }
    return render(request, 'faqs.html', context)