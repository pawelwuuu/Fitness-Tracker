from django.contrib import admin
from .models import ExerciseTip

@admin.register(ExerciseTip)
class ExerciseTipAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('title', 'content')