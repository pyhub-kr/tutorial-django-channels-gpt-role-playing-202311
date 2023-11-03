# 오르미 3기, 장고 특강

프로젝트 시작 준비

1. `.env` 파일을 아래와 같이 생성합니다. 각자의 api key를 지정합니다.

```
LANGUAGE_CODE=ko-kr
OPENAI_API_KEY=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
```

2. 가상환경이 있다면 생성/활성화해주시고, 없으시다면 사용하지 않으셔도 됩니다. 대신 다른 프로젝트하실 때 라이브러리 재설치가 필요하실 수 있습니다.
3. 아래 명령으로 필요한 라이브러리를 설치합니다. 
    - `python -m pip install -r requirements.txt`
4. 데이터베이스를 생성하고 슈퍼유저 계정을 생성합니다.
    - `python manage.py migrate`
    - `python manage.py createsuperuser`
5. 장고 개발서버를 구동합니다.
    - `python manage.py runserver`

---

이진석 (me@pyhub.kr)
