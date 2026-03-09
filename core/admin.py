from django.contrib import admin
from .models import Project, Skill, ContactMessage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display  = ('title', 'category', 'order', 'is_visible', 'created_at')
    list_filter   = ('category', 'is_visible')
    list_editable = ('order', 'is_visible')
    search_fields = ('title', 'description', 'tags')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display  = ('name', 'emoji', 'level', 'order')
    list_editable = ('order', 'level')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display  = ('name', 'email', 'subject', 'is_read', 'created_at')
    list_filter   = ('is_read',)
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    list_editable = ('is_read',)
