import json
import os


BASE_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = './data/worker.json'
DATA_PATH = os.path.join(BASE_ROOT_DIR, FILE_PATH)
USERS = 'users'


# 例として使用する辞書データ
DATA_STRUCT = {
    USERS: {
    }
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

    def update_user_data(self, user_id, key, value):
        """特定のユーザーデータを更新する"""
        if USERS in self.data and user_id in self.data[USERS]:
            self.data[USERS][user_id][key] = value
            self.save_data()

    def generate_unique_user_id(self):
        """利用可能な最小の整数型ユーザーIDを生成する"""
        existing_ids = set(int(uid) for uid in self.data.get(USERS, {}).keys())
        new_id = 1
        while new_id in existing_ids:
            new_id += 1
        return new_id

    def add_user(self, name=None, mail_ad=None, age=None):
        """新しいユーザーを追加する。ユーザーIDは自動で生成される"""
        user_id = self.generate_unique_user_id()
        user_data = {
            "name": name if name is not None else None,
            "age": age if age is not None else None,
            "email": mail_ad if mail_ad is not None else None,
            "is_member": True
        }

        if USERS not in self.data:
            self.data[USERS] = {}
        self.data[USERS][user_id] = user_data  # IDを文字列として保存
        self.save_data()
        return user_id  # 追加されたユーザーIDを返す    

    def remove_user(self, user_id):
        """ユーザーを削除する"""
        if USERS in self.data and user_id in self.data[USERS]:
            del self.data[USERS][user_id]
            self.save_data()

    def save_data(self):
        """データをファイルに保存する"""
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)