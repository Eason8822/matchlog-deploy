from django.contrib import admin
from .models import Match

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ("date", "team", "opponent", "score_for", "score_against", "result")
    list_filter = ("team", "opponent", "date")
    search_fields = ("team", "opponent", "note")

# Register your models here.
