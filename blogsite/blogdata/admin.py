from django.contrib import admin
from .models import Blog, Tag, UserMessage
# Register your models here.

@admin.action(permissions=["change"])
def make_published(modeladmin, request, queryset):
    queryset.update(status="p")

@admin.action(permissions=["change"])
def make_draft(modeladmin, request, queryset):
    queryset.update(status="d")


class BlogAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    list_display = ["title", "slug", 'created_at', 'status', 'tags_partition', 'persian_date']
    ordering = ['-created_at']
    empty_value_display = "----"
    list_display_links = ["title"]
    prepopulated_fields = {"slug": ["title"]}
    actions = [make_published,make_draft]
    search_fields = ["title"]
    readonly_fields = ["status"]
    list_filter = ["status"]


    # list_display_links = None
    # fields = ["title", "slug"]
    # exclude = ['status']

    def tags_partition(self, obj):
        tags = ", ".join([tag.title for tag in obj.tags_published()])
        return tags


admin.site.register(Blog,BlogAdmin)
admin.site.register(Tag)
admin.site.register(UserMessage)