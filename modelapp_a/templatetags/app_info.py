from django import template

register = template.Library()

@register.assignment_tag
def get_app_name():
    app_name = "modelapp_a"
    return app_name
