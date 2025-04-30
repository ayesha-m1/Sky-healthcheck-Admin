from django.shortcuts import render

def home(request):
    return render(request, 'dashboard/home.html')
<<<<<<< HEAD

def team_department_view(request):
    # Static data instead of database queries
    teams = []
    departments = []
    return render(request, 'dashboard/team_department.html', {
        'teams': teams,
        'departments': departments
    })
=======
from django.shortcuts import render
from .models import Team, Department,TeamMember  # Make sure this matches your models

def team_department_view(request):
    teams = Team.objects.all().select_related('department').prefetch_related('members')
    departments = Department.objects.all()
    
    context = {
        'teams': teams,
        'departments': departments,
    }
    return render(request, 'dashboard/team_department.html', context)
>>>>>>> 094fb77 (DATA BASE ADDED FOR DATA)

def welcome(request):
    return render(request, 'dashboard/welcome.html')

def view_user(request):
    # Static data
    users = []
    return render(request, 'dashboard/view_user.html', {'users': users})

def view_session(request):
    # Static data
    sessions = []
<<<<<<< HEAD
    return render(request, 'dashboard/view_session.html', {'sessions': sessions})
=======
    return render(request, 'dashboard/view_session.html', {'sessions': sessions})

def login(request):
    # Static data
    login = []
    return render(request, 'dashboard/login.html', {'login': login})

def signup(request):
    # Static data
    signup = []
    return render(request, 'dashboard/signup.html', {'signup': signup})

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from .models import Team, TeamMember
import json

@require_GET
def team_members(request):
    team_id = request.GET.get('team_id')
    try:
        team = Team.objects.get(pk=team_id)
        members = team.members.all()
        return JsonResponse({
            'members': [{'name': member.name} for member in members]
        })
    except Team.DoesNotExist:
        return JsonResponse({'error': 'Team not found'}, status=404)

@csrf_exempt
@require_POST
def add_member(request):
    try:
        data = json.loads(request.body)
        team_id = data.get('team_id')
        name = data.get('name')
        
        team = Team.objects.get(pk=team_id)
        TeamMember.objects.create(team=team, name=name)
        
        return JsonResponse({'success': True})
    except Team.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Team not found'}, status=404)
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)

@csrf_exempt
@require_POST
def delete_team(request):
    try:
        data = json.loads(request.body)
        team_id = data.get('team_id')
        
        team = Team.objects.get(pk=team_id)
        team.delete()
        
        return JsonResponse({'success': True})
    except Team.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Team not found'}, status=404)
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)
>>>>>>> 094fb77 (DATA BASE ADDED FOR DATA)
