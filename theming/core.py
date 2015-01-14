import json, os
from django.conf import settings


class Theme(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        
        theme_root = getattr(settings, 'THEME_ROOT', None)
        theme_media_root = getattr(settings, 'THEME_MEDIA_ROOT', None)
        theme_media_url = getattr(settings, 'THEME_MEDIA_URL', None)

        self.theme_root = os.path.join(theme_root, self.slug)
        self.media_root = os.path.join(theme_media_root, self.slug)
        self.media_url = os.path.join(theme_media_url, self.slug)
        
        self.template_dir = os.path.join(self.theme_root, 'templates')

class ThemeManager(object):

    _metadata = 'metadata.json'

    def __init__(self):
        self.theme_root = getattr(settings, 'THEME_ROOT', None)
        self.theme_default = getattr(settings, 'DEFAULT_THEME', 'default')
        self.themes = {}

    def add_theme(self, theme):
        if type(theme) is Theme:
            self.themes.update({theme.slug: theme})

    def get_theme(self, slug):
        try:
            if self.theme_root:
                metadata_path = os.path.join(
                    self.theme_root, slug, self._metadata
                )
                with open(metadata_path, 'r') as metadata:
                    theme = json.load(metadata)
                    return Theme(**theme)
            else:
                raise Exception('THEME_ROOT is not defined')
        except IOError as e:
            raise Exception(e)

    def get_default(self):
        return self.get_theme(self.theme_default)

    def search_themes(self):
        try:
            if self.theme_root:
                for (root, dirs, names) in os.walk(self.theme_root):
                    if self._metadata in names:
                        root_metadata = os.path.join(root, self._metadata)
                        with open(root_metadata, 'r') as metadata:
                            theme = json.load(metadata)
                            theme_obj = Theme(**theme)
                            self.add_theme(theme_obj)
                return self.themes
            else:
                raise Exception('THEME_ROOT is not defined')
        except IOError:
            raise Exception('Metadata is malformed')