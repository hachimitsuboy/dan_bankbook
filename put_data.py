from firebase_admin import firestore
import uuid
def put_data(date, deposit, withdraw, interest, total, sign): 
    # 下のファイルは先程ダウンロードした秘密鍵のパスを入れてください
    print('入力内容', date, deposit, withdraw, interest, total, sign)
    db = firestore.client()
    doc_ref = db.collection('user').document(str(uuid.uuid1()))
    doc_ref.set({
        'date': date,
        'deposit': deposit,
        'withdraw': withdraw,
        'interest': interest,
        'total': total,
        'sign': sign
    })