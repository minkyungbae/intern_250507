# Youtube LongForm Crawling
유튜브 영상 속 데이터를 크롤링하는 프로젝트입니다.

# 기능
- 여러 YouTube 동영상 데이터 수집
- Selenium을 이용한 웹 크롤링

# 기술 스택
- Python
- Selenium
- BeautifulSoup4
- Pandas

# 폴더 구조
```
rhoonart
├─ README.md                          -> 폴더 구조 설명
├─ change-form/                       -> CSV 폴더 및 datetime format 코드 파일 포함
│  ├─ csv/
│  │  ├─ album/
│  │  ├─ label/
│  │  ├─ musician/
│  │  ├─ ownership/
│  │  ├─ payout_buyer/
│  │  ├─ payout_creator/
│  │  ├─ settlement/
│  │  ├─ shorts/
│  │  ├─ track/
│  │  └─ user/
│  └─ format_datetime.py              -> 날짜 표기 형식 변환과 unique id를 UUID로 변경하는 코드
├─ crawling/
│  ├─ 01.base-code.ipynb              -> 크롤링 기본 코드
│  ├─ 02.one-product.ipynb            -> 크롤링 제품 한 가지만 가져오는 코드 (이케아로 예시)
│  ├─ 03-1.youtube.ipynb              -> 2차 유튜브 크롤링 코드(250514)
│  ├─ 03-2.youtube.ipynb              -> 3차 유튜브 크롤링 코드(250515) : 함수화까지 완료
|  ├─ 03-3.youtube.ipynb              -> 4차 유튜브 크롤링 코드(250516) : 최종
│  ├─ 03.youtube.ipynb                -> 1차 유튜브 크롤링 코드(250513)
│  └─ 04.real-code.ipynb              -> 실제로 쓰고 있는 코드
├─ pip 명령어.txt
└─ requirements.txt

```