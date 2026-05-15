import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib
import os

print("="*65)
print("⚔️ HUẤN LUYỆN ĐỐI CHỨNG: NAIVE BAYES (SSDP FLOOD)")
print("="*65)

file_path = 'data/dataset_SSDP_Flood_FULL_20cols.csv'
print(f"[1/7] Đang nạp dữ liệu từ: {file_path}")
start_time = time.time()
df = pd.read_csv(file_path)

print("[2/7] Đang làm sạch dữ liệu (Loại bỏ NaN và Vô cực)...")
df = df.replace([np.inf, -np.inf], np.nan).dropna()
print(f"      -> Kích thước dữ liệu sạch: {df.shape[0]:,} dòng.")

X = df.drop('Label', axis=1)
y = df['Label']

print("[3/7] Đang chia tập Huấn luyện và Kiểm thử...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)

print("[4/7] Đang chuẩn hóa dữ liệu...")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("[5/7] Đang huấn luyện mô hình Gaussian Naive Bayes...")
train_start = time.time()
nb_model = GaussianNB()
nb_model.fit(X_train_scaled, y_train)
train_end = time.time()
print(f"      -> Thời gian huấn luyện: {train_end - train_start:.4f} giây.")

print("[6/7] Đang đánh giá trên tập Kiểm thử...")
predict_start = time.time()
y_pred = nb_model.predict(X_test_scaled)
predict_end = time.time()
print(f"      -> Thời gian suy luận (Inference): {predict_end - predict_start:.4f} giây.")

acc = accuracy_score(y_test, y_pred)
print(f"\n✅ ĐỘ CHÍNH XÁC TỔNG THỂ (Accuracy): {acc * 100:.4f}%\n")
print("📊 BẢNG BÁO CÁO PHÂN LOẠI:")
print(classification_report(y_test, y_pred, target_names=['Bình thường (0)', 'SSDP Flood (1)']))

print("[7/7] Đang lưu mô hình và xuất biểu đồ Ma trận nhầm lẫn...")
os.makedirs('models', exist_ok=True)
joblib.dump(nb_model, 'models/nb_ssdp_model.pkl')
joblib.dump(scaler, 'models/nb_ssdp_scaler.pkl')
print("      -> Đã lưu mô hình: models/nb_ssdp_model.pkl")

cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(7, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Reds',
            xticklabels=['Dự đoán Sạch', 'Dự đoán SSDP'],
            yticklabels=['Thực tế Sạch', 'Thực tế SSDP'])
plt.title('Baseline: Naive Bayes Confusion Matrix (SSDP)', fontsize=14, pad=15)
plt.ylabel('Actual Label', fontsize=12)
plt.xlabel('Predicted Label', fontsize=12)
plt.tight_layout()
plt.savefig('confusion_matrix_ssdp_nb_baseline.png', dpi=300)
plt.close()

total_time = time.time() - start_time
print("🎉 HOÀN TẤT! Đã lưu ảnh: confusion_matrix_ssdp_nb_baseline.png")
print(f"\n⏱️ Tổng thời gian chạy script: {total_time:.2f} giây.")
