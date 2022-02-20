from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from dezumi.users.models.User import Follow, Like, UserAchievement

User = get_user_model()


class UserAchievementsInline(admin.TabularInline):
    model = UserAchievement
    extra = 1


admin.site.register(Follow)
class FollowsInline(admin.TabularInline):
    model = Follow
    extra = 1
    fk_name = "follower"


admin.site.register(Like)
class LikesInline(admin.TabularInline):
    model = Like
    extra = 1
    fk_name = "liker"


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    inlines = (UserAchievementsInline, FollowsInline, LikesInline)
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
            _("Shows"),
            {
                "fields": (
                    "shows_likes",
                    "shows_dislikes",
                    "shows_favorites",
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
