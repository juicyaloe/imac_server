# imac_server

### Django를 활용한 야구 게임 앱 서버입니다. ( 개발 중 )

#### 사용한 스택
- nginx + Docker + Django Rest Framework + Postgres
---
### API

|METHOD|URL|설명|
|------|---|---|
|POST|DOMAIN/api/users/register/|회원가입|

- 입력값  

{  
  "username": [아이디: string]  
  "password": [비밀번호: string]  
  "email: [이메일: string]  
}  

- 반환값  

성공: 201  
실패: 그 외  

---
|METHOD|URL|설명|
|------|---|---|
|POST|DOMAIN/api/users/login/|로그인|

- 입력값  

{  
  "username": [아이디: string]  
  "password": [비밀번호: string]  
}  

- 반환값  

성공: 200  
실패: 그 외  

---
|METHOD|URL|설명|
|------|---|---|
|GET|DOMAIN/api/users/profiles/|전체 유저 조회|

- 입력값  

없음

- 반환값  

성공: 200  
{  
  ”id”: [회원의 고유 아이디]  
  ”username”: [회원의 아이디]  
  ”nickname”: [회원의 닉네임(처음에 회원가입하면 아이디랑 같음)]
  ”players”: [회원의 선수 목록]  
} 의 리스트들  

실패: 그 외  
