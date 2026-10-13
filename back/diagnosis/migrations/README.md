# diagnosis/migrations

`DiagnosisResult` 테이블을 만드는 Django 마이그레이션입니다.

| 파일 | 내용 |
| --- | --- |
| `0001_initial.py` | 모델 최초 생성. Django 6.0.4, 2026-04-24 |
| `__init__.py` | 패키지 표시 |

적용:

```bash
python manage.py migrate
```

모델 필드를 바꾸면 이 디렉터리에 새 마이그레이션을 추가한 뒤 다시 `migrate`를 실행합니다.
