from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from dezumi.social.models.Post import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    readonly_fields = ['total_likes', 'total_comments', 'user']
    fieldsets = (
        (
            _("Post info"),
            {
                "fields": (
                    "user",
                    "content",
                    "serie",
                ),
            },
        ),
        (
            _("Statistics"),
            {
                "fields": (
                    "total_likes",
                    "total_comments",
                ),
            },
        ),
    )
    list_display = ["content", "serie", "user", "total_likes", "total_comments"]
    search_fields = ["content", "serie", "user"]
