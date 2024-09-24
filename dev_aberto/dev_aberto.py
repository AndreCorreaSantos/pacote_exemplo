import requests
import gettext
import os
import locale
from datetime import datetime
from dateutil import parser

def hello():
    
    lang = os.environ.get('LANG', 'pt_BR').split(':')[0]
    locale.setlocale(locale.LC_ALL, lang)

    locale_path = os.path.join(os.path.dirname(__file__), 'locale')
    translation = gettext.translation('messages', localedir=locale_path, languages=[lang], fallback=True)
    translation.install()
    _ = translation.gettext

    c = requests.get('https://api.github.com/repos/insper/dev-aberto/commits')
    info = c.json()
    commit_info = info[0]['commit']['author']
    date = commit_info['date']
    name = commit_info['name']


    date_parsed = parser.isoparse(date)
    date_formatted = date_parsed.strftime('%c')

    return date_formatted, name
