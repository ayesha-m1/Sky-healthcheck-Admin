from django.contrib import admin
from .models import Department, Team, TeamMember

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')
    list_filter = ('department',)

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'team')
    list_filter = ('team',)

    from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Team, Department, TeamMember, Session

admin.site.register(User, UserAdmin)
admin.site.register(Team)
admin.site.register(Department)
admin.site.register(TeamMember)
admin.site.register(Session)