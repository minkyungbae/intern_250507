
```
rhoonart
├─ README.md                                                -> 폴더 구조 설명
├─ change-form                                              -> CSV 폴더 및 datetime format 코드 파일 포함
│  ├─ csv
│  │  ├─ album
│  │  │  ├─ album.csv
│  │  │  ├─ album.py                                        -> 빈칸이 있던 unique id 컬럼 추가하는 코드
│  │  │  └─ album_converted_1.csv
│  │  ├─ label
│  │  │  ├─ label.csv
│  │  │  └─ label_converted_1.csv
│  │  ├─ musician
│  │  │  ├─ musician.csv
│  │  │  ├─ musician.py                                     -> 빈칸이 있던 unique id 컬럼 추가하는 코드
│  │  │  └─ musician_converted_1.csv
│  │  ├─ ownership
│  │  │  ├─ ownership.csv
│  │  │  ├─ ownership.py                                    -> 빈칸이 있던 unique id 컬럼 추가하는 코드
│  │  │  └─ ownership_converted_1.csv
│  │  ├─ payout_buyer
│  │  │  ├─ payout_buyer.csv
│  │  │  └─ payout_buyer_converted_1.csv
│  │  ├─ payout_creator
│  │  │  ├─ payout_creator.csv
│  │  │  ├─ payout_creator.py                               -> 빈칸이 있던 unique id 컬럼 추가하는 코드
│  │  │  └─ payout_creator_converted_1.csv
│  │  ├─ settlement
│  │  │  ├─ flo
│  │  │  │  ├─ settlement_flo.csv
│  │  │  │  └─ settlement_flo_converted_1.csv
│  │  │  ├─ genie
│  │  │  │  ├─ settlement_genie.csv
│  │  │  │  └─ settlement_genie_converted_1.csv
│  │  │  ├─ melon
│  │  │  │  ├─ settlement_melon.csv
│  │  │  │  ├─ settlement_melon.py                           -> 빈칸이 있던 unique id 컬럼 추가하는 코드
│  │  │  │  └─ settlement_melon_converted_1.csv
│  │  │  ├─ vibe
│  │  │  │  ├─ settlement_vibe.csv
│  │  │  │  └─ settlement_vibe_converted_1.csv
│  │  │  └─ youtube
│  │  │     ├─ settlement_youtube.csv
│  │  │     └─ settlement_youtube_converted_1.csv
│  │  ├─ shorts
│  │  │  ├─ channels
│  │  │  │  ├─ shorts_channels.csv
│  │  │  │  ├─ shorts_channels.py                            -> 빈칸이 있던 unique id 컬럼 추가하는 코드
│  │  │  │  └─ shorts_channels_converted_1.csv
│  │  │  ├─ contracts
│  │  │  │  ├─ shorts_contracts.csv
│  │  │  │  └─ shorts_contracts_converted_1.csv
│  │  │  ├─ licensed_video
│  │  │  │  ├─ shorts_licensed_video.csv
│  │  │  │  └─ shorts_licensed_video_converted_1.csv
│  │  │  └─ permission_video
│  │  │     ├─ shorts_permission_video.csv
│  │  │     ├─ shorts_permission_video.py                    -> 빈칸이 있던 unique id 컬럼 추가하는 코드
│  │  │     └─ shorts_permission_video_converted_1.csv
│  │  ├─ track
│  │  │  ├─ track.csv
│  │  │  └─ track_converted_1.csv
│  │  └─ user
│  │     ├─ user.csv
│  │     ├─ user_complete.csv
│  │     └─ user_converted_1.csv
│  └─ format_datetime.py                                    -> 날짜 표기 형식 변환과 unique id를 UUID로 변경하는 코드
├─ crawling
│  ├─ 01.base-code.ipynb                                    -> 크롤링 기본 코드
│  ├─ 02.one-product.ipynb                                  -> 크롤링 제품 한 가지만 가져오는 코드 (이케아로 예시)
│  ├─ 03-1.youtube.ipynb                                    -> 2차 유튜브 크롤링 코드(250514)
│  ├─ 03-2.youtube.ipynb                                    -> 3차 유튜브 크롤링 코드(250515) : 함수화까지 완료
│  ├─ 03.youtube.ipynb                                      -> 1차 유튜브 크롤링 코드(250513)
│  └─ 04.real-code.ipynb                                    -> 실제로 쓰고 있는 코드
│  ├─ 침착맨_유튜브_250513.xlsx
│  ├─ 침착맨_유튜브_250513_1.xlsx
│  ├─ 침착맨_유튜브_250514.xlsx
│  ├─ 침착맨_유튜브_250514_1.xlsx
│  ├─ 침착맨_유튜브_250514_2.xlsx
│  ├─ 침착맨_유튜브_250514_3.xlsx
│  ├─ 침착맨_유튜브_250515.xlsx
│  └─ 침착맨_유튜브_250515_1.xlsx
├─ pip 명령어.txt
└─ requirements.txt

```