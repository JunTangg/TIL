# 190527 기초 설치 및 사용법 학습

## markdown 작성하기

### 제목작성

제목은 Semantic 하게 작성한다.

### 나열(리스트) 작성하기

#### 순서가 있는 리스트

1. WeMakeO 앱을 받는다.
2. 회원가입한다.
   * 카카오
   * 페북
   * 네이버
3. W카페를 찾는다.
4. 커피를 주문한다.
5. 알림이 오면 픽업하러 간다.


#### 순서가 없는 리스트

* 파이썬 설치하기
* 타이포라 설치하기
* Git 설치하기

### 일반 문단 작성하기

오늘 점심은 무엇일까요

오늘 점심은 탄수화물 폭탄입니다

### 코드블럭작성하기

터미널에서 `python -e` 라고 입력하면, 코드가 실행됩니다.

```python
def index():
	return 'hi'
def create():
    save()
```

### 수식작성

ctrl + shift + m
$$

$$

### 표만들기

ctrl + t

| title |      |      |      |      | content | desc |
| ----- | ---- | ---- | ---- | ---- | ------- | ---- |
|       |      |      |      |      |         |      |
| dddd  |      |      |      |      |         |      |
|       |      |      |      |      |         |      |
|       |      |      |      |      |         |      |

행 추가 : 표안에서 ctrl enter 혹은 more action

열 추가 More action

## CLI -terminal 기초 명령어 학습

```sh
$ touch a.txt # a.txt를 생성한다.
$ mkdir test # test 폴더/디렉토리를 생성한다. Make Directory
$ cd test # test 디렉토리로 이동한다. Change Directory
$ cd ~ # 홈(~)으로 이동한다.
$ cd - # 뒤로가기
$ cd .. # 위로가기
$ ls # List 현재 디레토리 안의 파일/디렉토리 목록을 표시한다.
$ ls -a # 숨김폴더까지 전부 표시
$ pwd # 현재 내가 위치한 디렉토리를 표시한다. Present Workikng Directory
$ clear # 페이지를 깨끗하게 지운다.
$ rm a.txt # a.txt파일 삭제
$ rm -r test/ # test/ 디렉토리 삭제
```

## Git 기초명령

```sh
git init # pwd 에서 git 으로 버전관리 시작 (.git/ 를 만든다.)
git config --global user.name "Jun_Hyeokwon" # 이름 입력
git coofig --global user.email "gogo4845_@naver.com"

git status # 현재 상태를 출력
git add 0_basic # 0_basic을 관리대상 지정
git add -A # 해당폴더에 있는 모든파일 add
git add . # 상동

git commit -m ' Message' # 사진찰칵 + 메세지 

git remote add origin <remote url> # 드라이브 등록
```



```sh
# 반드시 확인
$pwd
/c/User/student/TIL #TIL에 있는걸 확인

#수업 중간 중간
$ git add.
$ git commit -m '남길 메시지'
# 적절한 타이밍에!

#집에가기전에
$ git push origin master
```



## Python 기초

### 객체지향 프로그래밍 규칙

* is_---  : return 값이 true 혹은 false

* 동사형 : return 값이 있는 경우 

* 명사 : 변수이름

* Class 이름 : 소문자로 시작 -> 내장,   대문자 시작 -> 사용자 지정 

  

### Class

* 객체

  ```python
  class Fourth():
      late = '9:10'
      lunch = '12:10'
      finish = '18:00'
  
  Fourth.late = '9:15' # 값 수정, 초기 입력 등을 할 수 있다
      
  ```

  

* 초기화 : 객체 괄호안에서 속성값을 지정하는 것을 가능하게 해줌

  ```python
  class Student(Fourth):
      def __init__(self, name, age):
          self.name = name
          self.age = age
          
  Student1 = Student('전혁원', 27) # 위의 코드와 달리 변수를 초기부터 입력 가능
  ```

* 객체지향 :

  ```python
  s = Student()
  Student.set_values(s, '창희', 99)
  print(s.name)
  s.set_values('혁원', 27)
  print(s.name)
  ```


