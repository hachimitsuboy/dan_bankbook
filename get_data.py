from firebase_admin import firestore
def get_data():

  # 下のファイルは先程ダウンロードした秘密鍵のパスを入れてください
  db = firestore.client()
  users = db.collection('user')  
  docs = users.get()
  return docs