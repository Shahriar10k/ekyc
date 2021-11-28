from django.shortcuts import render,redirect
from pages.filters import courseFilter
from entries.models import Course
from entries.forms import Course_form
from django.contrib import messages

mydata = {} # dictionary to store session data

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def CourseList(request):

    course_list = Course.objects.all().order_by('couse_code')
    coFilter = courseFilter(request.GET, queryset=course_list)
    course_list = coFilter.qs

    context = {'course_list': course_list, 'coFilter': coFilter}
    return render(request, 'pages/course_list.html',context)

def updateCourse(request): 

    #if POST coming from student list "edit" button then fetch intance using course_code
    if 'courseCode' in request.POST:
        course_code = request.POST.get('courseCode')
        print(course_code)
        course = Course.objects.get(couse_code=course_code)
        form = Course_form(instance=course)
        mydata['courseCode'] = course_code        
    #if POST coming from editing the form then fetch instance using globally stored course_code
    else:
        course_code = mydata['courseCode']
        course = Course.objects.get(couse_code=course_code)
        form = Course_form(instance=course)
    context = {'form': form, 'course':course}    

    if request.method == 'POST' :
        form = Course_form(request.POST, instance=course)

        if form.is_valid():
            form.save()
            messages.success(request, "Course Info Updated")
            return redirect('course_list')

    return render(request, 'pages/update_course.html', context)

def deleteCourse(request):
    if 'id' in request.POST:
        course_id = request.POST.get('id')
        #print(stu_id)

    course = Course.objects.get(couse_code=course_id)
    course.delete()

    messages.success(request, f'Course Successfully Deleted.')
    return redirect('course_list')

def createCourse(request):
    form1 = Course_form()

    if request.method == 'POST':
        form1 = Course_form(request.POST)
        if form1.is_valid():
            form1.save()

            messages.success(request, "Course Information Added.")
            return redirect('course_list')

    context = {'form1': form1, }

    return render(request, 'pages/add_course.html', context)