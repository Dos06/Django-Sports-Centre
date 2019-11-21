from django.shortcuts import render
from django.http import HttpResponse
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


# a function to show details of a user
def detail(request, member_id):
    return HttpResponse("<h2>Details for User id: " + str(member_id) + "</h2>")
