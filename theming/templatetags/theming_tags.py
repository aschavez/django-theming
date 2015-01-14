import os
from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def theme(file):
    theme_obj = settings.request_handler.theme
    media_path = os.path.join(theme_obj.media_root, file)
    theme_dev = getattr(settings, 'THEME_DEV', False)
    if not theme_dev:
        if os.path.exists(media_path):
            return os.path.join(theme_obj.media_url, file)
        else:
            static_url = getattr(settings, 'STATIC_URL', None)
            return os.path.join(static_url, file)
    else:
        return os.path.join('/themes', theme_obj.slug, 'media', file)