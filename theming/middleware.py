import re
from django.conf import settings
from theming.core import Theme, ThemeManager

class ThemingMiddleware(object):

    theme_manager = ThemeManager()

    def process_request(self, request):
        settings.request_handler = request
        request.theme = self.theme_manager.get_default()
        theme_config = getattr(settings, 'THEME_CONFIG', None)
        if theme_config:
            try:
                host = request.get_host()
                for (regex, value) in theme_config:
                    if re.search(regex, host):
                        request.theme = self.theme_manager.get_theme(value)
                        break
            except Theme.DoesNotExist:
                pass