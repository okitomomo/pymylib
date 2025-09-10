from mylib import EnvLoader

def test_env_load():
    el = EnvLoader()
    assert el.load("ログ出力", "IS_OUT_LOG_I") == True
    assert el.load("テスト", "IS_OUT_LOG_T") == False

def test_env_get():
    el = EnvLoader()
    assert el.get("TEST") == ""
    assert el.load("ログ出力", "IS_OUT_LOG_I") == True
    assert el.get("IS_OUT_LOG_I") == "TRUE"
