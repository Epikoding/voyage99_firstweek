from pymongo import MongoClient
import jwt
import hashlib
import certifi
from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime, timedelta

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.feuh6.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca) #minsu
# client = MongoClient('mongodb+srv://test:sparta@sparta.eacl0.mongodb.net/sparta?retryWrites=true&w=majority', tlsCAFile=ca) #동재

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
@app.route('/log')
def login():
    return render_template('login.html')

# 회원 가입 페이지 이동
@app.route('/join')
def join():
    return render_template('join.html')

# my짤 페이지 이동
@app.route('/posts/mine', methods=["GET"])
# @app.route('/posts/mine')
def mine():
    return render_template('mine.html')

# 짤 데이터 DB에 저장
# @app.route('/upload', methods=["POST"])
@app.route('/upload') #중간 완성
def upload():
    tag_receive = set()

    # id_receive = request.form['id_give']    # 쿠키로 받아도 될듯
    # tag_receive.add(request.form['tag_give'])
    # url_receive = request.form['url_give']
    # hit_receive = request.form['hit_give']
    # like_receive = request.form['like_give']

    # 테스트용 자료 삽입 ==============================
    id_receive = "test9"
    tag_receive.add("개발자9")
    tag_receive.add("내코드9")
    tag_receive.add("코린이9")
    url_receive = "https://mblogthumb-phinf.pstatic.net/MjAxNzAxMTlfMTU1/MDAxNDg0ODE0NzQ2ODYy.FI39syRS9iOfd5uoCH6bP2JJnxt0960S2vpo2bfjulog.X-4Q-dnKE5N2A6EfRwpvfhA1ZGCxb8S8m4GVTJew6VEg.JPEG.cosl922/d6645e47-511c-447e-a7c5-74c603619348.jpg?type=w800"
    # url_receive = "https://dimg.donga.com/wps/NEWS/IMAGE/2021/02/03/105264221.3.jpg"
    # url_receive = "https://lolalambchops.com/wp/wp-content/uploads/2020/11/2021-Thanksgiving-Memes.jpeg0"
    # 테스트용 자료 삽입 ==============================

    today = datetime.now()   # datetime 클래스로 현재 날짜와시간 만들어줌 -> 현재 시각을 출력하는 now() 메서드
    date_receive = today.strftime('%Y-%m-%d-%H-%M-%S')
    hit_receive = 0
    like_receive = 0

    post_list = list(db.posts.find({}, {'_id': False}))

    tag_receive = list(tag_receive)  # 임시로 set타입을 list 타입으로 변환 / mongodb or dict 에 set타입 오류 발견됨
    print(tag_receive)

    if len(post_list) == 0:
        post_num = 1
    else:
        post_num = post_list[-1]['post_num'] + 1

    doc = {
        'post_num': post_num,
        'id': id_receive,
        'tag': tag_receive,
        'url': url_receive,
        'date': date_receive,
        'hit': hit_receive,
        'like': like_receive
    }

    db.posts.insert_one(doc)

    return redirect(url_for("home"))  # 어디로 갈까?


# 태그 비교 하여 불러 오기
# @app.route('/posts/tag', methods=["GET"])
@app.route('/posts/tag') #중간 완성
def posts_tag():
    # tag_receive = request.values.get('tag_give')
    tag_receive = "개발자4"  # 테스트용 코드
    post_list = list(db.posts.find({'tag': tag_receive}, {'_id': False}))
    print(post_list)
    return redirect(url_for("home"))


# 검색 하여 데이터 불러 오기
# @app.route('/posts/search', methods=["GET"])
@app.route('/posts/search') #작업중
def posts_search():
    # tag_receive = request.values.get('tag_give')
    tag_receive = "개발자4 코린이4"  # 테스트용 코드

    posts = set()

    for tag_receive in tag_receive.split():
        if (list(db.posts.find({'tag': tag_receive}, {'_id': False}))):
            posts_list = list(db.posts.find({'tag': tag_receive}, {'_id': False}))
            posts_tuple = tuple(posts_list)
            print(type(posts_tuple))
            posts.add(posts_tuple)
            print(posts)
            print("내부")
    print("외부")
    print(posts)

    # post_list = list(db.posts.find({'tag': tag_receive}, {'_id': False}))
    # print(post_list)
    return redirect(url_for("home"))


# 조회수 올리기
@app.route('/posts/hit-up', methods=["POST"])
def posts_hit_up():
    return


# 좋아요 or 취소 선택
@app.route('/posts/like', methods=["POST"])
def posts_like():
    return


# 짤줍 : 원하는 짤 모으기
@app.route('/posts/save', methods=["POST"])
def posts_save():
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


@app.route('/join/check_dup', methods=['POST'])
def check_dup():
    username_receive = request.form['username_give']
    exists = bool(db.users.find_one({"username": username_receive}))
    # print(value_receive, type_receive, exists)
    return jsonify({'result': 'success', 'exists': exists})


# =========================================================================================
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
