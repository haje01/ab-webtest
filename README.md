# ab-webtest
Airbridge Web SDK 를 이용한 테스트 

## 준비 및 실행

설치할 것: minikube, skaffold

실행 방법 

```
skafffold dev
```

## 설명

- Flask 서버가 Airbridge WebSDK 을 이용한 이벤트 호출 페이지를 렌더링 
- 클라이언트용 컨테이너 이미지에는 Playwright 를 통해 Headless Chrome 이 설치
- 클라이언트는 가짜 유저 정보 생성 후 Palywright 를 통해 서버에 이벤트 호출 요청 

