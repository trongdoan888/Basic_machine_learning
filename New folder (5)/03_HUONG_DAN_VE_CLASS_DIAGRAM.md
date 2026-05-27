# 📐 HƯỚNG DẪN VẼ CLASS DIAGRAM - HỆ THỐNG HOTEL BOOKING

**Dự án:** Quan Trọng Hotel (Parkside Sunline Hotel)  
**Loại sơ đồ:** Class Diagram (UML)  
**Số lượng classes:** 12 classes chính  
**Công cụ đề xuất:** Visual Paradigm, StarUML, Draw.io, Lucidchart

---

## 🎯 MỤC TIÊU

Vẽ Class Diagram đầy đủ hiển thị:
- **12 Classes chính** của hệ thống
- **Attributes** (thuộc tính) của mỗi class
- **Methods** (phương thức) chính của mỗi class
- **Relationships:** Association, Aggregation, Composition, Inheritance, Dependency
- **Multiplicities:** 1..1, 1..*, 0..*, 0..1

---

## 📏 KÍCH THƯỚC VÀ LAYOUT

**Khổ giấy:** A3 ngang (Landscape) - BẮT BUỘC (vì nhiều classes)  
**Layout:** Layered horizontal (phân tầng ngang)  
**Kích thước mỗi class box:**
- Chiều rộng: 6-8cm
- Chiều cao: Tùy theo số attributes/methods (8-15cm)

---

## 🎨 CẤU TRÚC MỘT CLASS BOX

**Hình dạng:** Rectangle chia làm 3 phần ngang

```
┌──────────────────────────────────────┐
│          Class Name                  │ ← Compartment 1: Tên class
├──────────────────────────────────────┤
│  - attribute1: Type                  │ ← Compartment 2: Attributes
│  - attribute2: Type                  │
│  + attribute3: Type                  │
├──────────────────────────────────────┤
│  + method1(): ReturnType             │ ← Compartment 3: Methods
│  - method2(param): ReturnType        │
│  + method3(): void                   │
└──────────────────────────────────────┘
```

### **Ký hiệu visibility:**
- `+` : public
- `-` : private
- `#` : protected
- `~` : package

### **Font sizes:**
- Class name: 12pt, Bold
- Attributes: 10pt, Regular
- Methods: 10pt, Regular

### **Màu sắc:**
- Entity classes (Room, Booking, Customer): Light blue (#E3F2FD)
- Utility classes (Payment, Email): Light yellow (#FFF9C4)
- Manager classes (BookingManager): Light green (#C8E6C9)

---

## 📦 DANH SÁCH 12 CLASSES CHÍNH

### **LAYER 1: ENTITY CLASSES (Entities) - HÀNG TRÊN**

---

#### **CLASS 1: Room**

**Vị trí:** Góc trên bên trái (X: 2cm, Y: 2cm)

```
┌──────────────────────────────────────┐
│              Room                    │
├──────────────────────────────────────┤
│  - roomId: int                       │
│  - roomName: string                  │
│  - roomType: RoomType                │
│  - basePrice: decimal                │
│  - pricePerNight: decimal            │
│  - numberOfRooms: int                │
│  - maxAdults: int                    │
│  - maxChildren: int                  │
│  - roomSize: int                     │
│  - description: string               │
│  - amenities: List<string>           │
│  - gallery: List<Image>              │
│  - averageRating: float              │
│  - status: RoomStatus                │
│  - createdDate: DateTime             │
│  - modifiedDate: DateTime            │
├──────────────────────────────────────┤
│  + getRoomDetails(): Room            │
│  + checkAvailability(dates): bool    │
│  + updatePrice(price): void          │
│  + updateInventory(count): void      │
│  + addToGallery(image): void         │
│  + getAverageRating(): float         │
│  + blockDates(dates): void           │
│  + isAvailable(date): bool           │
└──────────────────────────────────────┘
```

**Giải thích attributes:**
- `roomId`: Primary key (int)
- `roomType`: Enum - RoomType (Family Suite, Apartment, Executive Double, etc.)
- `numberOfRooms`: Số lượng phòng available (inventory)
- `status`: Enum - RoomStatus (Active, Inactive, Maintenance)

---

#### **CLASS 2: Booking**

**Vị trí:** Giữa hàng trên (X: 11cm, Y: 2cm)

```
┌──────────────────────────────────────┐
│             Booking                  │
├──────────────────────────────────────┤
│  - bookingId: int                    │
│  - bookingNumber: string             │
│  - customerId: int                   │
│  - roomId: int                       │
│  - checkInDate: DateTime             │
│  - checkOutDate: DateTime            │
│  - numberOfNights: int               │
│  - adults: int                       │
│  - children: int                     │
│  - basePrice: decimal                │
│  - extrasTotal: decimal              │
│  - subtotal: decimal                 │
│  - discountAmount: decimal           │
│  - taxAmount: decimal                │
│  - totalAmount: decimal              │
│  - status: BookingStatus             │
│  - paymentMethod: string             │
│  - paymentStatus: PaymentStatus      │
│  - specialRequests: string           │
│  - bookingDate: DateTime             │
│  - lastModified: DateTime            │
├──────────────────────────────────────┤
│  + createBooking(): Booking          │
│  + calculateTotal(): decimal         │
│  + applyDiscount(coupon): void       │
│  + addExtras(extras): void           │
│  + updateStatus(status): void        │
│  + confirmBooking(): bool            │
│  + cancelBooking(): void             │
│  + sendConfirmation(): void          │
│  + generateInvoice(): Invoice        │
│  + isEditable(): bool                │
└──────────────────────────────────────┘
```

**Enums related:**
- `BookingStatus`: Pending, Processing, Confirmed, CheckedIn, CheckedOut, Completed, Cancelled, NoShow
- `PaymentStatus`: Pending, Paid, Failed, Refunded

---

#### **CLASS 3: Customer**

**Vị trí:** Góc trên bên phải (X: 20cm, Y: 2cm)

```
┌──────────────────────────────────────┐
│            Customer                  │
├──────────────────────────────────────┤
│  - customerId: int                   │
│  - userId: int                       │
│  - firstName: string                 │
│  - lastName: string                  │
│  - email: string                     │
│  - phone: string                     │
│  - address: string                   │
│  - city: string                      │
│  - country: string                   │
│  - postalCode: string                │
│  - dateOfBirth: DateTime             │
│  - registrationDate: DateTime        │
│  - totalBookings: int                │
│  - totalSpent: decimal               │
│  - loyaltyPoints: int                │
│  - preferences: string               │
├──────────────────────────────────────┤
│  + register(): bool                  │
│  + login(credentials): bool          │
│  + updateProfile(data): void         │
│  + getBookingHistory(): List         │
│  + getTotalSpent(): decimal          │
│  + addLoyaltyPoints(points): void    │
│  + canWriteReview(room): bool        │
└──────────────────────────────────────┘
```

---

### **LAYER 2: SUPPORTING ENTITIES - HÀNG GIỮA 1**

---

#### **CLASS 4: Extra**

**Vị trí:** Trái hàng giữa 1 (X: 2cm, Y: 14cm)

```
┌──────────────────────────────────────┐
│              Extra                   │
├──────────────────────────────────────┤
│  - extraId: int                      │
│  - extraName: string                 │
│  - description: string               │
│  - price: decimal                    │
│  - unit: string                      │
│  - type: ExtraType                   │
│  - isRequired: bool                  │
│  - maxQuantity: int                  │
│  - status: ExtraStatus               │
├──────────────────────────────────────┤
│  + calculatePrice(qty): decimal      │
│  + isAvailable(): bool               │
│  + updatePrice(price): void          │
└──────────────────────────────────────┘
```

**ExtraType enum:** PerNight, OneTime, PerPerson, Package

**Examples:**
- High Floor: 0đ (Trip type)
- Extra bed: 300,000đ (PerNight, number type)
- Honeymoon package: 1,500,000đ (OneTime)

---

#### **CLASS 5: Coupon**

**Vị trí:** Giữa hàng giữa 1 (X: 8cm, Y: 14cm)

```
┌──────────────────────────────────────┐
│             Coupon                   │
├──────────────────────────────────────┤
│  - couponId: int                     │
│  - couponCode: string                │
│  - description: string               │
│  - discountType: DiscountType        │
│  - discountValue: decimal            │
│  - minOrderAmount: decimal           │
│  - maxDiscountAmount: decimal        │
│  - usageLimit: int                   │
│  - usedCount: int                    │
│  - startDate: DateTime               │
│  - expiryDate: DateTime              │
│  - status: CouponStatus              │
├──────────────────────────────────────┤
│  + validate(): bool                  │
│  + isExpired(): bool                 │
│  + canBeUsed(): bool                 │
│  + calculateDiscount(total): decimal │
│  + incrementUsage(): void            │
│  + getRemainingUsage(): int          │
└──────────────────────────────────────┘
```

**DiscountType enum:** Fixed, Percentage

**Example:**
- sale50k: Fixed, 50000đ
- sale_test: Percentage, 50%

---

#### **CLASS 6: Review**

**Vị trí:** Giữa phải hàng giữa 1 (X: 14cm, Y: 14cm)

```
┌──────────────────────────────────────┐
│             Review                   │
├──────────────────────────────────────┤
│  - reviewId: int                     │
│  - roomId: int                       │
│  - customerId: int                   │
│  - bookingId: int                    │
│  - rating: int                       │
│  - title: string                     │
│  - reviewText: string                │
│  - images: List<Image>               │
│  - isVerifiedPurchase: bool          │
│  - status: ReviewStatus              │
│  - createdDate: DateTime             │
│  - approvedDate: DateTime            │
├──────────────────────────────────────┤
│  + submitReview(): bool              │
│  + approve(): void                   │
│  + reject(): void                    │
│  + addImages(images): void           │
│  + isEditable(): bool                │
└──────────────────────────────────────┘
```

**ReviewStatus enum:** Pending, Approved, Rejected

**Business rule:** Only customers who have completed a booking can review (isVerifiedPurchase = true)

---

#### **CLASS 7: Invoice**

**Vị trí:** Phải hàng giữa 1 (X: 20cm, Y: 14cm)

```
┌──────────────────────────────────────┐
│            Invoice                   │
├──────────────────────────────────────┤
│  - invoiceId: int                    │
│  - invoiceNumber: string             │
│  - bookingId: int                    │
│  - customerId: int                   │
│  - companyName: string               │
│  - companyAddress: string            │
│  - companyPhone: string              │
│  - companyEmail: string              │
│  - customerName: string              │
│  - customerAddress: string           │
│  - items: List<InvoiceItem>          │
│  - subtotal: decimal                 │
│  - discount: decimal                 │
│  - tax: decimal                      │
│  - totalAmount: decimal              │
│  - issueDate: DateTime               │
│  - dueDate: DateTime                 │
│  - paidDate: DateTime                │
│  - status: InvoiceStatus             │
├──────────────────────────────────────┤
│  + generatePDF(): byte[]             │
│  + sendEmail(email): bool            │
│  + markAsPaid(): void                │
│  + calculateTotals(): void           │
└──────────────────────────────────────┘
```

---

### **LAYER 3: UTILITY & MANAGER CLASSES - HÀNG GIỮA 2**

---

#### **CLASS 8: Payment**

**Vị trí:** Trái hàng giữa 2 (X: 2cm, Y: 24cm)

```
┌──────────────────────────────────────┐
│            Payment                   │
├──────────────────────────────────────┤
│  - paymentId: int                    │
│  - bookingId: int                    │
│  - amount: decimal                   │
│  - paymentMethod: PaymentMethod      │
│  - paymentStatus: PaymentStatus      │
│  - transactionId: string             │
│  - paidDate: DateTime                │
│  - notes: string                     │
├──────────────────────────────────────┤
│  + processPayment(): bool            │
│  + verifyPayment(): bool             │
│  + refund(amount): bool              │
│  + updateStatus(status): void        │
└──────────────────────────────────────┘
```

**PaymentMethod enum:** BankTransfer, CashOnArrival, CreditCard (future)

---

#### **CLASS 9: RoomType (Enum/Value Object)**

**Vị trí:** Giữa hàng giữa 2 (X: 8cm, Y: 24cm)

```
┌──────────────────────────────────────┐
│           RoomType                   │
│          «enumeration»               │
├──────────────────────────────────────┤
│  SUPERIOR_DOUBLE                     │
│  DELUXE_DOUBLE                       │
│  DELUXE_TWIN                         │
│  EXECUTIVE_DOUBLE                    │
│  APARTMENT                           │
│  FAMILY_SUITE                        │
├──────────────────────────────────────┤
│  + getName(): string                 │
│  + getDescription(): string          │
│  + getBasePrice(): decimal           │
└──────────────────────────────────────┘
```

---

#### **CLASS 10: Availability**

**Vị trí:** Giữa phải hàng giữa 2 (X: 14cm, Y: 24cm)

```
┌──────────────────────────────────────┐
│          Availability                │
├──────────────────────────────────────┤
│  - availabilityId: int               │
│  - roomId: int                       │
│  - date: DateTime                    │
│  - availableCount: int               │
│  - blockedCount: int                 │
│  - bookedCount: int                  │
│  - isBlocked: bool                   │
│  - blockReason: string               │
├──────────────────────────────────────┤
│  + checkAvailable(date): int         │
│  + blockDate(reason): void           │
│  + unblockDate(): void               │
│  + decrementInventory(): void        │
│  + incrementInventory(): void        │
│  + getTotalAvailable(): int          │
└──────────────────────────────────────┘
```

**Business logic:**
- `availableCount` = `numberOfRooms` - `bookedCount` - `blockedCount`

---

### **LAYER 4: MANAGER/CONTROLLER CLASSES - HÀNG DƯỚI**

---

#### **CLASS 11: BookingManager**

**Vị trí:** Trái hàng dưới (X: 2cm, Y: 32cm)

```
┌──────────────────────────────────────┐
│        BookingManager                │
│         «controller»                 │
├──────────────────────────────────────┤
│  - bookingRepository: Repository     │
│  - availabilityService: Service      │
│  - emailService: EmailService        │
├──────────────────────────────────────┤
│  + searchAvailableRooms(criteria)    │
│  + createBooking(data): Booking      │
│  + confirmBooking(id): bool          │
│  + cancelBooking(id): bool           │
│  + updateBookingStatus(id, status)   │
│  + getBookingDetails(id): Booking    │
│  + getBookingsByCustomer(id): List   │
│  + getBookingsByDateRange(dates)     │
│  + calculateBookingTotal(booking)    │
│  + applyDiscount(booking, coupon)    │
│  + sendConfirmationEmail(booking)    │
└──────────────────────────────────────┘
```

---

#### **CLASS 12: EmailService**

**Vị trí:** Giữa hàng dưới (X: 10cm, Y: 32cm)

```
┌──────────────────────────────────────┐
│         EmailService                 │
│          «service»                   │
├──────────────────────────────────────┤
│  - smtpServer: string                │
│  - smtpPort: int                     │
│  - senderEmail: string               │
│  - emailTemplate: Template           │
├──────────────────────────────────────┤
│  + sendBookingConfirmation(booking)  │
│  + sendInvoice(invoice): bool        │
│  + sendCancellation(booking): bool   │
│  + sendReminder(booking): bool       │
│  - buildEmailContent(template): str  │
│  - attachPDF(invoice): Attachment    │
└──────────────────────────────────────┘
```

---

## 🔗 RELATIONSHIPS (Mối quan hệ giữa các classes)

### **1. Association (Quan hệ thông thường)**

**Ký hiệu:** Đường thẳng liền nét, có label và multiplicity

#### **Customer ─── Booking**
```
Customer 1 ─────────── * Booking
         "makes"
```
- **Multiplicity:** 1 Customer có thể tạo nhiều Bookings (1..*)
- **Direction:** Customer → Booking
- **Label:** "makes" hoặc "creates"

**Cách vẽ:**
1. Vẽ line từ Customer class đến Booking class
2. Ghi "1" gần Customer, "*" gần Booking
3. Viết label "makes" ở giữa line (trên hoặc dưới)

---

#### **Booking ─── Room**
```
Booking * ─────────── 1 Room
         "reserves"
```
- Multiplicity: Nhiều Bookings có thể book cùng 1 Room (*..*..1)
- Label: "reserves" hoặc "books"

---

#### **Booking ─── Payment**
```
Booking 1 ─────────── 1 Payment
         "has"
```
- Multiplicity: 1 Booking có 1 Payment (1..1)
- Label: "has" hoặc "processes"

---

#### **Room ─── Review**
```
Room 1 ─────────── * Review
     "receives"
```
- Multiplicity: 1 Room có nhiều Reviews (*..*)
- Label: "receives" hoặc "has"

---

#### **Customer ─── Review**
```
Customer 1 ─────────── * Review
         "writes"
```
- Multiplicity: 1 Customer viết nhiều Reviews (1..*)
- Label: "writes" hoặc "submits"

---

### **2. Aggregation (Quan hệ tập hợp - whole/part, part có thể tồn tại độc lập)**

**Ký hiệu:** Diamond rỗng ở phía "whole"

#### **Booking ◇─── Extra**
```
Booking 1 ◇─────────── * Extra
          "includes"
```
- Booking bao gồm nhiều Extras (optional)
- Extra có thể tồn tại độc lập với Booking
- Diamond rỗng ở Booking side

**Cách vẽ:**
1. Vẽ line từ Booking đến Extra
2. Thêm diamond shape (◇) ở Booking end
3. Ghi multiplicity: "1" ở Booking, "*" ở Extra
4. Label: "includes" hoặc "contains"

---

#### **Booking ◇─── Coupon**
```
Booking * ◇─────────── 0..1 Coupon
          "uses"
```
- Booking có thể dùng 0 hoặc 1 Coupon
- Coupon tồn tại độc lập
- Diamond ở Booking side

---

### **3. Composition (Quan hệ bao gồm - part không thể tồn tại độc lập)**

**Ký hiệu:** Diamond đặc (filled) ở phía "whole"

#### **Booking ◆─── Invoice**
```
Booking 1 ◆─────────── 1 Invoice
          "generates"
```
- 1 Booking tạo 1 Invoice
- Invoice không tồn tại nếu không có Booking
- Filled diamond ở Booking side

**Cách vẽ:**
1. Vẽ line từ Booking đến Invoice
2. Thêm filled diamond (◆) ở Booking end
3. Multiplicity: "1..1"
4. Label: "generates" hoặc "produces"

---

#### **Room ◆─── Availability**
```
Room 1 ◆─────────── * Availability
     "tracks"
```
- 1 Room có nhiều Availability records (mỗi ngày 1 record)
- Availability không có ý nghĩa nếu không có Room
- Filled diamond ở Room side

---

### **4. Dependency (Phụ thuộc)**

**Ký hiệu:** Dashed arrow (mũi tên nét đứt)

#### **BookingManager ··········> Booking**
```
BookingManager ··········> Booking
               «uses»
```
- BookingManager sử dụng Booking class
- Dependency relationship

**Cách vẽ:**
1. Vẽ dashed line (- - - -) từ BookingManager đến Booking
2. Thêm arrowhead ở Booking end
3. Stereotype: «uses» hoặc «creates»

---

#### **BookingManager ··········> EmailService**
```
BookingManager ··········> EmailService
               «uses»
```

---

#### **EmailService ··········> Invoice**
```
EmailService ··········> Invoice
             «uses»
```

---

### **5. Association Class (Class kết hợp)**

Khi relationship có attributes riêng

#### **Booking ─── Extra (với quantity và price)**
```
       Booking ────────── Extra
          │                  
          │                  
     ┌────▼────┐            
     │ BookingExtra         │            
     ├──────────────────┤            
     │ - quantity: int      │            
     │ - unitPrice: decimal │            
     │ - totalPrice: decimal│            
     └──────────────────┘            
```

**Cách vẽ:**
1. Vẽ association line giữa Booking và Extra
2. Vẽ dashed line từ line này đến BookingExtra class
3. BookingExtra class chứa attributes về relationship

---

## 🎨 MÃU SẮC ĐỀ XUẤT

```css
/* Entity Classes (Domain Objects) */
Room, Booking, Customer, Review:
  Background: #E3F2FD (Light Blue)
  Border: #1976D2 (Blue), 1.5pt

/* Supporting Entities */
Extra, Coupon, Invoice, Payment:
  Background: #FFF9C4 (Light Yellow)
  Border: #F57C00 (Orange), 1.5pt

/* Utility Classes */
Availability, RoomType:
  Background: #F5F5F5 (Light Gray)
  Border: #616161 (Gray), 1.5pt

/* Manager/Controller Classes */
BookingManager, EmailService:
  Background: #C8E6C9 (Light Green)
  Border: #388E3C (Green), 1.5pt

/* Text */
All text: #000000 (Black)
Private members (-): #D32F2F (Red) - optional
Public members (+): #388E3C (Green) - optional
```

---

## 📐 LAYOUT POSITIONING (Chi tiết tọa độ)

**Canvas size:** 42cm × 35cm (A3 Landscape)

### **Layer 1: Top (Y: 2cm)**
- Room: (2cm, 2cm)
- Booking: (11cm, 2cm)
- Customer: (20cm, 2cm)

### **Layer 2: Middle 1 (Y: 14cm)**
- Extra: (2cm, 14cm)
- Coupon: (8cm, 14cm)
- Review: (14cm, 14cm)
- Invoice: (20cm, 14cm)

### **Layer 3: Middle 2 (Y: 24cm)**
- Payment: (2cm, 24cm)
- RoomType: (8cm, 24cm)
- Availability: (14cm, 24cm)

### **Layer 4: Bottom (Y: 32cm)**
- BookingManager: (2cm, 32cm)
- EmailService: (10cm, 32cm)

**Note:** Điều chỉnh Y positions nếu classes quá cao

---

## ✏️ CÁCH VẼ TỪNG BƯỚC

### **Bước 1: Vẽ tất cả class boxes (12 classes)**
1. Mở tool UML
2. Chọn "Class" từ palette
3. Vẽ 12 class boxes theo layout đã chỉ định
4. Đặt tên cho từng class
5. Set màu nền theo loại class

**Thứ tự vẽ:**
1-3: Room, Booking, Customer (Layer 1)
4-7: Extra, Coupon, Review, Invoice (Layer 2)
8-10: Payment, RoomType, Availability (Layer 3)
11-12: BookingManager, EmailService (Layer 4)

---

### **Bước 2: Thêm attributes cho mỗi class**
1. Click vào class box
2. Chọn "Add Attribute"
3. Nhập: `visibility name : type`
   - Example: `- roomId : int`
   - Example: `+ roomName : string`
4. Lặp lại cho tất cả attributes

**Tips:**
- Attributes thông thường để private (-)
- IDs (primary keys) để private
- Status, enum fields có thể public (+)

---

### **Bước 3: Thêm methods cho mỗi class**
1. Click vào class box
2. Chọn "Add Method"
3. Nhập: `visibility name(params) : returnType`
   - Example: `+ getRoomDetails() : Room`
   - Example: `- calculatePrice(nights: int) : decimal`
4. Lặp lại cho tất cả methods

**Tips:**
- Getter/setter methods: public (+)
- Business logic methods: public (+)
- Helper methods: private (-)

---

### **Bước 4: Vẽ relationships**

**Thứ tự vẽ relationships (từ quan trọng → ít quan trọng):**

1. **Customer ─ Booking** (Association 1..*)
2. **Booking ─ Room** (Association *..1)
3. **Booking ◆─ Invoice** (Composition 1..1)
4. **Booking ─ Payment** (Association 1..1)
5. **Booking ◇─ Extra** (Aggregation 1..*)
6. **Booking ◇─ Coupon** (Aggregation *..0..1)
7. **Room ─ Review** (Association 1..*)
8. **Customer ─ Review** (Association 1..*)
9. **Room ◆─ Availability** (Composition 1..*)
10. **Room ─ RoomType** (Association *..1)
11. **BookingManager ··> Booking** (Dependency)
12. **BookingManager ··> EmailService** (Dependency)
13. **EmailService ··> Invoice** (Dependency)

**Cho mỗi relationship:**
1. Chọn relationship type từ palette
2. Click class nguồn
3. Drag đến class đích
4. Set multiplicity (1, *, 0..1, etc.)
5. Add label (if needed)
6. Add role names (optional)

---

### **Bước 5: Format & Style**
1. Align all class boxes (dùng tool Align)
2. Distribute evenly (spacing đều)
3. Make sure all lines don't overlap
4. Add colors to classes
5. Check font sizes consistency
6. Add stereotypes («enumeration», «service», etc.)

---

### **Bước 6: Add Legend & Notes**

Vẽ hộp legend ở góc dưới phải:
```
┌─────────────────────────────────┐
│ Legend:                         │
│ □ Entity Class                 │
│ □ Supporting Entity            │
│ □ Utility Class                │
│ □ Manager/Controller           │
│                                 │
│ ───── Association              │
│ ◇──── Aggregation              │
│ ◆──── Composition              │
│ ·····> Dependency              │
│                                 │
│ + : public                      │
│ - : private                     │
│ # : protected                   │
└─────────────────────────────────┘
```

---

## ✅ CHECKLIST HOÀN THÀNH

- [ ] 12 classes được vẽ với đúng vị trí
- [ ] Mỗi class có 3 compartments (name, attributes, methods)
- [ ] Tất cả attributes có visibility và type
- [ ] Tất cả methods có visibility, params (if any), và return type
- [ ] Màu sắc được áp dụng theo loại class
- [ ] 13 relationships được vẽ đầy đủ
- [ ] Multiplicities được ghi rõ ràng (1, *, 0..1, etc.)
- [ ] Relationship labels có ý nghĩa (makes, has, uses, etc.)
- [ ] Không có lines chéo nhau (hoặc dùng bridge)
- [ ] Legend được thêm vào
- [ ] Font sizes consistent
- [ ] Sơ đồ fit A3 landscape và print được

---

## 📝 MẪU TEXT MÔ TẢ (Cho báo cáo)

> **Hình X.X: Class Diagram - Hệ thống Đặt phòng Khách sạn**
>
> Class Diagram mô tả cấu trúc hướng đối tượng của hệ thống Hotel Booking, bao gồm 12 classes chính được tổ chức thành 4 layers:
>
> **Layer 1 - Entity Classes:** Các đối tượng nghiệp vụ chính bao gồm Room (Phòng), Booking (Đặt phòng), và Customer (Khách hàng). Đây là các entities cốt lõi của hệ thống.
>
> **Layer 2 - Supporting Entities:** Các entities hỗ trợ như Extra (Dịch vụ bổ sung), Coupon (Mã giảm giá), Review (Đánh giá), và Invoice (Hóa đơn).
>
> **Layer 3 - Utility Classes:** Các classes tiện ích như Payment (Thanh toán), RoomType (Loại phòng), và Availability (Tình trạng phòng trống).
>
> **Layer 4 - Manager/Controller:** BookingManager và EmailService quản lý business logic và external services.
>
> **Relationships:** Sơ đồ thể hiện các mối quan hệ: Association (Customer makes Booking), Composition (Booking generates Invoice), Aggregation (Booking includes Extras), và Dependency (BookingManager uses EmailService).

---

## 💡 BEST PRACTICES

1. **Naming conventions:**
   - Class names: PascalCase (Room, BookingManager)
   - Attributes: camelCase (roomId, checkInDate)
   - Methods: camelCase (getRoomDetails, calculateTotal)

2. **Abstraction level:**
   - Chỉ hiển thị attributes/methods quan trọng
   - Bỏ qua getter/setter đơn giản nếu quá nhiều
   - Focus vào business logic methods

3. **Avoid clutter:**
   - Không vẽ tất cả possible relationships
   - Chỉ vẽ relationships chính
   - Dùng notes cho clarifications

4. **Consistency:**
   - Same font size cho cùng loại text
   - Same line thickness cho cùng loại relationship
   - Colors consistent across same types

---

## ⏱️ THỜI GIAN ƯỚC TÍNH

- Vẽ 12 class boxes: 30-45 phút
- Thêm attributes/methods: 1-1.5 giờ
- Vẽ relationships: 30-45 phút
- Format & style: 20-30 phút

**TỔNG:** 2.5-3.5 giờ

---

**HOÀN THÀNH! 🎉**

**File này được tạo bởi Claude AI - Ngày: 26/05/2026**
