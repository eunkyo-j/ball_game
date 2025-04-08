# 🎮 공 피하기 게임 (Dodge the Ball Game)

## 📌 소개

이 게임은 사용자가 방향키로 정사각형 캐릭터를 조작하여 화면 안을 튕기며 움직이는 공들을 피해 살아남는 **공 피하기 게임**입니다.  
게임 시작 전 난이도 선택 창이 제공되며, 선택한 난이도에 따라 등장하는 공의 개수가 달라집니다.  

- 캐릭터는 매 게임마다 **랜덤한 색상**으로 등장합니다.
- 게임 중 공에 **한 번이라도 부딪히면 즉시 게임 오버**!
- 게임이 끝난 뒤에는 **자동으로 난이도 선택 화면**으로 돌아가며 다시 도전할 수 있습니다.

---

## 🎮 게임 방법

1. 프로그램을 실행하면 `Easy`, `Normal`, `Hard` 중 하나의 난이도를 선택할 수 있습니다.
2. 난이도에 따라 등장하는 공의 개수는 다음과 같습니다:

   - Easy: 5개  
   - Normal: 10개  
   - Hard: 17개  

3. 방향키(← ↑ ↓ →)를 이용해 사용자 캐릭터(정사각형)를 조작합니다.
4. 화면 안을 튕기며 움직이는 공에 **부딪히지 않고 최대한 오래 버티는 것**이 목표입니다.

---

## 🛠 사용 기술

- Python 3
- pygame 라이브러리

---

## 📁 설치 및 실행 방법

```bash
# pygame 설치
pip install pygame

# 게임 실행
python ballgame.py
```

---

## 🧠 주요 기능 설명

- **공 객체 클래스화**: 공의 위치, 속도, 방향, 충돌 등을 객체로 관리
- **랜덤 색상의 사용자 캐릭터 생성**
- **충돌 감지 기능**: 공과 플레이어 사이의 사각형 충돌 판별
- **난이도에 따른 공 개수 조절**
- **게임 종료 후 자동 재시작 (난이도 선택 화면 복귀)**

---

## 💻 코드 구조 (요약)

```python
class Ball:
    def __init__(self, ...):
        # 공의 초기 위치, 속도 등 설정

    def move(self):
        # 공이 벽에 닿으면 튕기도록 처리

    def draw(self, surface):
        # 공 그리기

def show_start_screen():
    # 난이도 선택 UI

def game_loop(ball_count):
    # 본 게임 루프 (캐릭터 이동, 충돌 판정 등)
```

---

## 🖼 게임 예시 화면

> 아래 이미지는 실제 게임 실행 화면 예시입니다.  
![Image](https://github.com/user-attachments/assets/6c2ac554-1018-4cc5-94bf-8cdbabc10383)

![Image](https://github.com/user-attachments/assets/3483f344-0a0f-44ab-b158-a80c6d90bec8)

![Image](https://github.com/user-attachments/assets/80ef42cd-ec12-4b6f-b3a1-86ddd60bbd79)

![Image](https://github.com/user-attachments/assets/b84a5b05-a1c1-453a-839d-c608512a846e)

---

## 📦 기타

- 게임 화면 크기: 640x480
- 공의 움직임: 화면 벽에 닿으면 반사되어 튕김
- 캐릭터 모양: 정사각형 (크기 고정)
- 게임 중 종료: 창 닫기 버튼 또는 ESC 키

---

## 👩‍💻 제작자

- 개발자: [eunkyo-j](https://github.com/eunkyo-j)
- 프로젝트명: 개인 미니 게임 프로젝트

---

## ✅ To-do (선택적으로 추가할 수 있는 기능)

- 제한 시간에 따라 점수 측정
- 최고 기록 저장
- 공 종류 다양화 (속도/크기 랜덤 등)
- BGM 및 효과음 추가
