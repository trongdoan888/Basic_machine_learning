import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import time

print("="*60)
print("🌳 HUẤN LUYỆN CHUYÊN GIA: RANDOM FOREST (MIRAI BOTNET)")
print("="*60)

file_path = 'data/dataset_Mirai_FULL_20cols.csv'
print(f"[1/6] Đang nạp dữ liệu từ: {file_path}")
start_time = time.time()
df = pd.read_csv(file_path)

X = df.drop('Label', axis=1)
y = df['Label']
feature_names = X.columns # Lấy tên cột tự động từ file CSV

print("[2/6] Đang chia tập Huấn luyện và Kiểm thử...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)

print("[3/6] Đang huấn luyện Rừng ngẫu nhiên (100 cây)...")
train_start = time.time()
rf_model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42, n_jobs=-1)
rf_model.fit(X_train, y_train)
train_end = time.time()
print(f"      -> Thời gian huấn luyện: {train_end - train_start:.2f} giây.")

print("[4/6] Đang dự đoán trên tập Kiểm thử...")
y_pred = rf_model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"\n✅ ĐỘ CHÍNH XÁC TỔNG THỂ (Accuracy): {acc * 100:.4f}%\n")
print("📊 BẢNG BÁO CÁO PHÂN LOẠI:")
print(classification_report(y_test, y_pred, target_names=['Bình thường (0)', 'Mirai (1)']))

print("[5/6] Đang xuất biểu đồ Ma trận nhầm lẫn...")
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(7, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Oranges',
            xticklabels=['Dự đoán Sạch', 'Dự đoán Mirai'],
            yticklabels=['Thực tế Sạch', 'Thực tế Mirai'])
plt.title('Confusion Matrix - Random Forest (Mirai)', fontsize=14, pad=15)
plt.ylabel('Actual Label', fontsize=12)
plt.xlabel('Predicted Label', fontsize=12)
plt.tight_layout()
plt.savefig('confusion_matrix_mirai_rf_FULL.png', dpi=300)
plt.close()

print("[6/6] Đang trích xuất và vẽ Top Đặc trưng quan trọng...")
importances = rf_model.feature_importances_
feature_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
feature_df = feature_df.sort_values(by='Importance', ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=feature_df, palette='viridis')
plt.title('Top 10 Feature Importances (Mirai Botnet)', fontsize=14, pad=15)
plt.xlabel('Importance Score', fontsize=12)
plt.ylabel('Features', fontsize=12)
plt.tight_layout()
plt.savefig('feature_importance_mirai_rf.png', dpi=300)
print("📸 Đã lưu thành công: feature_importance_mirai_rf.png")
plt.show()

total_time = time.time() - start_time
print(f"\n⏱️ Tổng thời gian hoàn thành: {total_time:.2f} giây.")