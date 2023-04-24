# ab-webtest
Airbridge Web SDK 를 이용한 테스트 

## 준비 및 실행

1. 설치: 
- [minikube](https://minikube.sigs.k8s.io/docs/start/)
- [skaffold](https://skaffold.dev/)

2. Airbridge 앱 정보를 Base64 인코딩:

```bash
echo -n '<앱 이름>' | base64
echo -n '<WebSDK 토큰>' | base64
```

3. 2 의 출력물로 Secret 생성:
```bash
kubectl apply -f - <<EOF 
apiVersion: v1
kind: Secret 
metadata:
  name: abtest
type: Opaque 
data:
    app: <인코딩된 앱 이름>
    token: <인코딩된 WebSDK 토큰>
EOF
```

Skaffold 로 실행:
```bash
skaffold deploy
```

## 설명

- Flask 서버가 Airbridge WebSDK 을 이용한 이벤트 호출 페이지를 렌더링 
- 클라이언트용 컨테이너 이미지에는 Playwright 를 통해 Headless Chrome 이 설치
- 클라이언트는 가짜 유저 정보 생성 후 Palywright 를 통해 서버에 이벤트 호출 요청 

