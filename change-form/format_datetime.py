import pandas as pd
import uuid
import os

# UUID 생성 (32자리)
def generate_uuid_from_text(text):
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, text))


def format_datetime_display(date_str):
    try:
        # 입력된 날짜 문자열을 pandas datetime 객체로 변환
        datetime_obj = pd.to_datetime(date_str, errors='coerce')
        
        if pd.isna(datetime_obj):
            return None  # 파싱 실패 시
        
        # 'YYYY-MM-DD HH:MM:SS' 형식으로 출력
        return datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
    
    except Exception as e:
        print(f"[경고] 날짜 포맷 중 오류 발생: {e}")
        return None


# CSV 파일에 컬럼 생성 함수
def process_sheet(file_path, output_path):

    # 입력 파일 존재 여부 및 출력 디렉터리 확인
    if not os.path.isfile(file_path):
        print("❌ 입력한 파일 경로가 존재하지 않습니다.")
        return
    if not os.path.isdir(output_path):
        print("❌ 변환 경로가 존재하지 않습니다.")
        return

    # low_memory=False로 해두면 파일 크기가 매우 큰 경우에는 메모리 사용량이 많아질 수 있지만 파일을 더 천천히 읽을 수 있게 되어, 데이터 타입 추론이 더 정확해짐
    df = pd.read_csv(file_path, low_memory=False)
    
    """
    1. Creation Date -> created_date
    2. Modified Date -> modified_date
    3. id 컬럼은 맨 뒤에 추가
    """

    # 'created_date'와 'modified_date'를 해당 컬럼 바로 뒤에 삽입
    df.insert(df.columns.get_loc('Creation Date') + 1, 'created_date', pd.NA)
    df.insert(df.columns.get_loc('Modified Date') + 1, 'modified_date', pd.NA)
    # 'id' 컬럼은 마지막 열에 추가
    df['id'] = None


    # 각 컬럼에 입력될 값들 정의
    # iterrows : Pandas에서 DateFrame을 한 행(row)씩 반복(iterate)할 수 있게 해주는 함수
    # pandas의 at[row_index, column_label] 함수를 써서 단일 셀의 값에 빠르게 접근
    for idx, row in df.iterrows():

        # ID 생성(UUID로 생성) - UUID 생성 시, 빈 문자열 방지
        unique_id = row.get('unique id')
        if pd.notna(unique_id):
            uid_str = str(unique_id).strip()
            if uid_str:
                df.at[idx, 'id'] = generate_uuid_from_text(uid_str)

        # "Creation Date"를 KST 기준으로 변환하여 "created_date"에 저장
        row_creation = row.get('Creation Date')
        if pd.notna(row_creation):
            df.at[idx, 'created_date'] = format_datetime_display(row_creation)

        # "Modified Date"를 KST 기준으로 변환하여 "modified_date"에 저장
        row_modified = row.get('Modified Date')
        if pd.notna(row_modified):
            df.at[idx, 'modified_date'] = format_datetime_display(row_modified)


    # "네"/"아니오" -> True/False 변환 (공백, NaN 포함 상황 처리)
    def convert_yes_no(value):
        if isinstance(value, str):
            stripped = value.strip()  # 앞뒤 공백 제거
            if stripped == '네':
                return True
            elif stripped == '아니오':
                return False
        return value  # 그 외는 그대로

    df = df.applymap(convert_yes_no)

    # 파일 저장
    file_name = os.path.basename(file_path)
    base_name, ext = os.path.splitext(file_name)  # base_name은 'file', ext는 '.csv'
    base_name = f"{base_name}_converted"  # 'file_converted'


    # 기존 파일들과 비교
    existing_files = [f for f in os.listdir(output_path) if f.endswith(ext)]  # 기존 파일 리스트
    counter = 1
    output_file_name = f"{base_name}_{counter}{ext}"  # 'file_converted_1.csv'

    while output_file_name in existing_files:
        counter += 1
        output_file_name = f"{base_name}_{counter}{ext}"  # 'file_converted_2.csv'

    output_file_path = os.path.join(output_path, output_file_name)

    # 결과를 csv로 저장
    df.to_csv(output_file_path, index=False, encoding='utf-8-sig') # 한글 깨지지 않도록 인코딩 추가. (Windows Excel에서 열 때 한글 깨질 수도)
    print(f"✅ 변환 완료! 결과 저장: {output_file_path}")


# 사용자 입력
file_path = input("파일 경로를 입력하세요 : ")
output_path = input("변환 경로를 입력하세요 : ")
process_sheet(file_path, output_path)