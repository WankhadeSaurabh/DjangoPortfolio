from django.contrib import admin
from .models import (
    Skill,
    Project,
    Education,
    Experience,
    Certification,
    Contact,
)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "level")
    search_fields = ("name", "category")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "technologies", "created_at")
    search_fields = ("title", "technologies")
    ordering = ("-created_at",)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("degree", "institution", "year")
    search_fields = ("degree", "institution")


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("position", "company", "start_date", "end_date")
    search_fields = ("position", "company")


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("title", "organization", "issue_date")
    search_fields = ("title", "organization")


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    search_fields = ("name", "email", "subject")