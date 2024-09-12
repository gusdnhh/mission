import cv2
import os

# 원본 폴더와 저장 폴더 경로 설정
input_dir = 'dataAug/org'
output_dir = 'dataAug/aug'

# 출력 폴더가 존재하지 않으면 생성
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 입력 디렉토리에서 파일을 순회
for filename in os.listdir(input_dir):
    # 파일 경로 생성
    input_filepath = os.path.join(input_dir, filename)
    
    # 이미지 파일만 처리
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # 이미지 읽기
        img = cv2.imread(input_filepath)
        
        if img is None:
            print(f"이미지를 불러올 수 없습니다: {input_filepath}")
            continue
        
        # 수직으로 이미지 뒤집기
        vflipped_img = cv2.flip(img, 0)
        
        # 수평으로 이미지 뒤집기
        hflipped_img = cv2.flip(img, 1)

        # 저장 파일 경로 생성
        base_filename, file_ext = os.path.splitext(filename)
        vflip_output_path = os.path.join(output_dir, f"{base_filename}_vflip{file_ext}")
        hflip_output_path = os.path.join(output_dir, f"{base_filename}_hflip{file_ext}")

        # 이미지 저장
        cv2.imwrite(vflip_output_path, vflipped_img)
        cv2.imwrite(hflip_output_path, hflipped_img)

        print(f"{filename} 처리 완료: {vflip_output_path}, {hflip_output_path}")

print("모든 파일이 처리되었습니다.")
