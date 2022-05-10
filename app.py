import certifi
from pymongo import MongoClient
from flask import Flask, render_template

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.feuh6.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca) #minsu
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
@app.route('/sign-in', methods=["POST"])
def sign_in():
    return


# page 구분선 =========================================================================================


# 회원 가입
@app.route('/sign-up', methods=["POST"])
def sign_up():
    return









# =========================================================================================
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
