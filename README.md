

# 오픈소스 기초설계 (나)반 1조 


## 구성원
- **[김재훈](https://github.com/zaehuun) (팀장)**   
> 목 운동 인식을 위한 Teachable Machine 오픈 소스 조사 및 구현   
목 운동 동작 학습 진행 및 Teachable Machine 커스터마이징 작업   
동작 구분 값을 받기 위한 python 웹 서버 구축   
아이템 획득 시 아이템 지우는 코드 작성   
LED Matrix에 자료 구조 Queue 적용하여 속도감 표현      
차량 충돌 인식 코드 작성   
출력 카운트 출력을 위한 List 생성   
팀원들이 작업한 코드들 에러 핸들링   

- **[김기원](https://github.com/justkiwon)(팀원)**
> 개발용 라즈베리파이 세팅   
LED Matrix 연결 및 라즈베리파이 상 구동 환경 세팅   
키 입력 제어 코드 작성   
시간 측정을 위한 코드 작성
시간에 따른 LED Matrix 색상 변경 코드 작성   
아이템 랜덤 생성 코드 작성   
메모리 관리를 위해 랜덤으로 생성하는 길의 개수를 제한하는 코드 작업   
게임 시작 시 출발 카운트 색상 변경하는 코드 작성   
 
- **[고재원](https://github.com/jaewon1778)(팀원)**
> 음성 인식을 위한 Google STT 오픈 소스 조사 및 구현   
Google STT를 통한 메인 실행 파일 통합 작업 진행   
시간에 따른 레이싱 게임 속도 변화 코드 작성
랜덤으로 레이싱 게임의 길을 생성하는 코드 작성   
랜덤으로 길 생성하는 코드 함수화 진행   
아이템 획득 확인하는 코드 작성
아이템 획득 시 점수에 반영하는 코드 작성   
충돌 시 디스플레이 효과 출력 코드 작성   
터미널 실시간으로 현재 점수 출력하는 코드 작성   
게임 시작 시 출발 카운트 출력하는 코드 작성   

 

## Open Souce
LED Matrix 출력을 위한 오픈 소스 : [LED Matrix](https://learn.adafruit.com/connecting-a-16x32-rgb-led-matrix-panel-to-a-raspberry-pi/experimental-python-code)
   
목 운동 인식을 위한 오픈 소스 : [Teachable Machine](https://teachablemachine.withgoogle.com/)
  
음성 인식을 위한 오픈 소스 : [Google STT](https://cloud.google.com/speech-to-text/docs/?hl=ko)

목 운동 인식의 결과 값을 서버로 전달 받기 위한 오픈 소스 : [Flask](https://flask-docs-kr.readthedocs.io/ko/latest/)


## Install
 
```
sudo pip3 install flask
```
```
sudo pip3 install keyboard
```
   
## How to Start
```
git clone https://github.com/zaehuun/osscap2020.git && cd osscap2020
```
```
cd final
```
```
python3 transcribe_streaming_infinite.py
```
- "키보드" 라고 말했을 때   
```
※ 방향키로 조절하는 레이싱 게임 실행
방향키 조작 : a - 좌로 이동, d - 우로 이동, q - 게임 종료
랜덤으로 생성되는 길을 방향키로 조작하여 피하며 진행
아이템 획득 시 추가 점수를 획득하며 실시간으로 터미널 창을 통해 점수 확인 가능
충돌 시 LED Matrix가 꺼지며 터미널 창을 통해 최종 스코어 확인 가능
```


- "포즈" 라고 말했을 때
```
※ 목 운동 동작으로 조절하는 레이싱 게임 실행
※ 웹 캠 연결 필요
※ 바로 레이싱 게임이 시작되지만 초기 동작 확인을 위해 처음 레이싱 게임은 진행하지 않음
1. 크롬 실행 후 http://localhost:5000/ 로 접속
2. start를 클릭 후 웹 캠 접근 권한 창이 뜨면 수락 버튼 클릭하여 웹 캠 화면 확인
3. 웹 캠을 통해 자세 교정 (※ 어깨 라인까지만 나오도록 학습하였기에 어깨선 아래로 상체가 보이면 인식에 어려움 있음.)
4. 각 동작 별 인식 값 확인 (하단 이미지 참고)
5. 인식이 제대로 되면 Ctrl + C를 입력하여 레이싱 게임 종료 후 다시 "포즈" 라고 말한 뒤 레이싱 게임 진행
6. 게임 진행 과정은 키보드 버전 레이싱 게임과 같음
7. 종료 되면 Ctrl + C를 눌러 서버 종료 후 STT로 

```
<p float="left">
  <img width="280" src="https://user-images.githubusercontent.com/72431775/100602280-084eab00-3347-11eb-985f-142ff95bdfca.png"> 
  <img width="280" src="https://user-images.githubusercontent.com/72431775/100602641-8317c600-3347-11eb-9128-3cb0a086678c.png">
  <img width="280" src="https://user-images.githubusercontent.com/72431775/100602726-a3e01b80-3347-11eb-9db8-43100806752d.png">
</p>
  
   **가만히! (Class1: 0.95이상 일 때)____________좌측으로 이동! (Class2: 0.95이상 일 때)____우측으로 이동! (Class3: 0.95이상 일 때)**


- "끝" 이라고 말했을 때
```
메인 실행 파일이 종료되며 실행 종료
```

