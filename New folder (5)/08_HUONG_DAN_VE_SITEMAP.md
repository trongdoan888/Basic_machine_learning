# 📐 HƯỚNG DẪN VẼ SITEMAP - HỆ THỐNG HOTEL BOOKING

**Dự án:** Quan Trọng Hotel (Parkside Sunline Hotel)  
**Loại sơ đồ:** Sitemap (Information Architecture)  
**Số lượng sitemaps:** 2 sitemaps chính  
**Công cụ đề xuất:** Draw.io, Figma, Adobe XD, Lucidchart, MindMeister

---

## 🎯 MỤC TIÊU

### **Sitemap là gì?**
Sitemap (sơ đồ cấu trúc trang web) mô tả:
- **Tất cả các trang** trong website
- **Cấu trúc phân cấp** (hierarchy) của trang
- **Navigation flow** (luồng điều hướng)
- **Relationships** giữa các trang

### **Mục đích:**
- Hiển thị toàn bộ cấu trúc website
- Giúp user hiểu cách navigate
- Giúp developer hiểu cần code bao nhiêu pages
- Cơ sở cho thiết kế navigation menu

---

## 🎨 CẤU TRÚC MỘT PAGE NODE

**Hình dạng:** Rounded rectangle

```
┌─────────────────────────┐
│     Page Name           │ ← Page title
├─────────────────────────┤
│ /page-url               │ ← URL slug
│ UC-XX, UC-YY            │ ← Related Use Cases
└─────────────────────────┘
```

### **Kích thước:**
- Width: 5-6cm
- Height: 2-2.5cm
- Border radius: 0.5cm

### **Màu sắc theo loại page:**
- **Homepage:** #1976D2 (Blue) - Bold
- **Main pages:** #42A5F5 (Light Blue)
- **Sub pages:** #90CAF9 (Very Light Blue)
- **Forms/Actions:** #66BB6A (Green)
- **Admin pages:** #FFA726 (Orange)

### **Ký hiệu kết nối:**
- **──** : Normal navigation link
- **═══** : Primary navigation (main menu)
- **- - -** : Secondary link (footer, sidebar)
- **↓** : Parent-child relationship

---

# PART 1: FRONTEND SITEMAP (Guest/Public) 🌐

## 📊 TỔNG QUAN FRONTEND

**Số lượng pages:** ~20 pages  
**Levels:** 3 levels (Homepage → Main → Sub)  
**Navigation:** Main menu, Footer menu, Breadcrumb

---

## 🏠 LEVEL 0: HOMEPAGE (Root)

```
╔═════════════════════════╗
║      HOMEPAGE           ║
║   (Trang chủ)          ║
╠═════════════════════════╣
║ /                       ║
║ UC-01 (Search trigger)  ║
╚═════════════════════════╝
```

**Vị trí:** Center top (X: 15cm, Y: 2cm)

**Màu:** #1976D2 (Blue Bold)  
**Viền:** 3pt

**Nội dung Homepage:**
- Header (Logo, Menu, Search widget)
- Hero section (Search form - UC-01)
- Featured rooms (Highlights)
- Services overview
- Testimonials/Reviews
- Call-to-action
- Footer

**Related UCs:**
- UC-01: Tìm kiếm phòng (Search form on homepage)

---

## 📑 LEVEL 1: MAIN PAGES (Primary Navigation)

### **Page 1.1: About Us**

```
┌─────────────────────────┐
│      About Us           │
│    (Giới thiệu)         │
├─────────────────────────┤
│ /about                  │
│ Marketing content       │
└─────────────────────────┘
```

**Vị trí:** Left (X: 3cm, Y: 7cm)

**Màu:** #42A5F5 (Light Blue)

**Nội dung:**
- Hotel story
- Mission & Vision
- Team members
- Awards & Certifications
- Location map

---

### **Page 1.2: Rooms** ⭐

```
┌─────────────────────────┐
│       Rooms             │
│      (Phòng)           │
├─────────────────────────┤
│ /rooms                  │
│ UC-01, UC-02            │
└─────────────────────────┘
```

**Vị trí:** Center-left (X: 9cm, Y: 7cm)

**Màu:** #42A5F5 (Light Blue)  
**QUAN TRỌNG** - Core functionality page

**Nội dung:**
- Search form (UC-01)
- Filter sidebar (Price, Rating, Room Type)
- Room listings grid (UC-02)
- Pagination
- Sorting options

**Related UCs:**
- UC-01: Tìm kiếm phòng
- UC-02: Xem chi tiết phòng

**Sub-pages:**
- Single Room Detail (Level 2)

---

### **Page 1.3: Services**

```
┌─────────────────────────┐
│      Services           │
│     (Dịch vụ)          │
├─────────────────────────┤
│ /services               │
│ Marketing content       │
└─────────────────────────┘
```

**Vị trí:** Center (X: 15cm, Y: 7cm)

**Màu:** #42A5F5 (Light Blue)

**Nội dung:**
- Room service
- Restaurant
- Spa & Wellness
- Airport transfer
- Tour booking

---

### **Page 1.4: Gallery**

```
┌─────────────────────────┐
│      Gallery            │
│    (Thư viện ảnh)      │
├─────────────────────────┤
│ /gallery                │
│ Photo/Video gallery     │
└─────────────────────────┘
```

**Vị trí:** Center-right (X: 21cm, Y: 7cm)

**Màu:** #42A5F5 (Light Blue)

**Nội dung:**
- Hotel photos
- Room photos
- Facilities photos
- Lightbox viewer

---

### **Page 1.5: Contact**

```
┌─────────────────────────┐
│      Contact            │
│     (Liên hệ)          │
├─────────────────────────┤
│ /contact                │
│ Contact form            │
└─────────────────────────┘
```

**Vị trí:** Right (X: 27cm, Y: 7cm)

**Màu:** #42A5F5 (Light Blue)

**Nội dung:**
- Contact form
- Address & Map
- Phone & Email
- Business hours

---

## 🏨 LEVEL 2: SUB-PAGES (Secondary Navigation)

### **Page 2.1: Single Room Detail** ⭐⭐

```
┌─────────────────────────┐
│   Single Room           │
│   (Chi tiết phòng)     │
├─────────────────────────┤
│ /room/{room-slug}       │
│ UC-02, UC-04, UC-17     │
└─────────────────────────┘
```

**Parent:** Rooms (1.2)  
**Vị trí:** Below Rooms (X: 9cm, Y: 11cm)

**Màu:** #90CAF9 (Very Light Blue)

**Nội dung:**
- Room gallery (photos)
- Room details (UC-02)
  - Name, Type, Price
  - Capacity (adults, children)
  - Size, Bed type, View
  - Amenities
- Tabs:
  - Description
  - Additional Info
  - Pricing Plans
  - Reviews (UC-17)
- Booking form (UC-04)
  - Check-in/out dates
  - Guest count
  - Extras (UC-04)
  - Add to Cart button
- Related rooms

**Related UCs:**
- UC-02: Xem chi tiết phòng
- UC-04: Thêm extras
- UC-17: Đánh giá phòng (Review tab)

---

### **Page 2.2: Room Type Archive**

```
┌─────────────────────────┐
│   Room Type Archive     │
│  (Loại phòng)          │
├─────────────────────────┤
│ /room-type/{type-slug}  │
│ UC-01, UC-02            │
└─────────────────────────┘
```

**Parent:** Rooms (1.2)  
**Vị trí:** Below Rooms (X: 11cm, Y: 11cm)

**Màu:** #90CAF9

**Nội dung:**
- Filtered room list by type
- Example: /room-type/family-suite
- Show all Family Suite rooms

---

## 🛒 LEVEL 2: BOOKING FLOW PAGES

### **Page 2.3: Cart** ⭐

```
┌─────────────────────────┐
│        Cart             │
│      (Giỏ hàng)        │
├─────────────────────────┤
│ /cart                   │
│ UC-06, UC-07            │
└─────────────────────────┘
```

**Parent:** Accessible from any page (header cart icon)  
**Vị trí:** Below Homepage (X: 13cm, Y: 11cm)

**Màu:** #66BB6A (Green) - Action page

**Nội dung:**
- Cart table (UC-06)
  - Room name, dates, guests
  - Price breakdown
  - Extras
  - Quantity (always 1 for rooms)
  - Remove button (UC-07)
- Coupon input (UC-05)
- Cart totals
  - Subtotal
  - Discount
  - Total
- Proceed to Checkout button

**Related UCs:**
- UC-06: Xem giỏ hàng
- UC-07: Xóa khỏi giỏ
- UC-05: Áp coupon

---

### **Page 2.4: Checkout** ⭐⭐

```
┌─────────────────────────┐
│      Checkout           │
│   (Thanh toán)         │
├─────────────────────────┤
│ /checkout               │
│ UC-08, UC-09, UC-10     │
└─────────────────────────┘
```

**Parent:** Cart (2.3)  
**Vị trí:** Below Cart (X: 13cm, Y: 14cm)

**Màu:** #66BB6A (Green) - Action page

**Nội dung:**
- Billing form (UC-09)
  - First name, Last name
  - Email, Phone
  - Address, City, Country
  - Special requests
- Order review (UC-08)
  - Room details
  - Dates, guests
  - Price breakdown
- Payment methods (UC-10)
  - ⚪ Chuyển khoản ngân hàng
  - ⚪ Thanh toán khi nhận hàng
- Terms & conditions checkbox
- Place Order button

**Related UCs:**
- UC-08: Checkout
- UC-09: Nhập thông tin
- UC-10: Xác nhận booking

---

### **Page 2.5: Order Received (Confirmation)** ⭐

```
┌─────────────────────────┐
│   Order Received        │
│   (Xác nhận)           │
├─────────────────────────┤
│ /checkout/order-received│
│ UC-11, UC-12            │
└─────────────────────────┘
```

**Parent:** Checkout (2.4)  
**Vị trí:** Below Checkout (X: 13cm, Y: 17cm)

**Màu:** #66BB6A (Green)

**Nội dung:**
- Success message (UC-11)
- Order details (UC-12)
  - Order number (#1598)
  - Date
  - Total
  - Payment method
- Booking details
  - Room name
  - Check-in/out dates
  - Guests
  - Extras
- Customer details
- Next steps
- Download Invoice button (UC-27)

**Related UCs:**
- UC-11: Hoàn tất
- UC-12: Xem xác nhận
- UC-13: Nhận email (triggered automatically)

---

## 👤 LEVEL 2: ACCOUNT PAGES

### **Page 2.6: My Account**

```
┌─────────────────────────┐
│     My Account          │
│   (Tài khoản)          │
├─────────────────────────┤
│ /my-account             │
│ Login/Register/Dashboard│
└─────────────────────────┘
```

**Vị trí:** Far right (X: 25cm, Y: 11cm)

**Màu:** #90CAF9

**Nội dung:**
- Dashboard (if logged in)
  - Welcome message
  - Recent orders
  - Account details
- Login form (if not logged in)
- Register form

**Sub-pages:**
- Dashboard
- Orders
- Account details
- Logout

---

### **Page 2.7: Orders (My Bookings)**

```
┌─────────────────────────┐
│       Orders            │
│    (Đơn hàng)          │
├─────────────────────────┤
│ /my-account/orders      │
│ Booking history         │
└─────────────────────────┘
```

**Parent:** My Account (2.6)  
**Vị trí:** Below My Account (X: 25cm, Y: 14cm)

**Màu:** #90CAF9

**Nội dung:**
- Orders table
  - Order number
  - Date
  - Status
  - Total
  - Actions (View)
- View order detail link

---

### **Page 2.8: View Order Detail**

```
┌─────────────────────────┐
│    View Order           │
│  (Chi tiết đơn)        │
├─────────────────────────┤
│ /my-account/view-order/ID│
│ Order #1598 details     │
└─────────────────────────┘
```

**Parent:** Orders (2.7)  
**Vị trí:** Below Orders (X: 25cm, Y: 17cm)

**Màu:** #90CAF9

**Nội dung:**
- Order information
- Room details
- Booking dates
- Payment info
- Download Invoice

---

## 📄 LEVEL 2: UTILITY PAGES

### **Page 2.9: Search Results**

```
┌─────────────────────────┐
│   Search Results        │
│   (Kết quả)            │
├─────────────────────────┤
│ /search/?s=query        │
│ UC-01                   │
└─────────────────────────┘
```

**Vị trí:** Right of Rooms (X: 15cm, Y: 11cm)

**Màu:** #90CAF9

**Nội dung:**
- Search query display
- Filtered rooms (UC-01)
- No results message

---

### **Page 2.10: 404 Error Page**

```
┌─────────────────────────┐
│      404 Error          │
│   (Không tìm thấy)     │
├─────────────────────────┤
│ /404                    │
│ Error page              │
└─────────────────────────┘
```

**Màu:** #EF5350 (Red)

**Nội dung:**
- 404 message
- Search box
- Back to homepage link

---

## 📐 FRONTEND SITEMAP LAYOUT

```
                    ╔═══════════════╗
                    ║   HOMEPAGE    ║
                    ╚═══════════════╝
                            │
        ┌───────────┬───────┼───────┬───────────┐
        │           │       │       │           │
   ┌────────┐  ┌───────┐ ┌────────┐ ┌────────┐ ┌────────┐
   │ About  │  │ Rooms │ │Services│ │Gallery │ │Contact │
   └────────┘  └───┬───┘ └────────┘ └────────┘ └────────┘
                   │
        ┌──────────┼──────────┐
        │          │          │
   ┌─────────┐ ┌──────────┐ ┌────────────┐
   │ Single  │ │Room Type │ │   Cart     │
   │  Room   │ │ Archive  │ └──────┬─────┘
   └────┬────┘ └──────────┘        │
        │                           │
   (Review Tab)              ┌──────────┐
     UC-17                   │ Checkout │
                             └─────┬────┘
                                   │
                           ┌────────────┐
                           │   Order    │
                           │  Received  │
                           └────────────┘
```

**Canvas size:** 35cm x 25cm (A3 Landscape)

**Coordinates:**
- Level 0 (Y: 2cm): Homepage (15cm)
- Level 1 (Y: 7cm): About (3cm), Rooms (9cm), Services (15cm), Gallery (21cm), Contact (27cm)
- Level 2 (Y: 11-17cm): Sub-pages arranged below parents

---

## 🎨 MÀU SẮC FRONTEND SITEMAP

```css
/* Pages by Level */
Homepage (Level 0): #1976D2 (Blue Bold), 3pt border
Main Pages (Level 1): #42A5F5 (Light Blue), 2pt border
Sub Pages (Level 2): #90CAF9 (Very Light Blue), 1.5pt border

/* Special Pages */
Booking Flow (Cart, Checkout, Confirmation): #66BB6A (Green), 2pt border
Account Pages: #90CAF9 (Light Blue)
Error Pages: #EF5350 (Red)

/* Connectors */
Primary navigation: #1976D2 (Blue), 2pt solid
Secondary links: #90A4AE (Gray), 1pt solid
Parent-child: #424242 (Dark Gray), 1.5pt solid
```

---

# PART 2: ADMIN SITEMAP (Backend) 🔧

## 📊 TỔNG QUAN BACKEND

**Số lượng pages:** ~15 pages  
**Access:** /wp-admin/ (WordPress Admin)  
**User role:** Administrator  
**Related UCs:** UC-21 to UC-27

---

## 🏠 LEVEL 0: ADMIN DASHBOARD (Root)

```
╔═════════════════════════╗
║   Admin Dashboard       ║
║   (Bảng điều khiển)    ║
╠═════════════════════════╣
║ /wp-admin/              ║
║ Overview & Statistics   ║
╚═════════════════════════╝
```

**Vị trí:** Center top (X: 15cm, Y: 2cm)

**Màu:** #FF9800 (Orange Bold)  
**Viền:** 3pt

**Nội dung:**
- Welcome message
- Statistics widgets
  - Total bookings
  - Revenue
  - Pending bookings
  - Recent orders
- Quick actions
- Activity log

---

## 📑 LEVEL 1: MAIN ADMIN SECTIONS

### **Section 1.1: Bookings** ⭐⭐

```
┌─────────────────────────┐
│      Bookings           │
│   (Đặt phòng)          │
├─────────────────────────┤
│ /wp-admin/edit.php      │
│ ?post_type=hb_booking   │
│ UC-21                   │
└─────────────────────────┘
```

**Vị trí:** Left (X: 3cm, Y: 7cm)

**Màu:** #FF9800 (Orange)  
**QUAN TRỌNG NHẤT**

**Nội dung:**
- Bookings list table (UC-21)
  - Booking Order #
  - Customer
  - Date
  - Check-in/out
  - Total
  - Status (Pending/Processing/Cancelled)
- Filters
  - All / Pending / Processing / Cancelled
  - Date range
  - Customer search
- Bulk actions
- Calendar view

**Related UCs:**
- UC-21: Quản lý booking

**Sub-pages:**
- Edit Booking (Level 2)
- Calendar View (Level 2)

---

### **Section 1.2: Rooms** ⭐

```
┌─────────────────────────┐
│       Rooms             │
│      (Phòng)           │
├─────────────────────────┤
│ /wp-admin/edit.php      │
│ ?post_type=hb_room      │
│ UC-22, UC-23            │
└─────────────────────────┘
```

**Vị trí:** Center-left (X: 9cm, Y: 7cm)

**Màu:** #FF9800 (Orange)

**Nội dung:**
- Rooms list table (UC-22)
  - Room name
  - Room type
  - Price
  - Inventory
  - Status
- Add New Room button
- Bulk actions

**Related UCs:**
- UC-22: Quản lý phòng
- UC-23: Quản lý tồn kho

**Sub-pages:**
- Edit Room (Level 2)
- Add New Room (Level 2)

---

### **Section 1.3: Extras**

```
┌─────────────────────────┐
│       Extras            │
│   (Dịch vụ thêm)       │
├─────────────────────────┤
│ /wp-admin/edit.php      │
│ ?post_type=hb_extra     │
│ UC-25                   │
└─────────────────────────┘
```

**Vị trí:** Center (X: 15cm, Y: 7cm)

**Màu:** #FF9800 (Orange)

**Nội dung:**
- Extras list (UC-25)
  - Name (High Floor, Extra bed, Honeymoon)
  - Price
  - Unit
  - Type (number, trip)
  - Required
- Add New Extra button

**Related UCs:**
- UC-25: Quản lý extras

---

### **Section 1.4: Coupons**

```
┌─────────────────────────┐
│      Coupons            │
│    (Mã giảm giá)       │
├─────────────────────────┤
│ /wp-admin/              │
│ post.php?post_type=coupon│
│ UC-26                   │
└─────────────────────────┘
```

**Vị trí:** Center-right (X: 21cm, Y: 7cm)

**Màu:** #FF9800 (Orange)

**Nội dung:**
- Coupons list (UC-26)
  - Code (sale50k, sale_test)
  - Type (Fixed, Percentage)
  - Amount
  - Usage / Limit
  - Expiry date
- Add Coupon button

**Related UCs:**
- UC-26: Quản lý coupon

---

### **Section 1.5: Customers**

```
┌─────────────────────────┐
│     Customers           │
│    (Khách hàng)        │
├─────────────────────────┤
│ /wp-admin/              │
│ admin.php?page=customers│
│ Analytics               │
└─────────────────────────┘
```

**Vị trí:** Right (X: 27cm, Y: 7cm)

**Màu:** #FF9800 (Orange)

**Nội dung:**
- Customers table
  - Name
  - Email
  - Total bookings
  - Total spent
  - Last activity
- Customer filters

---

## 🏨 LEVEL 2: SUB-ADMIN PAGES

### **Page 2.1: Edit Booking** ⭐

```
┌─────────────────────────┐
│    Edit Booking         │
│  (Chỉnh sửa booking)   │
├─────────────────────────┤
│ /wp-admin/post.php      │
│ ?post=123&action=edit   │
│ UC-21                   │
└─────────────────────────┘
```

**Parent:** Bookings (1.1)  
**Vị trí:** Below Bookings (X: 3cm, Y: 11cm)

**Màu:** #FFB74D (Light Orange)

**Nội dung:**
- Booking details
  - Customer info (readonly)
  - Room
  - Check-in/out dates
  - Guests (adults, children)
  - Extras
  - Price breakdown
- Status dropdown
  - Pending → Processing → Confirmed
  - Cancel button
- Payment status
- Notes/Special requests
- Update button

**Related UCs:**
- UC-21: Quản lý booking (update status)

---

### **Page 2.2: Booking Calendar View**

```
┌─────────────────────────┐
│   Calendar View         │
│  (Xem theo lịch)       │
├─────────────────────────┤
│ /wp-admin/              │
│ admin.php?page=calendar │
│ UC-21                   │
└─────────────────────────┘
```

**Parent:** Bookings (1.1)  
**Vị trí:** Below Bookings (X: 5cm, Y: 11cm)

**Màu:** #FFB74D

**Nội dung:**
- Monthly calendar
- Bookings displayed as blocks
- Click to view/edit booking
- Filter by room

---

### **Page 2.3: Edit Room** ⭐

```
┌─────────────────────────┐
│     Edit Room           │
│  (Chỉnh sửa phòng)     │
├─────────────────────────┤
│ /wp-admin/post.php      │
│ ?post=110&action=edit   │
│ UC-22, UC-23, UC-24     │
└─────────────────────────┘
```

**Parent:** Rooms (1.2)  
**Vị trí:** Below Rooms (X: 9cm, Y: 11cm)

**Màu:** #FFB74D (Light Orange)

**Nội dung:**
- Room Settings tabs:
  1. **General** (UC-22)
     - Name, Description
     - Room type
     - Max adults, children
     - Room size
     - Amenities
  2. **Pricing** (UC-22)
     - Regular price per night
     - Date-based pricing
     - Add other pricing plan
  3. **Block Special Date** (UC-24) ⭐
     - Calendar view
     - Block This Month button
     - Open This Month button
     - Select dates to block
  4. **Gallery** (UC-22)
     - Upload room photos
  5. **Deposit** (optional)
  6. **Regulations** (optional)
  7. **FAQ** (optional)
  8. **Facilities** (optional)
  9. **External OTA Platforms**
     - Expedia, Trip.com, Agoda links
  10. **Extra Options** (UC-25)
      - Assign extras to room

**Related UCs:**
- UC-22: Quản lý phòng
- UC-23: Quản lý tồn kho (inventory field)
- UC-24: Khóa ngày (Block Special Date tab)

---

### **Page 2.4: Add New Extra**

```
┌─────────────────────────┐
│    Add New Extra        │
│  (Thêm dịch vụ)        │
├─────────────────────────┤
│ /wp-admin/post-new.php  │
│ ?post_type=hb_extra     │
│ UC-25                   │
└─────────────────────────┘
```

**Parent:** Extras (1.3)  
**Vị trí:** Below Extras (X: 15cm, Y: 11cm)

**Màu:** #FFB74D

**Nội dung:**
- Title input
- Description editor
- Extra Settings:
  - Price
  - Unit
  - Type (dropdown: Trip, Number)
  - Required checkbox
- Publish button

**Related UCs:**
- UC-25: Quản lý extras

---

### **Page 2.5: Add/Edit Coupon**

```
┌─────────────────────────┐
│   Add/Edit Coupon       │
│  (Thêm mã giảm giá)    │
├─────────────────────────┤
│ /wp-admin/post.php      │
│ ?post_type=shop_coupon  │
│ UC-26                   │
└─────────────────────────┘
```

**Parent:** Coupons (1.4)  
**Vị trí:** Below Coupons (X: 21cm, Y: 11cm)

**Màu:** #FFB74D

**Nội dung:**
- Coupon code input
- Description
- Discount type
  - ⚪ Fixed cart discount
  - ⚪ Percentage discount
- Coupon amount
- Minimum spend
- Maximum spend
- Usage limit
- Expiry date
- Publish button

**Related UCs:**
- UC-26: Quản lý coupon

---

## 📊 LEVEL 2: REPORTS & SETTINGS

### **Page 2.6: Reports**

```
┌─────────────────────────┐
│      Reports            │
│     (Báo cáo)          │
├─────────────────────────┤
│ /wp-admin/              │
│ admin.php?page=reports  │
│ Analytics               │
└─────────────────────────┘
```

**Vị trí:** Bottom left (X: 3cm, Y: 15cm)

**Màu:** #FFB74D

**Nội dung:**
- Revenue reports
- Booking statistics
- Room occupancy rate
- Customer analytics
- Date range filters
- Export CSV

---

### **Page 2.7: Settings**

```
┌─────────────────────────┐
│      Settings           │
│     (Cài đặt)          │
├─────────────────────────┤
│ /wp-admin/              │
│ admin.php?page=settings │
│ Configuration           │
└─────────────────────────┘
```

**Vị trí:** Bottom center (X: 9cm, Y: 15cm)

**Màu:** #FFB74D

**Nội dung:**
- General settings
- Booking settings
- Payment settings
- Email settings
- Checkout fields
- Tax settings

---

### **Page 2.8: Invoice Settings (PDF)** ⭐

```
┌─────────────────────────┐
│   Invoice Settings      │
│  (Cài đặt hóa đơn)     │
├─────────────────────────┤
│ /wp-admin/              │
│ admin.php?page=invoice  │
│ UC-27                   │
└─────────────────────────┘
```

**Vị trí:** Bottom right (X: 15cm, Y: 15cm)

**Màu:** #FFB74D

**Nội dung:**
- Shop Information
  - Company logo
  - Company name (Q&T Hospitality Company Limited)
  - Address (72-74 Đại Cồ Việt...)
  - Phone, Email
  - VAT number
- Invoice template
- PDF settings
  - Font size
  - Logo height

**Related UCs:**
- UC-27: Tạo hóa đơn PDF

---

## 📐 ADMIN SITEMAP LAYOUT

```
                 ╔═══════════════════╗
                 ║ Admin Dashboard   ║
                 ╚═══════════════════╝
                           │
       ┌───────────┬───────┼────────┬──────────┐
       │           │       │        │          │
  ┌─────────┐ ┌───────┐ ┌──────┐ ┌────────┐ ┌──────────┐
  │Bookings │ │ Rooms │ │Extras│ │Coupons │ │Customers │
  └────┬────┘ └───┬───┘ └──┬───┘ └───┬────┘ └──────────┘
       │          │        │         │
  ┌────┴────┐ ┌──┴───┐ ┌──┴───┐ ┌──┴───┐
  │  Edit   │ │ Edit │ │ Add  │ │ Edit │
  │ Booking │ │ Room │ │Extra │ │Coupon│
  └─────────┘ └──────┘ └──────┘ └──────┘
       │          │
  ┌─────────┐ ┌────────────┐
  │Calendar │ │Block Dates │
  │  View   │ │   (UC-24)  │
  └─────────┘ └────────────┘

       ┌──────────┐ ┌──────────┐ ┌──────────────┐
       │ Reports  │ │ Settings │ │Invoice Setup │
       └──────────┘ └──────────┘ └──────────────┘
```

**Canvas size:** 35cm x 20cm (A3 Landscape)

---

## 🎨 MÀU SẮC ADMIN SITEMAP

```css
/* Pages by Level */
Dashboard (Level 0): #FF9800 (Orange Bold), 3pt border
Main Sections (Level 1): #FF9800 (Orange), 2pt border
Sub Pages (Level 2): #FFB74D (Light Orange), 1.5pt border

/* Special Pages */
Booking Management: #FF9800 (Orange) - Most important
Settings Pages: #FFB74D (Light Orange)

/* Connectors */
Main navigation: #FF6F00 (Deep Orange), 2pt solid
Sub-navigation: #FFB74D (Light Orange), 1.5pt solid
```

---

## ✅ CHECKLIST VẼ SITEMAP

### **Frontend Sitemap:**
- [ ] Homepage làm root (center top)
- [ ] 5 main pages (Level 1) arranged horizontally
- [ ] Sub-pages (Level 2) arranged below parents
- [ ] Booking flow: Cart → Checkout → Order Received
- [ ] Account pages: My Account → Orders → View Order
- [ ] Màu sắc phân biệt levels
- [ ] Lines kết nối rõ ràng
- [ ] URLs được ghi đầy đủ
- [ ] UCs được reference

### **Admin Sitemap:**
- [ ] Dashboard làm root (center top)
- [ ] 5 main sections arranged horizontally
- [ ] Edit pages below parents
- [ ] Settings pages at bottom
- [ ] UC-24 (Block Dates) highlighted
- [ ] UC-27 (Invoice) included
- [ ] Màu orange consistent
- [ ] Access paths (/wp-admin/) clear

---

## 📝 MẪU TEXT MÔ TẢ

### **Frontend Sitemap:**

> **Hình X.X: Frontend Sitemap - Cấu trúc Website Công khai**
>
> Sitemap mô tả cấu trúc 20 trang website dành cho khách hàng, được tổ chức thành 3 levels:
>
> **Level 0 - Homepage:** Trang chủ là điểm vào chính với search form (UC-01) và featured rooms.
>
> **Level 1 - Main Pages:** 5 trang chính trong main menu: About Us, Rooms, Services, Gallery, và Contact. Trong đó, Rooms là trang quan trọng nhất với chức năng tìm kiếm và hiển thị phòng.
>
> **Level 2 - Sub Pages:** Bao gồm Single Room Detail (UC-02, UC-04, UC-17), booking flow (Cart → Checkout → Order Received tương ứng UC-06 → UC-10 → UC-12), và account pages (My Account, Orders, View Order).
>
> **Navigation:** Main menu ở header chứa Level 1 pages. Footer chứa additional links. Breadcrumb hiển thị path hierarchy.

---

### **Admin Sitemap:**

> **Hình X.X: Admin Sitemap - Cấu trúc Quản trị**
>
> Admin Sitemap mô tả 15 trang quản trị trong WordPress Admin, được tổ chức thành 2 levels:
>
> **Level 0 - Dashboard:** Trang tổng quan với statistics và quick actions.
>
> **Level 1 - Main Sections:** 5 sections chính: Bookings (UC-21), Rooms (UC-22, UC-23), Extras (UC-25), Coupons (UC-26), và Customers. Mỗi section có list view để quản lý items.
>
> **Level 2 - Edit Pages:** Bao gồm Edit Booking (UC-21), Edit Room với Block Special Date tab (UC-24), Add/Edit Extra (UC-25), Add/Edit Coupon (UC-26), và Invoice Settings (UC-27).
>
> **Reports & Settings:** 3 pages bổ sung ở bottom: Reports (analytics), Settings (configuration), và Invoice Settings (PDF generation setup).

---

## 💡 BEST PRACTICES

### **Sitemap Design:**
1. **Hierarchy clear:** Parent-child relationships rõ ràng
2. **Consistent sizing:** Cùng level cùng size
3. **Color coding:** Màu sắc phân biệt levels và page types
4. **URL included:** Ghi rõ URL paths
5. **UC references:** Reference UCs để link với requirements
6. **Alignment:** Pages cùng level align ngang

### **Information Architecture:**
1. **Max 3 clicks rule:** User không phải click quá 3 lần
2. **Breadcrumb friendly:** Hierarchy support breadcrumb navigation
3. **Mobile consideration:** Structure work cho mobile menu
4. **Search friendly:** Flat structure tốt cho SEO

---

## ⏱️ THỜI GIAN ƯỚC TÍNH

| Sitemap | Pages | Levels | Thời gian |
|---------|-------|--------|-----------|
| Frontend Sitemap | 20 pages | 3 levels | 1.5-2 giờ |
| Admin Sitemap | 15 pages | 2 levels | 1-1.5 giờ |

**TỔNG:** 2.5-3.5 giờ cho cả 2 sitemaps

---

## 🚀 XUẤT FILE

**Formats:**
- **PNG:** 300 DPI
- **PDF:** Vector (zoom không vỡ)
- **SVG:** Editable

**Tools:**
- Draw.io: Export as PNG/PDF/SVG
- Figma: Export as PNG/PDF
- Adobe XD: Share link hoặc export

---

**HOÀN THÀNH! 🎉**

**File này được tạo bởi Claude AI - Ngày: 26/05/2026**
