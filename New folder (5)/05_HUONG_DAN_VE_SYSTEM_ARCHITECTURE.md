# 📐 HƯỚNG DẪN VẼ SYSTEM ARCHITECTURE DIAGRAM

**Dự án:** Quan Trọng Hotel (Parkside Sunline Hotel)  
**Architecture Type:** 3-Tier Architecture (Presentation, Application, Data)  
**Deployment:** LAMP Stack (Linux, Apache, MySQL, PHP)  
**Công cụ đề xuất:** Draw.io, Lucidchart, Microsoft Visio, Visual Paradigm

---

## 🎯 MỤC TIÊU

Vẽ kiến trúc hệ thống đầy đủ hiển thị:
- **3 Tiers/Layers:** Presentation, Application, Data
- **Components:** Frontend, Backend, Database, External Services
- **Technologies:** WordPress, PHP, MySQL, Apache, WooCommerce
- **Communication:** HTTP requests, Database queries, Email protocols
- **Deployment:** Server infrastructure, hosting environment

---

## 📏 KÍCH THƯỚC VÀ LAYOUT

**Khổ giấy:** A4 hoặc A3 ngang (Landscape)  
**Layout:** Vertical tiers (3 tầng ngang xếp theo chiều dọc)  
**Spacing:**
- Giữa các tiers: 4cm
- Giữa các components trong 1 tier: 2cm

---

## 🎨 CẤU TRÚC TỔNG QUAN

```
┌─────────────────────────────────────────────────────────────────┐
│                     CLIENT DEVICES                              │ ← Layer 0
│  Desktop Browser | Mobile Browser | Tablet                      │
└─────────────────────────────────────────────────────────────────┘
                            ↓ HTTPS/HTTP
┌─────────────────────────────────────────────────────────────────┐
│                  PRESENTATION LAYER (Tier 1)                    │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐        │
│  │ Guest UI     │  │ Admin UI     │  │ Email        │        │
│  │ (Frontend)   │  │ (Dashboard)  │  │ Templates    │        │
│  └──────────────┘  └──────────────┘  └──────────────┘        │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│                  APPLICATION LAYER (Tier 2)                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐        │
│  │ WordPress    │  │ WP Hotel     │  │ WooCommerce  │        │
│  │ Core         │  │ Booking      │  │ Engine       │        │
│  └──────────────┘  └──────────────┘  └──────────────┘        │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│                     DATA LAYER (Tier 3)                         │
│  ┌──────────────────────────────────────────────────────┐      │
│  │            MySQL Database                            │      │
│  │  (wp_posts, wp_postmeta, wp_users, ...)             │      │
│  └──────────────────────────────────────────────────────┘      │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│                   EXTERNAL SERVICES                             │
│  [SMTP Server] [Payment Gateway] [CDN] [Backup Storage]        │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📦 LAYER 0: CLIENT DEVICES (Thiết bị người dùng)

**Vị trí:** Hàng trên cùng (Y: 1cm)

**Hình dạng:** Rectangle với icon

```
┌─────────────────────────────────────────────────────────────────┐
│                        CLIENT DEVICES                           │
│                                                                 │
│  ┌──────────┐     ┌──────────┐     ┌──────────┐              │
│  │ 💻 Desktop│     │ 📱 Mobile│     │ 💼 Tablet│              │
│  │  Browser │     │  Browser │     │  Browser │              │
│  ├──────────┤     ├──────────┤     ├──────────┤              │
│  │ Chrome   │     │ Safari   │     │ Chrome   │              │
│  │ Firefox  │     │ Chrome   │     │ Safari   │              │
│  │ Safari   │     │ Firefox  │     │ Edge     │              │
│  │ Edge     │     │ Edge     │     │          │              │
│  └──────────┘     └──────────┘     └──────────┘              │
│                                                                 │
│  User Actions: Search, Book, Review, Admin Management          │
└─────────────────────────────────────────────────────────────────┘
```

**Components:**
1. **Desktop Browser Box**
   - Size: 4cm x 3cm
   - Icon: 💻
   - Label: "Desktop Browser"
   - Browsers: Chrome, Firefox, Safari, Edge

2. **Mobile Browser Box**
   - Size: 3.5cm x 3cm
   - Icon: 📱
   - Label: "Mobile Browser"
   - Browsers: Safari (iOS), Chrome (Android)

3. **Tablet Browser Box**
   - Size: 3.5cm x 3cm
   - Icon: 💼
   - Label: "Tablet Browser"

**Màu:** Light gray (#F5F5F5)  
**Viền:** 1pt, #9E9E9E

---

## 🎨 TIER 1: PRESENTATION LAYER (Tầng giao diện)

**Vị trí:** Hàng thứ 2 (Y: 7cm)

**Hình dạng:** Rounded rectangle lớn bao bọc 3 components

```
┌─────────────────────────────────────────────────────────────────┐
│              PRESENTATION LAYER (Frontend - UI)                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐  │
│  │  Guest UI      │  │  Admin UI      │  │  Email         │  │
│  │  (Public)      │  │  (Dashboard)   │  │  Templates     │  │
│  ├────────────────┤  ├────────────────┤  ├────────────────┤  │
│  │ • Homepage     │  │ • Dashboard    │  │ • Booking      │  │
│  │ • Search Form  │  │ • Bookings     │  │   Confirmation │  │
│  │ • Room List    │  │ • Rooms        │  │ • Invoice      │  │
│  │ • Room Detail  │  │ • Customers    │  │ • Reminder     │  │
│  │ • Cart         │  │ • Pricing      │  │ • Cancellation │  │
│  │ • Checkout     │  │ • Coupons      │  │                │  │
│  │ • Confirmation │  │ • Reports      │  │                │  │
│  │ • Review Form  │  │ • Settings     │  │                │  │
│  │                │  │                │  │                │  │
│  │ Technology:    │  │ Technology:    │  │ Technology:    │  │
│  │ - HTML5        │  │ - HTML5        │  │ - HTML/CSS     │  │
│  │ - CSS3         │  │ - CSS3         │  │ - PHP          │  │
│  │ - JavaScript   │  │ - JavaScript   │  │                │  │
│  │ - jQuery       │  │ - jQuery       │  │                │  │
│  │ - AJAX         │  │ - AJAX         │  │                │  │
│  │ - Astra Theme  │  │ - WP Admin UI  │  │                │  │
│  └────────────────┘  └────────────────┘  └────────────────┘  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### **Component 1: Guest UI (Public Frontend)**

**Vị trí trong tier:** Trái (X: 2cm trong tier)

**Kích thước:** 6cm x 10cm

**Màu nền:** #E3F2FD (Light Blue)

**Nội dung:**
```
Guest UI (Public Frontend)
├─ Pages:
│  ├─ Homepage (UC-XX)
│  ├─ Search & Filter (UC-01)
│  ├─ Room Listings (UC-02)
│  ├─ Room Detail (UC-02)
│  ├─ Booking Form (UC-04)
│  ├─ Cart Page (UC-06)
│  ├─ Checkout (UC-08, 09, 10)
│  ├─ Confirmation (UC-12)
│  └─ Review Form (UC-17)
├─ Technologies:
│  ├─ HTML5 + CSS3
│  ├─ JavaScript + jQuery
│  ├─ AJAX (real-time updates)
│  ├─ Astra Theme v4.13.0
│  └─ Responsive Design
└─ Features:
   ├─ Search autocomplete
   ├─ Date picker
   ├─ Price calculator
   ├─ Image gallery
   ├─ Form validation
   └─ Shopping cart
```

---

### **Component 2: Admin UI (Backend Dashboard)**

**Vị trí:** Giữa (X: 10cm trong tier)

**Kích thước:** 6cm x 10cm

**Màu nền:** #FFF9C4 (Light Yellow)

**Nội dung:**
```
Admin UI (Dashboard)
├─ Modules:
│  ├─ Dashboard Overview
│  ├─ Bookings Management (UC-21)
│  ├─ Rooms Management (UC-22)
│  ├─ Inventory (UC-23)
│  ├─ Calendar / Block Dates (UC-24)
│  ├─ Extras Management (UC-25)
│  ├─ Coupons (UC-26)
│  ├─ Customers
│  ├─ Reports & Analytics
│  └─ Settings
├─ Technologies:
│  ├─ WordPress Admin UI
│  ├─ PHP Backend
│  ├─ JavaScript + jQuery
│  ├─ AJAX (async operations)
│  └─ WP REST API
└─ Features:
   ├─ Drag-drop calendar
   ├─ Data tables
   ├─ Charts (analytics)
   ├─ Bulk actions
   ├─ Export CSV/PDF
   └─ User permissions
```

---

### **Component 3: Email Templates**

**Vị trí:** Phải (X: 18cm trong tier)

**Kích thước:** 5cm x 10cm

**Màu nền:** #C8E6C9 (Light Green)

**Nội dung:**
```
Email Templates
├─ Types:
│  ├─ Booking Confirmation (UC-13)
│  ├─ Invoice Attached (UC-27)
│  ├─ Booking Reminder
│  ├─ Check-in Reminder
│  ├─ Cancellation Notice
│  ├─ Review Request
│  └─ Admin Notifications
├─ Technologies:
│  ├─ HTML Email
│  ├─ CSS (inline styles)
│  ├─ PHP (template engine)
│  └─ WP Mail SMTP
└─ Features:
   ├─ Responsive email
   ├─ Dynamic content
   ├─ PDF attachments
   ├─ Brand logo
   └─ Personalization
```

---

## 🔧 TIER 2: APPLICATION LAYER (Tầng ứng dụng)

**Vị trí:** Hàng thứ 3 (Y: 20cm)

**Hình dạng:** Rounded rectangle lớn bao bọc 4 components chính

```
┌─────────────────────────────────────────────────────────────────┐
│           APPLICATION LAYER (Business Logic - Backend)          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────┐  ┌──────────────┐  ┌─────────────┐  ┌────────┐ │
│  │WordPress │  │ WP Hotel     │  │ WooCommerce │  │ Astra  │ │
│  │  Core    │  │  Booking     │  │   Engine    │  │ Theme  │ │
│  │  6.9     │  │   v2.3.0     │  │   v10.7.0   │  │v4.13.0 │ │
│  └──────────┘  └──────────────┘  └─────────────┘  └────────┘ │
│       ↓               ↓                 ↓               ↓      │
│  ┌────────────────────────────────────────────────────────┐   │
│  │            PHP 8.0 Runtime Environment                 │   │
│  │  (Processes requests, Business logic, API calls)       │   │
│  └────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌────────────────────────────────────────────────────────┐   │
│  │                 WEB SERVER                              │   │
│  │  Apache 2.4 + mod_php + mod_rewrite                    │   │
│  │  • URL routing  • .htaccess  • SSL/TLS                 │   │
│  └────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### **Component 1: WordPress Core 6.9**

**Vị trí:** Trái (X: 2cm trong tier)

**Kích thước:** 5cm x 8cm

**Màu nền:** #BBDEFB (Blue)

**Nội dung:**
```
WordPress Core 6.9
├─ Core Functions:
│  ├─ User Authentication
│  ├─ Post Management (CPT)
│  ├─ Media Library
│  ├─ Theme System
│  ├─ Plugin Architecture
│  ├─ Hooks & Filters
│  ├─ Database Abstraction (wpdb)
│  └─ WP REST API
├─ Responsibilities:
│  ├─ Request routing
│  ├─ User sessions
│  ├─ Post/Meta CRUD
│  ├─ Taxonomy management
│  └─ Admin backend
└─ Version: 6.9
```

---

### **Component 2: WP Hotel Booking Plugin v2.3.0**

**Vị trí:** Giữa trái (X: 8cm trong tier)

**Kích thước:** 6cm x 8cm

**Màu nền:** #FFF9C4 (Yellow) - QUAN TRỌNG NHẤT

**Nội dung:**
```
WP Hotel Booking v2.3.0
├─ Core Modules:
│  ├─ Room Management
│  ├─ Booking Engine
│  ├─ Availability Calendar
│  ├─ Pricing Engine
│  ├─ Search & Filter
│  ├─ Extra Services
│  ├─ Coupon System
│  └─ Review System
├─ Custom Post Types:
│  ├─ hb_room
│  ├─ hb_booking
│  ├─ hb_extra_room
│  └─ hb_coupon
├─ Features:
│  ├─ Room search algorithm
│  ├─ Availability checker
│  ├─ Price calculator
│  ├─ Date blocking
│  ├─ Inventory management
│  ├─ Booking workflow
│  └─ Email notifications
└─ Integrations:
   ├─ WooCommerce (orders)
   ├─ WordPress (posts/meta)
   └─ Email (SMTP)
```

---

### **Component 3: WooCommerce v10.7.0**

**Vị trí:** Giữa phải (X: 15cm trong tier)

**Kích thước:** 5.5cm x 8cm

**Màu nền:** #FFE082 (Light Orange)

**Nội dung:**
```
WooCommerce v10.7.0
├─ Core Functions:
│  ├─ Product Management
│  │  (Rooms as Products)
│  ├─ Cart System
│  ├─ Checkout Process
│  ├─ Order Management
│  ├─ Payment Processing
│  ├─ Coupon System
│  └─ Tax Calculation
├─ Tables:
│  ├─ wp_woocommerce_order_items
│  ├─ wp_woocommerce_order_itemmeta
│  └─ wp_posts (orders)
├─ Payment Methods:
│  ├─ Bank Transfer (Offline)
│  ├─ Cash on Arrival
│  └─ (No online gateway)
└─ Features:
   ├─ Order emails
   ├─ Invoice generation
   ├─ Customer accounts
   └─ Order tracking
```

---

### **Component 4: Astra Theme v4.13.0**

**Vị trí:** Phải (X: 21cm trong tier)

**Kích thước:** 4cm x 8cm

**Màu nền:** #E1BEE7 (Light Purple)

**Nội dung:**
```
Astra Theme v4.13.0
├─ UI Components:
│  ├─ Header
│  ├─ Footer
│  ├─ Navigation
│  ├─ Sidebar
│  └─ Page Templates
├─ Features:
│  ├─ Responsive layout
│  ├─ Customizer options
│  ├─ WooCommerce styling
│  ├─ Performance optimized
│  └─ SEO friendly
└─ Technologies:
   ├─ HTML5 + CSS3
   ├─ JavaScript
   └─ PHP templating
```

---

### **Component 5: PHP Runtime & Web Server**

**Vị trí:** Dưới cùng của tier 2 (full width)

**Kích thước:** 24cm x 3cm (horizontal strip)

**Màu nền:** #ECEFF1 (Blue Gray)

**Nội dung:**
```
┌────────────────────────────────────────────────────────────┐
│  PHP 8.0 Runtime Environment                               │
│  • Object-oriented programming  • Composer dependencies    │
│  • Session management           • Error handling           │
└────────────────────────────────────────────────────────────┘
┌────────────────────────────────────────────────────────────┐
│  Apache 2.4 Web Server                                     │
│  • HTTP/HTTPS handling  • URL rewriting  • Virtual hosts   │
│  • mod_php              • mod_rewrite    • SSL/TLS         │
└────────────────────────────────────────────────────────────┘
```

---

## 🗄️ TIER 3: DATA LAYER (Tầng dữ liệu)

**Vị trí:** Hàng thứ 4 (Y: 32cm)

**Hình dạng:** Rounded rectangle lớn với database icon

```
┌─────────────────────────────────────────────────────────────────┐
│                     DATA LAYER (Storage)                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │            🗄️  MySQL Database 8.0                        │  │
│  │               (hotel_booking_db)                          │  │
│  ├──────────────────────────────────────────────────────────┤  │
│  │                                                           │  │
│  │  Core Tables:                                            │  │
│  │  ├─ wp_posts (rooms, bookings, extras, coupons)         │  │
│  │  ├─ wp_postmeta (metadata for all posts)                │  │
│  │  ├─ wp_users (customers, admins)                        │  │
│  │  └─ wp_usermeta (user metadata)                         │  │
│  │                                                           │  │
│  │  Taxonomy Tables:                                        │  │
│  │  ├─ wp_terms (room types)                               │  │
│  │  ├─ wp_term_taxonomy (taxonomy definitions)              │  │
│  │  └─ wp_term_relationships (post-term mapping)           │  │
│  │                                                           │  │
│  │  WooCommerce Tables:                                     │  │
│  │  ├─ wp_woocommerce_order_items                          │  │
│  │  └─ wp_woocommerce_order_itemmeta                       │  │
│  │                                                           │  │
│  │  Review Tables:                                          │  │
│  │  ├─ wp_comments (reviews)                               │  │
│  │  └─ wp_commentmeta (review metadata)                    │  │
│  │                                                           │  │
│  │  Storage:                                                │  │
│  │  • Data Files: /var/lib/mysql/hotel_booking_db/         │  │
│  │  • Size: ~500MB (estimated)                             │  │
│  │  • Encoding: utf8mb4_unicode_ci                          │  │
│  │  • Engine: InnoDB (transactions, FK constraints)        │  │
│  │                                                           │  │
│  │  Backup Strategy:                                        │  │
│  │  • Daily automated backups                              │  │
│  │  • Retention: 30 days                                    │  │
│  │  • Location: Remote backup server                       │  │
│  │                                                           │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Kích thước:** Full width, 12cm height

**Màu nền:** #C8E6C9 (Light Green)

---

## 🌐 TIER 4: EXTERNAL SERVICES (Dịch vụ bên ngoài)

**Vị trí:** Hàng dưới cùng (Y: 46cm)

**Hình dạng:** Rectangle với icons

```
┌─────────────────────────────────────────────────────────────────┐
│                    EXTERNAL SERVICES                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────┐  ┌──────────────┐  ┌────────────┐  ┌─────────┐ │
│  │📧 SMTP   │  │💳 Payment    │  │🌐 CDN      │  │💾Backup │ │
│  │  Server  │  │   Gateway    │  │  (Optional)│  │ Storage │ │
│  ├──────────┤  ├──────────────┤  ├────────────┤  ├─────────┤ │
│  │ Gmail    │  │ Bank         │  │ Cloudflare │  │ S3 or   │ │
│  │ SMTP     │  │ Transfer     │  │ or         │  │ Local   │ │
│  │          │  │ (Offline)    │  │ KeyCDN     │  │ Server  │ │
│  │Port: 587 │  │              │  │            │  │         │ │
│  │TLS/SSL   │  │ No online    │  │ Static     │  │ Daily   │ │
│  │          │  │ payment      │  │ assets     │  │ backup  │ │
│  └──────────┘  └──────────────┘  └────────────┘  └─────────┘ │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### **Service 1: SMTP Email Server**
- Provider: Gmail SMTP hoặc dedicated SMTP service
- Port: 587 (TLS) hoặc 465 (SSL)
- Authentication: Username + Password hoặc OAuth
- Usage: Gửi booking confirmation, invoices, reminders

### **Service 2: Payment Gateway (Offline)**
- Method: Bank Transfer (Chuyển khoản ngân hàng trực tiếp)
- Cash on Arrival (Thanh toán khi nhận hàng)
- NO online payment gateway (PayPal, Stripe)

### **Service 3: CDN (Optional)**
- Provider: Cloudflare, KeyCDN
- Purpose: Cache static assets (images, CSS, JS)
- Benefit: Faster page load, reduced server load

### **Service 4: Backup Storage**
- Location: Remote server hoặc cloud (AWS S3, Google Cloud)
- Frequency: Daily automated backups
- Retention: 30 days

---

## 🔗 COMMUNICATION FLOWS (Luồng giao tiếp)

### **Flow 1: Guest Booking Process**

```
Browser (Client)
  ↓ HTTPS GET /rooms?checkin=2026-05-26
Apache Web Server
  ↓ Parse request, route to WordPress
WordPress Core
  ↓ Load WP Hotel Booking plugin
WP Hotel Booking Plugin
  ↓ Query: SELECT * FROM wp_posts WHERE post_type='hb_room'
MySQL Database
  ↑ Return: Room data
WP Hotel Booking
  ↑ Render: Room listings
Browser
  ↓ User clicks "Book Room"
  ↓ AJAX POST /wp-admin/admin-ajax.php
WP Hotel Booking
  ↓ Add to WooCommerce Cart
WooCommerce
  ↓ Store in session / wp_usermeta
Browser
  ↓ Navigate to /checkout
WordPress + WooCommerce
  ↓ Render checkout form
Browser (User fills form)
  ↓ POST /checkout (booking data)
WooCommerce
  ↓ Create Order (wp_posts: shop_order)
  ↓ Create Order Items (wp_woocommerce_order_items)
WP Hotel Booking
  ↓ Create Booking (wp_posts: hb_booking)
  ↓ UPDATE inventory
MySQL Database
  ↓ Insert records
WP Hotel Booking
  ↓ Trigger email notification
SMTP Server
  ↓ Send confirmation email
Customer Email Inbox
```

---

### **Flow 2: Admin Managing Booking**

```
Admin Browser
  ↓ HTTPS GET /wp-admin/edit.php?post_type=hb_booking
Apache → WordPress Core → WP Admin UI
  ↓ Load WP Hotel Booking Admin
WP Hotel Booking
  ↓ Query: SELECT * FROM wp_posts WHERE post_type='hb_booking'
MySQL Database
  ↑ Return: Booking list
Admin UI
  ↓ Admin clicks "Edit Booking #123"
  ↓ GET /wp-admin/post.php?post=123&action=edit
WP Hotel Booking
  ↓ Load booking data from wp_postmeta
MySQL Database
  ↑ Return: Booking details (dates, customer, total, etc.)
Admin UI (Edit screen)
  ↓ Admin changes status: Pending → Confirmed
  ↓ POST /wp-admin/post.php (save action)
WP Hotel Booking
  ↓ UPDATE wp_postmeta SET meta_value='hb-confirmed'
  ↓ Trigger email notification
SMTP Server
  ↓ Send "Booking Confirmed" email
Customer Email
```

---

## 🎨 MÃU SẮC & ICONS

```css
/* Layers */
Client Devices: #F5F5F5 (Light Gray)
Presentation Layer: #E3F2FD (Light Blue)
Application Layer: #FFF9C4 (Light Yellow)
Data Layer: #C8E6C9 (Light Green)
External Services: #FFCCBC (Light Orange)

/* Components */
WordPress Core: #BBDEFB (Blue)
WP Hotel Booking: #FFF59D (Yellow) - MAIN
WooCommerce: #FFE082 (Orange)
Astra Theme: #E1BEE7 (Purple)
MySQL Database: #A5D6A7 (Green)

/* Icons */
Desktop: 💻
Mobile: 📱
Tablet: 💼
Email: 📧
Database: 🗄️
Payment: 💳
Cloud: ☁️
Backup: 💾
Lock (HTTPS): 🔒
```

---

## 📐 LAYOUT COORDINATES

**Canvas size:** 30cm × 50cm (A3 Portrait)

### **Y-coordinates (Top to bottom):**
- Client Devices: Y = 1cm
- Presentation Layer: Y = 7cm
- Application Layer: Y = 20cm
- Data Layer: Y = 32cm
- External Services: Y = 46cm

### **Arrows between tiers:**
- Double-headed arrows (↕) for bi-directional communication
- Solid lines for direct connections
- Dashed lines for async/indirect connections

---

## ✏️ CÁCH VẼ TỪNG BƯỚC

### **Bước 1: Vẽ 5 layers (horizontal strips)**
1. Vẽ 5 rounded rectangles ngang
2. Đặt labels: Client Devices, Presentation, Application, Data, External
3. Tô màu theo palette

---

### **Bước 2: Vẽ components trong mỗi layer**
1. Presentation: 3 boxes (Guest UI, Admin UI, Email)
2. Application: 4 boxes (WordPress, WP Hotel Booking, WooCommerce, Astra)
3. Data: 1 big box (MySQL)
4. External: 4 small boxes (SMTP, Payment, CDN, Backup)

---

### **Bước 3: Add details**
- Thêm text descriptions trong mỗi component
- Liệt kê technologies, features
- Add icons (💻📱📧🗄️💳)

---

### **Bước 4: Vẽ arrows (communication flows)**
1. Client → Presentation: HTTPS/HTTP
2. Presentation → Application: PHP function calls
3. Application → Data: SQL queries
4. Application → External: SMTP, API calls

**Arrow styles:**
- Solid thick arrow (3pt): Main data flow
- Dashed arrow (2pt): Async/optional flow
- Double-headed (↔): Bi-directional

---

### **Bước 5: Add annotations**
- Protocol labels (HTTPS, SQL, SMTP)
- Port numbers (80, 443, 587, 3306)
- Data formats (JSON, HTML, SQL)

---

## ✅ CHECKLIST

- [ ] 5 layers được vẽ rõ ràng
- [ ] Client devices có 3 types (desktop, mobile, tablet)
- [ ] Presentation layer có 3 components
- [ ] Application layer có 4 main components
- [ ] Data layer có MySQL với table list
- [ ] External services có 4 services
- [ ] Arrows hiển thị communication flows
- [ ] Icons được thêm vào
- [ ] Màu sắc consistent
- [ ] Technologies được list đầy đủ
- [ ] Legend giải thích colors/arrows
- [ ] Fit A3 portrait

---

## 📝 MẪU TEXT MÔ TẢ

> **Hình X.X: System Architecture Diagram - 3-Tier Architecture**
>
> Kiến trúc hệ thống Hotel Booking được thiết kế theo mô hình 3-tier (Presentation-Application-Data) chạy trên LAMP stack.
>
> **Tier 1 - Presentation Layer:** Frontend UI bao gồm Guest UI (public pages), Admin UI (dashboard), và Email Templates. Sử dụng HTML5, CSS3, JavaScript, jQuery và Astra Theme.
>
> **Tier 2 - Application Layer:** Backend logic với 4 components chính:
> - WordPress Core 6.9: Quản lý posts, users, authentication
> - WP Hotel Booking v2.3.0: Core booking engine, search, pricing
> - WooCommerce v10.7.0: Cart, checkout, orders, payments
> - Astra Theme v4.13.0: UI theming và responsive layout
>
> **Tier 3 - Data Layer:** MySQL Database 8.0 lưu trữ 15 tables chính (wp_posts, wp_postmeta, wp_users, etc.) sử dụng InnoDB engine với foreign key constraints.
>
> **External Services:** SMTP server (Gmail), Payment Gateway (offline), CDN (optional), Backup Storage.
>
> **Communication:** Client gửi HTTPS requests → Apache Web Server → PHP Runtime → WordPress + Plugins → MySQL Database. Responses trả về theo chiều ngược lại. Email notifications gửi qua SMTP server.

---

## 💡 BEST PRACTICES

1. **Layering:** Rõ ràng separation of concerns
2. **Arrows:** Label protocols và data formats
3. **Colors:** Consistent trong cùng loại component
4. **Icons:** Sử dụng emoji hoặc vector icons
5. **Whitespace:** Đủ khoảng trống giữa components

---

## ⏱️ THỜI GIAN ƯỚC TÍNH

- Vẽ 5 layers: 20-30 phút
- Vẽ components: 40-50 phút
- Add details: 30-40 phút
- Vẽ arrows & flows: 20-30 phút
- Format & style: 15-20 phút

**TỔNG:** 2-2.5 giờ

---

**HOÀN THÀNH! 🎉**

**File này được tạo bởi Claude AI - Ngày: 26/05/2026**
