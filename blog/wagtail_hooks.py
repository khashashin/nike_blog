# -*- coding: utf-8 -*-

from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)
from . models import BlogPage

class BlogPageModelAdmin(ModelAdmin):
    model = BlogPage
    menu_label = 'Write new Post'
    menu_icon = 'edit'
    menu_order = 100  # will put in 3rd place (000 being 1st, 100 2nd)
    list_display = ('title', 'date', 'last_modified')
    list_filter = ('title', 'date', 'last_modified')
    search_fields = ('title',)

modeladmin_register(BlogPageModelAdmin)
