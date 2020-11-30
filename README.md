# 오픈소스 기초설계 (나)반 1조 


## 구성원
- **[김재훈](https://github.com/zaehuun) (팀장)**   
> 목 운동 인식을 위한 Teachable Machine 오픈 소스 조사 및 구현   
목 운동 동작 학습 진행 및 Teachable Machine 커스터마이징 작업   
동작 구분 값을 받기 위한 python 웹 서버 구축   
아이템 획득 시 아이템 지우는 코드 작성   
LED Matrix에 자료 구조 Queue 적용 작업 진행   
차량 충돌 인식 코드 작성   
팀원들이 작업한 코드들 에러 핸들링

- **[김기원](https://github.com/justkiwon)(팀원)**
> 개발용 라즈베리파이 세팅   
LED Matrix 연결 및 라즈베리파이 상 구동 환경 세팅   
키 입력 제어 코드 작성   
시간 측정을 위한 코드 작성
시간에 따른 LED Matrix 색상 변경 코드 작성   
아이템 랜덤 생성 코드 작성   
메모리 관리를 위해 랜덤으로 생성하는 길의 개수를 제한하는 코드 작업   
 
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
