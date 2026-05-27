# 📐 HƯỚNG DẪN VẼ ACTIVITY DIAGRAMS - 21 USE CASES

**Dự án:** Quan Trọng Hotel (Parkside Sunline Hotel)  
**Loại sơ đồ:** Activity Diagrams (UML)  
**Số lượng diagrams:** 21 Activity Diagrams (1 cho mỗi UC)  
**Công cụ đề xuất:** Visual Paradigm, StarUML, Draw.io, Lucidchart

---

## 🎯 MỤC TIÊU

Activity Diagram mô tả:
- **Flow of activities** (luồng hoạt động) từ đầu đến cuối
- **Decisions** (điểm quyết định) và **branches** (nhánh)
- **Parallel activities** (hoạt động song song) nếu có
- **Swim lanes** (phân làn theo actor) nếu cần

---

## 🎨 CẤU TRÚC ACTIVITY DIAGRAM

### **Các thành phần cơ bản:**

```
    ● ← Initial node (filled circle)
    ↓
┌─────────────┐
│  Activity   │ ← Activity (rounded rectangle)
└─────────────┘
    ↓
    ◇ ← Decision (diamond)
   / \
  /   \
 ↓     ↓
Yes    No
    ↓
┌─────────────┐
│  Activity   │
└─────────────┘
    ↓
    ◎ ← Final node (bull's eye)
```

### **Ký hiệu:**
- **●** : Initial node (0.5cm)
- **◎** : Final node (0.8cm)
- **Rectangle (rounded)** : Activity
- **◇ Diamond** : Decision point
- **━━━━** : Fork/Join bar (parallel)
- **→** : Control flow (arrow)

---

## 📋 TEMPLATE CHUNG CHO TẤT CẢ ACTIVITY DIAGRAMS

### **Header mỗi diagram:**
```
Activity Diagram: UC-XX - Tên Use Case
Actor: Guest / Admin
Description: Mô tả ngắn
```

### **Kích thước:**
- Activity box: 6-8cm width x 1.5-2cm height
- Decision diamond: 3cm x 3cm
- Canvas: A4 Portrait (21cm x 29.7cm)

### **Màu sắc:**
- Start activity: #C8E6C9 (Light Green)
- Normal activities: #BBDEFB (Light Blue)
- Decision activities: #FFF9C4 (Light Yellow)
- Error/Cancel activities: #FFCDD2 (Light Red)
- Success activities: #A5D6A7 (Green)

---

# 21 ACTIVITY DIAGRAMS CHI TIẾT

---

## UC-01: TÌM KIẾM PHÒNG (Search Rooms) 🔍

**Actor:** Guest  
**Entry Point:** Homepage hoặc Rooms page  
**Success:** Display available rooms

### **Activity Flow:**

```
    ●
    ↓
┌──────────────────────┐
│ Access search page   │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Enter check-in date  │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Enter check-out date │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Select # of guests   │
│ (Adults + Children)  │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Select room type     │
│ (Optional)           │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Click "Search"       │
└──────────────────────┘
    ↓
    ◇ Validate dates?
   / \
  /   \
 No    Yes
 ↓     ↓
┌──────┐ ┌─────────────────────┐
│Show  │ │Query available rooms│
│error │ └─────────────────────┘
└──────┘         ↓
         ┌─────────────────────┐
         │Apply filters        │
         │(Price, Rating, Type)│
         └─────────────────────┘
                 ↓
                 ◇ Results > 0?
                / \
               /   \
              No   Yes
              ↓     ↓
       ┌───────────┐ ┌──────────────┐
       │Show "No   │ │Display room  │
       │rooms"     │ │list with     │
       │message    │ │pagination    │
       └───────────┘ └──────────────┘
              ↓             ↓
              └──────┬──────┘
                     ↓
                     ◎
```

**Decisions:**
1. **Validate dates?** → Check-out > Check-in, Dates >= Today
2. **Results > 0?** → Query returned rooms or not

---

## UC-02: XEM CHI TIẾT PHÒNG (View Room Details) 🏨

**Actor:** Guest  
**Entry Point:** Room list page  
**Success:** Display room full information

### **Activity Flow:**

```
    ●
    ↓
┌──────────────────────┐
│ Browse room list     │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Click on room card   │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Load room details    │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Display gallery      │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Display description  │
│ • Name, Type, Price  │
│ • Capacity, Size     │
│ • Bed, View, Amenities│
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Display tabs:        │
│ • Description        │
│ • Additional Info    │
│ • Pricing Plans      │
│ • Reviews (UC-17)    │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Show booking form    │
│ (UC-04)              │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Show related rooms   │
└──────────────────────┘
    ↓
    ◇ User action?
   /│\
  / │ \
 /  │  \
View Book Browse
tabs      more
 ↓   ↓    ↓
 ◎  UC-04 UC-02
```

**Decisions:**
1. **User action?** → View tabs / Book room / Browse more rooms

---

## UC-03: THÊM PHÒNG VÀO GIỎ (Add to Cart) 🛒

**Actor:** Guest  
**Entry Point:** Single room page (after UC-02)  
**Success:** Item added to cart

### **Activity Flow:**

```
    ●
    ↓
┌──────────────────────┐
│ On room detail page  │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Enter check-in date  │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Enter check-out date │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Enter # of guests    │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ [Optional] Add extras│
│ (UC-04)              │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Click "Add to Cart"  │
└──────────────────────┘
    ↓
    ◇ Room available?
   / \
  /   \
 No    Yes
 ↓     ↓
┌──────┐ ┌─────────────────────┐
│Show  │ │Calculate total price│
│error │ └─────────────────────┘
└──────┘         ↓
         ┌─────────────────────┐
         │Add item to cart     │
         │(WooCommerce)        │
         └─────────────────────┘
                 ↓
         ┌─────────────────────┐
         │Show success message │
         │"Added to cart"      │
         └─────────────────────┘
                 ↓
                 ◇ User choice?
                /│\
               / │ \
              /  │  \
          View Continue Book
          cart shopping more
           ↓     ↓      ↓
         UC-06  UC-02  UC-02
```

**Decisions:**
1. **Room available?** → Check inventory for dates
2. **User choice?** → View cart / Continue shopping / Book more rooms

---

## UC-04: THÊM EXTRAS (Add Extra Services) ➕

**Actor:** Guest  
**Entry Point:** Room detail page booking form  
**Success:** Extras added to booking

### **Activity Flow:**

```
    ●
    ↓
┌──────────────────────┐
│ View booking form    │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Display available    │
│ extras for room:     │
│ • High Floor (0đ)    │
│ • Extra bed (300K)   │
│ • Honeymoon (1.5M)   │
└──────────────────────┘
    ↓
    ◇ User wants extras?
   / \
  /   \
 No    Yes
 ↓     ↓
Skip  ┌─────────────────────┐
      │Select extras        │
      │• Check checkboxes   │
      │• Enter quantity     │
      └─────────────────────┘
              ↓
      ┌─────────────────────┐
      │Calculate extra cost │
      └─────────────────────┘
              ↓
      ┌─────────────────────┐
      │Update total price   │
      │Base + Extras        │
      └─────────────────────┘
              ↓
      ┌─────────────────────┐
      │Display breakdown:   │
      │• Room: 3,000,000đ   │
      │• Extras: 300,000đ   │
      │• Total: 3,300,000đ  │
      └─────────────────────┘
 ↓            ↓
 └─────┬──────┘
       ↓
┌──────────────────────┐
│ Continue to UC-03    │
│ (Add to Cart)        │
└──────────────────────┘
       ↓
       ◎
```

**Decisions:**
1. **User wants extras?** → Skip or select extras

---

## UC-05: ÁP DỤNG MÃ GIẢM GIÁ (Apply Coupon) 🎟️

**Actor:** Guest  
**Entry Point:** Cart page (UC-06)  
**Success:** Discount applied

### **Activity Flow:**

```
    ●
    ↓
┌──────────────────────┐
│ On cart page         │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ View coupon input    │
│ field                │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Enter coupon code    │
│ e.g. "sale50k"       │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Click "Apply coupon" │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Validate coupon      │
└──────────────────────┘
    ↓
    ◇ Valid?
   /│\
  / │ \
Invalid Expired Valid
  ↓   ↓      ↓
┌────┐┌────┐ ┌─────────────────────┐
│Show││Show│ │Calculate discount   │
│err-││err-│ │• Fixed: -50,000đ    │
│or  ││or  │ │• Percent: -50%      │
└────┘└────┘ └─────────────────────┘
  ↓    ↓            ↓
  └────┴─────┐ ┌─────────────────────┐
             │ │Apply discount       │
             │ └─────────────────────┘
             │         ↓
             │ ┌─────────────────────┐
             │ │Update cart totals:  │
             │ │• Subtotal           │
             │ │• Discount: -50,000đ │
             │ │• New Total          │
             │ └─────────────────────┘
             │         ↓
             │ ┌─────────────────────┐
             │ │Show success message │
             │ │"Coupon applied"     │
             │ └─────────────────────┘
             ↓         ↓
             └────┬────┘
                  ↓
                  ◎
```

**Decisions:**
1. **Valid?** → Check if code exists, not expired, usage limit not reached

---

## UC-06: XEM GIỎ HÀNG (View Cart) 🛍️

**Actor:** Guest  
**Entry Point:** Cart icon in header  
**Success:** Display cart contents

### **Activity Flow:**

```
    ●
    ↓
┌──────────────────────┐
│ Click cart icon      │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Load cart page       │
└──────────────────────┘
    ↓
    ◇ Cart empty?
   / \
  /   \
 Yes   No
 ↓     ↓
┌──────┐ ┌─────────────────────┐
│Show  │ │Display cart table:  │
│"Cart │ │• Room name          │
│empty"│ │• Dates, Guests      │
│msg   │ │• Price per night    │
└──────┘ │• # Nights           │
         │• Extras             │
         │• Subtotal           │
         │• Remove button      │
         └─────────────────────┘
         ┌─────────────────────┐
         │Display coupon input │
         │(UC-05)              │
         └─────────────────────┘
         ┌─────────────────────┐
         │Display cart totals: │
         │• Subtotal           │
         │• Discount           │
         │• Total              │
         └─────────────────────┘
         ┌─────────────────────┐
         │Show action buttons: │
         │• Continue shopping  │
         │• Proceed to checkout│
         └─────────────────────┘
 ↓               ↓
 └───────┬───────┘
         ↓
         ◇ User action?
        /│\
       / │ \
    Shop Update Checkout
           ↓
         UC-07
```

**Decisions:**
1. **Cart empty?** → Show empty message or cart contents
2. **User action?** → Continue shopping / Update cart / Checkout

---

## UC-07: XÓA KHỎI GIỎ (Remove from Cart) 🗑️

**Actor:** Guest  
**Entry Point:** Cart page (UC-06)  
**Success:** Item removed

### **Activity Flow:**

```
    ●
    ↓
┌──────────────────────┐
│ On cart page         │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Click "Remove" (×)   │
│ button on item       │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Remove item from cart│
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Recalculate totals   │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Refresh cart page    │
└──────────────────────┘
    ↓
    ◇ Cart now empty?
   / \
  /   \
 Yes   No
 ↓     ↓
┌──────┐ ┌─────────────────────┐
│Show  │ │Show updated cart    │
│"Cart │ │with new totals      │
│empty"│ └─────────────────────┘
└──────┘         ↓
 ↓       ┌─────────────────────┐
 │       │Show success message │
 │       │"Item removed"       │
 │       └─────────────────────┘
 ↓               ↓
 └───────┬───────┘
         ↓
         ◎
```

**Decisions:**
1. **Cart now empty?** → Show empty message or remaining items

---

## UC-08: CHECKOUT (Proceed to Checkout) 💳

**Actor:** Guest  
**Entry Point:** Cart page  
**Success:** Navigate to checkout page

### **Activity Flow:**

```
    ●
    ↓
┌──────────────────────┐
│ On cart page         │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Review cart items    │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Click "Proceed to    │
│ checkout" button     │
└──────────────────────┘
    ↓
    ◇ User logged in?
   / \
  /   \
 No    Yes
 ↓     ↓
┌──────┐ Skip
│Prompt│
│Login/│
│Regis-│
│ter   │
└──┬───┘
   ↓
   ◇ Login/Register?
  / \
 /   \
Cancel Login
 ↓     ↓
Exit  ┌─────────────────────┐
      │Navigate to checkout │
      │page                 │
      └─────────────────────┘
              ↓
      ┌─────────────────────┐
      │Load checkout form   │
      │(UC-09)              │
      └─────────────────────┘
              ↓
              ◎
```

**Decisions:**
1. **User logged in?** → Prompt login or proceed
2. **Login/Register?** → Cancel or authenticate

---

## UC-09: NHẬP THÔNG TIN KHÁCH (Enter Customer Info) 📝

**Actor:** Guest  
**Entry Point:** Checkout page  
**Success:** Valid customer info entered

### **Activity Flow:**

```
    ●
    ↓
┌──────────────────────┐
│ On checkout page     │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Display billing form:│
│ • First name *       │
│ • Last name *        │
│ • Email *            │
│ • Phone *            │
│ • Address *          │
│ • City               │
│ • Country            │
│ • Postal code        │
│ • Special requests   │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Enter first name     │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Enter last name      │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Enter email          │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Enter phone          │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Enter address        │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Enter city, country  │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ [Optional] Special   │
│ requests             │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Review order summary:│
│ • Room details       │
│ • Dates, Guests      │
│ • Extras             │
│ • Totals             │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Continue to UC-10    │
│ (Select payment)     │
└──────────────────────┘
    ↓
    ◎
```

**No major decisions** - Linear flow with form filling

---

## UC-10: XÁC NHẬN ĐẶT PHÒNG (Confirm Booking) ✅

**Actor:** Guest  
**Entry Point:** Checkout page (after UC-09)  
**Success:** Booking confirmed, order created

### **Activity Flow:**

```
    ●
    ↓
┌──────────────────────┐
│ Customer info filled │
│ (UC-09)              │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Select payment method│
│ ⚪ Bank transfer     │
│ ⚪ Cash on arrival   │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Check T&C checkbox * │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Click "Place Order"  │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Validate all fields  │
└──────────────────────┘
    ↓
    ◇ Valid?
   / \
  /   \
 No    Yes
 ↓     ↓
┌──────┐ ┌─────────────────────┐
│Show  │ │Create WooCommerce   │
│error │ │Order                │
│msgs  │ └─────────────────────┘
└──────┘         ↓
         ┌─────────────────────┐
         │Create Booking       │
         │(hb_booking post)    │
         └─────────────────────┘
                 ↓
         ┌─────────────────────┐
         │Update room inventory│
         │(decrease available) │
         └─────────────────────┘
                 ↓
         ┌─────────────────────┐
         │Generate order number│
         │e.g. #1598           │
         └─────────────────────┘
                 ↓
         ┌─────────────────────┐
         │Set status: Pending  │
         └─────────────────────┘
                 ↓
         ┌─────────────────────┐
         │Continue to UC-11    │
         │(Complete)           │
         └─────────────────────┘
 ↓               ↓
 └───────┬───────┘
         ↓
         ◎
```

**Decisions:**
1. **Valid?** → Check required fields, T&C checked, payment method selected

---

## UC-11: HOÀN TẤT ĐẶT PHÒNG (Complete Booking) 🎉

**Actor:** Guest  
**Entry Point:** After UC-10  
**Success:** Navigate to confirmation page

### **Activity Flow:**

```
    ●
    ↓
┌──────────────────────┐
│ Booking created      │
│ (UC-10)              │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Trigger email        │
│ notification (UC-13) │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Generate invoice PDF │
│ (UC-27)              │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Clear cart           │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Redirect to Order    │
│ Received page        │
│ (UC-12)              │
└──────────────────────┘
    ↓
    ◎
```

**No decisions** - Sequential automated actions

---

## UC-12: XEM TRANG XÁC NHẬN (View Confirmation) 📄

**Actor:** Guest  
**Entry Point:** After UC-11  
**Success:** Display order confirmation

### **Activity Flow:**

```
    ●
    ↓
┌──────────────────────┐
│ Redirected from      │
│ checkout             │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Load Order Received  │
│ page                 │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Display success msg: │
│ "Thank you. Your     │
│ booking confirmed."  │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Display order info:  │
│ • Order #1598        │
│ • Date               │
│ • Total: 6,950,000đ  │
│ • Payment method     │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Display booking info:│
│ • Room: Family Suite │
│ • Check-in: 26/5/26  │
│ • Check-out: 27/5/26 │
│ • Guests: 2 adults   │
│ • Extras: High Floor │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Display customer info│
│ • Name, Email, Phone │
│ • Address            │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Show download invoice│
│ button (UC-27)       │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Show next steps:     │
│ "Check your email"   │
└──────────────────────┘
    ↓
    ◎
```

**No decisions** - Display information only

---

## UC-13: NHẬN EMAIL XÁC NHẬN (Receive Email) 📧

**Actor:** System (automated), Guest (receives)  
**Entry Point:** Triggered by UC-11  
**Success:** Email sent and received

### **Activity Flow:**

```
    ●
    ↓
┌──────────────────────┐
│ Booking confirmed    │
│ (UC-11 trigger)      │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ System: Prepare email│
│ data                 │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Load email template  │
│ (booking-confirm.html)│
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Insert booking data: │
│ • Order #            │
│ • Customer name      │
│ • Room details       │
│ • Dates, Guests      │
│ • Total amount       │
│ • Payment method     │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Attach invoice PDF   │
│ (UC-27)              │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Send email via SMTP  │
│ To: customer email   │
│ Subject: "Booking    │
│ Confirmation #1598"  │
└──────────────────────┘
    ↓
    ◇ Sent successfully?
   / \
  /   \
 No    Yes
 ↓     ↓
┌──────┐ ┌─────────────────────┐
│Log   │ │Guest: Receive email │
│error │ │in inbox             │
│Retry │ └─────────────────────┘
└──────┘         ↓
         ┌─────────────────────┐
         │Guest: Open email    │
         └─────────────────────┘
                 ↓
         ┌─────────────────────┐
         │Guest: View booking  │
         │details & invoice    │
         └─────────────────────┘
 ↓               ↓
 └───────┬───────┘
         ↓
         ◎
```

**Decisions:**
1. **Sent successfully?** → Log error and retry, or deliver to inbox

---

## UC-17: ĐÁNH GIÁ PHÒNG (Write Review) ⭐

**Actor:** Guest (after completing booking)  
**Entry Point:** Room detail page, Reviews tab  
**Success:** Review submitted

### **Activity Flow:**

```
    ●
    ↓
┌──────────────────────┐
│ On room detail page  │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Click "Reviews" tab  │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ View existing reviews│
└──────────────────────┘
    ↓
    ◇ Eligible to review?
   / \
  /   \
 No    Yes
 ↓     ↓
┌──────┐ ┌─────────────────────┐
│Show  │ │Click "Write Review" │
│msg:  │ │button               │
│"Must │ └─────────────────────┘
│book" │         ↓
└──────┘ ┌─────────────────────┐
         │Review modal opens   │
         └─────────────────────┘
                 ↓
         ┌─────────────────────┐
         │Select rating (1-5★) │
         └─────────────────────┘
                 ↓
         ┌─────────────────────┐
         │Enter review title   │
         └─────────────────────┘
                 ↓
         ┌─────────────────────┐
         │Enter review text    │
         └─────────────────────┘
                 ↓
         ┌─────────────────────┐
         │[Optional] Upload    │
         │images (max 5)       │
         └─────────────────────┘
                 ↓
         ┌─────────────────────┐
         │Click "Submit Review"│
         └─────────────────────┘
                 ↓
         ┌─────────────────────┐
         │Save review          │
         │Status: Pending      │
         │(awaiting approval)  │
         └─────────────────────┘
                 ↓
         ┌─────────────────────┐
         │Show success message:│
         │"Review submitted    │
         │for approval"        │
         └─────────────────────┘
 ↓               ↓
 └───────┬───────┘
         ↓
         ◎
```

**Decisions:**
1. **Eligible to review?** → Must have completed booking for this room

---

## UC-21: QUẢN LÝ BOOKING (Admin - Manage Bookings) 🔧

**Actor:** Admin  
**Entry Point:** Admin Dashboard → Bookings  
**Success:** View/Edit/Update bookings

### **Activity Flow:**

```
    ●
    ↓
┌──────────────────────┐
│ Login to wp-admin    │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Navigate to Bookings │
│ menu                 │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ View bookings list:  │
│ • Order #            │
│ • Customer           │
│ • Date, Check-in/out │
│ • Total              │
│ • Status             │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Apply filters:       │
│ • All/Pending/etc    │
│ • Date range         │
│ • Customer search    │
└──────────────────────┘
    ↓
    ◇ Admin action?
   /│\
  / │ \
 /  │  \
View Edit Calendar
detail    view
 ↓   ↓    ↓
┌────┐┌────┐┌─────────────────┐
│UC- ││    ││Switch to        │
│21  ││    ││calendar         │
│con-││    ││• View bookings  │
│tin.││    ││  by date        │
└────┘│    ││• Color-coded    │
      │    ││• Click to edit  │
      ↓    │└─────────────────┘
┌─────────────────────┐│
│Click booking to edit││
└─────────────────────┘│
      ↓                ↓
┌─────────────────────┐
│Edit booking page:   │
│• Customer info      │
│• Room, Dates        │
│• Status dropdown    │
│• Payment status     │
└─────────────────────┘
      ↓
┌─────────────────────┐
│Change status:       │
│Pending → Processing │
│      → Confirmed    │
└─────────────────────┘
      ↓
┌─────────────────────┐
│Click "Update"       │
└─────────────────────┘
      ↓
┌─────────────────────┐
│Save changes         │
│Update database      │
└─────────────────────┘
      ↓
┌─────────────────────┐
│Show success message │
│"Booking updated"    │
└─────────────────────┘
      ↓
      ◎
```

**Decisions:**
1. **Admin action?** → View detail / Edit booking / Calendar view

---

## UC-22: QUẢN LÝ PHÒNG (Admin - Manage Rooms) 🏨

**Actor:** Admin  
**Entry Point:** Admin Dashboard → Rooms  
**Success:** View/Edit/Add rooms

### **Activity Flow:**

```
    ●
    ↓
┌──────────────────────┐
│ Navigate to Rooms    │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ View rooms list:     │
│ • Room name          │
│ • Type               │
│ • Price per night    │
│ • Inventory          │
│ • Status             │
└──────────────────────┘
    ↓
    ◇ Action?
   /│\
  / │ \
Add Edit View
new
 ↓   ↓    ↓
┌────┐┌──────────────────┐
│Add ││Click room to edit│
│New │└──────────────────┘
│Room│       ↓
│flow│┌──────────────────┐
└────┘│Edit Room page    │
      │Room Settings tabs│
      └──────────────────┘
             ↓
      ┌──────────────────┐
      │Tab 1: General    │
      │• Name, Type      │
      │• Description     │
      │• Capacity        │
      │• Size, Amenities │
      └──────────────────┘
             ↓
      ┌──────────────────┐
      │Tab 2: Pricing    │
      │• Regular price   │
      │• Date-based      │
      │  pricing         │
      │(UC-22 continues) │
      └──────────────────┘
             ↓
      ┌──────────────────┐
      │Tab 3: Block Dates│
      │(UC-24)           │
      └──────────────────┘
             ↓
      ┌──────────────────┐
      │Tab 4: Gallery    │
      │• Upload photos   │
      └──────────────────┘
             ↓
      ┌──────────────────┐
      │Tab 5+: Other tabs│
      └──────────────────┘
             ↓
      ┌──────────────────┐
      │Click "Update"    │
      └──────────────────┘
             ↓
      ┌──────────────────┐
      │Save changes      │
      └──────────────────┘
             ↓
             ◎
```

**Decisions:**
1. **Action?** → Add new / Edit existing / View only

---

## UC-23: QUẢN LÝ TỒN KHO (Admin - Manage Inventory) 📊

**Actor:** Admin  
**Entry Point:** Edit Room page → General tab  
**Success:** Inventory updated

### **Activity Flow:**

```
    ●
    ↓
┌──────────────────────┐
│ On Edit Room page    │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Go to General tab    │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ View current         │
│ inventory count      │
│ (hb_number_of_rooms) │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Change inventory:    │
│ e.g. 18 → 20         │
└──────────────────────┘
    ↓
    ◇ Valid number?
   / \
  /   \
 No    Yes
 ↓     ↓
┌──────┐ ┌─────────────────────┐
│Show  │ │Update inventory in  │
│error │ │database (postmeta)  │
└──────┘ └─────────────────────┘
                 ↓
         ┌─────────────────────┐
         │Recalculate          │
         │availability         │
         └─────────────────────┘
                 ↓
         ┌─────────────────────┐
         │Click "Update" button│
         └─────────────────────┘
                 ↓
         ┌─────────────────────┐
         │Save to database     │
         └─────────────────────┘
                 ↓
         ┌─────────────────────┐
         │Show success message │
         │"Room updated"       │
         └─────────────────────┘
 ↓               ↓
 └───────┬───────┘
         ↓
         ◎
```

**Decisions:**
1. **Valid number?** → Must be positive integer >= 0

---

## UC-24: KHÓA NGÀY (Admin - Block Special Dates) 🚫

**Actor:** Admin  
**Entry Point:** Edit Room → Block Special Date tab  
**Success:** Dates blocked for booking

### **Activity Flow:**

```
    ●
    ↓
┌──────────────────────┐
│ On Edit Room page    │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Click "Block Special │
│ Date" tab            │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ View calendar (May   │
│ 2026)                │
└──────────────────────┘
    ↓
    ◇ Action?
   /│\
  / │ \
Block Open Select
month month specific
 ↓     ↓    dates
┌───┐ ┌───┐  ↓
│All││All│ ┌─────────────────────┐
│   ││   │ │Click date(s) to     │
│   ││   │ │block, e.g. 26th     │
└───┘└───┘ └─────────────────────┘
 ↓    ↓           ↓
 │    │   ┌─────────────────────┐
 │    │   │Selected dates       │
 │    │   │highlight in yellow  │
 │    │   └─────────────────────┘
 ↓    ↓           ↓
 └────┴─────┬─────┘
            ↓
    ┌──────────────────────┐
    │[Optional] Enter      │
    │block reason:         │
    │"Maintenance" /       │
    │"Private event"       │
    └──────────────────────┘
            ↓
    ┌──────────────────────┐
    │Click "Update" button │
    └──────────────────────┘
            ↓
    ┌──────────────────────┐
    │Save blocked dates to │
    │availability table    │
    │is_blocked = 1        │
    └──────────────────────┘
            ↓
    ┌──────────────────────┐
    │Prevent bookings for  │
    │those dates           │
    └──────────────────────┘
            ↓
    ┌──────────────────────┐
    │Show success message  │
    │"Dates blocked"       │
    └──────────────────────┘
            ↓
            ◎
```

**Decisions:**
1. **Action?** → Block entire month / Open month / Select specific dates

---

## UC-25: QUẢN LÝ EXTRAS (Admin - Manage Extra Services) ➕

**Actor:** Admin  
**Entry Point:** Admin Dashboard → Extras  
**Success:** Extra added/edited

### **Activity Flow:**

```
    ●
    ↓
┌──────────────────────┐
│ Navigate to Extras   │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ View extras list:    │
│ • Honeymoon (1.5M)   │
│ • Extra bed (300K)   │
│ • High Floor (0đ)    │
└──────────────────────┘
    ↓
    ◇ Action?
   / \
  /   \
Add   Edit
new  existing
 ↓     ↓
┌────┐┌──────────────────┐
│    ││Click extra to    │
│    ││edit              │
│    │└──────────────────┘
│    │       ↓
│    │┌──────────────────┐
│    ││Or: Click "Add New│
│    ││Extra Room"       │
│    │└──────────────────┘
 ↓   ↓
 └───┴──────┐
            ↓
    ┌──────────────────────┐
    │Add/Edit Extra page   │
    └──────────────────────┘
            ↓
    ┌──────────────────────┐
    │Enter title:          │
    │e.g. "Extra bed"      │
    └──────────────────────┘
            ↓
    ┌──────────────────────┐
    │Enter description     │
    │(optional)            │
    └──────────────────────┘
            ↓
    ┌──────────────────────┐
    │Extra Settings:       │
    │• Price: 300,000      │
    │• Unit: 1             │
    │• Type: number/trip   │
    │• Required: yes/no    │
    └──────────────────────┘
            ↓
    ┌──────────────────────┐
    │Click "Publish/Update"│
    └──────────────────────┘
            ↓
    ┌──────────────────────┐
    │Save extra to database│
    │(hb_extra_room post)  │
    └──────────────────────┘
            ↓
    ┌──────────────────────┐
    │Extra now available   │
    │in booking forms      │
    └──────────────────────┘
            ↓
            ◎
```

**Decisions:**
1. **Action?** → Add new extra / Edit existing extra

---

## UC-26: QUẢN LÝ COUPON (Admin - Manage Coupons) 🎟️

**Actor:** Admin  
**Entry Point:** Admin Dashboard → Coupons  
**Success:** Coupon created/edited

### **Activity Flow:**

```
    ●
    ↓
┌──────────────────────┐
│ Navigate to Coupons  │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ View coupons list:   │
│ • sale50k (50,000đ)  │
│ • sale_test (50%)    │
└──────────────────────┘
    ↓
    ◇ Action?
   / \
  /   \
Add   Edit
new
 ↓     ↓
┌────┐┌──────────────────┐
│    ││Click coupon      │
│    │└──────────────────┘
│    │       ↓
│    │┌──────────────────┐
│    ││Or: Click "Add    │
│    ││Coupon"           │
│    │└──────────────────┘
 ↓   ↓
 └───┴──────┐
            ↓
    ┌──────────────────────┐
    │Add/Edit Coupon page  │
    └──────────────────────┘
            ↓
    ┌──────────────────────┐
    │Enter coupon code:    │
    │e.g. "SUMMER2026"     │
    └──────────────────────┘
            ↓
    ┌──────────────────────┐
    │Enter description     │
    └──────────────────────┘
            ↓
    ┌──────────────────────┐
    │Select discount type: │
    │⚪ Fixed cart         │
    │⚪ Percentage         │
    └──────────────────────┘
            ↓
    ┌──────────────────────┐
    │Enter discount amount:│
    │50000 or 50           │
    └──────────────────────┘
            ↓
    ┌──────────────────────┐
    │[Optional] Settings:  │
    │• Minimum spend       │
    │• Maximum discount    │
    │• Usage limit         │
    │• Expiry date         │
    └──────────────────────┘
            ↓
    ┌──────────────────────┐
    │Click "Publish/Update"│
    └──────────────────────┘
            ↓
    ┌──────────────────────┐
    │Save coupon to        │
    │database              │
    └──────────────────────┘
            ↓
    ┌──────────────────────┐
    │Coupon now usable in  │
    │cart (UC-05)          │
    └──────────────────────┘
            ↓
            ◎
```

**Decisions:**
1. **Action?** → Add new / Edit existing

---

## UC-27: TẠO HÓA ĐƠN PDF (Generate Invoice) 📄

**Actor:** System (automated after UC-11)  
**Entry Point:** Booking confirmed  
**Success:** PDF generated and attached to email

### **Activity Flow:**

```
    ●
    ↓
┌──────────────────────┐
│ Booking confirmed    │
│ (trigger from UC-11) │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Load invoice settings│
│ from admin config    │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Get company info:    │
│ • Logo               │
│ • Name: Q&T Hosp.   │
│ • Address            │
│ • Phone, Email       │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Get booking data:    │
│ • Order #1598        │
│ • Customer info      │
│ • Room details       │
│ • Check-in/out dates │
│ • Items (room+extras)│
│ • Totals             │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Load PDF template    │
│ (invoice layout)     │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Build PDF structure: │
│ • Header (logo)      │
│ • Company info       │
│ • Invoice #          │
│ • Customer details   │
│ • Items table        │
│ • Totals             │
│ • Footer (T&C)       │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Generate PDF using   │
│ TCPDF/mPDF library   │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Save PDF to:         │
│ /wp-content/uploads/ │
│ invoices/1598.pdf    │
└──────────────────────┘
    ↓
┌──────────────────────┐
│ Make available for:  │
│ • Download on order  │
│   confirmation page  │
│ • Email attachment   │
│   (UC-13)            │
└──────────────────────┘
    ↓
    ◎
```

**No decisions** - Automated PDF generation process

---

## ✅ CHECKLIST VẼ 21 ACTIVITY DIAGRAMS

- [ ] Initial node (●) ở đầu mỗi diagram
- [ ] Final node (◎) ở cuối
- [ ] Activities trong rounded rectangles
- [ ] Decisions trong diamonds (◇)
- [ ] Arrows có hướng rõ ràng
- [ ] Decision branches có labels (Yes/No, Valid/Invalid)
- [ ] Màu sắc consistent
- [ ] Activities có tên rõ ràng
- [ ] Fork/Join bars nếu có parallel activities
- [ ] Swim lanes nếu có multiple actors
- [ ] Reference đến UCs khác khi cần (UC-04, UC-27, etc.)

---

## 🎨 MÀU SẮC CHO TẤT CẢ ACTIVITY DIAGRAMS

```css
/* Activities by Type */
Start activities: #C8E6C9 (Light Green)
Normal activities: #BBDEFB (Light Blue)
Decision activities: #FFF9C4 (Light Yellow)
Error handling: #FFCDD2 (Light Red)
Success/Complete: #A5D6A7 (Green)

/* Nodes */
Initial node (●): #000000 (Black)
Final node (◎): #000000 (Black)

/* Connectors */
Normal flow: #424242 (Dark Gray), 2pt solid
Decision branches: #616161 (Gray), 1.5pt solid
Error flow: #D32F2F (Red), 2pt dashed
```

---

## ⏱️ THỜI GIAN ƯỚC TÍNH

| UC Group | Số diagrams | Complexity | Thời gian/diagram | Tổng |
|----------|-------------|------------|-------------------|------|
| UC-01 đến UC-13 (Guest) | 13 | Medium | 45-60 phút | 10-13 giờ |
| UC-17 (Review) | 1 | Medium | 45 phút | 45 phút |
| UC-21 đến UC-27 (Admin) | 7 | Medium-High | 1-1.5 giờ | 7-10 giờ |

**TỔNG:** 18-24 giờ cho tất cả 21 Activity Diagrams

---

## 💡 TIPS VẼ NHANH

1. **Tạo template:** Vẽ 1 diagram chuẩn, copy làm base cho các UC tương tự
2. **Group similar UCs:** UC-03, UC-04, UC-05 có flow giống nhau
3. **Focus on decisions:** Đây là phần quan trọng nhất
4. **Keep it simple:** Không cần quá chi tiết, focus vào main flow
5. **Use tool libraries:** Visual Paradigm, Draw.io có sẵn UML shapes

---

**HOÀN THÀNH FILE ACTIVITY DIAGRAMS! 🎉**

**File này được tạo bởi Claude AI - Ngày: 26/05/2026**
