from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from dezumi.shows.models import Show, PersonShow, ShowVisual, Studio

admin.site.register(Studio)
admin.site.register(ShowVisual)


admin.site.register(PersonShow)
class PersonShowInline(admin.TabularInline):
    model = PersonShow
    extra = 1


@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):

    inlines = (PersonShowInline,)
    readonly_fields = ['total_likes', 'total_favorites', 'total_completed', 'total_watching', 'total_dropped', 'total_plan', 'total_reviews', 'total_recommended', 'total_not_recommended']
    fieldsets = (
        (
            _("Show info"),
            {
                "fields": (
                    "title",
                    "key_art",
                    "synopsis",
                    "airing",
                    "season",
                    "characters",
                    "studio",
                    "release_date",
                    "episodes",
                    "duration",
                    "show_type",
                    "visuals",
                ),
            },
        ),
        (
            _("Statistics"),
            {
                "fields": (
                    "total_likes",
                    "total_favorites",
                    "total_completed",
                    "total_watching",
                    "total_dropped",
                    "total_plan",
                    "total_reviews",
                    "total_recommended",
                    "total_not_recommended",
                ),
            },
        ),
    )
    list_display = ["title", "season", "studio", "episodes", "airing", "total_likes", "total_favorites", "total_completed"]
    search_fields = ["title", "studio", "show_type"]
