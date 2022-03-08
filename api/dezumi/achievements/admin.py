from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from dezumi.achievements.models.Achievement import Achievement


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {"fields": ("title", "description", "badge")}),
    )
    list_display = ["title", "description", "badge"]
    search_fields = ["title", "description"]
