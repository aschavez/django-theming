# -*- coding: utf-8 -*-
import shutil, os, errno

from optparse import make_option
from django.core.management.base import CommandError, BaseCommand
from django.utils.six.moves import input

from theming.core import ThemeManager

class Command(BaseCommand):

    theme_manager = ThemeManager()

    option_list = BaseCommand.option_list + (
        make_option('-l', '--link',
            action='store_true',
            dest='link',
            default=False,
            help='Create a symbolic link to each file instead of copying.'),
        make_option('-f', '--force',
            action='store_true',
            dest='force',
            default=False,
            help='Force to overwrite content.'),
    )

    def set_options(self, **options):
        self.link = options['link']
        self.force = options['force']

    def handle(self, *args, **options):
        self.set_options(**options)

        themes = self.theme_manager.search_themes()
        for key, theme in themes.iteritems():
            src = os.path.join(theme.theme_root, 'media')
            dest = theme.media_root
            self._copy_directory(src, dest, self.link, self.force)

    def _copy_directory(self, src, dest, use_symlinks=False, use_force=False):
        try:
            if use_force:
                shutil.rmtree(dest)
            shutil.copytree(src, dest, use_symlinks)
        except shutil.Error as e:
            print('Directory not copied. Error: %s' % e)
        except OSError as e:
            print('Directory not copied. Error: %s' % e)
            if e.errno == errno.EEXIST:
                message = ['\n']
                message.append('There are existing files in the destination.\n')
                message.append('Do you want to delete the destination\'s contents?.\n')
                message.append('Type y/n.\n')
                if input(''.join(message)) != 'y':
                    raise CommandError("Collecting themes files cancelled.")
                self.force = True
                self._copy_directory(src, dest, use_symlinks, True)