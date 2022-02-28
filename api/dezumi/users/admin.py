from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from dezumi.users.models.UserInteractions import UserFollow, UserLike, UserInteraction
from dezumi.users.models.User import UserAchievement

User = get_user_model()


admin.site.register(UserAchievement)
class UserAchievementsInline(admin.TabularInline):
    model = UserAchievement
    extra = 1


admin.site.register(UserFollow)
class UserFollowsInline(admin.TabularInline):
    model = UserFollow
    extra = 1


admin.site.register(UserLike)
class UserLikesInline(admin.TabularInline):
    model = UserLike
    extra = 1


class UserInteractionsInline(admin.TabularInline):
    model = UserInteraction
    extra = 1 


class UserInteractionAdmin(admin.ModelAdmin):

    inlines = (UserFollowsInline, UserLikesInline)
    readonly_fields = ['user',]
    fieldsets = (
        (
            _("User - Shows"),
            {
                "fields": (
                    "shows_likes",
                    "shows_dislikes",
                    "shows_favorites",
                ),
            },
        ),
        (
            _("User - Person"),
            {
                "fields": (
                    "people_follows",
                    "people_likes",
                    "people_favorites",
                ),
            },
        ),
    )
    list_display = ["user",]
    search_fields = ["user",]


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    inlines = (UserAchievementsInline, UserInteractionsInline)
    readonly_fields = ['total_likes', 'total_followers', 'total_friends', 'level', 'experience']
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "birth_date", "country", "gender", "email")}),
        (
            _("Profile"),
            {
                "fields": (
                    "name",
                    "picture",
                    "level",
                    "experience",
                    "featured_title",
                    "is_verified",
                ),
            },
        ),
        (
            _("Statistics"),
            {
                "fields": (
                    "total_likes",
                    "total_followers",
                    "total_friends",
                ),
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_private",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "name", "level", "gins", "is_verified", "is_private"]
    search_fields = ["username", "name", "email", "first_name", "last_name"]
