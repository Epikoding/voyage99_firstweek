from pymongo import MongoClient
import jwt
import hashlib
import certifi
from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime, timedelta
import random

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.feuh6.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca) #minsu
# client = MongoClient('mongodb+srv://test:sparta@sparta.eacl0.mongodb.net/sparta?retryWrites=true&w=majority', tlsCAFile=ca) #동재

db = client.dbfirstweek
app = Flask(__name__)

# 비밀 키 설정
SECRET_KEY = 'SPARTA'
# page 구분선 =========================================================================================


# @app.route('/test')
def test():

    # for y in range(100):
    tester = "minsu"
    pw_receive = "minsu1"
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()  # 패스워드 암호화


    testnum = []
    for i in range(30):
        testnum.append(random.randrange(0, 50))

    doc = {
        "id": tester,
        "pw": pw_hash,
        "post_num": testnum
    }
    db.users.insert_one(doc)

    # db.users.delete_many({'id': {'$regex': "minsu"}})

    return redirect(url_for("home"))  # 어디로 갈까?
# main 페이지 호출
@app.route('/')
def home():
    token_receive = request.cookies.get('mytoken')  # 쿠키값 받아 오기
    post_list = list(db.posts.find({}, {'_id': False}).sort('post_num', -1))  # DB posts collection 에서 짤 데이터 불러 오기

    posts = list()  # client 전달용 list 변수 선언
    # posts 재정렬 (기존 리스트를 4개의 묶음 리스트로 변경)
    temp_posts = list()
    amount = len(post_list)
    for i in range(amount):
        temp_posts.append(post_list[i])
        if len(temp_posts) == (amount // 4):
            posts.append(temp_posts)
            temp_posts = list()
    if temp_posts:
        posts.append(temp_posts)

    # 쿠키값(로그인 판별) 여부에 따른 index.html 전송 자료 결정
    if token_receive is not None:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"id": payload["id"]})    # DB users collection 에서 user 데이터 불러 오기
        login_status = 1  # 로그인 판벌(bool 사용 해봐도 될듯)
        return render_template('index.html', posts=posts, user_info=user_info, login_status=login_status)
    else:
        login_status = 0
        return render_template('index.html', posts=posts, login_status=login_status)


# 로그인 페이지 이동
@app.route('/log')
def login():
    return render_template('login.html')

# 회원 가입 페이지 이동
@app.route('/join')
def join():
    return render_template('join.html')

# my짤 페이지 이동
@app.route('/posts/mine', methods=["GET"])  #중간 완성
def mine():
    token_receive = request.cookies.get('mytoken')  # 쿠키값 받아 오기

    # 쿠키값(로그인 판별) 여부에 따른 mine.html 전송 자료 결정
    if token_receive is not None:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"id": payload["id"]})  # DB users collection 에서 user 데이터 불러 오기
        user_zzal = user_info['post_num']  # user 데이터에 저장된 짤 번호 리스트 불러오기

        zzal_list = list()  # mine.html 전달용 짤 저장 리스트 선언
        for zzal in user_zzal: # user가 찜해둔 짤 하나씩 가져 오기 ( mongodb query 문을 통한 한번에 작업 방법 스터디 필요! )
            zzal_list.append(db.posts.find_one({'post_num': zzal}))  # DB posts collection 에서 짤 데이터 불러 오기

        posts = list()  # client 전달용 list 변수 선언
        # posts 재정렬 (기존 리스트를 4개의 묶음 리스트로 변경)
        temp_posts = list()
        amount = len(zzal_list)
        for i in range(amount):
            temp_posts.append(zzal_list[i])
            if len(temp_posts) == (amount // 4):
                posts.append(temp_posts)
                temp_posts = list()
        if temp_posts:
            posts.append(temp_posts)

        login_status = 1  # 로그인 판벌(bool 사용 해봐도 될듯)
        return render_template('mine.html', posts=posts, puser_info=user_info, login_status=login_status)
    else:
        login_status = 0
        return render_template('mine.html', login_status=login_status)

# 짤 데이터 DB에 저장
# @app.route('/upload', methods=["POST"])
@app.route('/upload', methods=["POST"]) #중간 완성
def upload():
    tag_receive = set()
    token_receive = request.cookies.get('mytoken')  # 쿠키값 받아 오기
    payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])

    id_receive = payload["id"]    # 쿠키로 받아도 될듯
    tag_receive.add(request.form['tag_give'])   # 클라에서 받아오는 값
    url_receive = request.form['url_give']      # 클라에서 받아오는 값
    hit_receive = 0
    like_receive = 0
    today = datetime.now()   # datetime 클래스로 현재 날짜와시간 만들어줌 -> 현재 시각을 출력하는 now() 메서드
    date_receive = today.strftime('%Y-%m-%d-%H-%M-%S')

    post_list = list(db.posts.find({}, {'_id': False}))

    tag_receive = list(tag_receive)  # 임시로 set타입을 list 타입으로 변환 / mongodb or dict 에 set타입 오류 발견됨

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
@app.route('/posts/tag', methods=["GET"])
def posts_tag():
    tag_receive = request.values.get('tag_give')
    post_list = list(db.posts.find({'tag': tag_receive[1:]}, {'_id': False}).sort('post_num', -1))
    posts = list()  # client 전달용 list 변수 선언
    # posts 재정렬 (기존 리스트를 4개의 묶음 리스트로 변경)
    temp_posts = list()
    amount = len(post_list)
    for i in range(amount):
        temp_posts.append(post_list[i])
        if len(temp_posts) == (amount // 4):
            posts.append(temp_posts)
            temp_posts = list()
    if temp_posts:
        posts.append(temp_posts)

    return jsonify({'posts': posts})


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
        print("login: ", "payload: ", payload, "token: ", token)
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

# 회원가입 시 db에 가서 아이디가 있는지 확인
@app.route('/join/id_check', methods=['POST'])
def id_check():
    id_receive = request.form['id_give']
    exists = bool(db.users.find_one({"id": id_receive}))
    # print(value_receive, type_receive, exists)
    return jsonify({'result': 'success', 'exists': exists})


# 로그인 시 ~님 클릭할 수 있으며 본인 계정 설정 변경할 수 있음. 다만 정말로 비밀번호 바꾸게 변경할 수 있게 하지는 않음.
@app.route('/editprofile')
def editprofile():
    token_receive = request.cookies.get('mytoken')
    if token_receive is not None:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"id": payload["id"]})
        login_status = 1
        return render_template('editprofile.html', user_info=user_info, login_status=login_status)
    else:
        login_status = 0
        return render_template('editprofile.html', login_status=login_status)



# =========================================================================================
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
