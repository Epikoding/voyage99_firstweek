# 🏖️ 짤방못잃어

---

## 🎑 만들게 된 배경 및 설명

개발자들은 대화를 할 때 유독 짤방을 많이 이용하는 것 같습니다. 다만 때때로 복사 붙여넣기 할 짤방을 찾고 검색하는데 필요 이상의 시간이 들 때가 있는데요. 가령 만화 캐릭터 ‘루피'가 주인공이고 루피의 짤방 대사는 기억이 나지만, 그 내용이 기억이 안 날 때 짤방 검색을 하고 찾는 데 시간이 걸릴 수 있습니다. 구글에 ‘루피'라고 검색하면 수 많은 이미지가 나올테니까요. '짤방못잃어'는 태그 기능을 제공하여 보다 쉽고 편리하게 짤방을 저장하고 공유할 수 있게끔 도와주는 플랫폼입니다.

---

## 👥 **1. 제작 기간 & 팀원 소개**

- 2022년 05월 08일 ~ 2022년 05월 12일
- 4인 1조 팀 프로젝트

| 이름 | 블로그 주소 | 이메일 주소 | 포지션 |
| --- | --- | --- | --- |
| 이동재 | https://velog.io/@djlesque | djlesque@gmail.com | 백엔드 |
| 권지은 | https://github.com/itsstacy/til | stacykwon86@gmail.com | 프론트엔드 |
| 한지용 | https://velog.io/@jigom | hjy583@naver.com | 프론트엔드 |
| 김민수 | https://minssu86.github.io/ | manager.kim86@gmail.com | 백엔드 |

> 조원 / 각자 역할 및 기능 개발 설명
> 
> 
> > **이동재**
> > 
> > - MongoDB를 활용한 DB 설계.
> > - 로그인&회원가입에 관련된 페이지 제작 및 기능 제작.
> > - `index.html`에 이미지 업로드 시 링크와 태그 DB로 `POST`, DB에서 클라이언트 `GET` 기능 제작.
> > - 효과적인 협업을 위한 노션 템플릿 제작.
> 
> > **권지은**
> > 
> > - html, css, javascript를 활용한 웹페이지 구성
> > - my짤 페이지 서버- 클라이언트 간 연결
> 
> > **한지용**
> > 
> > - html, css, javascript를 활용한 웹페이지 구성
> > - javascript를 활용한 modal 구현
> 
> > **김민수**
> > 
> > - MongoDB를 활용한 DB 설계 및 관리.
> > - python을 사용 sever 구축.
> > - javascript 사용  DB에서 불러온 데이터 출력.

---

## 🔨 **2. 사용 기술 및 툴**

`Back-end`

- jinja2
- flask
- jwt
- pymongo

`Front-end`

- html
- css
- javascript
- jquery
- Bulma
- ajax

`deploy`

- aws

---

## 🖇️ **3. 짤방못잃어 링크**


🔗 [http://real-minsu.shop/](http://real-minsu.shop/)


---

## 🖇️ **4. S.A (Starting Assignment)**

🔗 [https://velog.io/@djlesque/항해991주차-3조-S.AStarting-Assignment](https://velog.io/@djlesque/%ED%95%AD%ED%95%B4991%EC%A3%BC%EC%B0%A8-3%EC%A1%B0-S.AStarting-Assignment)


---

## 🖇️ **5. 실행화면 유튜브 링크**

🔗 [https://youtu.be/PaqJGbiqBpk](https://youtu.be/PaqJGbiqBpk)


---

## 💯 **6. 핵심기능**

- 회원가입, 로그인 & 로그아웃
    - JWT를 사용.
    - 회원가입 시 user db를 조회하여 아이디 중복 확인 기능 제공.
    - 아이디&비밀번호 모두 정규식을 사용하여 특수문자와 최대글자수 구현.
    
- 메인페이지
    - swiper, Image upload, modal 기능 구현
    - Swiper 라이브러리 이용 Slide기능 & Image upload 기능 구현
    - jinja2 Template Engine 사용 SSR(Server Side Rendering) 기능 구현
    - AJAX 사용 비동기 데이터 전송 (태그, 검색 기능)
    
- 마이페이지
    - jinja2 Template Engine 사용 SSR(Server Side Rendering) 기능 구현.
    - Database 정보 delete 기능 구현

---

## 🎮 **7. Trouble shooting**

> Github Push & Merge
> 
> 
> > 이슈 내용 : Merge 과정에서 각자 개발 환경에서의 차이로 Merge 에러 발생.
> > 
> 
> > 해결 방법 : 실제로 작업을 하고 필수로 Push해야 하는 작업물만 체크하여 Commit 후 Push. 조원들과 화상통화로 실시간 pull, request, merge.
> > 

> Jinja2와 Javascript 간의 호환
> 
> 
> > 이슈 내용 : DB에서 넘겨온 jinja2 데이터를 Javascript 에 적용이 되지 않아 문제가 발생.
> > 
> 
> > 해결 방법 : 팀원들의 도움으로 JQuery의 this를 활용하여, 현재 활성화된 창의 데이터를 가져와 문제를 해결함. 다만 좋아요 기능 - `app.py`의 `def posts_like()`  & `index.html`의 `function toggle_like()` - 은 시간상 문제로 해결하지 못함.
> > 

> 클라이언트 → 서버로 문자열이 전달될 때, 해당 문자열의 중복없이 태그 각각 리스트로 넣는 작업
> 
> 
> > 이슈 내용 : `upload.html`에서 링크와 문자열을 db로 전달할 때 문자열 그래도 전달되는 문제 발생.
> > 
> 
> > 해결 방법 : 하기 8번 **‘필수 기능'** 참고.
> > 

> Javascript Modal 창 구현 이슈
> 
> 
> > 이슈 내용 : Javascript를 활용하여 Modal 창을 열고 닫는데 문제를 겪음, 특히 Modal 창이 아닌 배경이 눌렸을 때 Modal창을 닫는 것에 많은 어려움을 겪음.
> > 
> 
> > 해결 방법 : 구글 검색을 통해 코드 테스트 및 적용. 보여지는 화면에서도 Modal창이 중앙으로 위치할 수 있도록 수정이 필요.
> > 

> CSS, HTML을 활용한 Layout 배치 및 구성 이슈.
> 
> 
> > 이슈 내용 : diplay 속성에 대한 지식 부족으로 인해 Layout 및 component 배치에 어려움을 겪음.
> > 
> 
> > 해결 방법 : 팀원의 도움으로 display: flex 속성에 대한 특징과 다양한 css 및 html 기법을 배울 수 있었음.
> > 

> aws sever 상에서 로그인 기능 미작동
> 
> 
> > 이슈 내용 :  로컬에서 사용 확인한 로그인 기능이 aws서버상에서 작동이 안되는 이슈.
> > 
> 
> > 해결 방법 :  token 생성 구문에 유니코드 인코딩 문제로 파. `.decode(’utf8’)` 를 입력하여 디코딩 작업.
> > 

> SSR시 서버-클라이언트 간 연결
> 
> 
> > 이슈 내용 : SSR을 서버에서 작업하고 클라이언트로 가져올 때 value 값이 맞지않아 작동이 안되었음
> > 
> 
> > 해결 방법 : value값 구분을 명확히 하고 전체 구조를 이해한 후 가져옴
> > 

> 문제가 발생했을 때 그것을 바로 적지 않은 것.
> 
> 
> > 이슈 내용 : 마지막으로 프로젝트를 제출하면서 회고록처럼 트러블슈팅을 적으려니 어떤 것이 문제였는지 기억이 나지 않음.
> > 
> 
> > 해결 방법 : 앞으로 1. 문제가 발생했을 때, 2.문제를 해결할 때 짧게나마 적는 습관을 드릴 것.
> > 

> json내에 불러오려고 하는 key가 없을 때 오작동하는 현상
> 
> 
> > 이슈 내용 :  json에서 key를 받아올 때 (특정 상황에서) 아직 key가 입력되지 않아서 없을 때 서버에 keyerror가 발생해서 코드를 수정해야 하는 상황
> > 
> 
> > 해결 방법 : 파이썬에서 들여쓰기를 잘못해서 오류가 생겼는데 팀원의 조언을 통해 해결함.
> > 

> 문제가 발생했을 때 그것을 바로 적지 않은 것.
> 
> 
> > 이슈 내용 : 마지막으로 프로젝트를 제출하면서 회고록처럼 트러블슈팅을 적으려니 어떤 것이 문제였는지 기억이 나지 않음.
> > 
> 
> > 해결 방법 : 앞으로 1. 문제가 발생했을 때, 2.문제를 해결할 때 짧게나마 적는 습관을 가질 것.
> > 

---

## ⚙️ **8. 필수 기능**

- 로그인
    - hashlib  사용 비밀번호 암호화
    - 토큰 생성하여 front로 전달
    
    ```python
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
    ```
    
    - server에서 전달 받은 토큰을 사용하여 쿠키 생성
    
    ```jsx
    // ajax 콜 app.py로 전송 및 로그인 진행
            $.ajax({
                type: "POST",
                url: "/login",
                data: {
                    id_give: id,
                    pw_give: pw
                },
                success: function (response) {
                    if (response['result'] == 'success') {
                        $.cookie('mytoken', response['token'], {path: '/'});
                        alert(response['msg'])
                        window.location.replace("/")
                    } else {
                        alert(response['msg'])
                    }
                }
            })
    ```
    
    - 페이지 이동시 서버단에서 쿠키값을 받아 로그인 유무 판별
    
    ```python
    token_receive = request.cookies.get('mytoken')  # 쿠키값 받아 오기
    # 쿠키값(로그인 판별) 여부에 따른 index.html 전송 자료 결정
        if token_receive is not None:
            payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
            user_info = db.users.find_one({"id": payload["id"]})    # DB users collection 에서 user 데이터 불러 오기
            login_status = 1  # 로그인 판벌(bool 사용 해봐도 될듯)
            return render_template('index.html', posts=posts, user_info=user_info, login_status=login_status)
        else:
            login_status = 0
            return render_template('index.html', posts=posts, login_status=login_status)
    ```
    

- jinja2 사용 자료 전달
    - DB에서 받은  데이터 ‘posts’ 리스트에 담아 html에 전달
    
    ```python
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
    
    						# =======  중략 =======
    
            return render_template('index.html', posts=posts, user_info=user_info, login_status=login_status)
    ```
    
    - 서버에서 받아온 posts 데이터를 jinja2 템플릿을 이용 html 출력
    
    ```python
    <div class="grid">
            {% for i in range(4) %}
                <div class="line">
                    {% for post in posts[i] %}
                        <div class="imgwrapper" onclick="">
                            <img class="zzal" src="{{ post.url }}">
                            <div class="tagposition">
                                <div class="imgtagbox" id="">
                                    {% for tag in post.tag %}
                                        <button class="imgtag" id="">{{ tag }}</button>
                                    {% endfor %}
                                </div>
                            </div>
                        </div>
                    {% endfor %}
                </div>
            {% endfor %}
        </div>
    ```
    
- 문자열 → 문자열 중복없는 리스트로 변환
    
    ```python
    # 받는 태그 empty 세트 생성
    tag_receive = set()
    
    # index.html에서 태그 받아오기
    temp_tag_receive = request.form['tag_give']
    temp_tag_receive.split(',')
    length_tag_receive = len(temp_tag_receive.split(','))
    for i in range(length_tag_receive):
        tag_receive.add(temp_tag_receive.split(',')[i].strip())
    
    # 받은 태그 리스트로 변환
    tag_receive = list(tag_receive)
    print(tag_receive)
    
    ```
    

---

## 📐 **9. 기타사항**

- 회고, TIL, WIL을 포함한 자세한 기술적 설명은 맨 위 ‘**1. 제작 기간 & 팀원 소개’을 참고 바랍니다.**
- 기타 문의사항이 있으시면 이메일로 문의 부탁드립니다.

---

## 💏 **10. 3조 한줄 회고**

> 미니 프로젝트를 진행하면서 팀원들과의 의사소통이 무엇보다 중요하다는 것을 알 수 있었다. 그리고 의사소통 전에 내가 어떤 부분에 문제가 있고, 어떤 부분을 수행했으며, 어떤 결과가 나왔다는 것을 단계적으로 말하는 것이 명확한 의사 전달에 도움이 된다는 것을 깨달을 수 있었다. 그리고 프로젝트를 진행하면서 나의 부족한 점도 많이 느낄 수 있었다. 부족한 부분을 느낌으로만 가져가지 않고 실천할 수 있는 자세를 가져야겠다.
> 
> 
> 마지막으로 고생해주신 우리 3조 팀원님들 수고하셨고, 항해 99일 마지막 날에 다같이 모여서 담소를 나눌 수 있었으면 좋겠습니다. 3조 파이팅! ***- 한지용***
> 

> 결과적으로 너무 아쉽고도 뿌듯했던 프로젝트였다. 프로젝트를 제출을 하고 프로젝트를 복기를 해보니, “별거 아닌 기능인데 왜 이렇게 오래 걸렸지?”라는 생각이 드는 코드들이 많았다. 그 점이 아쉬운 부분이다. 반면 짧은 기간이었지만 우리가 의도했던 많은 기능들이 효과&효율적으로 동작을 하는 것이 내 스스로를 뿌듯하게 만든다. 또한 코드를 짜는 것 뿐만 아니라, TIL작성, 깃허브 이용 등 많은 것을 배웠고 앞으로도 잘 할 수 있을거라 믿는다.
> 
> 
> 중도 탈락없이 남은 기간동안 최선을 다해주신 모든 이들에게 고마움을 돌린다. 남은 기간동안 앞으로도 모든 팀원들이 복되고 의미있는 항해를 하길 바란다. ***- 이동재***
> 

> 미니 프로젝트로 시작했지만 다양한 기능을 구현해볼 수 있는 구조의 웹을 만들어볼 수 있어서 좋았고 협업의 중요성과 시너지를 경험해봤던 좋은 경험이었다. 그리고 팀원들을 너무 잘 만난 것 같다! 모든 팀원이 책임감 있고 주체적이어서 각자 맡은 부분에 대해 열정적으로 기여했고, 서로 막히는 부분이 있으면 같이 생각하면서 이겨나간 시간들이 정말 소중한 경험이었다. 저희 팀원님들은 정말 모두 성공하실 것 같아요! 다들 화이팅입니다!!! ***- 권지은***
> 

> 일주일이라는 어쩌면 짧은시간이 이렇게나 농도 깊게 느껴진건 오랜만인거 같다. 미니 프로젝트를 시작하면서 커다란 목표를 세웠다 향후 99일간의 도전에 밑거름이 되도록 개발자 다움에 접근하는 것이였다. 기술적인 부분도 욕심이 났지만 이번 기회는 마인드 셋부터 다잡는 시간이었다. 사소하게는 사고하는 방식부터 시작하여 기록하고, 정리하고, 깊이 있게 탐구하려는 노력을 했던것 같다. 그리고 또 하나 좋었던것은 팀원들과 협업을 하며 그들로 부터 다양한 장점들을 보고 배우는 것이였다. 하루 종일 함께 하는 동안 내가 부족한 부분을 어떻게 채워야하는지 팀원들로 부터 방법을 알아가는 시간이 된거 같아 좋은 시간이였다.
끝으로 한주간 고생한 팀원 너무 고맙고 화이팅입니다! ***- 김민수***
>
