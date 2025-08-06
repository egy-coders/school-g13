from django.db import models

"""
Courses (category - title - description - price - pub_date - level)
Students
Categories (Web - Network)

ORM 
courses = Course.objects.all()


relationships
one-to-one
one-to-many
many-to-many

one to many
one category -> *courses
one course -> one category
one to *

one student -> * courses
* students <- one course
many-to-many
"""

class Category(models.Model):
    name = models.CharField(max_length=150, unique=True) # #1 Web Developement (Django - ReactJs - ...) - #2 Data Science - #3 Marketing

    class Meta:
        verbose_name_plural = 'Categories' # Categroys 

    def __str__(self):
        return f"{self.name}"

class Course(models.Model): # Courses Table in database core_course
    LEVEL_CHOICES = (
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advacned', 'Advacned'),
    )
    cat = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='courses') # one-to-many (Web Develope | Networking) | cat_id = 1 , 2 , 3
    title = models.CharField(max_length=200, unique=True) # default (required) not nullable | string
    description = models.TextField() # Big string
    level = models.CharField(choices=LEVEL_CHOICES)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00) # 159.99 $ | Decimals digits
    pub_date = models.DateField(null=True, blank=True)

    image = models.ImageField(upload_to='courses', default='default.png', blank=True) # png, jpg | max_size: 2MB

    class Meta: # options 
        # db_table = 'my_courses'
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        # unique_together = 
        get_latest_by = 'pub_date'


    def __str__(self):
        return f"{self.title}"
    

"""
Omar (CCNA - Python - C++)
"""
class Student(models.Model):
    name = models.CharField(max_length=200)
    dob = models.DateField()
    courses = models.ManyToManyField(Course, through='Enrollment')
    image = models.ImageField(upload_to='students', default='avatar.png')

    """
    # Student - Course (M2M) 2 relations 1 -> *
        student_courses (Omar - Python - 94 | Omar - C++ - 85)
    """

    def __str__(self):
        return f"{self.name}"
    
    """
    Omar - Python - scroe: 94
    """

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    scroe = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.student} | {self.course} | {self.scroe}%"
    
    class Meta:
        unique_together = ['student', 'course']

# class User(models.Model):
#     username = 
#     email = 
#     phone = 
#     image = 
#     student = models.OneToOneField(Student)