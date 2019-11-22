from django.shortcuts import render
from django.http import HttpResponse

# from Database.Database import sqlite3_add_member_to_db
from .models import User
# from django.template import loader
from django.shortcuts import render
# from .templates import ProjectPython


# Create your views here.

# a test function
def test(request):
    return HttpResponse('TEST RESPONSE')


# a function to show User's homepage
def index(request):
    all_users = User.objects.all()          # connect to DB, table users
    # template = loader.get_template('user/ProjectPython/Index.html')
    context = {
        'all_users': all_users,
    }
    return render(request, 'user/ProjectPython/Index.html', context)

    # html = ''
    # for user in all_users:
    #     url = '/user/' + str(user.member_id) + '/'
    #     html += '<a href="' + url + '">' + user.first_name + ' ' + user.last_name + '</a><br>'
    # return HttpResponse(html)


# true index(sorry dos)
def true_index(request):
    return render(request, 'ProjectPython/Index.html')



# a function to show details of a user
def detail(request, member_id):
    return HttpResponse("<h2>Details for User id: " + str(member_id) + "</h2>")

def login_and_register(request):

    # if (request.POST.get('inputEmail')):


    first_name = request.POST.get('user-name')
    second_name = request.POST.get('user-surname')
    age = request.POST.get('user-age')
    gender = request.POST.get('user-gender')
    login = request.POST.get('user-login')
    password = request.POST.get('user-password')
    activity = request.POST.get('user-activity')

    # sqlite3_add_member_to_db(first_name, second_name, login, password, gender, age, activity)

    return render(request, 'ProjectPython/Sample/login.html')

