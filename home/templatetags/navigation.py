# -*- coding: utf-8 -*-
from django import template
from django.utils import translation

register = template.Library()

@register.assignment_tag(takes_context=True)
def get_site_root(context):
    # NB this returns a core.Page, not the implementation-specific model used
    # so object-comparison to self will return false as objects would differ
    return context['request'].site.root_page

# Retrieves the top menu items - the immediate children of the parent page
# The has_menu_children method is necessary because the Foundation menu requires
# a dropdown class to be applied to a parent
@register.inclusion_tag('tags/sidebar_categories.html', takes_context=True)
def side_menu(context, parent, calling_page=None):
    menuitems = parent.get_children().live().in_menu()
    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }

@register.filter(name='addcss')
def addcss(field, css):
   return field.as_widget(attrs={"class":css})
