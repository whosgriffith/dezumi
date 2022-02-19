from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from dezumi.others.models.Individuals import Person, PersonVisual, Character, CharacterVisual

@admin.register(PersonVisual)
class PersonMediaAdmin(admin.ModelAdmin):

    fieldsets = (
        (_("Personal info"), {"fields": ("person",)}),
        (None, {"fields": ("file",)}),
    )
    list_display = ["full_name", "file"]
    search_fields = ["full_name",]
    # def full_name used for display of fk attributes (More: https://stackoverflow.com/a/7063318)
    def full_name(self, obj):
        return obj.person

class PersonVisualInline(admin.TabularInline):
    model = PersonVisual
    extra = 1


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):

    inlines = (PersonVisualInline,)
    readonly_fields = ['total_likes', 'total_followers', 'total_favorites']
    fieldsets = (
        (_("Personal info"), {"fields": ("first_name", "last_name", "birth_date", "country", "gender")}),
        (
            _("Statistics"),
            {
                "fields": (
                    "total_likes",
                    "total_followers",
                    "total_favorites",
                ),
            },
        ),
    )
    list_display = ["first_name", "last_name", "country", "gender"]
    search_fields = ["first_name", "last_name"]


@admin.register(CharacterVisual)
class CharacteVisualAdmin(admin.ModelAdmin):

    fieldsets = (
        (_("Personal info"), {"fields": ("character",)}),
        (None, {"fields": ("file",)}),
    )
    list_display = ["character", "file"]
    search_fields = ["character",]


class CharacterVisualInline(admin.TabularInline):
    model = CharacterVisual
    extra = 1


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):

    inlines = (CharacterVisualInline,)
    readonly_fields = ['total_likes', 'total_dislikes', 'total_favorites']
    fieldsets = (
        (_("Personal info"), {"fields": ("full_name", "age", "height", "gender")}),
        (
            _("Statistics"),
            {
                "fields": (
                    "total_likes",
                    "total_dislikes",
                    "total_favorites",
                ),
            },
        ),
        (_("Extra info"), {"fields": ("extra_info",)}),
    )
    list_display = ["full_name", "gender", "total_likes", "total_dislikes", "total_favorites"]
    search_fields = ["full_name"]

