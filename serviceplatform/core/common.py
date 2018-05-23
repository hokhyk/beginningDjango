# encoding:utf-8

from datetime import datetime
import re
import hashlib
from collections import namedtuple
from core.models import *


def datetoString(dt):
    return dt.strftime("%Y-%m-%d")


def stringtoDate(string):
    return datetime.strptime(string, "%Y-%m-%d")


def generate_md5(string):
    hl = hashlib.md5()
    hl.update(string.encode(encoding='utf-8'))
    return hl.hexdigest()


# check format
def check_id_card(id_card):
    if id_card:
        if len(id_card) == 18:
            m = re.match(r'^[1-9]\d{5}(18|19|([23]\d))\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$',id_card)
            return True if m else False

        else:
            return False

    else:
        return False


def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]



