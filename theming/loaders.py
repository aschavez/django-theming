import os
from django.conf import settings
from django.template.loaders.filesystem import Loader

class ThemeLoader(Loader):

    def get_template_sources(self, template_name, template_dirs=None):

        if not template_dirs:
            request = getattr(settings, 'request_handler', None)
            if request:
                template_dirs = (request.theme.template_dir,)

        return super(ThemeLoader, self).get_template_sources(
            template_name, template_dirs)