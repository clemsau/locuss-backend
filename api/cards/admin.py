from django.contrib import admin
from .models import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('deck', 'front_text', 'back_text',)
    ordering = ['created_at']
    pass
