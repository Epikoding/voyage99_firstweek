from pymongo import MongoClient
import jwt
import datetime
import hashlib
from flask import Flask, render_template, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
import certifi
ca = certifi.where()

# client = MongoClient('mongodb+srv://test:sparta@cluster0.feuh6.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca) #minsu
client = MongoClient('mongodb+srv://test:sparta@sparta.eacl0.mongodb.net/sparta?retryWrites=true&w=majority', tlsCAFile=ca) #동재

db = client.dbfirstweek
app = Flask(__name__)

# 비밀 키 설정
SECRET_KEY = 'SPARTA'
# page 구분선 =========================================================================================


# main 페이지 호출
@app.route('/')
def home():
    return render_template('index.html')


# 로그인 페이지 이동
@app.route('/login')
def login():
    return render_template('login.html')

# 회원 가입 페이지 이동
@app.route('/join')
def join():
    return render_template('join.html')

# my짤 페이지 이동
@app.route('/posts/mine', methods=["GET"])
def mine():
    return

# 짤 데이터 DB에 저장
@app.route('/upload', methods=["POST"])
def upload():
    return

# 태그 비교 하여 불러 오기
@app.route('/posts/tag', methods=["GET"])
def posts_tag():
    return

# 검색 하여 데이터 불러 오기
@app.route('/posts/search', methods=["GET"])
def posts_search():
    return

# page 구분선 =========================================================================================


# 로그인
@app.route('/login', methods=["POST"])
def sign_in():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()  # 패스워드 암호화
    result = db.users.find_one({'id': id_receive, 'pw': pw_hash})  # 동일한 유저가 있는지 확인

    # 동일한 유저가 있으면, 암호해독, 결과 -> 성공 및 환영인사.
    if result is not None:
        payload = {
            'id': id_receive,
            'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return jsonify({'result': 'success', 'token': token, 'msg': '환영합니다.'})
    # 동일한 유저가 없으면, 결과 -> 실패, 다시 로그인.
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/패스워드가 일치하지 않습니다.'})


# 회원 가입
@app.route('/join/save', methods=["POST"])
def sign_up():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()  # 패스워드 암호화

    doc = {
        "id": id_receive,
        "pw": pw_hash,
    }
    db.users.insert_one(doc)
    return jsonify({'result': 'success'})


@app.route('/join/id_check', methods=['POST'])
def id_check():
    id_receive = request.form['id_give']
    exists = bool(db.users.find_one({"id": id_receive}))
    # print(value_receive, type_receive, exists)
    return jsonify({'result': 'success', 'exists': exists})


# =========================================================================================
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
