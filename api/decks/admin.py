from django.contrib import admin
from .models import Deck


@admin.register(Deck)
class DeckAdmin(admin.ModelAdmin):
    list_display = ('title', 'front_label', 'back_label', 'owner',)
    ordering = ['created_at']
    pass
