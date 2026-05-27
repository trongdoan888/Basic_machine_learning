# 📐 HƯỚNG DẪN VẼ DATA FLOW DIAGRAMS (DFD) LEVEL 1 & 2

**Dự án:** Quan Trọng Hotel (Parkside Sunline Hotel)  
**Loại sơ đồ:** Data Flow Diagrams (DFD)  
**Số lượng diagrams:** 2 diagrams (Level 1 + Level 2)  
**Công cụ đề xuất:** Draw.io, Lucidchart, Visual Paradigm, Microsoft Visio

---

## 🎯 MỤC TIÊU

DFD mô tả:
- **Data flows** (luồng dữ liệu) trong hệ thống
- **Processes** (các quá trình xử lý)
- **Data stores** (nơi lưu trữ dữ liệu)
- **External entities** (entities bên ngoài)

### **3 Levels của DFD:**
- **Level 0 (Context):** Đã có ở File 02 - Context Diagram
- **Level 1:** Decompose system thành các processes chính
- **Level 2:** Decompose 1-2 processes Level 1 thành sub-processes

---

## 🎨 KÝ HIỆU DFD

### **Gane-Sarson Notation (Khuyến nghị):**

```
┌──────────────┐
│   External   │  ← External Entity (rectangle)
│   Entity     │
└──────────────┘

┌──────────────┐
│    1.0       │  ← Process (rounded rectangle)
│  Process     │     với số thứ tự
│    Name      │
└──────────────┘

═══════════════
   Data Store    ← Data Store (open rectangle)
 D1: Database
═══════════════

    ────>         ← Data Flow (arrow with label)
   label
```

### **Ký hiệu khác:**
- **Process:** Rounded rectangle với số (1.0, 2.0, ...)
- **External Entity:** Rectangle (giống Context Diagram)
- **Data Store:** Parallel lines ═══ với ID (D1, D2, ...)
- **Data Flow:** Arrow → với label mô tả dữ liệu

---

# DFD LEVEL 1: TỔNG QUAN HỆ THỐNG

## 📊 DECOMPOSITION CỦA LEVEL 0

**Level 0 (Context Diagram - File 02) có 1 process:**
- Process 0: Hotel Booking System

**Level 1 decompose thành 7 processes chính:**
1. Search & Browse Rooms
2. Booking Management
3. Cart & Checkout
4. Payment Processing
5. Review Management
6. Admin Room Management
7. Reporting & Analytics

---

## 🗺️ DFD LEVEL 1 - FULL DIAGRAM

**Canvas size:** A3 Landscape (42cm x 29.7cm)

### **External Entities (4):**

**E1: Guest**
```
┌──────────────┐
│    Guest     │  Vị trí: Top Left (3cm, 2cm)
└──────────────┘
```

**E2: Admin**
```
┌──────────────┐
│    Admin     │  Vị trí: Top Right (35cm, 2cm)
└──────────────┘
```

**E3: Email Server**
```
┌──────────────┐
│ Email Server │  Vị trí: Far Right (38cm, 15cm)
└──────────────┘
```

**E4: Payment Gateway**
```
┌──────────────┐
│   Payment    │  Vị trí: Far Right (38cm, 20cm)
│   Gateway    │
└──────────────┘
```

---

### **Processes (7):**

#### **Process 1.0: Search & Browse Rooms**

```
┌──────────────────────┐
│        1.0           │
│   Search & Browse    │  Vị trí: (8cm, 5cm)
│       Rooms          │
└──────────────────────┘
```

**Input Data Flows:**
- `Search Criteria` ← Guest (check-in, check-out, guests, type)

**Output Data Flows:**
- `Available Rooms` → Guest

**Access Data Stores:**
- Read: D1 Rooms, D2 Availability

**Description:** Tìm kiếm và lọc phòng theo tiêu chí, check availability

---

#### **Process 2.0: Booking Management**

```
┌──────────────────────┐
│        2.0           │
│     Booking          │  Vị trí: (18cm, 5cm)
│    Management        │
└──────────────────────┘
```

**Input Data Flows:**
- `Booking Request` ← Guest (room, dates, guests, extras)
- `Status Update` ← Admin (approve, cancel)

**Output Data Flows:**
- `Booking Confirmation` → Guest
- `Booking Status` → Admin

**Access Data Stores:**
- Read/Write: D3 Bookings
- Read: D1 Rooms, D2 Availability
- Write: D2 Availability (update inventory)

**Description:** Tạo, xem, cập nhật booking

---

#### **Process 3.0: Cart & Checkout**

```
┌──────────────────────┐
│        3.0           │
│      Cart &          │  Vị trí: (8cm, 12cm)
│     Checkout         │
└──────────────────────┘
```

**Input Data Flows:**
- `Add to Cart` ← Guest (room item)
- `Checkout Data` ← Guest (customer info, payment method)

**Output Data Flows:**
- `Cart Contents` → Guest
- `Order Data` → Process 4.0 (Payment Processing)

**Access Data Stores:**
- Read/Write: D4 Cart/Session
- Write: D5 Orders

**Description:** Quản lý giỏ hàng, nhập thông tin checkout

---

#### **Process 4.0: Payment Processing**

```
┌──────────────────────┐
│        4.0           │
│      Payment         │  Vị trí: (18cm, 12cm)
│     Processing       │
└──────────────────────┘
```

**Input Data Flows:**
- `Order Data` ← Process 3.0
- `Payment Confirmation` ← Payment Gateway (offline)

**Output Data Flows:**
- `Payment Status` → Process 2.0
- `Payment Request` → Payment Gateway

**Access Data Stores:**
- Write: D6 Payments

**Description:** Xử lý thanh toán, verify payment method

---

#### **Process 5.0: Review Management**

```
┌──────────────────────┐
│        5.0           │
│      Review          │  Vị trí: (28cm, 5cm)
│    Management        │
└──────────────────────┘
```

**Input Data Flows:**
- `Review Data` ← Guest (rating, text, images)
- `Approval Decision` ← Admin (approve/reject)

**Output Data Flows:**
- `Published Reviews` → Guest (display on room page)
- `Review Status` → Guest

**Access Data Stores:**
- Write: D7 Reviews
- Read: D3 Bookings (verify eligibility)

**Description:** Submit, moderate, publish reviews

---

#### **Process 6.0: Admin Room Management**

```
┌──────────────────────┐
│        6.0           │
│       Admin          │  Vị trí: (28cm, 12cm)
│       Room           │
│    Management        │
└──────────────────────┘
```

**Input Data Flows:**
- `Room Data` ← Admin (add/edit room)
- `Inventory Update` ← Admin (change quantity)
- `Block Dates` ← Admin (special dates)
- `Pricing Update` ← Admin (price changes)
- `Extras & Coupons` ← Admin

**Output Data Flows:**
- `Room List` → Admin
- `Availability Status` → Admin

**Access Data Stores:**
- Read/Write: D1 Rooms
- Read/Write: D2 Availability
- Read/Write: D8 Extras
- Read/Write: D9 Coupons

**Description:** CRUD rooms, manage inventory, pricing, extras, coupons

---

#### **Process 7.0: Reporting & Analytics**

```
┌──────────────────────┐
│        7.0           │
│    Reporting &       │  Vị trí: (8cm, 20cm)
│     Analytics        │
└──────────────────────┘
```

**Input Data Flows:**
- `Report Request` ← Admin (date range, filters)

**Output Data Flows:**
- `Reports` → Admin (revenue, occupancy, statistics)
- `Confirmation Email` → Email Server
- `Invoice` → Email Server

**Access Data Stores:**
- Read: D3 Bookings, D5 Orders, D6 Payments, D10 Customers

**Description:** Generate reports, send emails, create invoices

---

### **Data Stores (10):**

#### **D1: Rooms**
```
═══════════════════════
 D1: Rooms
 (wp_posts: hb_room)
═══════════════════════
```
**Vị trí:** (8cm, 9cm)  
**Data:** Room details (name, type, price, capacity, amenities)

---

#### **D2: Availability**
```
═══════════════════════
 D2: Availability
 (availability table)
═══════════════════════
```
**Vị trí:** (18cm, 9cm)  
**Data:** Room inventory, blocked dates

---

#### **D3: Bookings**
```
═══════════════════════
 D3: Bookings
 (wp_posts: hb_booking)
═══════════════════════
```
**Vị trí:** (18cm, 16cm)  
**Data:** Booking details (dates, guests, room, status)

---

#### **D4: Cart/Session**
```
═══════════════════════
 D4: Cart/Session
 (wp_usermeta)
═══════════════════════
```
**Vị trí:** (8cm, 16cm)  
**Data:** Temporary cart items

---

#### **D5: Orders**
```
═══════════════════════
 D5: Orders
 (wp_posts: shop_order)
═══════════════════════
```
**Vị trí:** (18cm, 18cm)  
**Data:** WooCommerce orders

---

#### **D6: Payments**
```
═══════════════════════
 D6: Payments
 (order metadata)
═══════════════════════
```
**Vị trí:** (28cm, 16cm)  
**Data:** Payment status, method, amount

---

#### **D7: Reviews**
```
═══════════════════════
 D7: Reviews
 (wp_comments)
═══════════════════════
```
**Vị trí:** (28cm, 9cm)  
**Data:** Reviews (rating, text, images, status)

---

#### **D8: Extras**
```
═══════════════════════
 D8: Extras
 (wp_posts: hb_extra)
═══════════════════════
```
**Vị trí:** (28cm, 18cm)  
**Data:** Extra services (name, price, type)

---

#### **D9: Coupons**
```
═══════════════════════
 D9: Coupons
 (shop_coupon)
═══════════════════════
```
**Vị trí:** (28cm, 20cm)  
**Data:** Discount codes

---

#### **D10: Customers**
```
═══════════════════════
 D10: Customers
 (wp_users)
═══════════════════════
```
**Vị trí:** (8cm, 24cm)  
**Data:** Customer info (name, email, phone)

---

## 🔗 DATA FLOWS LEVEL 1 (30+ flows)

### **Guest → Processes:**
1. `Search Criteria` → Process 1.0
2. `Booking Request` → Process 2.0
3. `Add to Cart` → Process 3.0
4. `Checkout Data` → Process 3.0
5. `Review Data` → Process 5.0

### **Admin → Processes:**
6. `Room Data` → Process 6.0
7. `Inventory Update` → Process 6.0
8. `Block Dates` → Process 6.0
9. `Status Update` → Process 2.0
10. `Approval Decision` → Process 5.0
11. `Report Request` → Process 7.0

### **Processes → Guest:**
12. `Available Rooms` ← Process 1.0
13. `Booking Confirmation` ← Process 2.0
14. `Cart Contents` ← Process 3.0
15. `Published Reviews` ← Process 5.0

### **Processes → Admin:**
16. `Booking Status` ← Process 2.0
17. `Room List` ← Process 6.0
18. `Reports` ← Process 7.0

### **Process to Process:**
19. `Order Data` (3.0 → 4.0)
20. `Payment Status` (4.0 → 2.0)

### **Processes ↔ Data Stores:**
21. Process 1.0 ⇄ D1 Rooms (Read)
22. Process 1.0 ⇄ D2 Availability (Read)
23. Process 2.0 ⇄ D3 Bookings (Read/Write)
24. Process 2.0 ⇄ D2 Availability (Write)
25. Process 3.0 ⇄ D4 Cart (Read/Write)
26. Process 3.0 → D5 Orders (Write)
27. Process 4.0 → D6 Payments (Write)
28. Process 5.0 → D7 Reviews (Write)
29. Process 6.0 ⇄ D1 Rooms (Read/Write)
30. Process 6.0 ⇄ D2 Availability (Read/Write)
31. Process 6.0 ⇄ D8 Extras (Read/Write)
32. Process 6.0 ⇄ D9 Coupons (Read/Write)
33. Process 7.0 ⇄ D3 Bookings (Read)
34. Process 7.0 ⇄ D5 Orders (Read)
35. Process 7.0 ⇄ D10 Customers (Read)

### **Processes → External:**
36. `Payment Request` (4.0 → Payment Gateway)
37. `Confirmation Email` (7.0 → Email Server)
38. `Invoice` (7.0 → Email Server)

### **External → Processes:**
39. `Payment Confirmation` (Payment Gateway → 4.0)

---

# DFD LEVEL 2: DECOMPOSE PROCESS 2.0 (BOOKING MANAGEMENT)

Process 2.0 là QUAN TRỌNG NHẤT, decompose thành 4 sub-processes:

---

## 📊 DFD LEVEL 2 - PROCESS 2.0

**Canvas size:** A4 Landscape (29.7cm x 21cm)

### **Sub-Processes:**

#### **Process 2.1: Create Booking**

```
┌──────────────────────┐
│        2.1           │
│      Create          │  Vị trí: (5cm, 5cm)
│     Booking          │
└──────────────────────┘
```

**Input:**
- `Booking Request` ← Guest (from Process 3.0 Checkout)

**Output:**
- `New Booking` → Process 2.2

**Access Data Stores:**
- Write: D3 Bookings
- Read: D1 Rooms, D2 Availability
- Write: D2 Availability (decrement inventory)

**Logic:**
- Validate dates, guests
- Check room availability
- Reserve inventory
- Create booking record
- Set status: Pending

---

#### **Process 2.2: Verify & Confirm Booking**

```
┌──────────────────────┐
│        2.2           │
│      Verify &        │  Vị trí: (15cm, 5cm)
│      Confirm         │
└──────────────────────┘
```

**Input:**
- `New Booking` ← Process 2.1
- `Payment Status` ← Process 4.0
- `Admin Approval` ← Admin

**Output:**
- `Confirmed Booking` → Process 2.4
- `Booking Status` → Guest

**Access Data Stores:**
- Read/Write: D3 Bookings (update status)

**Logic:**
- Check payment status
- Admin review (if needed)
- Update status: Pending → Processing → Confirmed
- Lock inventory

---

#### **Process 2.3: Update Booking**

```
┌──────────────────────┐
│        2.3           │
│      Update          │  Vị trí: (5cm, 12cm)
│     Booking          │
└──────────────────────┘
```

**Input:**
- `Status Change` ← Admin (Confirmed → CheckedIn → CheckedOut)
- `Cancellation Request` ← Guest or Admin

**Output:**
- `Updated Booking` → D3 Bookings
- `Inventory Release` → D2 Availability (if cancelled)

**Access Data Stores:**
- Read/Write: D3 Bookings
- Write: D2 Availability (release inventory)

**Logic:**
- Update booking status
- If cancelled: release inventory
- If checked-out: trigger review request

---

#### **Process 2.4: Notification & Invoice**

```
┌──────────────────────┐
│        2.4           │
│    Notification &    │  Vị trí: (15cm, 12cm)
│      Invoice         │
└──────────────────────┘
```

**Input:**
- `Confirmed Booking` ← Process 2.2
- `Updated Booking` ← Process 2.3

**Output:**
- `Confirmation Email` → Email Server
- `Invoice PDF` → D11 Invoices
- `Email with Invoice` → Guest

**Access Data Stores:**
- Write: D11 Invoices
- Read: D3 Bookings

**Logic:**
- Generate invoice PDF
- Send confirmation email with attachment
- Log notification

---

### **Data Stores in Level 2:**

#### **D1: Rooms** (from Level 1)
```
═══════════════════════
 D1: Rooms
═══════════════════════
```

#### **D2: Availability** (from Level 1)
```
═══════════════════════
 D2: Availability
═══════════════════════
```

#### **D3: Bookings** (from Level 1)
```
═══════════════════════
 D3: Bookings
═══════════════════════
```

#### **D11: Invoices** (new in Level 2)
```
═══════════════════════
 D11: Invoices
 (PDF files)
═══════════════════════
```

---

## 🔗 DATA FLOWS LEVEL 2 (15 flows)

1. `Booking Request` (Guest → 2.1)
2. `New Booking` (2.1 → 2.2)
3. `Payment Status` (Process 4.0 → 2.2)
4. `Admin Approval` (Admin → 2.2)
5. `Confirmed Booking` (2.2 → 2.4)
6. `Booking Status` (2.2 → Guest)
7. `Status Change` (Admin → 2.3)
8. `Cancellation Request` (Guest/Admin → 2.3)
9. `Updated Booking` (2.3 → D3)
10. `Inventory Release` (2.3 → D2)
11. `Updated Booking` (2.3 → 2.4)
12. `Confirmation Email` (2.4 → Email Server)
13. `Invoice PDF` (2.4 → D11)
14. 2.1 ⇄ D1 (Read rooms)
15. 2.1 ⇄ D2 (Read/Write availability)

---

## ✅ CHECKLIST VẼ DFD

### **Level 1:**
- [ ] 4 External entities (Guest, Admin, Email, Payment)
- [ ] 7 Processes (1.0 đến 7.0)
- [ ] 10 Data stores (D1 đến D10)
- [ ] 35+ Data flows với labels rõ ràng
- [ ] Process numbers đúng format (1.0, 2.0)
- [ ] Data store IDs consistent (D1, D2)
- [ ] Arrows có hướng chính xác
- [ ] No crossing lines (hoặc dùng bridges)

### **Level 2:**
- [ ] 4 Sub-processes (2.1 đến 2.4)
- [ ] Data stores từ Level 1 + new stores
- [ ] Input/Output flows từ Level 1
- [ ] Internal flows giữa sub-processes
- [ ] Process numbering: 2.1, 2.2, 2.3, 2.4

---

## 🎨 MÀU SẮC DFD

```css
/* External Entities */
Background: #FFF9C4 (Light Yellow)
Border: #F57C00 (Orange), 2pt

/* Processes */
Level 1: #E3F2FD (Light Blue)
Level 2: #BBDEFB (Blue - darker than Level 1)
Border: #1976D2 (Blue), 2pt
Text: #000000 (Black), 11pt Bold

/* Data Stores */
Background: #C8E6C9 (Light Green)
Lines: #388E3C (Green), 2pt
Text: #1B5E20 (Dark Green), 10pt

/* Data Flows */
Arrows: #424242 (Dark Gray), 1.5pt
Labels: #000000 (Black), 9pt
```

---

## 📝 MẪU TEXT MÔ TẢ

### **DFD Level 1:**

> **Hình X.X: Data Flow Diagram Level 1 - Hệ thống Đặt phòng**
>
> DFD Level 1 decompose hệ thống Hotel Booking thành 7 processes chính:
>
> 1. **Search & Browse Rooms** - Tìm kiếm và lọc phòng available
> 2. **Booking Management** - Tạo, xác nhận, cập nhật booking
> 3. **Cart & Checkout** - Quản lý giỏ hàng và checkout
> 4. **Payment Processing** - Xử lý thanh toán offline
> 5. **Review Management** - Submit và moderate reviews
> 6. **Admin Room Management** - CRUD rooms, inventory, pricing, extras, coupons
> 7. **Reporting & Analytics** - Generate reports và send emails
>
> Hệ thống sử dụng 10 data stores chính để lưu trữ Rooms, Availability, Bookings, Orders, Payments, Reviews, Extras, Coupons, và Customers. 4 external entities tương tác: Guest, Admin, Email Server, và Payment Gateway.

---

### **DFD Level 2:**

> **Hình X.X: Data Flow Diagram Level 2 - Booking Management Process**
>
> DFD Level 2 decompose Process 2.0 (Booking Management) thành 4 sub-processes:
>
> - **2.1 Create Booking** - Validate và tạo booking mới, reserve inventory
> - **2.2 Verify & Confirm** - Check payment, admin approval, confirm booking
> - **2.3 Update Booking** - Change status (CheckedIn, CheckedOut) hoặc cancel
> - **2.4 Notification & Invoice** - Generate invoice PDF và send email
>
> Sub-processes tương tác với 4 data stores: Rooms (D1), Availability (D2), Bookings (D3), và Invoices (D11). Process flow: Guest submits booking request → 2.1 creates → 2.2 verifies → 2.4 sends notification.

---

## 💡 BEST PRACTICES

1. **Consistent numbering:** Level 1: 1.0, 2.0 / Level 2: 2.1, 2.2
2. **Clear labels:** Data flows phải có tên cụ thể (Booking Request, not Data)
3. **No logic in flows:** Logic thuộc processes, flows chỉ mô tả data
4. **Balance:** DFD phải balanced - inputs/outputs Level 1 = inputs/outputs Level 0
5. **Data stores consistent:** Same store ID across levels
6. **No crossing:** Arrange để minimize crossing arrows

---

## ⏱️ THỜI GIAN ƯỚC TÍNH

| DFD | Entities | Processes | Stores | Flows | Thời gian |
|-----|----------|-----------|--------|-------|-----------|
| Level 1 | 4 | 7 | 10 | 35+ | 2-3 giờ |
| Level 2 | 2 | 4 | 4 | 15 | 1-1.5 giờ |

**TỔNG:** 3-4.5 giờ cho cả 2 DFD diagrams

---

**HOÀN THÀNH! 🎉**

**File này được tạo bởi Claude AI - Ngày: 26/05/2026**
