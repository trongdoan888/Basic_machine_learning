import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib
import os
import time

print("="*70)
print("⚔️ HUẤN LUYỆN ĐỐI CHỨNG: MẠNG NƠ-RON NHÂN TẠO - MLP (MIRAI BOTNET)")
print("="*70)

file_path = 'data/dataset_Mirai_FULL_20cols.csv'
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

print("[4/7] Đang chuẩn hóa dữ liệu (Bắt buộc để Mạng Nơ-ron hội tụ)...")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("[5/7] Đang huấn luyện MLP Neural Network (1 lớp ẩn - 50 nơ-ron)...")
print("      ⏳ Quá trình này sẽ tốn khá nhiều thời gian, vui lòng đợi...")
train_start = time.time()
mlp_model = MLPClassifier(hidden_layer_sizes=(50,), max_iter=200, random_state=42, early_stopping=True)
mlp_model.fit(X_train_scaled, y_train)
train_end = time.time()
print(f"      -> Thời gian huấn luyện (Fit): {train_end - train_start:.2f} giây.")

print("[6/7] Đang đánh giá trên tập Kiểm thử...")
predict_start = time.time()
y_pred = mlp_model.predict(X_test_scaled)
predict_end = time.time()
print(f"      -> Thời gian suy luận (Inference): {predict_end - predict_start:.4f} giây.")

acc = accuracy_score(y_test, y_pred)
print(f"\n✅ ĐỘ CHÍNH XÁC TỔNG THỂ (Accuracy): {acc * 100:.4f}%\n")
print("📊 BẢNG BÁO CÁO PHÂN LOẠI:")
print(classification_report(y_test, y_pred, target_names=['Bình thường (0)', 'Mirai (1)']))

print("[7/7] Đang lưu mô hình và xuất biểu đồ Ma trận nhầm lẫn...")
os.makedirs('models', exist_ok=True)
joblib.dump(mlp_model, 'models/mlp_mirai_model.pkl')
joblib.dump(scaler, 'models/mlp_mirai_scaler.pkl')
print("      -> Đã lưu mô hình: models/mlp_mirai_model.pkl")

cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(7, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Greys',
            xticklabels=['Dự đoán Sạch', 'Dự đoán Mirai'],
            yticklabels=['Thực tế Sạch', 'Thực tế Mirai'])
plt.title('Baseline: Neural Network Confusion Matrix (Mirai)', fontsize=14, pad=15)
plt.ylabel('Actual Label', fontsize=12)
plt.xlabel('Predicted Label', fontsize=12)
plt.tight_layout()
plt.savefig('confusion_matrix_mirai_mlp_baseline.png', dpi=300)
plt.close()
print("⚠️ Lưu ý: Mạng Nơ-ron là 'Hộp đen', không thể xuất biểu đồ Feature Importance!")
print("🎉 HOÀN TẤT! Đã lưu ảnh: confusion_matrix_mirai_mlp_baseline.png")

total_time = time.time() - start_time
print(f"\n⏱️ Tổng thời gian chạy script: {total_time:.2f} giây.")
