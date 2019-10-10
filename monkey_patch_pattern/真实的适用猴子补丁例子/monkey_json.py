# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/10/10 0010 10:18
import json
from datetime import datetime as _datetime
from datetime import date as _date

class _CustomEncoder(json.JSONEncoder):
    """自定义的json解析器，mongodb返回的字典中的时间格式是datatime，json直接解析出错"""

    def default(self, obj):
        if isinstance(obj, _datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, _date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


# noinspection PyProtectedMember,PyPep8,PyRedundantParentheses
def _dumps(obj, skipkeys=False, ensure_ascii=False, check_circular=True, allow_nan=True, cls=_CustomEncoder, indent=None, separators=None,
           default=None, sort_keys=False, **kw):
    if (not skipkeys and ensure_ascii and check_circular and allow_nan and cls is None and indent is None and separators is None and default is None and not sort_keys and not kw):
        return json._default_encoder.encode(obj)
    return cls(
        skipkeys=skipkeys, ensure_ascii=ensure_ascii,
        check_circular=check_circular, allow_nan=allow_nan, indent=indent,
        separators=separators, default=default, sort_keys=sort_keys, ).encode(obj)


def monkey_patch_json():
    json.dumps = _dumps


if __name__ == '__main__':
    dictx = {'a':1,'b':_datetime.now()}
    monkey_patch_json()   # 不打猴子补丁时候，datetime是python自定义对象，不能被json序列化，程序会出错。
    print(json.dumps(dictx))