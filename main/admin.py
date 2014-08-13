from django.contrib import admin

# # Import the UserProfile model individually.
from main.models import Bookmark, Tag, UserProfile


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('url', 'title', 'owner', 'date_updated')
    list_filter = ('owner',)
    search_fields = ['url', 'title', 'description']
    readonly_fields = ('date_created', 'date_updated')


admin.site.register(UserProfile)
admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Tag)
