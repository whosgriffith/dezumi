from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from dezumi.others.models.Individual import Person, PersonMedia

@admin.register(PersonMedia)
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

class MediaInline(admin.TabularInline):
    model = PersonMedia
    extra = 1


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):

    inlines = (MediaInline,)
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
