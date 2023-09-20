# flask라이브러리 로드

from flask import Flask, render_template


# Flask라는 class를 생성
# __init__() : 생성자 함수(초기화함수) → class가 생성될 때 단 한번만 실행이 되는 함수
# class에서 사용할 변수의 값들을 입력값으로 받아온다.
# Flask class에서 생성자 함수의 매개변수 중 필수 항목은
# __name__ 파일의 이름이 바뀌어도 쓸 수 있음
app = Flask(__name__)
# app = Flask('app.py')


# port 번호 설정
port = 3000

# api생성
# localhostl:3000/ 요청 시 아래의 함수를 호출
@app.route("/")
def index():
    # return "Hello World"
    return render_template('index.html')

app.run(port = port)
