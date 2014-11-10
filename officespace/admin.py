from django.contrib import admin
from officespace.models import office

admin.site.register(office)
#
# class PageAdmin(admin.ModelAdmin):
#     list_display = ('title', 'category', 'url')
#
# admin.site.register(Page, PageAdmin)
# admin.site.register(UserProfile)