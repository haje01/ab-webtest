# ab-webtest
Airbridge Web SDK 를 이용한 테스트 

## 준비

의존 패키지 설치
```
pip install -r requirements.txt
```

쉘 환경변수 노출 

```
export AB_APP_NAME=<AB APP 이름>
export AB_SDK_TOKEN=<AB Web SDK 토큰>
```

## 실행

다음 처럼 템플릿 렌더링을 하면,

```
python render.py
```

`index.html` 및 `tmp/` 폴더 아래 사용자별 HTML 파일 생성.

이후 웹 서버를 실행하고,

```
python -m http.server
```

웹 브라우저에서 `http://localhost:8000` 으로 접속 후 개별 링크를 클릭하거나, `Open All` 을 클릭하면 각 유저별 페이지가 열림.

페이지가 Open 될 때 유저별 AB SDK 호출이 진행.

## 응용

`render.py` 내의 `events` 나 `users` 를 더 다양하게 확장하여 시도.
