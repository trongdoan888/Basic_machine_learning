# 📐 HƯỚNG DẪN VẼ CONTEXT DIAGRAM (SYSTEM CONTEXT)

**Dự án:** Quan Trọng Hotel (Parkside Sunline Hotel)  
**Loại sơ đồ:** Context Diagram / Level 0 DFD  
**Mục đích:** Hiển thị ranh giới hệ thống và các external entities  
**Công cụ đề xuất:** Draw.io, Lucidchart, Visual Paradigm, Microsoft Visio

---

## 🎯 MỤC TIÊU

Vẽ Context Diagram để hiển thị:
- **Central Process:** Hệ thống Hotel Booking (1 process duy nhất ở giữa)
- **External Entities:** Các actors/systems bên ngoài (Guest, Admin, Email Server, WordPress Core, WooCommerce)
- **Data Flows:** Luồng dữ liệu vào/ra giữa entities và system
- **System Boundary:** Ranh giới rõ ràng giữa hệ thống và môi trường bên ngoài

---

## 📏 KÍCH THƯỚC VÀ LAYOUT

**Khổ giấy:** A4 hoặc A3 ngang (Landscape)  
**Layout:** Radial (tỏa tròn) - System ở giữa, entities xung quanh  
**Tỷ lệ:**
- Central System: Circle hoặc rounded rectangle lớn (8x8cm)
- External Entities: Rectangles nhỏ hơn (4x2cm)
- Khoảng cách từ center đến entities: 6-8cm

---

## 🎨 CÁC THÀNH PHẦN CẦN VẼ

### **1. CENTRAL SYSTEM (Hệ thống trung tâm)**

**Hình dạng:** Circle (vòng tròn) hoặc Rounded Rectangle

**Khuyến nghị:** Dùng **Circle** cho Context Diagram chuẩn DFD

**Kích thước:**
- Đường kính: 8cm
- Viền: 2-3pt, màu đen (#000000)

**Màu nền:** Light blue (#E3F2FD) hoặc white với viền đậm

**Label:**
```
┌─────────────────────┐
│                     │
│   Hotel Booking     │
│      System         │
│                     │
│  (Hệ thống đặt     │
│   phòng khách sạn) │
│                     │
│     Process 0       │ ← Có thể ghi số process
└─────────────────────┘
```

**Vị trí:** Chính giữa canvas

**Tọa độ cụ thể:**
- X: Center of canvas (50% width)
- Y: Center of canvas (50% height)

**Font:**
- Tên hệ thống: 14pt, Bold, Black
- Tên tiếng Việt: 11pt, Regular, Gray
- Process number: 10pt, Italic (optional)

---

### **2. EXTERNAL ENTITIES (Các thực thể bên ngoài)**

**Hình dạng:** Rectangle (hình chữ nhật)

**Kích thước mỗi entity:**
- Chiều rộng: 4-5cm
- Chiều cao: 2cm
- Viền: 1.5pt, màu đen

**Màu nền:** 
- User entities (Guest, Admin): Light yellow (#FFF9C4)
- System entities (WordPress, Email): Light gray (#F5F5F5)
- External services: Light green (#C8E6C9)

---

#### **Entity 1: Guest (Khách hàng)**

**Label:**
```
┌──────────────────────┐
│       👤             │ ← Icon (optional)
│      Guest           │
│   (Khách hàng)      │
└──────────────────────┘
```

**Vị trí:** Góc TRÊN BÊN TRÁI

**Tọa độ:**
- X: Center X - 10cm
- Y: Center Y - 10cm

**Data flows với system:**
- **Vào system:** Search criteria, Booking request, Payment info, Review data
- **Ra từ system:** Room availability, Booking confirmation, Invoice

---

#### **Entity 2: Admin (Quản trị viên)**

**Label:**
```
┌──────────────────────┐
│       👨‍💼            │
│      Admin           │
│  (Quản trị viên)    │
└──────────────────────┘
```

**Vị trí:** Góc TRÊN BÊN PHẢI

**Tọa độ:**
- X: Center X + 10cm
- Y: Center Y - 10cm

**Data flows:**
- **Vào system:** Room data, Pricing updates, Booking status, Block dates
- **Ra từ system:** Booking reports, Inventory status, Revenue analytics

---

#### **Entity 3: Email Server (SMTP)**

**Label:**
```
┌──────────────────────┐
│       📧             │
│   Email Server       │
│      (SMTP)          │
└──────────────────────┘
```

**Vị trí:** BÊN PHẢI

**Tọa độ:**
- X: Center X + 12cm
- Y: Center Y

**Data flows:**
- **Vào từ system:** Booking confirmation email, Invoice attachment
- **Ra đến:** Guest email address

---

#### **Entity 4: WordPress Core**

**Label:**
```
┌──────────────────────┐
│       🔷             │
│  WordPress Core      │
│    (CMS Platform)    │
└──────────────────────┘
```

**Vị trí:** DƯỚI BÊN TRÁI

**Tọa độ:**
- X: Center X - 10cm
- Y: Center Y + 10cm

**Data flows:**
- **Vào system:** User authentication, Post data, Media files
- **Ra từ system:** Room posts, Booking posts, Custom post types

---

#### **Entity 5: WooCommerce**

**Label:**
```
┌──────────────────────┐
│       🛒             │
│   WooCommerce        │
│  (E-commerce Engine) │
└──────────────────────┘
```

**Vị trí:** DƯỚI

**Tọa độ:**
- X: Center X
- Y: Center Y + 12cm

**Data flows:**
- **Vào system:** Order data, Payment status, Cart items
- **Ra từ system:** Product data (rooms), Booking orders, Invoices

---

#### **Entity 6: Payment Gateway (Optional)**

**Label:**
```
┌──────────────────────┐
│       💳             │
│  Payment Gateway     │
│   (Bank Transfer)    │
└──────────────────────┘
```

**Vị trí:** DƯỚI BÊN PHẢI

**Tọa độ:**
- X: Center X + 10cm
- Y: Center Y + 10cm

**Lưu ý:** Trong UC-10, bạn dùng "Thanh toán tại quầy", nên entity này có thể bỏ hoặc ghi chú "Offline Payment"

**Data flows:**
- **Vào system:** Payment confirmation (offline)
- **Ra từ system:** Payment request

---

#### **Entity 7: Database (MySQL) - Optional**

**Label:**
```
┌──────────────────────┐
│       🗄️             │
│   MySQL Database     │
│    (Data Storage)    │
└──────────────────────┘
```

**Vị trí:** BÊN TRÁI

**Tọa độ:**
- X: Center X - 12cm
- Y: Center Y

**Lưu ý:** Một số sơ đồ Context không vẽ database vì coi nó là internal component, nhưng vẽ cũng OK

**Data flows:**
- **Vào system:** Query requests
- **Ra từ system:** Room data, Booking data, Customer data

---

## 🔗 DATA FLOWS (Luồng dữ liệu)

**Hình dạng:** Arrow (mũi tên) với label

**Kiểu đường:**
- Solid line (liền nét) với arrowhead
- Độ dày: 1.5-2pt
- Màu: Dark gray (#424242)

**Label:**
- Font: 9-10pt, Italic
- Vị trí: Ở giữa hoặc trên đường arrow
- Nền: White hoặc transparent với padding nhỏ

---

### **A. GUEST ←→ SYSTEM**

#### **Guest → System (Input data flows)**

**Flow 1:**
```
Guest ────────→ System
   "Search criteria"
   (Check-in, Check-out, Guests)
```
- Tên flow: "Search criteria"
- Thành phần: Check-in date, Check-out date, Adults, Children, Room type

**Flow 2:**
```
Guest ────────→ System
   "Booking request"
   (Room selection + Extras)
```
- Tên flow: "Booking request"
- Thành phần: Room ID, Dates, Guest count, Extras, Coupon

**Flow 3:**
```
Guest ────────→ System
   "Customer information"
   (Name, Email, Phone, Address)
```
- Tên flow: "Customer information"
- Chi tiết: Họ tên, Email, SĐT, Địa chỉ, Ghi chú

**Flow 4:**
```
Guest ────────→ System
   "Payment selection"
   (Payment method)
```
- Tên flow: "Payment selection"
- Giá trị: "Chuyển khoản" hoặc "Thanh toán khi nhận hàng"

**Flow 5:**
```
Guest ────────→ System
   "Review data"
   (Rating, Comment, Photos)
```
- Tên flow: "Review data"
- Thành phần: Rating (1-5 stars), Review text, Title, Images

---

#### **System → Guest (Output data flows)**

**Flow 6:**
```
System ────────→ Guest
   "Room availability"
   (Available rooms list)
```
- Tên flow: "Room availability"
- Thành phần: Room list, Prices, Photos, Capacity

**Flow 7:**
```
System ────────→ Guest
   "Booking confirmation"
   (Order details)
```
- Tên flow: "Booking confirmation"
- Thành phần: Order #, Total, Dates, Payment method

**Flow 8:**
```
System ────────→ Guest
   "Invoice (PDF)"
   (Billing document)
```
- Tên flow: "Invoice"
- Format: PDF file với order details

---

### **B. ADMIN ←→ SYSTEM**

#### **Admin → System (Input data flows)**

**Flow 9:**
```
Admin ────────→ System
   "Room data"
   (Room info + Settings)
```
- Tên flow: "Room data"
- Thành phần: Room name, Type, Price, Capacity, Gallery, Amenities

**Flow 10:**
```
Admin ────────→ System
   "Pricing updates"
   (Price calendar)
```
- Tên flow: "Pricing updates"
- Thành phần: Regular price, Date-based pricing, Seasonal rates

**Flow 11:**
```
Admin ────────→ System
   "Booking status"
   (Status changes)
```
- Tên flow: "Booking status"
- Giá trị: Pending → Processing → Confirmed → Completed / Cancelled

**Flow 12:**
```
Admin ────────→ System
   "Block dates"
   (Special date blocking)
```
- Tên flow: "Block dates"
- Thành phần: Date ranges, Reason (maintenance, event)

**Flow 13:**
```
Admin ────────→ System
   "Extras & Coupons"
   (Optional services)
```
- Tên flow: "Extras & Coupons"
- Thành phần: Extra services (name, price), Coupon codes (discount)

---

#### **System → Admin (Output data flows)**

**Flow 14:**
```
System ────────→ Admin
   "Booking reports"
   (Analytics data)
```
- Tên flow: "Booking reports"
- Thành phần: Total bookings, Revenue, Status breakdown, Date range

**Flow 15:**
```
System ────────→ Admin
   "Inventory status"
   (Room availability)
```
- Tên flow: "Inventory status"
- Thành phần: Available rooms, Booked rooms, Blocked dates

**Flow 16:**
```
System ────────→ Admin
   "Customer list"
   (Guest database)
```
- Tên flow: "Customer list"
- Thành phần: Customer name, Email, Total spent, Order count

---

### **C. SYSTEM ←→ EMAIL SERVER**

**Flow 17:**
```
System ────────→ Email Server
   "Booking confirmation email"
   (HTML email)
```
- Tên flow: "Confirmation email"
- Thành phần: Order details, Customer info, Invoice attachment

**Flow 18:**
```
Email Server ────────→ Guest
   "Email delivery"
   (To: Guest email)
```
- Tên flow: "Email delivery"
- Note: Vẽ đường nét đứt (dashed) vì đây là indirect flow

---

### **D. SYSTEM ←→ WORDPRESS CORE**

**Flow 19:**
```
WordPress Core ────────→ System
   "User authentication"
   (Login session)
```
- Tên flow: "Authentication"
- Thành phần: User ID, Role (guest/admin), Session token

**Flow 20:**
```
System ────────→ WordPress Core
   "Custom post types"
   (Room, Booking posts)
```
- Tên flow: "Post data"
- Thành phần: hb_room, hb_booking, hb_extra_room, hb_coupon

**Flow 21:**
```
WordPress Core ────────→ System
   "Media files"
   (Room images)
```
- Tên flow: "Media"
- Thành phần: Room photos, Gallery images

---

### **E. SYSTEM ←→ WOOCOMMERCE**

**Flow 22:**
```
System ────────→ WooCommerce
   "Product data"
   (Rooms as products)
```
- Tên flow: "Product data"
- Thành phần: Room converted to WooCommerce product

**Flow 23:**
```
WooCommerce ────────→ System
   "Order data"
   (Booking orders)
```
- Tên flow: "Order data"
- Thành phần: Order ID, Items, Total, Payment status

**Flow 24:**
```
System ────────→ WooCommerce
   "Cart updates"
   (Add/remove items)
```
- Tên flow: "Cart updates"
- Actions: Add room, Add extra, Apply coupon, Remove item

**Flow 25:**
```
WooCommerce ────────→ System
   "Payment status"
   (Payment confirmation)
```
- Tên flow: "Payment status"
- Giá trị: Pending, Processing, Completed, Failed

---

### **F. SYSTEM ←→ DATABASE (Optional)**

**Flow 26:**
```
System ────────→ Database
   "Data queries"
   (SQL queries)
```
- Tên flow: "Query"
- Loại: SELECT, INSERT, UPDATE, DELETE

**Flow 27:**
```
Database ────────→ System
   "Query results"
   (Data records)
```
- Tên flow: "Results"
- Thành phần: Rooms, Bookings, Customers, Orders

---

## 🎨 MÃU SẮC VÀ STYLES

```css
/* Central System */
Background: #E3F2FD (Light Blue) hoặc #FFFFFF (White)
Border: #1976D2 (Blue), 3pt
Text: #000000 (Black), Bold

/* User Entities (Guest, Admin) */
Background: #FFF9C4 (Light Yellow)
Border: #F57C00 (Orange), 1.5pt
Text: #000000 (Black)

/* System Entities (WordPress, WooCommerce, Email) */
Background: #F5F5F5 (Light Gray)
Border: #616161 (Gray), 1.5pt
Text: #424242 (Dark Gray)

/* External Services (Payment, Database) */
Background: #C8E6C9 (Light Green)
Border: #388E3C (Green), 1.5pt
Text: #1B5E20 (Dark Green)

/* Data Flows (Arrows) */
Line Color: #424242 (Dark Gray)
Line Width: 1.5-2pt
Arrow Style: Solid arrowhead
Label Background: #FFFFFF with padding
Label Text: 9-10pt, Italic, #424242
```

---

## 📐 LAYOUT & POSITIONING

### **Recommended Layout: Radial (Tỏa tròn)**

```
         Entity 1 (Guest)
               ↓ ↑
               ↓ ↑
   Entity 4 ← SYSTEM → Entity 2 (Admin)
   (WordPress) ↓ ↑       ↓ ↑
               ↓ ↑       ↓ ↑
          Entity 5   Entity 3
        (WooCommerce) (Email)
               ↓ ↑
          Entity 6
         (Payment)
```

### **Vị trí cụ thể (với canvas 30x25cm):**

**Central System:**
- X: 15cm (center)
- Y: 12.5cm (center)
- Size: 8cm diameter circle

**External Entities:**
- Guest: (5cm, 2.5cm) - Góc trên trái
- Admin: (25cm, 2.5cm) - Góc trên phải
- Email Server: (27cm, 12.5cm) - Bên phải
- WordPress Core: (5cm, 22.5cm) - Góc dưới trái
- WooCommerce: (15cm, 24cm) - Dưới
- Payment Gateway: (25cm, 22.5cm) - Góc dưới phải
- Database (optional): (3cm, 12.5cm) - Bên trái

---

## ✏️ CÁCH VẼ TỪNG BƯỚC

### **Bước 1: Vẽ Central System**
1. Chọn tool "Circle" hoặc "Rounded Rectangle"
2. Vẽ ở giữa canvas (15cm, 12.5cm)
3. Set size: 8cm x 8cm
4. Fill color: #E3F2FD
5. Border: 3pt, #1976D2
6. Add text: "Hotel Booking System\n(Hệ thống đặt phòng khách sạn)\nProcess 0"
7. Text alignment: Center
8. Font: 14pt Bold (title), 11pt Regular (subtitle)

---

### **Bước 2: Vẽ External Entities (7 entities)**

**Cho mỗi entity:**
1. Chọn tool "Rectangle"
2. Vẽ theo vị trí đã chỉ định
3. Size: 4-5cm x 2cm
4. Fill color: Theo loại entity (Yellow/Gray/Green)
5. Border: 1.5pt, màu tương ứng
6. Add text: Entity name (tiếng Anh + tiếng Việt)
7. Alignment: Center
8. Font: 12pt Bold (name), 10pt Regular (Vietnamese)

**Thứ tự vẽ:**
1. Guest (5cm, 2.5cm)
2. Admin (25cm, 2.5cm)
3. Email Server (27cm, 12.5cm)
4. WordPress Core (5cm, 22.5cm)
5. WooCommerce (15cm, 24cm)
6. Payment Gateway (25cm, 22.5cm)
7. Database (3cm, 12.5cm) - optional

---

### **Bước 3: Vẽ Data Flows**

**Cho mỗi flow:**
1. Chọn tool "Connector" hoặc "Arrow"
2. Click vào entity source (điểm xuất phát)
3. Drag đến central system (hoặc ngược lại)
4. Release để tạo arrow
5. Set arrow properties:
   - Line style: Solid
   - Width: 1.5pt
   - Color: #424242
   - Arrowhead: Solid triangle
6. Add label:
   - Click vào arrow line
   - Insert text box
   - Type flow name
   - Font: 9pt Italic
   - Background: White với padding 2px

**Thứ tự vẽ data flows:**

**Priority 1 - Guest flows (8 flows):**
1. Guest → System: "Search criteria"
2. Guest → System: "Booking request"
3. Guest → System: "Customer information"
4. Guest → System: "Payment selection"
5. Guest → System: "Review data"
6. System → Guest: "Room availability"
7. System → Guest: "Booking confirmation"
8. System → Guest: "Invoice (PDF)"

**Priority 2 - Admin flows (8 flows):**
9. Admin → System: "Room data"
10. Admin → System: "Pricing updates"
11. Admin → System: "Booking status"
12. Admin → System: "Block dates"
13. Admin → System: "Extras & Coupons"
14. System → Admin: "Booking reports"
15. System → Admin: "Inventory status"
16. System → Admin: "Customer list"

**Priority 3 - External systems (11 flows):**
17. System → Email Server: "Confirmation email"
18. Email Server → Guest: "Email delivery" (dashed line)
19. WordPress → System: "User authentication"
20. System → WordPress: "Custom post types"
21. WordPress → System: "Media files"
22. System → WooCommerce: "Product data"
23. WooCommerce → System: "Order data"
24. System → WooCommerce: "Cart updates"
25. WooCommerce → System: "Payment status"
26. System → Database: "Data queries" (optional)
27. Database → System: "Query results" (optional)

---

### **Bước 4: Chỉnh sửa và hoàn thiện**

1. **Alignment check:**
   - Kiểm tra xem entities có căn thẳng hàng không
   - Dùng tool "Align" để chỉnh

2. **Arrow routing:**
   - Tránh các arrows chéo nhau
   - Dùng elbow (góc vuông) routing nếu cần
   - Ưu tiên đường thẳng hoặc cong tự nhiên

3. **Label positioning:**
   - Đảm bảo labels không đè lên arrows
   - Labels nên ở vị trí dễ đọc (trên hoặc cạnh arrow)

4. **Color consistency:**
   - Check tất cả entities cùng loại có màu giống nhau
   - System có màu nổi bật nhất

5. **Font consistency:**
   - Tất cả entity names: 12pt Bold
   - Tất cả flow labels: 9pt Italic
   - System name: 14pt Bold

6. **Add legend (chú thích):**
   Vẽ hộp legend ở góc dưới bên phải:
   ```
   ┌─────────────────────────┐
   │ Legend:                 │
   │ □ User Entity          │
   │ □ System Entity        │
   │ □ External Service     │
   │ → Data Flow            │
   │ ⇢ Indirect Flow        │
   └─────────────────────────┘
   ```

---

## 🖼️ ASCII REPRESENTATION (TỔNG QUAN)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│      [Guest]              [Admin]                                      │
│         │                    │                                          │
│         ↓                    ↓                                          │
│     Search criteria     Room data                                      │
│     Booking request     Pricing updates                                │
│     Customer info       Booking status                                 │
│         │                    │                                          │
│         └────────┐    ┌──────┘                                         │
│                  ↓    ↓                                                 │
│    [WordPress] ← → [HOTEL BOOKING] ← → [Email Server]                 │
│      Core           SYSTEM (0)          (SMTP)                          │
│                        ↑  ↓                                             │
│              ┌─────────┘  └─────────┐                                  │
│              ↓                      ↓                                    │
│        [WooCommerce]          [Payment Gateway]                        │
│         E-commerce              Bank Transfer                           │
│                                                                         │
│                        [MySQL Database]                                 │
│                         (Data Storage)                                  │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## ✅ CHECKLIST HOÀN THÀNH

- [ ] Central system được vẽ ở giữa với size phù hợp
- [ ] 7 external entities được vẽ đúng vị trí
- [ ] Tất cả entities có label rõ ràng (tiếng Anh + tiếng Việt)
- [ ] Màu sắc được áp dụng đúng theo loại entity
- [ ] Có ít nhất 20-25 data flows được vẽ
- [ ] Mỗi flow có label mô tả rõ ràng
- [ ] Arrows không chéo nhau (hoặc dùng bridge nếu bắt buộc)
- [ ] Font chữ consistent toàn sơ đồ
- [ ] Legend được thêm vào để giải thích ký hiệu
- [ ] Sơ đồ phù hợp để in A3/A4
- [ ] Có thể đọc và hiểu được ngay cả khi in đen trắng

---

## 📝 MẪU TEXT MÔ TẢ (Cho báo cáo)

**Đặt bên dưới sơ đồ:**

> **Hình X.X: Context Diagram - Hệ thống Đặt phòng Khách sạn**
>
> Context Diagram (Level 0 DFD) mô tả ranh giới của hệ thống Hotel Booking và các thực thể bên ngoài tương tác với hệ thống. Sơ đồ bao gồm:
>
> - **Hệ thống trung tâm:** Hotel Booking System (Process 0) xử lý tất cả logic đặt phòng, thanh toán và quản lý.
> - **External Entities:**
>   - **Guest (Khách hàng):** Tìm kiếm phòng, đặt phòng, thanh toán và đánh giá.
>   - **Admin (Quản trị viên):** Quản lý phòng, giá, tồn kho và xem báo cáo.
>   - **Email Server (SMTP):** Gửi email xác nhận đặt phòng cho khách.
>   - **WordPress Core:** Cung cấp nền tảng CMS, authentication và media management.
>   - **WooCommerce:** Xử lý giỏ hàng, đơn hàng và thanh toán.
>   - **Payment Gateway:** Xử lý thanh toán (Bank Transfer/Offline).
>   - **MySQL Database:** Lưu trữ tất cả dữ liệu hệ thống.
>
> - **Data Flows:** Có 27 luồng dữ liệu chính được định nghĩa, bao gồm: search criteria, booking requests, room data, order data, email notifications, và các báo cáo analytics.

---

## 💡 TIPS & BEST PRACTICES

1. **Simplicity:** Context Diagram nên đơn giản, chỉ hiển thị high-level view
2. **No internal processes:** Không vẽ các process bên trong hệ thống (để dành cho DFD Level 1)
3. **Bi-directional flows:** Nếu có data đi cả 2 chiều, vẽ 2 arrows riêng biệt hoặc dùng double-headed arrow
4. **Consistent naming:** Dùng noun phrases cho data flows (VD: "Booking request" chứ không phải "Request booking")
5. **External only:** Chỉ vẽ các entities BÊN NGOÀI system boundary

---

## ⏱️ THỜI GIAN ƯỚC TÍNH

- **Vẽ tay:** 1-1.5 giờ
- **Dùng tool (Draw.io, Visio):** 45-60 phút
- **Chỉnh sửa và hoàn thiện:** 15-20 phút

**TỔNG:** ~1.5-2 giờ

---

## 🚀 XUẤT FILE

**Formats đề xuất:**
- **PNG:** Độ phân giải 300dpi cho báo cáo in
- **PDF:** Vector format để zoom không bị vỡ
- **SVG:** Nếu cần edit sau này

**Settings khi export:**
- Resolution: 300 DPI (cho print)
- Background: White (không transparent)
- Margins: 1cm all sides

---

**HOÀN THÀNH! 🎉**

**File này được tạo bởi Claude AI - Ngày: 26/05/2026**
