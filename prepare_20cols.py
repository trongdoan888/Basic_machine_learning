import pandas as pd
import numpy as np
import zipfile
import os
import gc

print("="*65)
print("🚀 HỆ THỐNG XỬ LÝ TOÀN BỘ DỮ LIỆU & GÁN TÊN CHUYÊN NGÀNH")
print("="*65)

# Tự động giải nén archive.zip nếu thư mục archive/ chưa tồn tại
if not os.path.exists('archive'):
    print("[0] Đang giải nén archive.zip vào thư mục archive/...")
    with zipfile.ZipFile('archive.zip', 'r') as z:
        z.extractall('archive')
    print("    -> Giải nén hoàn tất!\n")

attacks = [
    {
        'name':  'SYN_DoS',
        'data':  'archive/SYN DoS/SYN_DoS_dataset.csv',
        'label': 'archive/SYN DoS/SYN_DoS_labels.csv'
    },
    {
        'name':  'SSDP_Flood',
        'data':  'archive/SSDP Flood/SSDP_Flood_dataset.csv',
        'label': 'archive/SSDP Flood/SSDP_Flood_labels.csv'
    },
    {
        'name':  'Mirai',
        'data':  'archive/Mirai Botnet/Mirai_dataset.csv',
        'label': 'archive/Mirai Botnet/mirai_labels.csv'
    },
]

# Gán tên chuyên ngành quốc tế cho 20 cột
feature_names = [
    'F1 (MAC-IP: Weight)', 'F2 (MAC-IP: Mean)', 'F3 (MAC-IP: Variance)',
    'F4 (Source IP: Weight)', 'F5 (Source IP: Mean)', 'F6 (Source IP: Variance)',
    'F7 (Channel IP-IP: Weight)', 'F8 (Channel IP-IP: Mean)', 'F9 (Channel IP-IP: Variance)',
    'F10 (Channel IP-IP: Magnitude)', 'F11 (Channel IP-IP: Radius)', 'F12 (Channel IP-IP: Covariance)', 'F13 (Channel IP-IP: Correlation)',
    'F14 (Channel Jitter: Weight)', 'F15 (Channel Jitter: Mean)', 'F16 (Channel Jitter: Variance)',
    'F17 (Socket IP-Port: Weight)', 'F18 (Socket IP-Port: Mean)', 'F19 (Socket IP-Port: Variance)', 'F20 (Socket IP-Port: Magnitude)'
]

chunk_size = 500000

os.makedirs('data', exist_ok=True)

for attack in attacks:
    print(f"\n[{attack['name']}] BẮT ĐẦU QUÉT TOÀN BỘ FILE...")

    list_normal = []
    list_attack = []

    data_reader  = pd.read_csv(attack['data'],  header=None, usecols=range(1, 21), names=feature_names, chunksize=chunk_size)
    label_reader = pd.read_csv(attack['label'], header=None, chunksize=chunk_size)

    chunk_count = 1

    for data_chunk, label_chunk in zip(data_reader, label_reader):
        print(f"   -> Đang xử lý khối thứ {chunk_count}...")

        if label_chunk.shape[1] > 1:
            label_chunk = label_chunk.iloc[:, 1].to_frame(name='Label')
        else:
            label_chunk = label_chunk.iloc[:, 0].to_frame(name='Label')

        data_chunk.reset_index(drop=True, inplace=True)
        label_chunk.reset_index(drop=True, inplace=True)

        chunk_full = pd.concat([data_chunk, label_chunk], axis=1)

        # Làm sạch dữ liệu: đổi inf thành NaN rồi xóa các dòng chứa NaN
        chunk_full = chunk_full.replace([np.inf, -np.inf], np.nan).dropna()

        normal_part = chunk_full[chunk_full['Label'] == 0]
        attack_part = chunk_full[chunk_full['Label'] == 1]

        if len(normal_part) > len(attack_part) * 2 and len(attack_part) > 0:
            normal_part = normal_part.sample(n=len(attack_part) * 2, random_state=42)

        list_normal.append(normal_part)
        list_attack.append(attack_part)

        chunk_count += 1
        del chunk_full, normal_part, attack_part
        gc.collect()

    print(f"\n[{attack['name']}] ĐÃ QUÉT XONG. Đang tổng hợp...")

    df_all_normal = pd.concat(list_normal, ignore_index=True)
    df_all_attack = pd.concat(list_attack, ignore_index=True)

    total_normal = len(df_all_normal)
    total_attack = len(df_all_attack)
    print(f"   -> Tổng thu thập được: {total_normal:,} dòng Sạch | {total_attack:,} dòng Tấn công")

    max_balanced = min(total_normal, total_attack)

    if max_balanced == 0:
        print(f"   ⚠️ LỖI: Không tìm thấy dữ liệu tấn công cho {attack['name']}.")
        continue

    final_normal = df_all_normal.sample(n=max_balanced, random_state=42)
    final_attack = df_all_attack.sample(n=max_balanced, random_state=42)

    df_final = pd.concat([final_normal, final_attack]).sample(frac=1, random_state=42).reset_index(drop=True)

    output_filename = f"data/dataset_{attack['name']}_FULL_20cols.csv"
    df_final.to_csv(output_filename, index=False)
    print(f"   ✅ ĐÃ LƯU TẬP DỮ LIỆU TOÀN DIỆN: {output_filename}\n")

    del df_all_normal, df_all_attack, final_normal, final_attack, df_final
    gc.collect()

print("🎉 HOÀN TẤT TRÍCH XUẤT VÀ LÀM SẠCH DỮ LIỆU!")
