# 📐 HƯỚNG DẪN VẼ USE CASE DIAGRAM - HỆ THỐNG HOTEL BOOKING

**Dự án:** Quan Trọng Hotel (Parkside Sunline Hotel)  
**Tổng số UC:** 21 Use Cases  
**Actors:** 2 (Guest, Admin)  
**Công cụ đề xuất:** Visual Paradigm, Draw.io, Lucidchart, StarUML

---

## 🎯 MỤC TIÊU

Vẽ sơ đồ Use Case tổng quan hiển thị:
- Tất cả 21 chức năng của hệ thống
- 2 actors và mối quan hệ với từng UC
- Phân nhóm UC theo module (Search, Booking, Admin, Review)
- Relationships giữa các UC (include, extend nếu có)

---

## 📏 KÍCH THƯỚC VÀ LAYOUT

**Khổ giấy:** A3 hoặc A4 ngang (Landscape)  
**Tỷ lệ:** 1:1 cho actors và UC  
**Khoảng cách:**
- Giữa actors và system boundary: 3cm
- Giữa các UC trong cùng nhóm: 1.5cm
- Giữa các nhóm UC: 3cm

---

## 🎨 CÁC THÀNH PHẦN CẦN VẼ

### **1. SYSTEM BOUNDARY (Hộp hệ thống)**

**Hình dạng:** Rectangle (hình chữ nhật) có viền đậm

**Kích thước:** 
- Chiều rộng: 25-30cm
- Chiều cao: 35-40cm (đủ chứa 21 UC)

**Vị trí:** Ở giữa canvas

**Label:** 
```
┌────────────────────────────────────────────────┐
│                                                │
│    Hotel Booking System                       │
│    (Hệ thống đặt phòng khách sạn)            │
│                                                │
│    [Các Use Cases bên trong]                  │
│                                                │
│                                                │
└────────────────────────────────────────────────┘
```

**Cách vẽ:**
1. Vẽ rectangle lớn ở giữa
2. Viết tiêu đề ở góc trên cùng bên trong: "Hotel Booking System"
3. Để trống không gian để chứa 21 UC ellipses

---

### **2. ACTORS (Người dùng/Hệ thống bên ngoài)**

#### **Actor 1: Guest (Khách đặt phòng)**

**Hình dạng:** Stick figure (người que)

**Vị trí:** Bên TRÁI của system boundary

**Cách vẽ:**
```
    O        ← Head (vòng tròn nhỏ)
   /|\       ← Body (3 lines: vai trái, thân, vai phải)
   / \       ← Legs (2 lines)
  
  Guest
```

**Chi tiết từng bước:**
1. Vẽ vòng tròn nhỏ (đường kính 1cm) cho đầu
2. Từ đáy vòng tròn, vẽ line thẳng đứng xuống dưới 2cm (thân)
3. Từ giữa thân, vẽ 2 lines chéo lên trái-phải 45° (vai)
4. Từ cuối thân, vẽ 2 lines chéo xuống trái-phải 30° (chân)
5. Viết label "Guest" bên dưới chân, căn giữa

**Vị trí cụ thể:**
- X: 5cm từ lề trái canvas
- Y: 15cm từ lề trên (để căn giữa theo chiều dọc với system boundary)

---

#### **Actor 2: Admin (Quản trị viên)**

**Hình dạng:** Stick figure (người que)

**Vị trí:** Bên PHẢI của system boundary

**Cách vẽ:** Giống hệt Actor 1, nhưng label là "Admin"

**Vị trí cụ thể:**
- X: Canvas width - 5cm (canh lề phải)
- Y: 15cm từ lề trên

---

### **3. USE CASES (Các chức năng)**

**Hình dạng:** Ellipse (hình oval ngang)

**Kích thước mỗi ellipse:**
- Chiều rộng: 4-5cm
- Chiều cao: 1.5cm

**Màu sắc đề xuất:**
- Guest UC: Màu xanh nhạt (#E3F2FD)
- Admin UC: Màu vàng nhạt (#FFF9C4)
- Viền: Màu đen (#000000)

**Label format:**
```
┌─────────────────────────┐
│  UC-XX: Tên UC         │  ← Mã UC + Dấu hai chấm + Tên
│  (English name)         │  ← Tên tiếng Anh (italic, nhỏ hơn)
└─────────────────────────┘
```

---

## 📍 VỊ TRÍ CỤ THỂ CỦA 21 USE CASES

### **NHÓM 1: SEARCH & BROWSE (Màu xanh nhạt) - BÊN TRÁI**

**Vị trí:** Góc trên bên trái của system boundary

```
X = 8cm từ lề trái system boundary
Y bắt đầu = 3cm từ lề trên system boundary
Khoảng cách giữa các UC: 2cm theo chiều dọc
```

**UC-01: Tìm kiếm phòng**
- Label: "UC-01: Tìm kiếm phòng\n(Search Rooms)"
- Vị trí: (X: 8cm, Y: 3cm)

**UC-02: Xem chi tiết phòng**
- Label: "UC-02: Xem chi tiết phòng\n(View Room Details)"
- Vị trí: (X: 8cm, Y: 6cm)

---

### **NHÓM 2: BOOKING FLOW (Màu xanh đậm hơn) - GIỮA TRÁI**

**Vị trí:** Giữa bên trái

```
X = 8cm
Y bắt đầu = 10cm
```

**UC-03: Thêm vào giỏ**
- Label: "UC-03: Thêm phòng vào giỏ\n(Add to Cart)"
- Vị trí: (X: 8cm, Y: 10cm)

**UC-04: Thêm dịch vụ bổ sung**
- Label: "UC-04: Thêm extras\n(Add Extra Services)"
- Vị trí: (X: 8cm, Y: 12.5cm)

**UC-05: Áp dụng mã giảm giá**
- Label: "UC-05: Áp coupon\n(Apply Coupon)"
- Vị trí: (X: 8cm, Y: 15cm)

**UC-06: Xem giỏ hàng**
- Label: "UC-06: Xem giỏ hàng\n(View Cart)"
- Vị trí: (X: 8cm, Y: 17.5cm)

**UC-07: Xóa khỏi giỏ**
- Label: "UC-07: Xóa sản phẩm\n(Remove from Cart)"
- Vị trí: (X: 8cm, Y: 20cm)

---

### **NHÓM 3: CHECKOUT (Màu xanh lá nhạt) - DƯỚI TRÁI**

**Vị trí:** Dưới cùng bên trái

```
X = 8cm
Y bắt đầu = 24cm
```

**UC-08: Tiến hành thanh toán**
- Label: "UC-08: Checkout\n(Proceed to Checkout)"
- Vị trí: (X: 8cm, Y: 24cm)

**UC-09: Nhập thông tin khách**
- Label: "UC-09: Nhập thông tin\n(Enter Customer Info)"
- Vị trí: (X: 8cm, Y: 26.5cm)

**UC-10: Xác nhận đặt phòng**
- Label: "UC-10: Xác nhận booking\n(Confirm Booking)"
- Vị trí: (X: 8cm, Y: 29cm)

**UC-11: Hoàn tất đặt phòng**
- Label: "UC-11: Hoàn tất\n(Complete Booking)"
- Vị trí: (X: 8cm, Y: 31.5cm)

**UC-12: Xem trang xác nhận**
- Label: "UC-12: Xem xác nhận\n(View Confirmation)"
- Vị trí: (X: 8cm, Y: 34cm)

**UC-13: Nhận email xác nhận**
- Label: "UC-13: Nhận email\n(Receive Email)"
- Vị trí: (X: 8cm, Y: 36.5cm)

---

### **NHÓM 4: REVIEW (Màu tím nhạt) - DƯỚI GIỮA**

**Vị trí:** Dưới cùng giữa

```
X = 16cm
Y = 36.5cm
```

**UC-17: Đánh giá phòng**
- Label: "UC-17: Đánh giá phòng\n(Write Review)"
- Vị trí: (X: 16cm, Y: 36.5cm)

---

### **NHÓM 5: ADMIN - BOOKING MANAGEMENT (Màu vàng) - PHẢI TRÊN**

**Vị trí:** Góc trên bên phải

```
X = 20cm từ lề trái system boundary
Y bắt đầu = 3cm
```

**UC-21: Quản lý đặt phòng**
- Label: "UC-21: Quản lý booking\n(Manage Bookings)"
- Vị trí: (X: 20cm, Y: 3cm)

---

### **NHÓM 6: ADMIN - ROOM MANAGEMENT (Màu vàng đậm) - GIỮA PHẢI**

**Vị trí:** Giữa bên phải

```
X = 20cm
Y bắt đầu = 8cm
```

**UC-22: Quản lý phòng**
- Label: "UC-22: Quản lý phòng\n(Manage Rooms)"
- Vị trí: (X: 20cm, Y: 8cm)

**UC-23: Quản lý tồn kho**
- Label: "UC-23: Quản lý tồn kho\n(Manage Inventory)"
- Vị trí: (X: 20cm, Y: 10.5cm)

**UC-24: Khóa ngày**
- Label: "UC-24: Khóa ngày\n(Block Special Dates)"
- Vị trí: (X: 20cm, Y: 13cm)

---

### **NHÓM 7: ADMIN - PRICING & OPTIONS (Màu cam nhạt) - DƯỚI PHẢI**

**Vị trí:** Dưới bên phải

```
X = 20cm
Y bắt đầu = 18cm
```

**UC-25: Quản lý extras**
- Label: "UC-25: Quản lý extras\n(Manage Extra Services)"
- Vị trí: (X: 20cm, Y: 18cm)

**UC-26: Quản lý coupon**
- Label: "UC-26: Quản lý coupon\n(Manage Coupons)"
- Vị trí: (X: 20cm, Y: 20.5cm)

---

### **NHÓM 8: ADMIN - INVOICING (Màu xanh lá) - CUỐI PHẢI**

**Vị trí:** Dưới cùng bên phải

```
X = 20cm
Y = 25cm
```

**UC-27: Tạo hóa đơn PDF**
- Label: "UC-27: Tạo hóa đơn\n(Generate Invoice)"
- Vị trí: (X: 20cm, Y: 25cm)

---

## 🔗 ASSOCIATIONS (Đường nối giữa Actors và UC)

**Hình dạng:** Straight line (đường thẳng) có mũi tên ở cuối (optional)

**Màu:** Đen (#000000)

**Độ dày:** 1-1.5pt

**Mũi tên:** Không bắt buộc (UML chuẩn không yêu cầu), nhưng nếu vẽ thì hướng từ Actor → UC

---

### **A. GUEST → USE CASES (14 đường nối)**

**Cách vẽ:**
1. Chọn tool "Association" hoặc "Line"
2. Click vào Actor Guest (bất kỳ điểm nào trên stick figure)
3. Kéo đến ellipse của UC
4. Release để tạo line

**Danh sách 14 associations:**

```
Guest ──────→ UC-01: Tìm kiếm phòng
Guest ──────→ UC-02: Xem chi tiết phòng
Guest ──────→ UC-03: Thêm vào giỏ
Guest ──────→ UC-04: Thêm extras
Guest ──────→ UC-05: Áp coupon
Guest ──────→ UC-06: Xem giỏ hàng
Guest ──────→ UC-07: Xóa khỏi giỏ
Guest ──────→ UC-08: Checkout
Guest ──────→ UC-09: Nhập thông tin
Guest ──────→ UC-10: Xác nhận booking
Guest ──────→ UC-11: Hoàn tất
Guest ──────→ UC-12: Xem xác nhận
Guest ──────→ UC-13: Nhận email
Guest ──────→ UC-17: Đánh giá
```

**Lưu ý:**
- Các đường nối không được chéo nhau (nếu chéo, dùng điểm uốn)
- Đường nối nên đi theo đường ngắn nhất
- Tránh góc vuông 90°, ưu tiên đường chéo tự nhiên

---

### **B. ADMIN → USE CASES (7 đường nối)**

**Danh sách 7 associations:**

```
Admin ──────→ UC-21: Quản lý booking
Admin ──────→ UC-22: Quản lý phòng
Admin ──────→ UC-23: Quản lý tồn kho
Admin ──────→ UC-24: Khóa ngày
Admin ──────→ UC-25: Quản lý extras
Admin ──────→ UC-26: Quản lý coupon
Admin ──────→ UC-27: Tạo hóa đơn
```

---

## 📦 GROUPING (Nhóm Use Cases - Optional nhưng đẹp)

Để dễ nhìn, bạn có thể vẽ các **packages** (hộp chấm chấm) để nhóm UC:

**Cách vẽ:**
1. Vẽ rectangle với viền nét đứt (dashed line)
2. Viết label ở góc trên cùng

**Các nhóm:**

### **Package 1: Search & Browse**
- Viền: Dashed rectangle màu xanh
- Label: "«subsystem» Search & Browse"
- Chứa: UC-01, UC-02

### **Package 2: Booking Process**
- Viền: Dashed rectangle màu xanh đậm
- Label: "«subsystem» Booking Process"
- Chứa: UC-03, UC-04, UC-05, UC-06, UC-07

### **Package 3: Checkout**
- Viền: Dashed rectangle màu xanh lá
- Label: "«subsystem» Checkout"
- Chứa: UC-08, UC-09, UC-10, UC-11, UC-12, UC-13

### **Package 4: Review System**
- Viền: Dashed rectangle màu tím
- Label: "«subsystem» Review"
- Chứa: UC-17

### **Package 5: Admin - Booking**
- Viền: Dashed rectangle màu vàng
- Label: "«subsystem» Admin - Bookings"
- Chứa: UC-21

### **Package 6: Admin - Rooms**
- Viền: Dashed rectangle màu vàng đậm
- Label: "«subsystem» Admin - Rooms"
- Chứa: UC-22, UC-23, UC-24

### **Package 7: Admin - Pricing**
- Viền: Dashed rectangle màu cam
- Label: "«subsystem» Admin - Pricing"
- Chứa: UC-25, UC-26

### **Package 8: Admin - Invoicing**
- Viền: Dashed rectangle màu xanh lá
- Label: "«subsystem» Admin - Reports"
- Chứa: UC-27

---

## 🎨 MÃU SẮC ĐỀ XUẤT (COLOR PALETTE)

```css
/* Guest Use Cases */
Search & Browse:     #E3F2FD (Light Blue)
Booking Process:     #BBDEFB (Blue)
Checkout:            #C8E6C9 (Light Green)
Review:              #E1BEE7 (Light Purple)

/* Admin Use Cases */
Booking Management:  #FFF9C4 (Light Yellow)
Room Management:     #FFE082 (Yellow)
Pricing:             #FFCC80 (Light Orange)
Invoicing:           #C5E1A5 (Light Green)

/* Other Elements */
System Boundary:     #FFFFFF (White) với viền #000000
Actors:              #000000 (Black)
Association lines:   #000000 (Black)
Package borders:     #9E9E9E (Grey) - Dashed
```

---

## 🔧 CÁC RELATIONSHIPS ĐẶC BIỆT (Include/Extend - Optional)

Nếu muốn chi tiết hơn, có thể thêm:

### **«include» relationships:**

**UC-08 (Checkout) include UC-09 (Nhập thông tin)**
```
UC-08 ··········> UC-09
      «include»
```

**Cách vẽ:**
1. Vẽ dashed arrow (mũi tên nét đứt) từ UC-08 đến UC-09
2. Viết "«include»" ở giữa mũi tên

**Các include khác:**
- UC-10 include UC-09 (Xác nhận cần thông tin)
- UC-11 include UC-13 (Hoàn tất thì gửi email)
- UC-22 include UC-23 (Quản lý phòng cần quản lý tồn kho)

---

### **«extend» relationships:**

**UC-04 (Thêm extras) extends UC-03 (Thêm vào giỏ)**
```
UC-04 <··········· UC-03
      «extend»
```

**Cách vẽ:**
1. Vẽ dashed arrow từ UC-04 đến UC-03 (ngược lại với include)
2. Viết "«extend»" ở giữa

**Các extend khác:**
- UC-05 extends UC-06 (Coupon là optional trong giỏ hàng)
- UC-07 extends UC-06 (Xóa là optional)

---

## ✅ CHECKLIST HOÀN THÀNH

Khi vẽ xong, check lại:

- [ ] System boundary có label rõ ràng
- [ ] 2 actors được vẽ đúng vị trí (trái/phải)
- [ ] 21 UC ellipses được vẽ đầy đủ
- [ ] Tất cả UC có mã số (UC-XX) và tên tiếng Việt
- [ ] Guest có 14 associations nối đến 14 UC
- [ ] Admin có 7 associations nối đến 7 UC
- [ ] Các đường nối không chéo nhau
- [ ] Màu sắc được áp dụng để phân biệt nhóm
- [ ] (Optional) Packages được vẽ để nhóm UC
- [ ] (Optional) Include/Extend relationships được thêm
- [ ] Font chữ dễ đọc (Arial, Calibri, hoặc Segoe UI)
- [ ] Kích thước phù hợp để in A3/A4

---

## 📸 HÌNH MINH HỌA ASCII (LAYOUT TỔNG QUAN)

```
┌────────────────────────────────────────────────────────────────────────────┐
│                                                                            │
│   Guest          ┌─────────────────────────────────────────────┐   Admin  │
│     O            │   Hotel Booking System                     │     O     │
│    /|\───────────│                                            │─────/|\   │
│    / \           │   ┌──────────────┐    ┌──────────────┐    │     / \   │
│                  │   │ UC-01:       │    │ UC-21:       │    │           │
│                  │   │ Search       │    │ Manage       │    │           │
│         ┌────────│   │ Rooms        │    │ Bookings     │    │───────┐   │
│         │        │   └──────────────┘    └──────────────┘    │       │   │
│         │        │                                            │       │   │
│         │        │   ┌──────────────┐    ┌──────────────┐    │       │   │
│         │        │   │ UC-02:       │    │ UC-22:       │    │       │   │
│         └────────│───│ View Room    │    │ Manage       │────│───────┘   │
│                  │   │ Details      │    │ Rooms        │    │           │
│                  │   └──────────────┘    └──────────────┘    │           │
│                  │                                            │           │
│                  │        [14 UC khác]      [5 UC khác]      │           │
│                  │                                            │           │
│                  └─────────────────────────────────────────────┘           │
│                                                                            │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## 💡 LƯU Ý KHI VẼ

1. **Không chéo lines:** Nếu bắt buộc phải chéo, dùng "bridge" (cầu nối nhỏ) để thể hiện đường nào ở trên
2. **Alignment:** Các UC trong cùng nhóm nên căn thẳng hàng dọc hoặc ngang
3. **Spacing:** Khoảng cách đều đặn tạo cảm giác chuyên nghiệp
4. **Label font:** 
   - UC name: 10-11pt, Bold
   - English name: 9pt, Italic
5. **Print test:** In thử ra giấy để check kích thước trước khi nộp

---

## 🎓 VÍ DỤ TEXT MÔ TẢ SƠ ĐỒ (Cho báo cáo)

**Mẫu text đặt bên dưới sơ đồ:**

> **Hình X.X: Use Case Diagram - Hệ thống Đặt phòng Khách sạn**
> 
> Sơ đồ Use Case tổng quan mô tả 21 chức năng chính của hệ thống, bao gồm:
> - **Guest (Khách hàng):** Tương tác với 14 use cases liên quan đến tìm kiếm, đặt phòng, thanh toán và đánh giá.
> - **Admin (Quản trị viên):** Quản lý 7 use cases về booking, phòng, tồn kho, giá và báo cáo.
> 
> Các use cases được nhóm thành 8 subsystems để dễ dàng quản lý và mở rộng: Search & Browse, Booking Process, Checkout, Review System, Admin Booking, Admin Rooms, Admin Pricing, và Admin Reports.

---

## 🚀 BẮT ĐẦU VẼ

**Thứ tự khuyến nghị:**
1. Vẽ System Boundary trước
2. Vẽ 2 Actors (Guest bên trái, Admin bên phải)
3. Vẽ 21 UC ellipses theo layout đã mô tả
4. Nối Guest với 14 UC của Guest
5. Nối Admin với 7 UC của Admin
6. (Optional) Thêm packages để nhóm
7. (Optional) Thêm include/extend relationships
8. Tô màu và chỉnh sửa layout
9. Thêm legend (chú thích) nếu cần
10. Export to PNG/PDF

**HOÀN THÀNH! 🎉**

---

**Thời gian ước tính:** 2-3 giờ (nếu vẽ tay hoặc dùng tool lần đầu)

**File này được tạo bởi Claude AI - Ngày: 26/05/2026**
