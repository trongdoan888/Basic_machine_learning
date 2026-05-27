# 📐 HƯỚNG DẪN VẼ COMPONENT & DEPLOYMENT DIAGRAMS

**Dự án:** Quan Trọng Hotel (Parkside Sunline Hotel)  
**Loại sơ đồ:** Component Diagram + Deployment Diagram (UML)  
**Số lượng diagrams:** 2 diagrams chính  
**Công cụ đề xuất:** Visual Paradigm, StarUML, Draw.io, Lucidchart

---

## 🎯 MỤC TIÊU

### **Component Diagram:**
- Hiển thị **components** (modules, plugins) của hệ thống
- Hiển thị **interfaces** (provided/required)
- Hiển thị **dependencies** giữa các components
- Mô tả cấu trúc logic của ứng dụng

### **Deployment Diagram:**
- Hiển thị **nodes** (physical/virtual servers)
- Hiển thị **artifacts** (files, databases)
- Hiển thị **communication paths** (protocols, ports)
- Mô tả cấu trúc vật lý triển khai hệ thống

---

# PART 1: COMPONENT DIAGRAM 🧩

## 📏 KÍCH THƯỚC VÀ LAYOUT

**Khổ giấy:** A4 Landscape (30cm x 21cm)  
**Layout:** Layered vertical (3 tầng dọc)  
**Component size:** 6-8cm x 4-5cm mỗi component

---

## 🎨 CẤU TRÚC MỘT COMPONENT

**UML Component notation:**

```
┌──────────────────────────────────┐
│  ┌──┐                            │
│  │  │  Component Name            │ ← Component icon + name
│  └──┘                            │
├──────────────────────────────────┤
│ «artifact»                       │ ← Stereotype (optional)
│ plugin-name.zip                  │
├──────────────────────────────────┤
│ Provided Interfaces:             │
│  ⊕ IBookingService               │ ← Provided (ball)
│  ⊕ ISearchService                │
│                                  │
│ Required Interfaces:             │
│  ⊖ IDatabaseService              │ ← Required (socket)
│  ⊖ IEmailService                 │
└──────────────────────────────────┘
```

### **Ký hiệu:**
- **Component icon:** Hình chữ nhật có 2 tabs nhỏ ở góc trên trái
- **⊕ (Ball):** Provided interface (component cung cấp)
- **⊖ (Socket):** Required interface (component cần)
- **→ (Arrow):** Dependency relationship

---

## 📦 DANH SÁCH 12 COMPONENTS CHÍNH

### **LAYER 1: PRESENTATION COMPONENTS (Frontend - Top)**

---

#### **Component 1: Guest UI Component**

**Vị trí:** Góc trên trái (X: 2cm, Y: 2cm)

```
┌──────────────────────────────────┐
│  ┌──┐                            │
│  │  │  Guest UI                  │
│  └──┘                            │
├──────────────────────────────────┤
│ «frontend»                       │
│ Astra Theme v4.13.0              │
├──────────────────────────────────┤
│ Responsibilities:                │
│  • Search form                   │
│  • Room listings                 │
│  • Booking form                  │
│  • Cart interface                │
│  • Checkout pages                │
│  • Review submission             │
│                                  │
│ Technologies:                    │
│  • HTML5, CSS3                   │
│  • JavaScript, jQuery            │
│  • AJAX                          │
│                                  │
│ Provided:                        │
│  ⊕ IUserInterface                │
│                                  │
│ Required:                        │
│  ⊖ IBookingService               │
│  ⊖ ISearchService                │
└──────────────────────────────────┘
```

**Màu nền:** #E3F2FD (Light Blue)  
**Viền:** 2pt, #1976D2 (Blue)

**Files included:**
- `/wp-content/themes/astra/` (PHP, CSS, JS files)
- Custom templates, layouts

---

#### **Component 2: Admin UI Component**

**Vị trí:** Giữa trên (X: 11cm, Y: 2cm)

```
┌──────────────────────────────────┐
│  ┌──┐                            │
│  │  │  Admin UI                  │
│  └──┘                            │
├──────────────────────────────────┤
│ «backend-ui»                     │
│ WordPress Admin                  │
├──────────────────────────────────┤
│ Responsibilities:                │
│  • Dashboard                     │
│  • Booking management            │
│  • Room management               │
│  • Reports & analytics           │
│  • Settings                      │
│                                  │
│ Technologies:                    │
│  • WordPress Admin API           │
│  • PHP, JavaScript               │
│  • React (Gutenberg)             │
│                                  │
│ Provided:                        │
│  ⊕ IAdminInterface               │
│                                  │
│ Required:                        │
│  ⊖ IBookingManager               │
│  ⊖ IRoomManager                  │
│  ⊖ IReportService                │
└──────────────────────────────────┘
```

**Màu nền:** #FFF9C4 (Light Yellow)  
**Viền:** 2pt, #F57C00 (Orange)

---

#### **Component 3: Email Template Component**

**Vị trí:** Góc trên phải (X: 20cm, Y: 2cm)

```
┌──────────────────────────────────┐
│  ┌──┐                            │
│  │  │  Email Templates           │
│  └──┘                            │
├──────────────────────────────────┤
│ «templates»                      │
│ HTML Email Templates             │
├──────────────────────────────────┤
│ Templates:                       │
│  • booking-confirmation.html     │
│  • invoice-email.html            │
│  • cancellation-notice.html      │
│  • review-request.html           │
│                                  │
│ Technologies:                    │
│  • HTML + Inline CSS             │
│  • PHP templating                │
│                                  │
│ Provided:                        │
│  ⊕ IEmailTemplate                │
│                                  │
│ Required:                        │
│  ⊖ IBookingData                  │
└──────────────────────────────────┘
```

**Màu nền:** #C8E6C9 (Light Green)  
**Viền:** 2pt, #388E3C (Green)

---

### **LAYER 2: APPLICATION COMPONENTS (Business Logic - Middle)**

---

#### **Component 4: WordPress Core**

**Vị trí:** Trái giữa (X: 2cm, Y: 9cm)

```
┌──────────────────────────────────┐
│  ┌──┐                            │
│  │  │  WordPress Core            │
│  └──┘                            │
├──────────────────────────────────┤
│ «framework»                      │
│ wordpress-6.9.zip                │
├──────────────────────────────────┤
│ Core Services:                   │
│  • Post/Page management          │
│  • User authentication           │
│  • Media library                 │
│  • Plugin architecture           │
│  • Theme system                  │
│  • REST API                      │
│  • Hooks & Filters               │
│                                  │
│ Provided:                        │
│  ⊕ IPostService                  │
│  ⊕ IUserService                  │
│  ⊕ IAuthService                  │
│  ⊕ IMediaService                 │
│  ⊕ IPluginAPI                    │
│                                  │
│ Required:                        │
│  ⊖ IDatabaseService              │
└──────────────────────────────────┘
```

**Màu nền:** #BBDEFB (Blue)  
**Viền:** 2pt, #1976D2 (Blue)

**Artifacts:**
- `/wp-includes/` (core PHP files)
- `/wp-admin/` (admin interface)
- `/wp-content/` (plugins, themes, uploads)

---

#### **Component 5: WP Hotel Booking Plugin** ⭐

**Vị trí:** Giữa (X: 11cm, Y: 9cm)

**ĐÂY LÀ COMPONENT QUAN TRỌNG NHẤT!**

```
┌──────────────────────────────────┐
│  ┌──┐                            │
│  │  │  WP Hotel Booking          │
│  └──┘                            │
├──────────────────────────────────┤
│ «plugin»                         │
│ wp-hotel-booking-v2.3.0.zip      │
├──────────────────────────────────┤
│ Core Modules:                    │
│  • Booking Engine                │
│  • Room Manager                  │
│  • Search & Filter               │
│  • Pricing Calculator            │
│  • Availability Checker          │
│  • Inventory Manager             │
│  • Extra Services                │
│  • Coupon System                 │
│  • Review System                 │
│                                  │
│ Provided:                        │
│  ⊕ IBookingService               │
│  ⊕ ISearchService                │
│  ⊕ IRoomService                  │
│  ⊕ IPricingService               │
│  ⊕ IAvailabilityService          │
│  ⊕ IInventoryService             │
│  ⊕ IExtraService                 │
│  ⊕ ICouponService                │
│  ⊕ IReviewService                │
│                                  │
│ Required:                        │
│  ⊖ IPostService (WordPress)      │
│  ⊖ IUserService (WordPress)      │
│  ⊖ IOrderService (WooCommerce)   │
│  ⊖ IEmailService                 │
└──────────────────────────────────┘
```

**Màu nền:** #FFF59D (Yellow) - HIGHLIGHT  
**Viền:** 3pt, #F57C00 (Orange) - BOLD

**Artifacts:**
- `/wp-content/plugins/wp-hotel-booking/`
- Custom Post Types: hb_room, hb_booking, hb_extra_room, hb_coupon
- Admin pages, REST endpoints

---

#### **Component 6: WooCommerce Plugin**

**Vị trí:** Phải giữa (X: 20cm, Y: 9cm)

```
┌──────────────────────────────────┐
│  ┌──┐                            │
│  │  │  WooCommerce               │
│  └──┘                            │
├──────────────────────────────────┤
│ «plugin»                         │
│ woocommerce-v10.7.0.zip          │
├──────────────────────────────────┤
│ Core Modules:                    │
│  • Cart System                   │
│  • Checkout Process              │
│  • Order Management              │
│  • Payment Gateway               │
│  • Coupon System                 │
│  • Tax Calculator                │
│  • Invoice Generator             │
│                                  │
│ Provided:                        │
│  ⊕ ICartService                  │
│  ⊕ ICheckoutService              │
│  ⊕ IOrderService                 │
│  ⊕ IPaymentService               │
│  ⊕ IInvoiceService               │
│                                  │
│ Required:                        │
│  ⊖ IPostService (WordPress)      │
│  ⊖ IUserService (WordPress)      │
│  ⊖ IProductData                  │
└──────────────────────────────────┘
```

**Màu nền:** #FFE082 (Orange Light)  
**Viền:** 2pt, #FF6F00 (Orange)

---

### **LAYER 3: DATA & UTILITY COMPONENTS (Bottom)**

---

#### **Component 7: Database Access Layer**

**Vị trí:** Trái dưới (X: 2cm, Y: 16cm)

```
┌──────────────────────────────────┐
│  ┌──┐                            │
│  │  │  Database Access Layer     │
│  └──┘                            │
├──────────────────────────────────┤
│ «data-access»                    │
│ wpdb Class                       │
├──────────────────────────────────┤
│ Responsibilities:                │
│  • SQL query execution           │
│  • Result mapping                │
│  • Transaction management        │
│  • Connection pooling            │
│                                  │
│ Methods:                         │
│  • get_results()                 │
│  • insert()                      │
│  • update()                      │
│  • delete()                      │
│  • prepare()                     │
│                                  │
│ Provided:                        │
│  ⊕ IDatabaseService              │
│                                  │
│ Required:                        │
│  ⊖ MySQL Connection              │
└──────────────────────────────────┘
```

**Màu nền:** #C8E6C9 (Green Light)  
**Viền:** 2pt, #388E3C (Green)

---

#### **Component 8: Email Service**

**Vị trí:** Giữa dưới (X: 11cm, Y: 16cm)

```
┌──────────────────────────────────┐
│  ┌──┐                            │
│  │  │  Email Service             │
│  └──┘                            │
├──────────────────────────────────┤
│ «service»                        │
│ WP Mail SMTP                     │
├──────────────────────────────────┤
│ Functions:                       │
│  • Send transactional emails     │
│  • Attach PDFs                   │
│  • Template rendering            │
│  • Queue management              │
│                                  │
│ Configuration:                   │
│  • SMTP server: smtp.gmail.com   │
│  • Port: 587 (TLS)               │
│  • Authentication: OAuth         │
│                                  │
│ Provided:                        │
│  ⊕ IEmailService                 │
│                                  │
│ Required:                        │
│  ⊖ IEmailTemplate                │
│  ⊖ SMTP Server                   │
└──────────────────────────────────┘
```

**Màu nền:** #E1BEE7 (Purple Light)  
**Viền:** 2pt, #7E57C2 (Purple)

---

#### **Component 9: PDF Generator**

**Vị trí:** Phải dưới (X: 20cm, Y: 16cm)

```
┌──────────────────────────────────┐
│  ┌──┐                            │
│  │  │  PDF Generator             │
│  └──┘                            │
├──────────────────────────────────┤
│ «library»                        │
│ TCPDF / mPDF                     │
├──────────────────────────────────┤
│ Functions:                       │
│  • Generate invoice PDFs         │
│  • Add header/footer             │
│  • Embed logo                    │
│  • Format tables                 │
│                                  │
│ Provided:                        │
│  ⊕ IPDFService                   │
│                                  │
│ Required:                        │
│  ⊖ IInvoiceData                  │
└──────────────────────────────────┘
```

**Màu nền:** #FFE0B2 (Orange Light)  
**Viền:** 2pt, #FF9800 (Orange)

---

## 🔗 COMPONENT DEPENDENCIES (Mối quan hệ)

### **Dependency Relationships:**

#### **1. Guest UI → WP Hotel Booking**
```
[Guest UI] ──────→ [WP Hotel Booking]
           «uses»
           IBookingService
```

**Dependency:** Guest UI gọi API của WP Hotel Booking để search, book rooms

---

#### **2. Admin UI → WP Hotel Booking**
```
[Admin UI] ──────→ [WP Hotel Booking]
            «uses»
            IRoomService, IBookingManager
```

---

#### **3. WP Hotel Booking → WordPress Core**
```
[WP Hotel Booking] ──────→ [WordPress Core]
                    «uses»
                    IPostService, IUserService
```

**Dependency:** Plugin sử dụng WordPress Post API để lưu rooms/bookings

---

#### **4. WP Hotel Booking → WooCommerce**
```
[WP Hotel Booking] ──────→ [WooCommerce]
                    «uses»
                    IOrderService, ICartService
```

**Dependency:** Booking tạo WooCommerce orders

---

#### **5. WP Hotel Booking → Email Service**
```
[WP Hotel Booking] ──────→ [Email Service]
                    «uses»
                    IEmailService
```

**Dependency:** Send confirmation emails

---

#### **6. WordPress Core → Database Access Layer**
```
[WordPress Core] ──────→ [Database Access Layer]
                  «uses»
                  IDatabaseService
```

---

#### **7. WooCommerce → PDF Generator**
```
[WooCommerce] ──────→ [PDF Generator]
               «uses»
               IPDFService
```

**Dependency:** Generate invoice PDFs

---

#### **8. Email Service → Email Templates**
```
[Email Service] ──────→ [Email Templates]
                 «uses»
                 IEmailTemplate
```

---

## 📐 LAYOUT COMPONENT DIAGRAM

```
┌──────────────────────────────────────────────────────────┐
│                    COMPONENT DIAGRAM                      │
├──────────────────────────────────────────────────────────┤
│                                                           │
│  ┌─────────┐    ┌─────────┐    ┌──────────────┐        │
│  │Guest UI │    │Admin UI │    │Email Template│        │
│  └────┬────┘    └────┬────┘    └──────┬───────┘        │
│       │              │                 │                 │
│       ↓              ↓                 ↓                 │
│  ┌─────────────────────────────────────────────┐        │
│  │          WP Hotel Booking Plugin            │        │
│  │               (Core Engine)                 │        │
│  └─────────────┬───────────────┬───────────────┘        │
│                ↓               ↓                         │
│       ┌──────────────┐   ┌─────────────┐               │
│       │WordPress Core│   │ WooCommerce │               │
│       └──────┬───────┘   └──────┬──────┘               │
│              ↓                   ↓                       │
│    ┌──────────────┐    ┌──────────────┐                │
│    │Database Layer│    │ PDF Generator│                │
│    └──────────────┘    └──────────────┘                │
│              ↓                                           │
│         [MySQL DB]                                      │
│                                                           │
└──────────────────────────────────────────────────────────┘
```

**Coordinates:**
- Layer 1 (Y: 2cm): Guest UI (2cm), Admin UI (11cm), Email Templates (20cm)
- Layer 2 (Y: 9cm): WordPress Core (2cm), WP Hotel Booking (11cm), WooCommerce (20cm)
- Layer 3 (Y: 16cm): DB Layer (2cm), Email Service (11cm), PDF Generator (20cm)

---

## 🎨 MÀU SẮC COMPONENT DIAGRAM

```css
/* Components by Type */
Frontend UI: #E3F2FD (Light Blue)
Backend UI: #FFF9C4 (Light Yellow)
Core Plugin (WP Hotel Booking): #FFF59D (Yellow - HIGHLIGHT)
Framework (WordPress): #BBDEFB (Blue)
Plugin (WooCommerce): #FFE082 (Orange Light)
Service Components: #E1BEE7 (Purple Light)
Data Access: #C8E6C9 (Green Light)
Templates: #C8E6C9 (Green Light)

/* Dependency Lines */
Uses dependency: #424242 (Dark Gray), 2pt solid arrow
Provided interface: #388E3C (Green), ball notation
Required interface: #D32F2F (Red), socket notation
```

---

# PART 2: DEPLOYMENT DIAGRAM 🖥️

## 📏 KÍCH THƯỚC VÀ LAYOUT

**Khổ giấy:** A4 Landscape (30cm x 21cm)  
**Layout:** Physical topology (mạng vật lý)  
**Node size:** 6-8cm x 5-7cm mỗi node

---

## 🎨 CẤU TRÚC MỘT NODE

**UML Node notation:**

```
┌────────────────────────────────────┐
│  ╔════════════════════════════╗   │
│  ║    Node Name               ║   │ ← 3D box (cube)
│  ╚════════════════════════════╝   │
├────────────────────────────────────┤
│ «device» or «execution environment»│
│ Operating System / Platform        │
├────────────────────────────────────┤
│ Artifacts:                         │
│  📦 application.war                │
│  📦 database.sql                   │
│                                    │
│ Properties:                        │
│  • CPU: 4 cores                    │
│  • RAM: 8GB                        │
│  • Storage: 100GB SSD              │
└────────────────────────────────────┘
```

### **Ký hiệu:**
- **Node (3D box):** Physical or virtual machine
- **📦 Artifact:** Deployable file
- **⟷ Communication path:** Network connection với protocol

---

## 🖥️ DANH SÁCH 7 NODES CHÍNH

### **NODE 1: Client Devices** 💻📱

**Vị trí:** Trên cùng bên trái (X: 2cm, Y: 2cm)

```
╔═══════════════════════════════════╗
║     Client Devices                ║
╚═══════════════════════════════════╝
├───────────────────────────────────┤
│ «device»                          │
│ Multiple Platforms                │
├───────────────────────────────────┤
│ Types:                            │
│  💻 Desktop Computers             │
│     • Windows 10/11               │
│     • macOS                       │
│     • Linux                       │
│                                   │
│  📱 Mobile Devices                │
│     • iOS (iPhone, iPad)          │
│     • Android                     │
│                                   │
│  💼 Tablets                       │
│                                   │
│ Browsers:                         │
│  • Chrome, Firefox                │
│  • Safari, Edge                   │
│                                   │
│ Network:                          │
│  • WiFi / 4G / 5G                 │
│  • HTTPS (443)                    │
└───────────────────────────────────┘
```

**Màu:** #F5F5F5 (Light Gray)

---

### **NODE 2: Web Server (Apache)** 🌐

**Vị trí:** Giữa trên (X: 11cm, Y: 2cm)

```
╔═══════════════════════════════════╗
║      Web Server                   ║
╚═══════════════════════════════════╝
├───────────────────────────────────┤
│ «execution environment»           │
│ Apache HTTP Server 2.4            │
│ Ubuntu 24.04 LTS                  │
├───────────────────────────────────┤
│ Artifacts:                        │
│  📦 httpd.conf                    │
│  📦 .htaccess                     │
│  📦 SSL certificates              │
│                                   │
│ Modules:                          │
│  • mod_php                        │
│  • mod_rewrite                    │
│  • mod_ssl                        │
│  • mod_headers                    │
│                                   │
│ Configuration:                    │
│  • DocumentRoot: /var/www/html    │
│  • Port: 80 (HTTP), 443 (HTTPS)   │
│  • Virtual Hosts: 1               │
│  • MaxClients: 150                │
│                                   │
│ Hardware:                         │
│  • CPU: 4 vCPU                    │
│  • RAM: 8GB                       │
│  • Storage: 100GB SSD             │
│  • Bandwidth: 1Gbps               │
└───────────────────────────────────┘
```

**Màu:** #E3F2FD (Light Blue)

---

### **NODE 3: PHP Runtime** 🐘

**Vị trí:** Phải trên (X: 20cm, Y: 2cm)

```
╔═══════════════════════════════════╗
║     PHP Runtime                   ║
╚═══════════════════════════════════╝
├───────────────────────────────────┤
│ «execution environment»           │
│ PHP 8.0                           │
├───────────────────────────────────┤
│ Artifacts:                        │
│  📦 php.ini                       │
│  📦 WordPress files               │
│  📦 Plugin files                  │
│                                   │
│ Extensions:                       │
│  • mysqli (MySQL)                 │
│  • gd (Image processing)          │
│  • curl (HTTP client)             │
│  • mbstring (Multibyte)           │
│  • xml                            │
│  • json                           │
│                                   │
│ Configuration:                    │
│  • memory_limit: 256M             │
│  • max_execution_time: 300s       │
│  • upload_max_filesize: 64M       │
│  • post_max_size: 64M             │
└───────────────────────────────────┘
```

**Màu:** #BBDEFB (Blue)

---

### **NODE 4: Application Server (WordPress)** 📦

**Vị trí:** Trái giữa (X: 2cm, Y: 10cm)

```
╔═══════════════════════════════════╗
║   Application Server              ║
║   (WordPress + Plugins)           ║
╚═══════════════════════════════════╝
├───────────────────────────────────┤
│ «execution environment»           │
│ WordPress 6.9 Platform            │
├───────────────────────────────────┤
│ Artifacts:                        │
│  📦 wordpress-6.9.zip             │
│  📦 wp-hotel-booking-v2.3.0.zip   │
│  📦 woocommerce-v10.7.0.zip       │
│  📦 astra-theme-v4.13.0.zip       │
│                                   │
│ Directory Structure:              │
│  /var/www/html/                   │
│   ├─ wp-admin/                    │
│   ├─ wp-includes/                 │
│   ├─ wp-content/                  │
│   │   ├─ plugins/                 │
│   │   │   ├─ wp-hotel-booking/    │
│   │   │   └─ woocommerce/         │
│   │   ├─ themes/                  │
│   │   │   └─ astra/               │
│   │   └─ uploads/                 │
│   └─ wp-config.php                │
│                                   │
│ Configuration:                    │
│  • DB_HOST: localhost             │
│  • DB_NAME: hotel_booking_db      │
│  • WP_DEBUG: false                │
└───────────────────────────────────┘
```

**Màu:** #FFF59D (Yellow - HIGHLIGHT)

---

### **NODE 5: Database Server (MySQL)** 🗄️

**Vị trí:** Giữa (X: 11cm, Y: 10cm)

```
╔═══════════════════════════════════╗
║    Database Server                ║
╚═══════════════════════════════════╝
├───────────────────────────────────┤
│ «database»                        │
│ MySQL 8.0                         │
│ Ubuntu 24.04 LTS                  │
├───────────────────────────────────┤
│ Artifacts:                        │
│  🗄️ hotel_booking_db.sql          │
│  🗄️ backup_daily.sql              │
│                                   │
│ Database:                         │
│  • Name: hotel_booking_db         │
│  • Encoding: utf8mb4_unicode_ci   │
│  • Engine: InnoDB                 │
│  • Tables: 15                     │
│  • Size: ~500MB                   │
│                                   │
│ Configuration:                    │
│  • Port: 3306                     │
│  • max_connections: 150           │
│  • innodb_buffer_pool_size: 2GB   │
│  • query_cache_size: 256MB        │
│                                   │
│ Backup:                           │
│  • Daily automated backup         │
│  • Retention: 30 days             │
│                                   │
│ Hardware:                         │
│  • CPU: 4 vCPU                    │
│  • RAM: 8GB                       │
│  • Storage: 200GB SSD (RAID 10)   │
└───────────────────────────────────┘
```

**Màu:** #C8E6C9 (Green Light)

---

### **NODE 6: Email Server (SMTP)** 📧

**Vị trí:** Phải giữa (X: 20cm, Y: 10cm)

```
╔═══════════════════════════════════╗
║     Email Server (SMTP)           ║
╚═══════════════════════════════════╝
├───────────────────────────────────┤
│ «external service»                │
│ Gmail SMTP / SendGrid             │
├───────────────────────────────────┤
│ Configuration:                    │
│  • Host: smtp.gmail.com           │
│  • Port: 587 (TLS)                │
│  • Auth: OAuth 2.0                │
│                                   │
│ Email Types:                      │
│  • Booking confirmation           │
│  • Invoice (with PDF)             │
│  • Cancellation notice            │
│  • Review request                 │
│  • Admin notifications            │
│                                   │
│ Rate Limits:                      │
│  • 500 emails/day (free)          │
│  • 100,000 emails/month (paid)    │
└───────────────────────────────────┘
```

**Màu:** #E1BEE7 (Purple Light)

---

### **NODE 7: Backup Storage** 💾

**Vị trí:** Dưới cùng giữa (X: 11cm, Y: 17cm)

```
╔═══════════════════════════════════╗
║     Backup Storage                ║
╚═══════════════════════════════════╝
├───────────────────────────────────┤
│ «storage»                         │
│ AWS S3 / Local Server             │
├───────────────────────────────────┤
│ Artifacts:                        │
│  💾 database-backup-YYYY-MM-DD.sql│
│  💾 files-backup-YYYY-MM-DD.tar.gz│
│                                   │
│ Backup Schedule:                  │
│  • Database: Daily at 2:00 AM     │
│  • Files: Weekly on Sunday        │
│                                   │
│ Retention Policy:                 │
│  • Daily backups: 30 days         │
│  • Weekly backups: 12 weeks       │
│  • Monthly backups: 12 months     │
│                                   │
│ Storage Capacity:                 │
│  • Total: 500GB                   │
│  • Used: ~150GB                   │
│  • Available: 350GB               │
└───────────────────────────────────┘
```

**Màu:** #FFCCBC (Orange Light)

---

## 🔗 COMMUNICATION PATHS (Đường truyền)

### **Path 1: Client ⟷ Web Server**
```
[Client Devices] ═══════════════════════> [Web Server]
                 HTTPS (Port 443)
                 HTTP (Port 80)
                 Protocol: TLS 1.3
```

**Mô tả:**
- Clients gửi HTTPS requests
- Web Server trả về HTML, CSS, JS, Images

---

### **Path 2: Web Server ⟷ PHP Runtime**
```
[Web Server] ═════════════════> [PHP Runtime]
             mod_php
             CGI/FastCGI
```

**Mô tả:**
- Apache forwards PHP requests to PHP-FPM
- PHP executes WordPress code

---

### **Path 3: PHP Runtime ⟷ Application Server**
```
[PHP Runtime] ═════════════════> [Application Server]
              Include/Require
              Function Calls
```

**Mô tả:**
- PHP loads WordPress files
- Executes plugin code

---

### **Path 4: Application Server ⟷ Database Server**
```
[Application Server] ═════════════════> [Database Server]
                     MySQL Protocol (Port 3306)
                     TCP/IP
```

**Mô tả:**
- WordPress/WooCommerce queries database
- SQL statements: SELECT, INSERT, UPDATE, DELETE

---

### **Path 5: Application Server ⟷ Email Server**
```
[Application Server] ═════════════════> [Email Server]
                     SMTP (Port 587)
                     TLS Encryption
```

**Mô tả:**
- Send transactional emails
- Attach PDF invoices

---

### **Path 6: Database Server ⟷ Backup Storage**
```
[Database Server] ═════════════════> [Backup Storage]
                  SCP / rsync / AWS CLI
                  Daily at 2:00 AM
```

**Mô tả:**
- Automated daily backups
- Transfer via secure connection

---

## 📐 LAYOUT DEPLOYMENT DIAGRAM

```
┌─────────────────────────────────────────────────────────────┐
│                    DEPLOYMENT DIAGRAM                        │
│                   (Physical Architecture)                    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────┐       HTTPS        ┌───────────┐            │
│  │ Client   │═══════443══════════>│Web Server │            │
│  │ Devices  │                     │ (Apache)  │            │
│  └──────────┘                     └─────┬─────┘            │
│   💻📱💼                                 │                  │
│                                         │ mod_php           │
│                                         ↓                    │
│                                  ┌───────────┐              │
│                                  │    PHP    │              │
│                                  │  Runtime  │              │
│                                  └─────┬─────┘              │
│                                        │                     │
│                                        ↓                     │
│                            ┌─────────────────────┐          │
│                            │  Application Server │          │
│                            │    (WordPress)      │          │
│                            └──────┬──────┬───────┘          │
│                                   │      │                  │
│                     MySQL (3306)  │      │  SMTP (587)      │
│                                   ↓      ↓                  │
│                          ┌─────────┐  ┌─────────┐          │
│                          │Database │  │  Email  │          │
│                          │ Server  │  │ Server  │          │
│                          └────┬────┘  └─────────┘          │
│                               │                             │
│                               │ Backup (daily)              │
│                               ↓                             │
│                          ┌─────────┐                       │
│                          │ Backup  │                       │
│                          │ Storage │                       │
│                          └─────────┘                       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎨 MÀU SẮC DEPLOYMENT DIAGRAM

```css
/* Nodes by Type */
Client Devices: #F5F5F5 (Light Gray)
Web Server: #E3F2FD (Light Blue)
PHP Runtime: #BBDEFB (Blue)
Application Server: #FFF59D (Yellow - HIGHLIGHT)
Database Server: #C8E6C9 (Green Light)
Email Server: #E1BEE7 (Purple Light)
Backup Storage: #FFCCBC (Orange Light)

/* Communication Paths */
HTTPS/HTTP: #1976D2 (Blue), 3pt solid
Database connection: #388E3C (Green), 2pt solid
Email (SMTP): #7E57C2 (Purple), 2pt solid
Backup: #FF6F00 (Orange), 2pt dashed

/* Protocol Labels */
Font: 9pt, Bold
Color: #424242 (Dark Gray)
Background: White with padding
```

---

## 📋 DEPLOYMENT SPECIFICATIONS TABLE

**Bảng chi tiết cấu hình triển khai:**

```
┌────────────────┬──────────────┬─────────┬─────────┬────────────┐
│ Node           │ OS           │ CPU     │ RAM     │ Storage    │
├────────────────┼──────────────┼─────────┼─────────┼────────────┤
│ Web Server     │ Ubuntu 24.04 │ 4 vCPU  │ 8GB     │ 100GB SSD  │
│ App Server     │ Same as Web  │ Same    │ Same    │ Same       │
│ DB Server      │ Ubuntu 24.04 │ 4 vCPU  │ 8GB     │ 200GB RAID │
│ Backup Storage │ AWS S3       │ N/A     │ N/A     │ 500GB      │
└────────────────┴──────────────┴─────────┴─────────┴────────────┘

┌────────────────┬───────────┬────────────────────────────────┐
│ Service        │ Port      │ Protocol                       │
├────────────────┼───────────┼────────────────────────────────┤
│ HTTP           │ 80        │ HTTP/1.1                       │
│ HTTPS          │ 443       │ HTTPS (TLS 1.3)                │
│ MySQL          │ 3306      │ MySQL Protocol over TCP        │
│ SMTP           │ 587       │ SMTP with STARTTLS             │
│ SSH            │ 22        │ SSH (for admin access)         │
└────────────────┴───────────┴────────────────────────────────┘
```

---

## ✅ CHECKLIST VẼ COMPONENT & DEPLOYMENT DIAGRAMS

### **Component Diagram:**
- [ ] 9-12 components được vẽ với component icon
- [ ] Mỗi component có stereotype («plugin», «service», etc.)
- [ ] Provided interfaces (⊕) được ghi rõ
- [ ] Required interfaces (⊖) được ghi rõ
- [ ] Dependencies (→) được vẽ đầy đủ
- [ ] WP Hotel Booking được highlight (màu vàng, viền bold)
- [ ] Màu sắc consistent theo loại component
- [ ] Layout 3 layers rõ ràng
- [ ] Legend giải thích ký hiệu

### **Deployment Diagram:**
- [ ] 6-7 nodes được vẽ với 3D box notation
- [ ] Mỗi node có stereotype («device», «execution environment», etc.)
- [ ] Artifacts (📦🗄️💾) được liệt kê
- [ ] Hardware specs được ghi (CPU, RAM, Storage)
- [ ] Communication paths (⟷) được vẽ
- [ ] Protocols và ports được label
- [ ] Application Server được highlight
- [ ] Topology rõ ràng (client → server → database)
- [ ] Backup path được thể hiện

---

## 📝 MẪU TEXT MÔ TẢ (Cho báo cáo)

### **Component Diagram:**

> **Hình X.X: Component Diagram - Kiến trúc Component**
>
> Component Diagram mô tả cấu trúc logic của hệ thống Hotel Booking, bao gồm 12 components chính được tổ chức thành 3 layers:
>
> **Layer 1 - Presentation:** Guest UI (frontend công khai), Admin UI (dashboard quản trị), và Email Templates (mẫu email).
>
> **Layer 2 - Application Logic:** WordPress Core cung cấp nền tảng CMS. WP Hotel Booking Plugin là core engine xử lý tất cả booking logic. WooCommerce xử lý cart, checkout và orders.
>
> **Layer 3 - Data & Utilities:** Database Access Layer (wpdb), Email Service (SMTP), và PDF Generator (invoice generation).
>
> **Key Dependencies:** Guest UI và Admin UI đều phụ thuộc vào WP Hotel Booking Plugin. Plugin này lại phụ thuộc vào WordPress Core (IPostService, IUserService) và WooCommerce (IOrderService). Tất cả components đều giao tiếp với Database thông qua Database Access Layer.

---

### **Deployment Diagram:**

> **Hình X.X: Deployment Diagram - Kiến trúc Triển khai Vật lý**
>
> Deployment Diagram mô tả cấu trúc vật lý triển khai hệ thống trên LAMP stack (Linux-Apache-MySQL-PHP):
>
> **Physical Nodes:**
> - **Client Devices:** Desktop, mobile, tablet browsers kết nối qua HTTPS (port 443)
> - **Web Server:** Apache 2.4 trên Ubuntu 24.04, 4 vCPU, 8GB RAM, xử lý HTTP requests
> - **PHP Runtime:** PHP 8.0 với các extensions (mysqli, gd, curl)
> - **Application Server:** WordPress 6.9 + WP Hotel Booking v2.3.0 + WooCommerce v10.7.0
> - **Database Server:** MySQL 8.0, 4 vCPU, 8GB RAM, 200GB RAID storage
> - **Email Server:** Gmail SMTP (port 587 với TLS)
> - **Backup Storage:** AWS S3 với daily automated backups
>
> **Communication:** Client gửi HTTPS requests (port 443) → Apache Web Server → PHP Runtime → WordPress Application → MySQL Database (port 3306). Email notifications gửi qua SMTP (port 587). Database backup hàng ngày vào lúc 2:00 AM.

---

## 💡 BEST PRACTICES

### **Component Diagram:**
1. **Component icon:** Luôn vẽ 2 tabs nhỏ ở góc trên trái
2. **Interfaces:** Rõ ràng provided (⊕) vs required (⊖)
3. **Dependencies:** Arrow từ client → server (uses direction)
4. **Layering:** Presentation → Logic → Data (top to bottom)
5. **Highlight:** Core components (WP Hotel Booking) màu nổi bật

### **Deployment Diagram:**
1. **3D notation:** Nodes phải có hình 3D (cube)
2. **Artifacts:** List files deployed trên mỗi node
3. **Specs:** Ghi rõ CPU, RAM, Storage
4. **Protocols:** Label tất cả communication paths với port
5. **Network topology:** Rõ ràng client → server → database

---

## ⏱️ THỜI GIAN ƯỚC TÍNH

| Diagram | Components/Nodes | Relationships | Thời gian |
|---------|------------------|---------------|-----------|
| Component Diagram | 12 components | 8 dependencies | 1.5-2 giờ |
| Deployment Diagram | 7 nodes | 6 comm paths | 1-1.5 giờ |

**TỔNG:** 2.5-3.5 giờ cho cả 2 diagrams

---

## 🚀 XUẤT FILE

**Formats đề xuất:**
- **PNG:** 300 DPI cho báo cáo in
- **PDF:** Vector format (không bị vỡ khi zoom)
- **SVG:** Nếu cần edit sau

**Settings:**
- Background: White
- Margins: 1cm
- Font: Arial/Calibri 10-12pt

---

**HOÀN THÀNH! 🎉**

**File này được tạo bởi Claude AI - Ngày: 26/05/2026**
