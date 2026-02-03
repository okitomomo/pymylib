from enum import Enum
from setuptools._distutils.util import strtobool
import os
import datetime

t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')

class LogType(Enum):
    """ログ種類のEnum列挙体"""
    I = "I"
    W = "W"
    E = "E"
    D = "D"

_TYPES = {
    LogType.I.value : {"print": True, "pre": "[INFO ]"},
    LogType.W.value : {"print": True, "pre": "[WARN ]"},
    LogType.E.value : {"print": True, "pre": "[ERROR]"},
    LogType.D.value : {"print": True, "pre": "[DEBUG]"},
}
"""ログ種類ごとの定義情報"""

def setup_log():
    """ログ種類ごとの出力有無をenvファイルから設定"""
    global _TYPES
    for type in LogType:
        val = os.environ.get("IS_OUT_LOG_" + type.value, "FALSE").strip()
        is_out_log = strtobool(val)
        _TYPES[type.value]["print"] = is_out_log

def log(type: LogType, msg: str):
    """コンソールログをprintする

    Args:
        type (LogType): ログ種類
        msg (str): 出力メッセージ
    """
    if not _TYPES[type.value]["print"] :
        return
    
    now = datetime.datetime.now(JST)
    d = now.strftime('%y/%m/%d %H:%M:%S')

    print( f"[{d}]"+ _TYPES[type.value]["pre"] + msg, flush=True)
