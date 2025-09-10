import os
from dotenv import load_dotenv
import os
from pathlib import Path

class EnvLoader:
    """環境変数読み込み
    """
    
    def __init__(self, env_path=None):
        """コンストラクタ

        Args:
            env_path (str, optional): .envファイルのパスを指定する。指定しない場合はカレントの.envを読み込む。
        """
        # .envファイルからの読み込み
        load_dotenv(dotenv_path=env_path,override=True)
        # 値の初期化
        self.values = {}

    def load(self, display_name, key_name):
        """ 環境変数から指定されたKEY名の値を読み込む

        Args:
            display_name (str): エラー時に使用する出力名
            key_name (str): 環境変数名

        Returns:
            bool: 取得成功時 True / 取得失敗時 False
        """
        value = os.getenv(key_name)

        # 環境変数から取得失敗時
        if value is None:
            print(f"[ERROR]環境変数【{display_name}({key_name})】が取得できませんでした。")
            return False
        
        # 環境変数から取得成功時
        self.values[key_name] = value
        return True
    
    def get(self, key_name):
        """読み込んだ値を取得する

        Args:
            key_name (str): 環境変数名

        Returns:
            str: 環境変数の値
        """

        if key_name not in self.values :
            print(f"[ERROR]環境変数【{key_name}】が読み込まれていません。")
            return ""
        return self.values[key_name]
        