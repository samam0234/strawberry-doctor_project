# 🍓 딸기 닥터 (Strawberry Doctor) - Django 웹 애플리케이션

## 프로젝트 개요

**딸기 닥터**는 AI Hub 시설작물(딸기) 데이터셋을 기반으로 한 **딸기 잎 질병 진단 웹 서비스**입니다.  
EfficientNet-B0 모델을 활용해 사용자가 업로드한 딸기 잎 이미지를 분석하여 **정상 / 역병 / 시들음병 / 잎끝마름 / 황화**를 자동 진단합니다.

- **개발 프레임워크**: Django 6.0.4
- **프론트엔드**: Tailwind CSS + jQuery + Chart.js + Cropper.js + Font Awesome 6.5.0 (로컬)
- **데이터 저장**: LocalStorage (진단 이력)
- **주요 특징**: 정적 HTML 데모 → Django 기반 동적 웹 앱으로 전환, myfarm 대시보드에 **실시간 건강 점수 계산** 기능 추가

---

## 전체 파일 구조

```
django-blog/                                ← 프로젝트 루트
├── manage.py
├── db.sqlite3
├── requirements.txt
├── static/                                 ← 정적 파일 (이미지, CSS, Font Awesome)
│   ├── css/
│   │   └── bootstrap.min.css               ← Font Awesome 6.5.0 (로컬)
│   ├── image/
│   │   └── strawberry_gradCam_image.PNG
│   └── webfonts/                           ← Font Awesome 6.5.0 Web Kit (woff2 파일들)
├── strawberry/                             ← 주요 Django 앱
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py                            ← 페이지 렌더링 로직
│   ├── urls.py                             ← 앱 URL 설정
├── templates/                              ← Django 템플릿 (앱별 분리 구조)
│   ├── base.html                           ← 공통 레이아웃 (Navbar + Footer)
│   ├── index.html                          ← 메인 랜딩 페이지
│   └── strawberry/                         ← Django strawberry 앱 템플릿
│       ├── training.html                   ← 진단 페이지 (이미지 업로드 + Cropper.js)
│       ├── history.html                    ← 진단 이력 페이지
│       ├── myfarm.html                     ← 내 농장 대시보드 (건강 점수 동적 계산)
│       └── report.html                     ← 연구 보고서 페이지
├── mysite/                                 ← Django 프로젝트 설정
│   ├── settings.py                         ← STATIC, TEMPLATES, DATABASES 등 핵심 설정
│   ├── urls.py                             ← 프로젝트 URL + static serving
│   ├── asgi.py
│   └── wsgi.py
└── venv/                                   ← Python 가상환경
```

---
---

## 사용자 가이드 (User Guide)

### 1. 서비스 이용 방법

1. **메인 페이지** (`/`)
   - Hero 섹션에서 **"지금 진단 시작하기"** 버튼 클릭
   
   밑에 이미지 참고 : 
   <img src='![alt text](image-1.png)'>
   <img src='![alt text](image-2.png)'>
   (체크 표시된 부분을 클릭하면 된다.)

2. **진단하기** (`/training/`)
   - 딸기 잎 사진 업로드
   - 분석할 부위를 드래그로 선택
   - **"선택한 부위 분석하기"** 클릭
   - Grad-CAM 히트맵과 진단 결과 확인
   <img src='![alt text](image-3.png)'>
   (체크 표시 클릭)
   <img src='![alt text](image-4.png)'>
   (딸기(설향) 관련 이미지 가져오기)
   <img src='![alt text](image-5.png)'>
   (테두리 부분으로 특정 부분 선택 후 '선택한 부위 분석하기' 클릭)
   <img src='![alt text](image-6.png)'>
   (결과 확인후 이력 확인할꺼면 '진단 이력 확인' & 다시 진단하고 싶으면 '새 이미지 진단하기' 클릭)

3. **진단 이력** (`/history/`)
   <img src='![alt text](image-8.png)'>
   - 모든 진단 기록 확인
   - 검색 및 필터 기능 사용
   - 각 기록 클릭 시 상세 모달 + PDF 다운로드 가능
   - 기록 삭제 시 '전체 삭제' 버튼 클릭
   <img src='![alt text](image-7.png)'>
   (검점 체크 표시한 부분 클릭)

4. **내 농장** (`/myfarm/`)
   <img src='![alt text](image-9.png)'>
   - **전체 농장 건강 점수** 실시간 확인 (동적 계산)
   - 환경 센서 정보, 생육 단계 분포, 최근 진단 기록 확인

5. **연구 보고서** (`/report/`)
   <img src='![alt text](image-10.png)'>
   - Baseline 결과, 데이터셋 요약, 다음 연구 단계 확인

---

## 개발자 가이드 (Developer Guide)

### 1. 프로젝트 구조 설명

- **mysite/**: Django 프로젝트 설정 폴더
  - `settings.py`: `STATICFILES_DIRS`, `TEMPLATES`, `DATABASES` 등 핵심 설정
  - `urls.py`: 프로젝트 URL + static 파일 서빙 설정

- **strawberry/**: 주요 앱 (Strawberry Doctor 기능 담당)
  - `views.py`: 각 페이지 렌더링 (`home`, `training`, `history`, `myfarm`, `report`)
  - `urls.py`: 앱 내부 URL 설정
  - `templates/strawberry/`: 모든 HTML 템플릿 (base.html 상속)

- **static/**: 정적 파일
  - `/css/bootstrap.min.css`: Font Awesome 6.5.0 (로컬)
  - `images/`: Grad-CAM 이미지 등
  - `webfonts/`: Font Awesome 폰트 파일 (필수)

### 2. 주요 수정 및 추가 기능

| 영역              | 변경 내용                                      | 이유 |
|-------------------|-----------------------------------------------|------|
| **base.html**     | container → main class="w-full"               | hero 배경 full-width 지원 |
| **index.html**    | static 이미지 경로 수정                        | static 이미지 정상 출력 |
| **myfarm.html**   | 건강 점수 **동적 계산** (비율 방식) 추가        | 실제 진단 이력 반영 |
| **views.py**      | `home()` → `'strawberry/index.html'` 수정     | 템플릿 경로 통일 |
| **urls.py**       | `static()` serving 코드 추가                  | static 파일 서빙 |

### 3. myfarm.html 건강 점수 계산 방식

- **계산 공식**: `(정상 진단 수 / 전체 진단 수) × 100`
- **예시**:
  - 정상만 있음 → **100점**
  - 정상 2 : 비정상 1 → **약 67점**
  - 정상 1 : 비정상 2 → **약 33점**
  - 비정상만 있음 → **0점**

---

**주의사항**  
- 위 **파일 접근 권한 가이드**를 팀원 모두에게 공유해주세요.  
- 잘못 건드리면 **서버가 안 켜지거나** 아이콘이 깨지거나 **static 파일 404 오류**가 발생합니다.  
- 수정이 필요하면 가능한 github 커밋을 통한 merge를 해서 공유하거나 카카오톡으로 공유해주세요.

---

**현재 프로젝트 상태**  
- 정적 HTML 5개 → Django 템플릿으로 완전 전환 완료
- static 파일 (이미지, Font Awesome) 정상 작동
- myfarm.html 건강 점수 **동적 계산** 기능 추가 완료


---


## 기초적 기능

- **Django MVC 구조** 적용 (`mysite` 프로젝트 + `strawberry` 앱)
- **정적 파일 관리** (`static/` 폴더 + `STATICFILES_DIRS` 설정)
- **템플릿 상속** (`base.html` → 5개 페이지 상속)
- **URL 라우팅** (`mysite/urls.py` → `strawberry/urls.py`)
- **LocalStorage 기반** 진단 이력 저장 (DB 연동 준비 단계)

---

## 상세 기능 및 HTML 5개 수정 내용

### 1. **base.html** (공통 레이아웃)
- **변경점**: `{% load static %}` 추가, `container mt-4` → `main class="w-full"`로 변경 (hero 배경 full-width 지원)
- **목적**: 모든 페이지에 일관된 Navbar와 Footer 제공

### 2. **index.html** (메인 페이지)
- **변경점**: Grad-CAM 이미지 경로를 `{% static %}`으로 수정
- **기존 HTML → Django**: 정적 `<img src="...">` → Django static 태그로 변경

### 3. **training.html** (진단 페이지)
- **변경점**: `base.html`Navbar와 Footer기능을 추가하기 위해 `{% extends '../base.html' %}`로 경로 추가
- **기존 기능 유지**: Cropper.js + jQuery + LocalStorage 저장

### 4. **history.html** (진단 이력 페이지)
- **변경점**: `base.html`Navbar와 Footer기능을 추가하기 위해 `{% extends '../base.html' %}`로 경로 추가
- **기존 기능 유지**: LocalStorage 기반 이력 목록 + PDF 다운로드

### 5. **report.html** (연구 보고서 페이지)
- **변경점**: `base.html`Navbar와 Footer기능을 추가하기 위해 `{% extends '../base.html' %}`로 경로 추가
- **기존 기능 유지**: Baseline 결과 및 파이프라인 설명

### 6. **myfarm.html** (내 농장 대시보드) — **가장 큰 변경**

- **기존**: 고정 87점 표시
- **변경**: **동적 건강 점수 계산** 기능 추가
  - **계산 방식** (정상 비율 기반):
    - 전체 진단 기록 중 **정상 진단 비율** × 100
    - 정상만 있으면 → **100점**
    - 비정상만 있으면 → **0점**
    - 정상 2 : 비정상 1 → **약 67점**
    - 정상 1 : 비정상 2 → **약 33점**
- **추가 기능**: 점수에 따라 색상 자동 변경 (녹색/주황/빨강)

---

## Django 변경 이유와 기대효과

### 변경 이유
- **정적 HTML → 동적 웹 앱 전환**: 기존 5개 HTML 파일은 데모용이었으나, Django로 전환하면서 **데이터 연동**과 **재사용성**을 높이기 위함
- **static 파일 관리 강화**: `STATICFILES_DIRS` 설정으로 이미지와 Font Awesome을 Django가 올바르게 인식하도록 함
- **템플릿 구조 통일**: `../base.html` 같은 절대경로로 웹사이트의 링크 주소가 잘못 찍히는 불상사를 막는 구조
- **myfarm.html 동적화**: 단순 대시보드 → **실제 진단 이력**을 반영한 **실시간 건강 점수** 제공

### 기대효과
- **사용자 경험 향상**: 농장 건강 점수가 진단 결과에 따라 **실시간으로 변동** → 농장 관리 동기 부여
- **유지보수성 향상**: Django MVC 구조로 코드가 체계적으로 정리됨
- **확장성 강화**: 향후 MariaDB + Docker 배포, AI 모델 연동이 용이
- **실제 서비스 수준 구현을 위한 시도**: 정적 데모 → 데이터 기반 스마트 농장 모니터링 시스템으로 진화

---

**현재 프로젝트 상태 요약**
- 정적 HTML 5개 → Django 템플릿으로 완전 전환 완료
- static 파일 (css, 이미지, Font Awesome) 정상 작동
- myfarm.html 건강 점수 **동적 비율 계산** 기능 추가 완료



---
---
---
---
---



## (추가된 내용)

### 6. myfarm.html 수정 이력 보고서 (2026년 4월 21일 기준)

**파일 위치**  
`templates/strawberry/myfarm.html`

**수정 목적**  
- Django 템플릿 전환 후 발생한 Chart.js 그래프 미표시 / 레이아웃 붕괴 문제를 해결  
- 건강 점수를 **실시간 동적 계산**으로 변경  
- 생육 단계 도넛 그래프와 평균 생육 지수 카드의 **수직 균형**을 맞춰 시각적 완성도 향상  
- 일반 팀원이 안전하게 수정할 수 있도록 안정화

**팀장·웹관리자 승인 완료** (4번 파일 접근 권한 가이드 준수)

#### 6-1. 주요 변경 사항 요약

| 변경 항목                    | 이전 코드                                      | 수정 후 코드                                      | 수정 이유                                                                 | 기대 효과 |
|-----------------------------|-----------------------------------------------|--------------------------------------------------|---------------------------------------------------------------------------|----------|
| **건강 점수 계산**          | 고정 100점                                    | `calculateHealthScore()` (정상 비율 × 100)      | LocalStorage 실제 진단 이력 연동                                          | 실시간 농장 건강 상태 표시 |
| **Chart.js onload**         | `window.onload` 중복                          | `window.addEventListener('load', ...)` 단일     | onload 충돌 버그 제거                                                     | 그래프 + 최근 기록 모두 정상 작동 |
| **도넛 그래프 레이아웃**    | `<canvas>`만 사용                             | `<div class="h-80 bg-gray-50 ...">` wrapper     | 그래프가 아래로 밀리거나 카드가 길어지는 현상 해결                       | 그래프 고정 위치 + 안정적 표시 |
| **평균 생육 지수 위치**     | `mt-8`                                        | `mt-12` (또는 `mt-16`)                           | 그래프 높이가 커지면서 오른쪽 카드가 위로 치우쳐 보이는 불균형 해결       | 왼쪽 그래프와 오른쪽 수치 **수직 균형** 완벽 맞춤 |

#### 6-2. 상세 수정 배경 및 기대 효과

1. **평균 생육 지수 수치 아래로 내림**  
   - 문제: 그래프 높이가 커지면서 오른쪽 카드의 “38cm / 6.8 / 8.7cm” 수치가 위로 치우쳐 보임  
   - 해결: `mt-8` → `mt-12` (필요 시 `mt-16`까지 조정 가능)  
   - 기대 효과: 좌우 카드의 **수직 시각적 균형**이 완벽해져 전체 대시보드가 더 전문적이고 깔끔해짐

2. **전체 안정성 강화**  
   - 건강 점수 동적화 + Chart.js 안정화 + 레이아웃 균형까지 한 번에 완료  
   - 콘솔 로그 추가로 디버깅 용이

#### 6-3. 적용 방법 (일반 팀원용)
1. `myfarm.html` 파일 열기
2. 위 표의 수정 코드를 해당 부분에 교체
3. 서버 완전 종료 후 재시작 (`python manage.py runserver`)
4. `/myfarm/` 페이지에서 **Ctrl + F5** 강력 새로고침

**수정 후 확인 포인트**  
- 평균 생육 지수 수치가 그래프와 수직으로 균형 있게 내려감  
- 건강 점수가 LocalStorage 이력에 따라 실시간 변동

---