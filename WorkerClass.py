##すべてのデータ操作はuser_idメインで行う
import json
import os


BASE_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = './data/worker.json'
DATA_PATH = os.path.join(BASE_ROOT_DIR, FILE_PATH)

USERS_ID_DATA_REF = 'users_id'
USERS_DATA_REF = 'users_data'

USER_WORK_LEVEL_REF = "level"
USER_PRIORITY_TIME = "優先時間"
USER_PRIORITY_CLASS = "担当クラス"

# 例として使用する辞書データ
DATA_STRUCT = {
    USERS_ID_DATA_REF: {
    },
    USERS_DATA_REF: {
    }
}

#データ構造
user_data_struct = {
    USER_WORK_LEVEL_REF: None, #猛者、普通、新人、パートで分ける
    USER_PRIORITY_TIME: None,
    USER_PRIORITY_CLASS: None,
}

# JSONファイルに書き込む関数を、ディレクトリの存在を確認して必要に応じて作成するように修正
def Init_Data_File(file_path, data):
    # ファイルパスからディレクトリ部分を取得
    directory = os.path.dirname(file_path)

    # ディレクトリが存在しない場合は作成
    if not os.path.exists(directory):
        os.makedirs(directory)

    # ファイルにデータを書き込む
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


class WorkerDataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self):
        """ファイルからデータをロードする"""
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        else:
            return {}

    def generate_unique_user_id(self):
        """利用可能な最小の整数型ユーザーIDを生成する""" ##randam生成にするか迷う
        existing_ids = set(int(uid) for uid in self.data.get(USERS_DATA_REF, {}).keys())
        new_id = 1
        while new_id in existing_ids:
            new_id += 1
        return new_id

    def add_user_id(self, name):
        """ユーザーを追加し、IDを割り当てる"""
        user_id = self.generate_unique_user_id() #idを生成
        self.data[USERS_ID_DATA_REF][user_id] = name #idを追加
        self.data[USERS_DATA_REF][user_id] = user_data_struct #データを追加
        self.save_data()
        return

    def remove_user(self, user_id):
        """ユーザーを削除する"""
        if USERS_ID_DATA_REF in self.data and user_id in self.data[USERS_ID_DATA_REF]:
            del self.data[USERS_ID_DATA_REF][user_id]
        if USERS_DATA_REF in self.data and user_id in self.data[USERS_DATA_REF]:
            del self.data[USERS_DATA_REF][user_id]
            self.save_data()

    def update_user_data(self, user_id, key, value):
        """特定のユーザーデータを更新する"""
        if USERS_DATA_REF in self.data and user_id in self.data[USERS_DATA_REF]:
            self.data[USERS_DATA_REF][user_id][key] = value
            self.save_data()

    def save_data(self):
        """データをファイルに保存する"""
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)


