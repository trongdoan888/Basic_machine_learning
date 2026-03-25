import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import time
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print("="*65)
print("🚀 HUẤN LUYỆN CHUYÊN GIA: LOGISTIC REGRESSION (SSDP FLOOD)")
print("="*65)

file_path = 'data/dataset_SSDP_Flood_FULL_20cols.csv'
print(f"[1/6] Đang nạp dữ liệu từ: {file_path}")
start_time = time.time()
df = pd.read_csv(file_path)

X = df.drop('Label', axis=1)
y = df['Label']
feature_names = X.columns # Tự động lấy tên từ file CSV

print("[2/6] Đang chia tập Huấn luyện và Kiểm thử...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)

print("[3/6] Đang chuẩn hóa dữ liệu (StandardScaler)...")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test) 

print("[4/6] Đang huấn luyện Hồi quy Logistic...")
train_start = time.time()
lr_model = LogisticRegression(max_iter=1000, random_state=42)
lr_model.fit(X_train_scaled, y_train)
train_end = time.time()
print(f"      -> Thời gian huấn luyện: {train_end - train_start:.2f} giây.")

print("[5/6] Đang dự đoán trên tập Kiểm thử...")
y_pred = lr_model.predict(X_test_scaled)
acc = accuracy_score(y_test, y_pred)
print(f"\n✅ ĐỘ CHÍNH XÁC TỔNG THỂ (Accuracy): {acc * 100:.4f}%\n")
print("📊 BẢNG BÁO CÁO PHÂN LOẠI:")
print(classification_report(y_test, y_pred, target_names=['Bình thường (0)', 'SSDP Flood (1)']))

print("[6/6] Đang xuất biểu đồ Ma trận nhầm lẫn & Trọng số...")
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(7, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Purples',
            xticklabels=['Dự đoán Sạch', 'Dự đoán SSDP'],
            yticklabels=['Thực tế Sạch', 'Thực tế SSDP'])
plt.title('Confusion Matrix - Logistic Regression (SSDP)', fontsize=14, pad=15)
plt.ylabel('Actual Label', fontsize=12)
plt.xlabel('Predicted Label', fontsize=12)
plt.tight_layout()
plt.savefig('confusion_matrix_ssdp_lr_FULL.png', dpi=300)
plt.close()

coefficients = lr_model.coef_[0]
importance = np.abs(coefficients)
coef_df = pd.DataFrame({'Feature': feature_names, 'Importance': importance, 'Actual_Coef': coefficients})
coef_df = coef_df.sort_values(by='Importance', ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x='Actual_Coef', y='Feature', data=coef_df, palette='coolwarm')
plt.title('Top 10 Feature Weights (SSDP Flood)', fontsize=14, pad=15)
plt.xlabel('Coefficient Value', fontsize=12)
plt.ylabel('Features', fontsize=12)
plt.tight_layout()
plt.savefig('feature_importance_ssdp_lr.png', dpi=300)
print("📸 Đã lưu thành công: feature_importance_ssdp_lr.png")
plt.show()

total_time = time.time() - start_time
print(f"\n⏱️ Tổng thời gian hoàn thành: {total_time:.2f} giây.")