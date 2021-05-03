# REST , REST API, RESTful

## REST

![REST%20,%20REST%20API,%20RESTful%208ac0922dae8a4a10ba1feffb0a544fef/rest.png](REST%20,%20REST%20API,%20RESTful%208ac0922dae8a4a10ba1feffb0a544fef/rest.png)

### REST : REpresentational State Transfer

HTTP를 이용해 통신하는 네트워크상에서 정한 약속 분산 하이퍼미디어 시스템을 위한 소프트웨어 설계 형식

REpresentational :자원을 대표하는 단어 or 식별자

State Transfer : 자원의 상태를 전송하는 방법

자원을 이름(자원의 표현)으로 구분하여 해당 자원의 상태(정보)를 주고 받는 모든 것을 의미한다

---

### REST 설계조건

1. Server - Client
2. STATELESS
3. Cache
4. Uniform Interface
5. Layered Sysyem
6. Code-On-Demand

## REST API

### API : Application Program Inteface

![REST%20,%20REST%20API,%20RESTful%208ac0922dae8a4a10ba1feffb0a544fef/Untitled.png](REST%20,%20REST%20API,%20RESTful%208ac0922dae8a4a10ba1feffb0a544fef/Untitled.png)

Request, Response로 오가는 구조화된 데이터

서버와 클라이언트 사이의 메신저 , 데이터를 주고 받는 형식

### REST API

![REST%20,%20REST%20API,%20RESTful%208ac0922dae8a4a10ba1feffb0a544fef/Untitled%201.png](REST%20,%20REST%20API,%20RESTful%208ac0922dae8a4a10ba1feffb0a544fef/Untitled%201.png)

REST 아키텍쳐 스타일을 따르는 API

HTTP(GET, POST)로 CRUD를 구현할 수 있는 API

특징 

1. uri은 http://{service root}/{collection}/i 형식
2. GET PUT DELETE POST를 지원함

