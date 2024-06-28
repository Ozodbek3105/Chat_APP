import json
from ctypes import Union


def malumotni_formatla(habar=None, kimga=None, kirdi=None, habar_turi=1, foydalanuvchi:(list | str) = None):
    data = {'habar_turi': habar_turi,
            'kimdan': foydalanuvchi,
            'kimga': kimga,
            'user_id': None,
            'habar': habar,
            'kirdi': kirdi
            }
    return json.dumps(data).encode('utf-8')
