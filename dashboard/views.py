from django.shortcuts import render

def home(request):
    return render(request, 'dashboard/home.html')

def team_department_view(request):
    # Static data instead of database queries
    teams = []
    departments = []
    return render(request, 'dashboard/team_department.html', {
        'teams': teams,
        'departments': departments
    })

def welcome(request):
    return render(request, 'dashboard/welcome.html')

def view_user(request):
    # Static data
    users = []
    return render(request, 'dashboard/view_user.html', {'users': users})

def view_session(request):
    # Static data
    sessions = []
    return render(request, 'dashboard/view_session.html', {'sessions': sessions})