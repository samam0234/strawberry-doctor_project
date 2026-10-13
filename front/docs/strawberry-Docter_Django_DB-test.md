# Django + MariaDB 연결 완료 보고서 (2026년 4월)

## PART 1

**연동 목적**  
LocalStorage에만 저장되던 진단 결과와 라벨링 통계를 **MariaDB**로 영구 저장하기 위한 첫 단계 완료.  
실제 모델 데이터는 아직 없으나, **Django ↔ MariaDB 연결 테스트 성공**.

**파일 위치 및 주요 설정**
- `mysite/settings.py`

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',      # MariaDB도 동일 엔진 사용
        'NAME': 'strawberry',                      # 데이터베이스 이름
        'USER': 'test1',                           # 사용자 계정
        'PASSWORD': '<DB_PASSWORD>',               # 비밀번호는 .env 로 관리
        'HOST': '192.168.0.56',                    # DB 서버 IP
        'PORT': '3307',                            # MariaDB 포트
    }
}
```

**수행 단계 및 결과**

| 단계 | 명령어 / 작업 | 결과 | 비고 |
|------|---------------|------|------|
| 1 | `pip install mysqlclient` | 설치 완료 | Django가 MariaDB와 통신할 수 있게 해주는 드라이버 |
| 2 | `settings.py`에 DATABASES 설정 추가 | 적용 완료 | OPTIONS 없이도 정상 작동 |
| 3 | MariaDB 서버에서 DB 생성 및 권한 부여 | 완료 | `strawberry` 데이터베이스 생성 |
| 4 | `python manage.py makemigrations` | **실행하지 않음** | models.py에 변경 사항이 없었기 때문 |
| 5 | `python manage.py migrate` | **성공** | 테이블 생성 없이 연결만 확인 완료 |

**연결 성공 증거**
- `python manage.py migrate` 명령어가 오류 없이 완료됨
- Django가 MariaDB 서버(`192.168.0.56:3307`)와 정상적으로 handshake 완료
- `OPTIONS` 설정(`STRICT_TRANS_TABLES`) 없이도 연결 성공 (현재 환경에서는 불필요)

**현재 상태**
- Django ↔ MariaDB **연결은 완전히 성공**했습니다.
- `models.py`에는 아직 `Diagnosis`, `LabelStats` 등의 모델이 등록되지 않았기 때문에 실제 테이블은 생성되지 않았습니다.
- LocalStorage는 기존처럼 계속 사용 가능 (백업 용도)

**다음 계획 (추천)**
1. `strawberry/models.py`에 Diagnosis / LabelStats 모델 추가
2. `python manage.py makemigrations strawberry`
3. `python manage.py migrate`
4. views.py에서 진단 결과를 DB에 저장하는 로직 구현
5. Admin 페이지에서 데이터 확인 (`python manage.py createsuperuser` 후 `/admin/` 접속)

**주의사항**
- `OPTIONS`는 나중에 테이블 생성 시 에러가 발생하면 추가하면 됩니다.
- 실제 운영 환경에서는 `PASSWORD`를 `settings.py`에 하드코딩하지 말고 `os.environ` 또는 `django-environ`으로 관리할 것을 권장합니다.

---

## PART 2