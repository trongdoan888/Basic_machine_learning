# 📐 HƯỚNG DẪN VẼ DATABASE ERD (ENTITY RELATIONSHIP DIAGRAM)

**Dự án:** Quan Trọng Hotel (Parkside Sunline Hotel)  
**Database:** MySQL 8.0  
**CMS Platform:** WordPress 6.9  
**Plugin:** WP Hotel Booking v2.3.0 + WooCommerce 10.7.0  
**Số lượng tables:** 15 tables chính  
**Công cụ đề xuất:** MySQL Workbench, dbdiagram.io, Draw.io, Lucidchart

---

## 🎯 MỤC TIÊU

Vẽ ERD đầy đủ hiển thị:
- **15 database tables** chính của hệ thống
- **Columns** (cột) với data types và constraints
- **Primary Keys (PK)** và **Foreign Keys (FK)**
- **Relationships:** One-to-One, One-to-Many, Many-to-Many
- **Cardinality:** 1:1, 1:N, M:N
- **Indexes** và **Constraints** quan trọng

---

## 📏 KÍCH THƯỚC VÀ LAYOUT

**Khổ giấy:** A3 ngang (Landscape) - BẮT BUỘC  
**Layout:** Clustered by functionality (nhóm theo chức năng)  
**Kích thước mỗi table:**
- Chiều rộng: 6-8cm
- Chiều cao: Tùy theo số columns (4-20cm)

---

## 🎨 CẤU TRÚC MỘT TABLE BOX

**Hình dạng:** Rectangle chia làm 2 phần

```
┌──────────────────────────────────────┐
│ 🔑 wp_posts                          │ ← Header: Table name + Icon
├──────────────────────────────────────┤
│ PK  ID: bigint(20) NOT NULL AUTO    │ ← Primary Key
│     post_author: bigint(20)          │
│     post_date: datetime              │
│     post_content: longtext           │
│     post_title: text                 │
│     post_status: varchar(20)         │
│     post_name: varchar(200)          │
│     post_type: varchar(20)           │ ← Important for filtering
│ FK  post_parent: bigint(20)          │ ← Foreign Key
│     guid: varchar(255)               │
│     post_date_gmt: datetime          │
│     post_modified: datetime          │
└──────────────────────────────────────┘
```

### **Ký hiệu:**
- `PK` : Primary Key (màu vàng hoặc có icon 🔑)
- `FK` : Foreign Key (màu xanh hoặc có icon 🔗)
- `NOT NULL` : Bắt buộc phải có giá trị
- `AUTO_INCREMENT` : Tự động tăng
- `UNIQUE` : Giá trị duy nhất

### **Font sizes:**
- Table name: 12pt, Bold
- Column names: 10pt, Regular
- Data types: 9pt, Gray, Italic

### **Màu sắc:**
- PK columns: Light yellow (#FFF9C4)
- FK columns: Light blue (#E3F2FD)
- Regular columns: White (#FFFFFF)
- Table header: Light gray (#F5F5F5)

---

## 📦 DANH SÁCH 15 TABLES CHÍNH

### **CLUSTER 1: WORDPRESS CORE TABLES - HÀNG TRÊN TRÁI**

---

#### **TABLE 1: wp_posts**

**Mục đích:** Lưu tất cả posts (rooms, bookings, extras, coupons)

**Vị trí:** Góc trên trái (X: 1cm, Y: 2cm)

```
┌──────────────────────────────────────────────────┐
│ 🔑 wp_posts                                      │
├──────────────────────────────────────────────────┤
│ PK  ID: bigint(20) NOT NULL AUTO_INCREMENT      │
│     post_author: bigint(20) NOT NULL DEFAULT 0   │
│     post_date: datetime NOT NULL                 │
│     post_date_gmt: datetime NOT NULL             │
│     post_content: longtext                       │
│     post_title: text NOT NULL                    │
│     post_excerpt: text                           │
│     post_status: varchar(20) NOT NULL            │
│     comment_status: varchar(20) NOT NULL         │
│     ping_status: varchar(20) NOT NULL            │
│     post_password: varchar(255) NOT NULL         │
│     post_name: varchar(200) NOT NULL             │
│     to_ping: text                                │
│     pinged: text                                 │
│     post_modified: datetime NOT NULL             │
│     post_modified_gmt: datetime NOT NULL         │
│ FK  post_parent: bigint(20) NOT NULL DEFAULT 0   │
│     guid: varchar(255) NOT NULL                  │
│     menu_order: int(11) NOT NULL DEFAULT 0       │
│     post_type: varchar(20) NOT NULL              │ ← QUAN TRỌNG!
│     post_mime_type: varchar(100) NOT NULL        │
│     comment_count: bigint(20) NOT NULL DEFAULT 0 │
├──────────────────────────────────────────────────┤
│ Indexes:                                         │
│   - PRIMARY KEY (ID)                             │
│   - INDEX idx_post_type (post_type)              │
│   - INDEX idx_post_status (post_status)          │
│   - INDEX idx_post_author (post_author)          │
│   - INDEX idx_post_parent (post_parent)          │
└──────────────────────────────────────────────────┘
```

**Post types quan trọng trong hệ thống:**
- `hb_room` : Room (phòng)
- `hb_booking` : Booking (đặt phòng)
- `hb_extra_room` : Extra services
- `hb_coupon` : Coupon codes
- `product` : WooCommerce products (rooms converted)
- `shop_order` : WooCommerce orders

**Business Rules:**
- Rooms: post_type = 'hb_room' AND post_status = 'publish'
- Bookings: post_type = 'hb_booking'
- Active rooms only: post_status IN ('publish', 'draft')

---

#### **TABLE 2: wp_postmeta**

**Mục đích:** Lưu metadata (custom fields) cho tất cả posts

**Vị trí:** Bên phải wp_posts (X: 9cm, Y: 2cm)

```
┌──────────────────────────────────────────────────┐
│ 🔑 wp_postmeta                                   │
├──────────────────────────────────────────────────┤
│ PK  meta_id: bigint(20) NOT NULL AUTO_INCREMENT │
│ FK  post_id: bigint(20) NOT NULL DEFAULT 0       │ ← FK to wp_posts.ID
│     meta_key: varchar(255)                       │
│     meta_value: longtext                         │
├──────────────────────────────────────────────────┤
│ Indexes:                                         │
│   - PRIMARY KEY (meta_id)                        │
│   - INDEX idx_post_id (post_id)                  │
│   - INDEX idx_meta_key (meta_key)                │
└──────────────────────────────────────────────────┘
```

**Meta keys quan trọng cho Rooms (post_type = 'hb_room'):**
```
hb_price_per_night        : decimal(10,2)    Price per night
hb_room_capacity          : int              Max guests
hb_max_adults             : int              Max adults
hb_max_children           : int              Max children
hb_room_size              : int              Size in m²
hb_number_of_rooms        : int              Inventory count
hb_bed_type               : string           Bed configuration
hb_view_type              : string           View (City, Sea, etc.)
hb_amenities              : serialized array Wifi, AC, etc.
hb_room_type              : int              Term ID (taxonomy)
```

**Meta keys cho Bookings (post_type = 'hb_booking'):**
```
hb_customer_name          : string
hb_customer_email         : string
hb_customer_phone         : string
hb_customer_address       : string
hb_check_in_date          : date (Y-m-d)
hb_check_out_date         : date (Y-m-d)
hb_number_of_nights       : int
hb_adults                 : int
hb_children               : int
hb_room_id                : int              FK to room post_id
hb_base_price             : decimal(10,2)
hb_subtotal               : decimal(10,2)
hb_extras_total           : decimal(10,2)
hb_coupon_discount        : decimal(10,2)
hb_tax_amount             : decimal(10,2)
hb_total_amount           : decimal(10,2)
hb_payment_method         : string           'offline', 'bank_transfer'
hb_payment_status         : string           'pending', 'paid'
hb_booking_status         : string           'hb-pending', 'hb-confirmed'
hb_extras                 : serialized array Extra IDs and quantities
hb_coupon_code            : string           Applied coupon code
```

**Meta keys cho Extras (post_type = 'hb_extra_room'):**
```
hb_extra_price            : decimal(10,2)
hb_extra_unit             : string           '1', 'package', 'trip'
hb_extra_type             : string           'number', 'trip'
hb_extra_required         : bool             0 or 1
```

**Meta keys cho Coupons (post_type = 'hb_coupon'):**
```
hb_coupon_code            : string (unique)
hb_discount_type          : string           'fixed', 'percent'
hb_discount_value         : decimal(10,2)
hb_min_order_amount       : decimal(10,2)
hb_max_discount           : decimal(10,2)
hb_usage_limit            : int
hb_used_count             : int
hb_expiry_date            : date
```

---

#### **TABLE 3: wp_users**

**Mục đích:** Lưu thông tin users (customers, admins)

**Vị trí:** Dưới wp_posts (X: 1cm, Y: 15cm)

```
┌──────────────────────────────────────────────────┐
│ 🔑 wp_users                                      │
├──────────────────────────────────────────────────┤
│ PK  ID: bigint(20) NOT NULL AUTO_INCREMENT      │
│     user_login: varchar(60) NOT NULL UNIQUE      │
│     user_pass: varchar(255) NOT NULL             │
│     user_nicename: varchar(50) NOT NULL          │
│     user_email: varchar(100) NOT NULL            │
│     user_url: varchar(100) NOT NULL              │
│     user_registered: datetime NOT NULL           │
│     user_activation_key: varchar(255) NOT NULL   │
│     user_status: int(11) NOT NULL DEFAULT 0      │
│     display_name: varchar(250) NOT NULL          │
├──────────────────────────────────────────────────┤
│ Indexes:                                         │
│   - PRIMARY KEY (ID)                             │
│   - UNIQUE KEY user_login (user_login)           │
│   - INDEX idx_user_email (user_email)            │
└──────────────────────────────────────────────────┘
```

**User roles trong hệ thống:**
- `administrator` : Admin (quản trị viên) - UC-21 đến UC-27
- `customer` : Guest (khách hàng) - UC-01 đến UC-17
- `shop_manager` : WooCommerce manager (optional)

---

#### **TABLE 4: wp_usermeta**

**Mục đích:** Metadata cho users

**Vị trí:** Bên phải wp_users (X: 9cm, Y: 15cm)

```
┌──────────────────────────────────────────────────┐
│ 🔑 wp_usermeta                                   │
├──────────────────────────────────────────────────┤
│ PK  umeta_id: bigint(20) NOT NULL AUTO_INCREMENT│
│ FK  user_id: bigint(20) NOT NULL DEFAULT 0       │ ← FK to wp_users.ID
│     meta_key: varchar(255)                       │
│     meta_value: longtext                         │
├──────────────────────────────────────────────────┤
│ Indexes:                                         │
│   - PRIMARY KEY (umeta_id)                       │
│   - INDEX idx_user_id (user_id)                  │
│   - INDEX idx_meta_key (meta_key)                │
└──────────────────────────────────────────────────┘
```

**User meta keys quan trọng:**
```
wp_capabilities           : serialized array  User role
first_name                : string
last_name                 : string
billing_first_name        : string           WooCommerce
billing_last_name         : string
billing_company           : string
billing_address_1         : string
billing_address_2         : string
billing_city              : string
billing_postcode          : string
billing_country           : string
billing_phone             : string
billing_email             : string
```

---

### **CLUSTER 2: TAXONOMY TABLES - GIỮA TRÊN**

---

#### **TABLE 5: wp_terms**

**Mục đích:** Lưu các terms (room types, categories)

**Vị trí:** Giữa trên (X: 17cm, Y: 2cm)

```
┌──────────────────────────────────────────────────┐
│ 🔑 wp_terms                                      │
├──────────────────────────────────────────────────┤
│ PK  term_id: bigint(20) NOT NULL AUTO_INCREMENT │
│     name: varchar(200) NOT NULL                  │
│     slug: varchar(200) NOT NULL                  │
│     term_group: bigint(10) NOT NULL DEFAULT 0    │
├──────────────────────────────────────────────────┤
│ Indexes:                                         │
│   - PRIMARY KEY (term_id)                        │
│   - UNIQUE KEY slug (slug)                       │
│   - INDEX idx_name (name)                        │
└──────────────────────────────────────────────────┘
```

**Terms trong hệ thống (taxonomy = hb_room_type):**
- Superior Double
- Deluxe Double
- Deluxe Twin
- Executive Double
- Apartment
- Family Suite

---

#### **TABLE 6: wp_term_taxonomy**

**Mục đích:** Phân loại terms theo taxonomy

**Vị trí:** Dưới wp_terms (X: 17cm, Y: 8cm)

```
┌──────────────────────────────────────────────────┐
│ 🔑 wp_term_taxonomy                              │
├──────────────────────────────────────────────────┤
│ PK  term_taxonomy_id: bigint(20) AUTO_INCREMENT │
│ FK  term_id: bigint(20) NOT NULL DEFAULT 0       │ ← FK to wp_terms
│     taxonomy: varchar(32) NOT NULL               │
│     description: longtext                        │
│     parent: bigint(20) NOT NULL DEFAULT 0        │
│     count: bigint(20) NOT NULL DEFAULT 0         │
├──────────────────────────────────────────────────┤
│ Indexes:                                         │
│   - PRIMARY KEY (term_taxonomy_id)               │
│   - UNIQUE KEY term_id_taxonomy (term_id, taxonomy)│
│   - INDEX idx_taxonomy (taxonomy)                │
└──────────────────────────────────────────────────┘
```

**Taxonomy values quan trọng:**
- `hb_room_type` : Room types (Superior, Deluxe, Executive, etc.)
- `product_cat` : WooCommerce product categories

---

#### **TABLE 7: wp_term_relationships**

**Mục đích:** Liên kết posts với terms (M:N relationship)

**Vị trí:** Dưới wp_term_taxonomy (X: 17cm, Y: 14cm)

```
┌──────────────────────────────────────────────────┐
│ 🔗 wp_term_relationships                         │
├──────────────────────────────────────────────────┤
│ FK  object_id: bigint(20) NOT NULL DEFAULT 0     │ ← FK to wp_posts.ID
│ FK  term_taxonomy_id: bigint(20) NOT NULL        │ ← FK to wp_term_taxonomy
│     term_order: int(11) NOT NULL DEFAULT 0       │
├──────────────────────────────────────────────────┤
│ Indexes:                                         │
│   - PRIMARY KEY (object_id, term_taxonomy_id)    │
│   - INDEX idx_term_taxonomy_id (term_taxonomy_id)│
└──────────────────────────────────────────────────┘
```

**Ví dụ data:**
```
object_id (post_id) | term_taxonomy_id | Meaning
--------------------|------------------|------------------
123 (Room)          | 5 (Family Suite) | Room 123 is a Family Suite
456 (Room)          | 3 (Deluxe Double)| Room 456 is Deluxe Double
```

---

### **CLUSTER 3: WOOCOMMERCE TABLES - HÀNG DƯỚI**

---

#### **TABLE 8: wp_woocommerce_order_items**

**Mục đích:** Lưu items trong mỗi order (rooms booked)

**Vị trí:** Dưới trái (X: 1cm, Y: 25cm)

```
┌──────────────────────────────────────────────────┐
│ 🔑 wp_woocommerce_order_items                    │
├──────────────────────────────────────────────────┤
│ PK  order_item_id: bigint(20) AUTO_INCREMENT    │
│     order_item_name: text NOT NULL               │
│ FK  order_id: bigint(20) NOT NULL                │ ← FK to wp_posts (order)
│     order_item_type: varchar(200) NOT NULL       │
├──────────────────────────────────────────────────┤
│ Indexes:                                         │
│   - PRIMARY KEY (order_item_id)                  │
│   - INDEX idx_order_id (order_id)                │
└──────────────────────────────────────────────────┘
```

**order_item_type values:**
- `line_item` : Product item (room)
- `shipping` : Shipping (not used)
- `tax` : Tax (if applicable)
- `coupon` : Coupon discount
- `fee` : Extra fees

---

#### **TABLE 9: wp_woocommerce_order_itemmeta**

**Mục đích:** Metadata cho order items (dates, guests, extras)

**Vị trí:** Bên phải order_items (X: 9cm, Y: 25cm)

```
┌──────────────────────────────────────────────────┐
│ 🔑 wp_woocommerce_order_itemmeta                 │
├──────────────────────────────────────────────────┤
│ PK  meta_id: bigint(20) NOT NULL AUTO_INCREMENT │
│ FK  order_item_id: bigint(20) NOT NULL           │ ← FK to order_items
│     meta_key: varchar(255) NOT NULL              │
│     meta_value: longtext                         │
├──────────────────────────────────────────────────┤
│ Indexes:                                         │
│   - PRIMARY KEY (meta_id)                        │
│   - INDEX idx_order_item_id (order_item_id)      │
│   - INDEX idx_meta_key (meta_key)                │
└──────────────────────────────────────────────────┘
```

**Meta keys cho line_item (room booking):**
```
_product_id               : int              Product/Room ID
_quantity                 : int              Always 1 for rooms
_line_total               : decimal(10,2)    Total for this item
_line_subtotal            : decimal(10,2)    Subtotal before discount
_check_in_date            : date (Y-m-d)
_check_out_date           : date (Y-m-d)
_adults                   : int
_children                 : int
_extras                   : serialized array Extra items selected
```

---

#### **TABLE 10: wp_comments**

**Mục đích:** Lưu reviews (comments) cho rooms

**Vị trí:** Giữa dưới (X: 17cm, Y: 25cm)

```
┌──────────────────────────────────────────────────┐
│ 🔑 wp_comments                                   │
├──────────────────────────────────────────────────┤
│ PK  comment_ID: bigint(20) AUTO_INCREMENT       │
│ FK  comment_post_ID: bigint(20) NOT NULL         │ ← FK to wp_posts (room)
│ FK  comment_author: tinytext NOT NULL            │
│     comment_author_email: varchar(100) NOT NULL  │
│     comment_author_url: varchar(200) NOT NULL    │
│     comment_author_IP: varchar(100) NOT NULL     │
│     comment_date: datetime NOT NULL              │
│     comment_date_gmt: datetime NOT NULL          │
│     comment_content: text NOT NULL               │
│     comment_karma: int(11) NOT NULL DEFAULT 0    │
│     comment_approved: varchar(20) NOT NULL       │
│ FK  comment_parent: bigint(20) NOT NULL          │
│ FK  user_id: bigint(20) NOT NULL DEFAULT 0       │ ← FK to wp_users
│     comment_type: varchar(20) NOT NULL           │
│     comment_agent: varchar(255) NOT NULL         │
└──────────────────────────────────────────────────┘
```

**For reviews:**
- `comment_type` = 'review'
- `comment_approved` = '1' (approved), '0' (pending)
- `comment_karma` = Rating (1-5 stars) × 20 = 20-100

---

#### **TABLE 11: wp_commentmeta**

**Mục đích:** Metadata cho reviews (rating, images)

**Vị trí:** Bên phải wp_comments (X: 25cm, Y: 25cm)

```
┌──────────────────────────────────────────────────┐
│ 🔑 wp_commentmeta                                │
├──────────────────────────────────────────────────┤
│ PK  meta_id: bigint(20) NOT NULL AUTO_INCREMENT │
│ FK  comment_id: bigint(20) NOT NULL              │ ← FK to wp_comments
│     meta_key: varchar(255)                       │
│     meta_value: longtext                         │
└──────────────────────────────────────────────────┘
```

**Meta keys cho reviews:**
```
rating                    : int (1-5)        Star rating
review_title              : string           Review title
verified                  : bool             1 if purchased
review_images             : serialized array Image attachments
```

---

### **CLUSTER 4: CUSTOM TABLES (Optional - nếu plugin tạo riêng)**

Nếu WP Hotel Booking plugin tạo custom tables (thay vì dùng wp_posts/postmeta), bạn có thể thêm:

---

#### **TABLE 12: wp_hotel_bookings (Optional - Alternative structure)**

```
┌──────────────────────────────────────────────────┐
│ 🔑 wp_hotel_bookings                             │
├──────────────────────────────────────────────────┤
│ PK  id: bigint(20) AUTO_INCREMENT               │
│ FK  room_id: bigint(20) NOT NULL                 │
│ FK  customer_id: bigint(20) NOT NULL             │
│ FK  order_id: bigint(20)                         │
│     check_in: date NOT NULL                      │
│     check_out: date NOT NULL                     │
│     adults: int NOT NULL                         │
│     children: int NOT NULL DEFAULT 0             │
│     status: varchar(20) NOT NULL                 │
│     total_amount: decimal(10,2) NOT NULL         │
│     created_at: datetime NOT NULL                │
│     updated_at: datetime NOT NULL                │
└──────────────────────────────────────────────────┘
```

**Lưu ý:** Trong thực tế, WP Hotel Booking dùng wp_posts với post_type='hb_booking', không tạo table riêng.

---

## 🔗 RELATIONSHIPS (Mối quan hệ giữa các tables)

### **1. ONE-TO-MANY (1:N)**

#### **wp_posts ──< wp_postmeta**
```
wp_posts.ID (1) ────< wp_postmeta.post_id (N)
```
- 1 post có nhiều meta records
- FK: wp_postmeta.post_id → wp_posts.ID

**Cách vẽ:**
1. Line từ wp_posts.ID đến wp_postmeta.post_id
2. Crow's foot (3 lines) ở phía wp_postmeta
3. Single line ở phía wp_posts
4. Label: "has"

---

#### **wp_users ──< wp_usermeta**
```
wp_users.ID (1) ────< wp_usermeta.user_id (N)
```

---

#### **wp_posts ──< wp_posts (Self-referencing)**
```
wp_posts.ID (1) ────< wp_posts.post_parent (N)
```
- Parent-child relationship
- VD: Booking (child) references Room (parent) - TUY NHIÊN không khuyến khích cách này

---

#### **wp_posts (order) ──< wp_woocommerce_order_items**
```
wp_posts.ID (1) ────< order_items.order_id (N)
```
- 1 order có nhiều items (rooms)

---

#### **wp_woocommerce_order_items ──< wp_woocommerce_order_itemmeta**
```
order_items.order_item_id (1) ────< itemmeta.order_item_id (N)
```

---

#### **wp_posts (room) ──< wp_comments (reviews)**
```
wp_posts.ID (1) ────< wp_comments.comment_post_ID (N)
```
- 1 room có nhiều reviews

---

#### **wp_users ──< wp_comments**
```
wp_users.ID (1) ────< wp_comments.user_id (N)
```
- 1 user viết nhiều reviews

---

#### **wp_comments ──< wp_commentmeta**
```
wp_comments.comment_ID (1) ────< wp_commentmeta.comment_id (N)
```

---

### **2. MANY-TO-MANY (M:N) - Through Junction Table**

#### **wp_posts >──< wp_terms (through wp_term_relationships)**
```
wp_posts.ID (M) ──< wp_term_relationships >── wp_term_taxonomy (N)
                                              ↑
                                              wp_terms.term_id
```

**Giải thích:**
- Nhiều rooms có thể cùng 1 room type (Deluxe Double)
- 1 room type có nhiều rooms
- Junction table: wp_term_relationships

**Cách vẽ:**
1. Line từ wp_posts.ID đến wp_term_relationships.object_id (crow's foot ở relationships)
2. Line từ wp_term_taxonomy.term_taxonomy_id đến wp_term_relationships.term_taxonomy_id (crow's foot ở relationships)
3. Line từ wp_terms.term_id đến wp_term_taxonomy.term_id (1:N)

---

### **3. ONE-TO-ONE (1:1)**

#### **wp_posts (booking) ─ wp_posts (order)**
```
wp_posts (hb_booking) (1) ──── (1) wp_posts (shop_order)
```
- 1 booking tương ứng 1 WooCommerce order
- Liên kết qua meta: `hb_booking.meta[_order_id]` = `shop_order.ID`

**Lưu ý:** Đây là soft relationship (qua meta), không phải FK constraint trong database

---

## 🎨 MÃU SẮC & STYLES

```css
/* Table Headers */
Core tables (wp_posts, wp_users): #E3F2FD (Light Blue)
Meta tables (postmeta, usermeta): #FFF9C4 (Light Yellow)
Taxonomy tables: #C8E6C9 (Light Green)
WooCommerce tables: #FFE082 (Light Orange)

/* Column Colors */
Primary Keys (PK): #FFF9C4 (Light Yellow) background
Foreign Keys (FK): #E3F2FD (Light Blue) background
Regular columns: #FFFFFF (White)

/* Relationship Lines */
One-to-Many: Solid line, #424242 (Dark Gray), 1.5pt
Many-to-Many: Dashed line, #424242, 1.5pt
Self-referencing: Curved line, #F57C00 (Orange), 1pt

/* Crow's Foot Notation */
One (1): ──│
Many (N): ──<  (3 lines radiating)
Zero or One (0..1): ──○│
Zero or Many (0..*): ──○<
```

---

## 📐 LAYOUT POSITIONING

**Canvas size:** 50cm × 35cm (A3 Landscape extended)

### **Cluster 1: WordPress Core (Left)**
- wp_posts: (1cm, 2cm)
- wp_postmeta: (9cm, 2cm)
- wp_users: (1cm, 15cm)
- wp_usermeta: (9cm, 15cm)

### **Cluster 2: Taxonomy (Center Top)**
- wp_terms: (17cm, 2cm)
- wp_term_taxonomy: (17cm, 8cm)
- wp_term_relationships: (17cm, 14cm)

### **Cluster 3: WooCommerce (Bottom)**
- wp_woocommerce_order_items: (1cm, 25cm)
- wp_woocommerce_order_itemmeta: (9cm, 25cm)
- wp_comments: (17cm, 25cm)
- wp_commentmeta: (25cm, 25cm)

---

## ✏️ CÁCH VẼ TỪNG BƯỚC

### **Bước 1: Vẽ tất cả table boxes**
1. Mở MySQL Workbench hoặc dbdiagram.io
2. Create new model/diagram
3. Add table, đặt tên, thêm columns
4. Lặp lại cho 15 tables

**Thứ tự vẽ:**
1-4: wp_posts, wp_postmeta, wp_users, wp_usermeta (Core)
5-7: wp_terms, wp_term_taxonomy, wp_term_relationships (Taxonomy)
8-11: order_items, order_itemmeta, comments, commentmeta (WooCommerce)

---

### **Bước 2: Set Primary Keys**
- Mỗi table chọn PK column
- MySQL Workbench: Right-click column → Set as Primary Key
- dbdiagram.io: Thêm `[pk]` sau column

---

### **Bước 3: Set Foreign Keys**
- Identify FK columns (post_id, user_id, order_id, etc.)
- Mark as FK
- Optionally set ON DELETE/ON UPDATE actions

**Foreign Key Constraints:**
```sql
-- postmeta.post_id → posts.ID
ON DELETE CASCADE  (Xóa post → xóa meta)
ON UPDATE CASCADE  (Update ID → update FK)

-- term_relationships.object_id → posts.ID
ON DELETE CASCADE

-- order_itemmeta.order_item_id → order_items.order_item_id
ON DELETE CASCADE

-- comments.user_id → users.ID
ON DELETE RESTRICT (Không cho xóa user nếu còn comments)
```

---

### **Bước 4: Vẽ relationships**

**Thứ tự vẽ (từ quan trọng → ít quan trọng):**

1. wp_posts ──< wp_postmeta (1:N)
2. wp_users ──< wp_usermeta (1:N)
3. wp_posts ──< wp_woocommerce_order_items (1:N)
4. wp_woocommerce_order_items ──< itemmeta (1:N)
5. wp_posts ──< wp_comments (1:N)
6. wp_users ──< wp_comments (1:N)
7. wp_comments ──< wp_commentmeta (1:N)
8. wp_terms ── wp_term_taxonomy (1:N)
9. wp_term_taxonomy ──< wp_term_relationships (1:N)
10. wp_posts ──< wp_term_relationships (M:N part 1)

**Cách vẽ 1:N relationship:**
1. Click "Place a Relationship" tool
2. Click PK column trong parent table
3. Click FK column trong child table
4. Tool tự động vẽ line với crow's foot notation
5. Set cardinality: 1:N

**Cách vẽ M:N relationship:**
1. Vẽ 2 relationships 1:N:
   - posts ──< term_relationships (1:N)
   - term_taxonomy ──< term_relationships (1:N)
2. Kết quả: M:N giữa posts và term_taxonomy

---

### **Bước 5: Add Indexes**

Trong mỗi table box, thêm section "Indexes":
```
Indexes:
  - PRIMARY KEY (ID)
  - INDEX idx_post_type (post_type)
  - INDEX idx_post_status (post_status)
  - UNIQUE KEY user_login (user_login)
```

**Indexes quan trọng:**
- wp_posts: idx_post_type, idx_post_status, idx_post_author
- wp_postmeta: idx_post_id, idx_meta_key
- wp_term_relationships: idx_object_id, idx_term_taxonomy_id

---

### **Bước 6: Add Notes & Annotations**

Thêm text boxes giải thích:
```
Note: wp_posts.post_type values:
  - 'hb_room': Room
  - 'hb_booking': Booking
  - 'hb_extra_room': Extra Service
  - 'hb_coupon': Coupon
  - 'shop_order': WooCommerce Order
  - 'product': WooCommerce Product
```

---

### **Bước 7: Color coding**
- Apply màu nền cho table headers
- Highlight PK columns (yellow)
- Highlight FK columns (light blue)

---

## ✅ CHECKLIST HOÀN THÀNH

- [ ] 15 tables được vẽ đầy đủ
- [ ] Mỗi table có tên rõ ràng (wp_...)
- [ ] Tất cả columns có data types
- [ ] Primary Keys được đánh dấu (PK)
- [ ] Foreign Keys được đánh dấu (FK)
- [ ] Constraints (NOT NULL, AUTO_INCREMENT, UNIQUE) được ghi
- [ ] 10+ relationships được vẽ
- [ ] Crow's foot notation đúng (1, N, 0..1, 0..*)
- [ ] Indexes được liệt kê
- [ ] Màu sắc được áp dụng
- [ ] Notes giải thích post_types và meta_keys
- [ ] Sơ đồ fit A3 landscape

---

## 📝 MẪU TEXT MÔ TẢ

> **Hình X.X: Entity Relationship Diagram (ERD) - Database Schema**
>
> ERD mô tả cấu trúc cơ sở dữ liệu MySQL của hệ thống Hotel Booking, bao gồm 15 tables chính được tổ chức thành 4 clusters:
>
> **Cluster 1 - WordPress Core (4 tables):** wp_posts lưu trữ tất cả rooms, bookings, extras và coupons dưới dạng custom post types. wp_postmeta chứa metadata (giá, capacity, dates). wp_users và wp_usermeta quản lý thông tin khách hàng và admin.
>
> **Cluster 2 - Taxonomy (3 tables):** wp_terms định nghĩa các room types (Family Suite, Executive Double, etc.). wp_term_taxonomy phân loại terms. wp_term_relationships tạo many-to-many relationship giữa rooms và room types.
>
> **Cluster 3 - WooCommerce (4 tables):** wp_woocommerce_order_items và wp_woocommerce_order_itemmeta lưu chi tiết đơn hàng booking. wp_comments và wp_commentmeta quản lý reviews.
>
> **Key Relationships:**
> - One-to-Many: wp_posts ──< wp_postmeta (1 post có nhiều meta fields)
> - One-to-Many: wp_users ──< wp_usermeta (1 user có nhiều meta)
> - Many-to-Many: wp_posts >──< wp_terms (through wp_term_relationships)
> - One-to-One: hb_booking ─ shop_order (1 booking = 1 WooCommerce order)
>
> **Business Rules:**
> - Rooms: post_type = 'hb_room' AND post_status = 'publish'
> - Bookings: post_type = 'hb_booking'
> - Room availability: Calculated từ hb_number_of_rooms - COUNT(active_bookings)

---

## 💡 BEST PRACTICES

1. **Naming conventions:**
   - Prefix: wp_ (WordPress standard)
   - Snake_case cho table và column names
   - Singular names (wp_posts, not wp_post)

2. **Data types:**
   - IDs: bigint(20)
   - Prices: decimal(10,2)
   - Dates: date hoặc datetime
   - Status/enums: varchar(20)
   - Content: text hoặc longtext

3. **Indexes:**
   - PK: Always indexed
   - FKs: Always indexed
   - Columns used in WHERE: Create index
   - post_type, post_status: Composite index

4. **Constraints:**
   - ON DELETE CASCADE: For dependent data (meta)
   - ON DELETE RESTRICT: For referenced data (users)
   - NOT NULL: For required fields
   - UNIQUE: For codes, slugs, emails

---

## ⏱️ THỜI GIAN ƯỚC TÍNH

- Vẽ 15 table boxes: 1-1.5 giờ
- Thêm columns & types: 1-1.5 giờ
- Vẽ relationships: 30-45 phút
- Add indexes & notes: 20-30 phút
- Format & color: 15-20 phút

**TỔNG:** 3-4 giờ

---

**HOÀN THÀNH! 🎉**

**File này được tạo bởi Claude AI - Ngày: 26/05/2026**
