#!/usr/bin/env python3
from dev_aberto import hello
import gettext
import os
import locale

if __name__ == '__main__':

    lang = os.environ.get('LANGUAGE', 'en_US').split(':')[0]
    locale.setlocale(locale.LC_ALL, lang)

    locale_path = os.path.join(os.path.dirname(__file__), 'locale')
    translation = gettext.translation('messages', localedir=locale_path, languages=[lang], fallback=True)
    translation.install()
    _ = translation.gettext

    date, name = hello()
    print(_('Último commit feito em:'), date, _('por'), name)
