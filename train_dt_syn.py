import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import time

print("="*55)
print("🌲 HUẤN LUYỆN CHUYÊN GIA: DECISION TREE (SYN DoS)")
print("="*55)

file_path = 'data/dataset_SYN_DoS_FULL_20cols.csv'
print(f"[1/5] Đang nạp dữ liệu từ: {file_path}")
start_time = time.time()
df = pd.read_csv(file_path)

X = df.drop('Label', axis=1)
y = df['Label']

print("[2/5] Đang chia tập Huấn luyện và Kiểm thử...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)

print("[3/5] Đang xây dựng Cây quyết định (max_depth=10)...")
train_start = time.time()
dt_model = DecisionTreeClassifier(max_depth=10, random_state=42, criterion='gini')
dt_model.fit(X_train, y_train)
train_end = time.time()
print(f"      -> Thời gian huấn luyện: {train_end - train_start:.2f} giây.")

print("[4/5] Đang đánh giá trên tập Kiểm thử...")
y_pred = dt_model.predict(X_test)

acc = accuracy_score(y_test, y_pred)
print(f"\n✅ ĐỘ CHÍNH XÁC TỔNG THỂ (Accuracy): {acc * 100:.4f}%\n")
print("📊 BẢNG BÁO CÁO PHÂN LOẠI:")
print(classification_report(y_test, y_pred, target_names=['Bình thường (0)', 'SYN DoS (1)']))

print("[5/5] Đang xuất biểu đồ Ma trận nhầm lẫn...")
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(7, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['Dự đoán Sạch', 'Dự đoán SYN DoS'],
            yticklabels=['Thực tế Sạch', 'Thực tế SYN DoS'])
plt.title('Confusion Matrix - Decision Tree (SYN DoS)', fontsize=14, pad=15)
plt.ylabel('Actual Label', fontsize=12)
plt.xlabel('Predicted Label', fontsize=12)
plt.tight_layout()
plt.savefig('confusion_matrix_syn_dt_FULL.png', dpi=300)
print("📸 Đã lưu thành công: confusion_matrix_syn_dt_FULL.png")
plt.show()

total_time = time.time() - start_time
print(f"\n⏱️ Tổng thời gian chạy script: {total_time:.2f} giây.")