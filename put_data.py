import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime


def put_data(): 
    # 下のファイルは先程ダウンロードした秘密鍵のパスを入れてください
    cred = credentials.Certificate("./dan-bankbook-firebase-adminsdk-hjd6u-8c0fe69935.json")
    firebase_admin.initialize_app(cred) 
    db = firestore.client()

    users = db.collection('user') # 'users'の情報を取得
    docs = users.stream()

    for doc in docs:
        print(doc.to_dict())

    doc_ref = db.collection('user').document()
    doc_ref.set({
        'date': datetime.datetime.now(),
        'deposit': '10',
        'withdraw': '5',
        'interest': '3',
        'total': '8',
        'sign': 'nagae'
    })