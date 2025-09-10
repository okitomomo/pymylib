from enum import Enum
from mylib.env_loader import * 
from distutils.util import strtobool
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

def _loadEnv():
    """envファイルの読み込み"""
    global el
    el = EnvLoader()
    for type in LogType:
        el.load(f"ログ出力[{type.value}]", "IS_OUT_LOG_" + type.value)

def _loadTypes():
    """ログ種類ごとの出力有無をenvファイルから設定"""
    global _TYPES
    for type in LogType:
        is_out_log = strtobool(el.get("IS_OUT_LOG_" + type.value))
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

# ログ出力使用の準備
_loadEnv()
_loadTypes()
    