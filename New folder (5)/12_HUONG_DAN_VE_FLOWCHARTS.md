# 📐 HƯỚNG DẪN VẼ FLOWCHARTS - 10 ALGORITHMS QUAN TRỌNG

**Dự án:** Quan Trọng Hotel (Parkside Sunline Hotel)  
**Loại sơ đồ:** Flowcharts (Algorithm Flowcharts)  
**Số lượng flowcharts:** 10 algorithms chính  
**Công cụ đề xuất:** Draw.io, Lucidchart, Microsoft Visio, Flowgorithm

---

## 🎯 MỤC TIÊU

Flowchart mô tả:
- **Algorithm** (thuật toán) xử lý logic
- **Decision points** (điểm quyết định)
- **Loops** (vòng lặp) nếu có
- **Input/Output** operations
- **Detailed logic** ở mức code

---

## 🎨 KÝ HIỆU FLOWCHART CHUẨN

```
    ⬭ ← Start/End (oval)
    
┌─────────┐
│ Process │ ← Process (rectangle)
└─────────┘

    ◇ ← Decision (diamond)
   / \
  /   \
 Yes   No

┌─────────┐
│░░░░░░░░░│ ← Input/Output (parallelogram)
└─────────┘

┌─────────────┐
│┌───────────┐│
││Sub-process││ ← Predefined process (double border)
│└───────────┘│
└─────────────┘

    → ← Flow direction (arrow)
```

---

# 10 FLOWCHARTS CHI TIẾT

---

## FC-01: PRICE CALCULATION ALGORITHM 💰

**Mục đích:** Tính tổng giá booking (base price + extras + nights - discount)

### **Flowchart:**

```
        ⬭ START
        ↓
    ┌─────────────┐
    │ INPUT:      │
    │ • roomId    │
    │ • checkIn   │
    │ • checkOut  │
    │ • adults    │
    │ • children  │
    │ • extras[]  │
    │ • couponCode│
    └─────────────┘
        ↓
    ┌─────────────┐
    │ Get room    │
    │ basePrice   │
    │ from DB     │
    └─────────────┘
        ↓
    ┌─────────────┐
    │ Calculate   │
    │ nights =    │
    │ checkOut -  │
    │ checkIn     │
    └─────────────┘
        ↓
    ┌─────────────┐
    │ baseTotal = │
    │ basePrice × │
    │ nights      │
    └─────────────┘
        ↓
    ┌─────────────┐
    │ Initialize  │
    │ extrasTotal │
    │ = 0         │
    └─────────────┘
        ↓
        ◇ Has extras?
       / \
      /   \
     No   Yes
     ↓     ↓
     │  ┌─────────────┐
     │  │ FOR each    │
     │  │ extra in    │
     │  │ extras[]    │
     │  └─────────────┘
     │     ↓
     │  ┌─────────────┐
     │  │ Get extra   │
     │  │ price & unit│
     │  └─────────────┘
     │     ↓
     │     ◇ Unit type?
     │    /│\
     │   / │ \
     │ Per Per One
     │Night Person Time
     │  ↓   ↓    ↓
     │  │   │ ┌──────┐
     │  │   │ │ cost=│
     │  │   │ │price │
     │  │   │ └──────┘
     │  │   ↓
     │  │ ┌──────────┐
     │  │ │ cost =   │
     │  │ │ price ×  │
     │  │ │ (adults+ │
     │  │ │ children)│
     │  │ └──────────┘
     │  ↓
     │ ┌────────────┐
     │ │ cost =     │
     │ │ price ×    │
     │ │ nights     │
     │ └────────────┘
     │  ↓
     │  └──┬──┬──┘
     │     ↓
     │  ┌─────────────┐
     │  │ extrasTotal │
     │  │ += cost     │
     │  └─────────────┘
     │     ↓
     │  ┌─────────────┐
     │  │ END FOR     │
     │  └─────────────┘
     ↓     ↓
     └──┬──┘
        ↓
    ┌─────────────┐
    │ subtotal =  │
    │ baseTotal + │
    │ extrasTotal │
    └─────────────┘
        ↓
        ◇ Has coupon?
       / \
      /   \
     No   Yes
     ↓     ↓
     │  ┌─────────────┐
     │  │ Validate    │
     │  │ coupon      │
     │  └─────────────┘
     │     ↓
     │     ◇ Valid?
     │    / \
     │   /   \
     │  No   Yes
     │  ↓     ↓
     │  │  ┌─────────────┐
     │  │  │ Get discount│
     │  │  │ type & value│
     │  │  └─────────────┘
     │  │     ↓
     │  │     ◇ Type?
     │  │    / \
     │  │   /   \
     │  │ Fixed Percent
     │  │  ↓     ↓
     │  │  │  ┌────────┐
     │  │  │  │discount│
     │  │  │  │= subto-│
     │  │  │  │tal×val%│
     │  │  │  └────────┘
     │  │  ↓
     │  │ ┌─────────┐
     │  │ │discount │
     │  │ │= value  │
     │  │ └─────────┘
     │  │  ↓
     │  │  └──┬──┘
     │  ↓     ↓
     │  └──┬──┘
     ↓     ↓
     └──┬──┘
        ↓
    ┌─────────────┐
    │ discount =  │
    │ discount or │
    │ 0           │
    └─────────────┘
        ↓
    ┌─────────────┐
    │ Calculate   │
    │ tax = 0     │
    │ (no tax)    │
    └─────────────┘
        ↓
    ┌─────────────┐
    │ total =     │
    │ subtotal -  │
    │ discount +  │
    │ tax         │
    └─────────────┘
        ↓
    ┌─────────────┐
    │ OUTPUT:     │
    │ • baseTotal │
    │ • extrasTotal│
    │ • subtotal  │
    │ • discount  │
    │ • tax       │
    │ • total     │
    └─────────────┘
        ↓
        ⬭ END
```

**Variables:**
- `basePrice`: decimal (3,000,000đ)
- `nights`: int
- `extrasTotal`: decimal
- `discount`: decimal
- `total`: decimal

---

## FC-02: AVAILABILITY CHECK ALGORITHM 📅

**Mục đích:** Check phòng có available cho dates không

### **Flowchart:**

```
        ⬭ START
        ↓
    ┌─────────────┐
    │ INPUT:      │
    │ • roomId    │
    │ • checkIn   │
    │ • checkOut  │
    └─────────────┘
        ↓
        ◇ Dates valid?
       / \
      /   \
     No   Yes
     ↓     ↓
┌────────┐  │
│ RETURN │  │
│ False  │  │
└────────┘  │
     ↓      ↓
     │  ┌─────────────┐
     │  │ Get room    │
     │  │ inventory   │
     │  │ count from  │
     │  │ DB          │
     │  └─────────────┘
     │     ↓
     │  ┌─────────────┐
     │  │ currentDate │
     │  │ = checkIn   │
     │  └─────────────┘
     │     ↓
     │  ┌─────────────┐
     │  │ WHILE       │
     │  │ currentDate │
     │  │ < checkOut  │
     │  └─────────────┘
     │     ↓
     │  ┌─────────────┐
     │  │ Query DB:   │
     │  │ bookings on │
     │  │ currentDate │
     │  └─────────────┘
     │     ↓
     │  ┌─────────────┐
     │  │ Count active│
     │  │ bookings    │
     │  └─────────────┘
     │     ↓
     │  ┌─────────────┐
     │  │ Query DB:   │
     │  │ blocked     │
     │  │ dates       │
     │  └─────────────┘
     │     ↓
     │     ◇ Is blocked?
     │    / \
     │   /   \
     │  Yes   No
     │  ↓     ↓
┌────────┐    │
│ RETURN │    │
│ False  │    │
└────────┘    │
     │        ↓
     │        ◇ Bookings ≥
     │        Inventory?
     │       / \
     │      /   \
     │     Yes   No
     │     ↓     ↓
┌────────┐      │
│ RETURN │      │
│ False  │      │
└────────┘      │
     │          ↓
     │     ┌─────────────┐
     │     │ currentDate │
     │     │ += 1 day    │
     │     └─────────────┘
     │          ↓
     │     ┌─────────────┐
     │     │ END WHILE   │
     │     └─────────────┘
     │          ↓
     │     ┌─────────────┐
     │     │ RETURN      │
     │     │ True        │
     │     └─────────────┘
     ↓          ↓
     └────┬─────┘
          ↓
          ⬭ END
```

**Logic:**
- Loop through each date from check-in to check-out
- Check if date is blocked
- Count active bookings for that date
- If bookings >= inventory OR blocked → NOT available
- If all dates pass → Available

---

## FC-03: BOOKING VALIDATION ALGORITHM ✅

**Mục đích:** Validate booking data trước khi tạo

### **Flowchart:**

```
        ⬭ START
        ↓
    ┌─────────────┐
    │ INPUT:      │
    │ • roomId    │
    │ • checkIn   │
    │ • checkOut  │
    │ • adults    │
    │ • children  │
    │ • customerInfo│
    └─────────────┘
        ↓
    ┌─────────────┐
    │ errors = [] │
    └─────────────┘
        ↓
        ◇ roomId exists?
       / \
      /   \
     No   Yes
     ↓     ↓
┌────────────┐ Skip
│ errors.add │
│ "Invalid   │
│  room"     │
└────────────┘
     ↓     ↓
     └──┬──┘
        ↓
        ◇ checkOut >
        checkIn?
       / \
      /   \
     No   Yes
     ↓     ↓
┌────────────┐ Skip
│ errors.add │
│ "Invalid   │
│  dates"    │
└────────────┘
     ↓     ↓
     └──┬──┘
        ↓
        ◇ checkIn ≥
        today?
       / \
      /   \
     No   Yes
     ↓     ↓
┌────────────┐ Skip
│ errors.add │
│ "Past date"│
└────────────┘
     ↓     ↓
     └──┬──┘
        ↓
        ◇ adults > 0?
       / \
      /   \
     No   Yes
     ↓     ↓
┌────────────┐ Skip
│ errors.add │
│ "Need ≥1   │
│  adult"    │
└────────────┘
     ↓     ↓
     └──┬──┘
        ↓
    ┌─────────────┐
    │ Get room    │
    │ maxAdults & │
    │ maxChildren │
    └─────────────┘
        ↓
        ◇ adults +
        children ≤
        capacity?
       / \
      /   \
     No   Yes
     ↓     ↓
┌────────────┐ Skip
│ errors.add │
│ "Exceeds   │
│  capacity" │
└────────────┘
     ↓     ↓
     └──┬──┘
        ↓
        ◇ Has customer
        name?
       / \
      /   \
     No   Yes
     ↓     ↓
┌────────────┐ Skip
│ errors.add │
│ "Name      │
│  required" │
└────────────┘
     ↓     ↓
     └──┬──┘
        ↓
        ◇ Has valid
        email?
       / \
      /   \
     No   Yes
     ↓     ↓
┌────────────┐ Skip
│ errors.add │
│ "Invalid   │
│  email"    │
└────────────┘
     ↓     ↓
     └──┬──┘
        ↓
        ◇ Has phone?
       / \
      /   \
     No   Yes
     ↓     ↓
┌────────────┐ Skip
│ errors.add │
│ "Phone     │
│  required" │
└────────────┘
     ↓     ↓
     └──┬──┘
        ↓
        ◇ errors.length
        = 0?
       / \
      /   \
     No   Yes
     ↓     ↓
┌────────────┐┌────────────┐
│ RETURN     ││ RETURN     │
│ False,     ││ True,      │
│ errors     ││ null       │
└────────────┘└────────────┘
     ↓          ↓
     └────┬─────┘
          ↓
          ⬭ END
```

**Validations:**
1. Room exists
2. Valid dates (checkout > checkin, future dates)
3. At least 1 adult
4. Guests within capacity
5. Customer info complete (name, email, phone)

---

## FC-04: COUPON VALIDATION ALGORITHM 🎟️

**Mục đích:** Validate coupon code trước khi apply

### **Flowchart:**

```
        ⬭ START
        ↓
    ┌─────────────┐
    │ INPUT:      │
    │ • couponCode│
    │ • cartTotal │
    │ • userId    │
    └─────────────┘
        ↓
    ┌─────────────┐
    │ Query DB for│
    │ coupon by   │
    │ code        │
    └─────────────┘
        ↓
        ◇ Coupon exists?
       / \
      /   \
     No   Yes
     ↓     ↓
┌────────────┐ │
│ RETURN     │ │
│ "Invalid   │ │
│  coupon"   │ │
└────────────┘ │
     ↓         ↓
     │     ┌─────────────┐
     │     │ Get coupon  │
     │     │ data:       │
     │     │ • discountType│
     │     │ • value     │
     │     │ • minSpend  │
     │     │ • maxDiscount│
     │     │ • usageLimit│
     │     │ • usedCount │
     │     │ • expiryDate│
     │     └─────────────┘
     │         ↓
     │         ◇ Expired?
     │        / \
     │       /   \
     │      Yes   No
     │      ↓     ↓
┌────────────┐    │
│ RETURN     │    │
│ "Coupon    │    │
│  expired"  │    │
└────────────┘    │
     │            ↓
     │            ◇ usedCount ≥
     │            usageLimit?
     │           / \
     │          /   \
     │         Yes   No
     │         ↓     ↓
┌────────────┐       │
│ RETURN     │       │
│ "Usage     │       │
│  limit     │       │
│  reached"  │       │
└────────────┘       │
     │               ↓
     │               ◇ cartTotal ≥
     │               minSpend?
     │              / \
     │             /   \
     │            No   Yes
     │            ↓     ↓
┌────────────┐          │
│ RETURN     │          │
│ "Minimum   │          │
│  not met"  │          │
└────────────┘          │
     │                  ↓
     │              ┌─────────────┐
     │              │ Calculate   │
     │              │ discount    │
     │              └─────────────┘
     │                  ↓
     │                  ◇ Type?
     │                 / \
     │                /   \
     │              Fixed Percent
     │               ↓     ↓
     │               │  ┌──────────┐
     │               │  │ discount=│
     │               │  │ cartTotal│
     │               │  │ × value% │
     │               │  └──────────┘
     │               ↓
     │          ┌──────────┐
     │          │ discount=│
     │          │ value    │
     │          └──────────┘
     │               ↓
     │               └──┬──┘
     │                  ↓
     │                  ◇ discount >
     │                  maxDiscount?
     │                 / \
     │                /   \
     │               Yes   No
     │               ↓     ↓
     │          ┌──────────┐ Skip
     │          │ discount=│
     │          │maxDiscount│
     │          └──────────┘
     │               ↓     ↓
     │               └──┬──┘
     │                  ↓
     │              ┌─────────────┐
     │              │ Increment   │
     │              │ usedCount   │
     │              └─────────────┘
     │                  ↓
     │              ┌─────────────┐
     │              │ RETURN      │
     │              │ Valid,      │
     │              │ discount    │
     │              └─────────────┘
     ↓                  ↓
     └────────┬─────────┘
              ↓
              ⬭ END
```

**Checks:**
1. Coupon exists
2. Not expired
3. Usage limit not reached
4. Cart total ≥ minimum spend
5. Calculate discount (fixed or percent)
6. Apply max discount cap if set

---

## FC-05: INVENTORY MANAGEMENT ALGORITHM 📊

**Mục đích:** Update inventory khi booking created/cancelled

### **Flowchart:**

```
        ⬭ START
        ↓
    ┌─────────────┐
    │ INPUT:      │
    │ • roomId    │
    │ • operation │
    │ • dates[]   │
    └─────────────┘
        ↓
        ◇ operation?
       /│\
      / │ \
   Decrease│Increase
     ↓   │   ↓
     │   │ ┌─────────────┐
     │   │ │ FOR date in │
     │   │ │ dates[]     │
     │   │ └─────────────┘
     │   │     ↓
     │   │ ┌─────────────┐
     │   │ │ Get current │
     │   │ │ booked count│
     │   │ │ for date    │
     │   │ └─────────────┘
     │   │     ↓
     │   │ ┌─────────────┐
     │   │ │ bookedCount │
     │   │ │ += 1        │
     │   │ └─────────────┘
     │   │     ↓
     │   │ ┌─────────────┐
     │   │ │ available = │
     │   │ │ inventory - │
     │   │ │ bookedCount │
     │   │ └─────────────┘
     │   │     ↓
     │   │ ┌─────────────┐
     │   │ │ UPDATE DB   │
     │   │ │ for date    │
     │   │ └─────────────┘
     │   │     ↓
     │   │ ┌─────────────┐
     │   │ │ END FOR     │
     │   │ └─────────────┘
     │   │     ↓
     │   └──┬──┘
     │      │
     │  ┌─────────────┐
     │  │ FOR date in │
     │  │ dates[]     │
     │  └─────────────┘
     │      ↓
     │  ┌─────────────┐
     │  │ Get current │
     │  │ booked count│
     │  └─────────────┘
     │      ↓
     │  ┌─────────────┐
     │  │ bookedCount │
     │  │ -= 1        │
     │  └─────────────┘
     │      ↓
     │      ◇ bookedCount
     │      < 0?
     │     / \
     │    /   \
     │   Yes   No
     │   ↓     ↓
     │  ┌────┐ Skip
     │  │Set │
     │  │to 0│
     │  └────┘
     │   ↓     ↓
     │   └──┬──┘
     │      ↓
     │  ┌─────────────┐
     │  │ available = │
     │  │ inventory - │
     │  │ bookedCount │
     │  └─────────────┘
     │      ↓
     │  ┌─────────────┐
     │  │ UPDATE DB   │
     │  │ for date    │
     │  └─────────────┘
     │      ↓
     │  ┌─────────────┐
     │  │ END FOR     │
     │  └─────────────┘
     ↓      ↓
     └──┬───┘
        ↓
    ┌─────────────┐
    │ RETURN      │
    │ Success     │
    └─────────────┘
        ↓
        ⬭ END
```

**Operations:**
- **Decrease:** When booking created (reserve)
- **Increase:** When booking cancelled (release)

**Logic:**
- Loop through dates
- Update booked count
- Recalculate available = inventory - booked

---

## FC-06: DATE BLOCKING LOGIC 🚫

**Mục đích:** Block dates cho maintenance hoặc special events

### **Flowchart:**

```
        ⬭ START
        ↓
    ┌─────────────┐
    │ INPUT:      │
    │ • roomId    │
    │ • startDate │
    │ • endDate   │
    │ • reason    │
    └─────────────┘
        ↓
        ◇ Dates valid?
       / \
      /   \
     No   Yes
     ↓     ↓
┌────────────┐ │
│ RETURN     │ │
│ Error      │ │
└────────────┘ │
     ↓         ↓
     │     ┌─────────────┐
     │     │ Check for   │
     │     │ existing    │
     │     │ bookings in │
     │     │ date range  │
     │     └─────────────┘
     │         ↓
     │         ◇ Has bookings?
     │        / \
     │       /   \
     │      Yes   No
     │      ↓     ↓
┌────────────┐    │
│ RETURN     │    │
│ "Cannot    │    │
│  block:    │    │
│  existing  │    │
│  bookings" │    │
└────────────┘    │
     │            ↓
     │        ┌─────────────┐
     │        │ currentDate │
     │        │ = startDate │
     │        └─────────────┘
     │            ↓
     │        ┌─────────────┐
     │        │ WHILE       │
     │        │ currentDate │
     │        │ ≤ endDate   │
     │        └─────────────┘
     │            ↓
     │        ┌─────────────┐
     │        │ Query DB    │
     │        │ availability│
     │        │ for date    │
     │        └─────────────┘
     │            ↓
     │            ◇ Record exists?
     │           / \
     │          /   \
     │         No   Yes
     │         ↓     ↓
     │    ┌────────┐ │
     │    │ INSERT │ │
     │    │ new    │ │
     │    │ record │ │
     │    └────────┘ │
     │         ↓     ↓
     │         └──┬──┘
     │            ↓
     │        ┌─────────────┐
     │        │ UPDATE      │
     │        │ is_blocked=1│
     │        │ block_reason│
     │        │ = reason    │
     │        └─────────────┘
     │            ↓
     │        ┌─────────────┐
     │        │ currentDate │
     │        │ += 1 day    │
     │        └─────────────┘
     │            ↓
     │        ┌─────────────┐
     │        │ END WHILE   │
     │        └─────────────┘
     │            ↓
     │        ┌─────────────┐
     │        │ RETURN      │
     │        │ Success,    │
     │        │ blockedCount│
     │        └─────────────┘
     ↓            ↓
     └──────┬─────┘
            ↓
            ⬭ END
```

**Logic:**
1. Validate dates
2. Check no existing bookings
3. Loop through date range
4. Mark each date as blocked
5. Set block reason

---

## FC-07: EMAIL NOTIFICATION ALGORITHM 📧

**Mục đích:** Send email với template và attachments

### **Flowchart:**

```
        ⬭ START
        ↓
    ┌─────────────┐
    │ INPUT:      │
    │ • to        │
    │ • type      │
    │ • bookingId │
    └─────────────┘
        ↓
        ◇ type?
       /│\
      / │ \
   Confir-│Cancel
   mation │
     ↓   │   ↓
     │   │ ┌─────────────┐
     │   │ │ Load        │
     │   │ │ cancellation│
     │   │ │ template    │
     │   │ └─────────────┘
     │   │     ↓
     │   │ ┌─────────────┐
     │   │ │ Get booking │
     │   │ │ data        │
     │   │ └─────────────┘
     │   │     ↓
     │   │ ┌─────────────┐
     │   │ │ Build email │
     │   │ │ body        │
     │   │ └─────────────┘
     │   │     ↓
     │   │ ┌─────────────┐
     │   │ │ Send via    │
     │   │ │ SMTP        │
     │   │ └─────────────┘
     │   │     ↓
     │   └──┬──┘
     │      │
     │  ┌─────────────┐
     │  │ Load        │
     │  │ confirmation│
     │  │ template    │
     │  └─────────────┘
     │      ↓
     │  ┌─────────────┐
     │  │ Get booking │
     │  │ data from DB│
     │  └─────────────┘
     │      ↓
     │  ┌─────────────┐
     │  │ Get customer│
     │  │ info        │
     │  └─────────────┘
     │      ↓
     │  ┌─────────────┐
     │  │ Get room    │
     │  │ details     │
     │  └─────────────┘
     │      ↓
     │  ┌─────────────┐
     │  │ Build email │
     │  │ body with   │
     │  │ data        │
     │  └─────────────┘
     │      ↓
     │      ◇ Has invoice?
     │     / \
     │    /   \
     │   No   Yes
     │   ↓     ↓
     │  Skip ┌─────────────┐
     │       │ Load invoice│
     │       │ PDF file    │
     │       └─────────────┘
     │         ↓
     │       ┌─────────────┐
     │       │ Attach PDF  │
     │       └─────────────┘
     │   ↓     ↓
     │   └──┬──┘
     │      ↓
     │  ┌─────────────┐
     │  │ Set SMTP    │
     │  │ config:     │
     │  │ • host      │
     │  │ • port      │
     │  │ • auth      │
     │  └─────────────┘
     │      ↓
     │  ┌─────────────┐
     │  │ Send email  │
     │  └─────────────┘
     ↓      ↓
     └──┬───┘
        ↓
        ◇ Sent success?
       / \
      /   \
     No   Yes
     ↓     ↓
┌────────────┐┌────────────┐
│ Log error  ││ Log success│
│ Retry later││ Update sent│
│            ││ status     │
└────────────┘└────────────┘
     ↓          ↓
     └────┬─────┘
          ↓
    ┌─────────────┐
    │ RETURN      │
    │ status      │
    └─────────────┘
        ↓
        ⬭ END
```

**Email Types:**
- Confirmation (with invoice)
- Cancellation
- Reminder
- Review request

---

## FC-08: PDF GENERATION ALGORITHM 📄

**Mục đích:** Generate invoice PDF from booking data

### **Flowchart:**

```
        ⬭ START
        ↓
    ┌─────────────┐
    │ INPUT:      │
    │ • bookingId │
    └─────────────┘
        ↓
    ┌─────────────┐
    │ Load invoice│
    │ settings    │
    │ from admin  │
    └─────────────┘
        ↓
    ┌─────────────┐
    │ Get company │
    │ info:       │
    │ • logo      │
    │ • name      │
    │ • address   │
    │ • phone     │
    │ • email     │
    └─────────────┘
        ↓
    ┌─────────────┐
    │ Get booking │
    │ data:       │
    │ • order #   │
    │ • customer  │
    │ • room      │
    │ • dates     │
    │ • items     │
    │ • totals    │
    └─────────────┘
        ↓
    ┌─────────────┐
    │ Initialize  │
    │ PDF library │
    │ (TCPDF)     │
    └─────────────┘
        ↓
    ┌─────────────┐
    │ Add page    │
    │ A4 portrait │
    └─────────────┘
        ↓
    ┌─────────────┐
    │ Add header: │
    │ • Logo (3cm)│
    │ • Company   │
    │   name      │
    └─────────────┘
        ↓
    ┌─────────────┐
    │ Add title:  │
    │ "INVOICE"   │
    │ large, bold │
    └─────────────┘
        ↓
    ┌─────────────┐
    │ Add invoice │
    │ # and date  │
    └─────────────┘
        ↓
    ┌─────────────┐
    │ Add company │
    │ details     │
    │ (address,   │
    │  phone, etc)│
    └─────────────┘
        ↓
    ┌─────────────┐
    │ Add customer│
    │ details     │
    │ (name,      │
    │  address)   │
    └─────────────┘
        ↓
    ┌─────────────┐
    │ Create table│
    │ headers:    │
    │ Item|Price| │
    │ Qty|Total   │
    └─────────────┘
        ↓
    ┌─────────────┐
    │ FOR each    │
    │ item in     │
    │ booking     │
    └─────────────┘
        ↓
    ┌─────────────┐
    │ Add table   │
    │ row:        │
    │ • Item name │
    │ • Price     │
    │ • Quantity  │
    │ • Subtotal  │
    └─────────────┘
        ↓
    ┌─────────────┐
    │ END FOR     │
    └─────────────┘
        ↓
    ┌─────────────┐
    │ Add totals: │
    │ • Subtotal  │
    │ • Discount  │
    │ • Tax       │
    │ • TOTAL     │
    │   (bold)    │
    └─────────────┘
        ↓
    ┌─────────────┐
    │ Add footer: │
    │ • T&C       │
    │ • Thank you │
    └─────────────┘
        ↓
    ┌─────────────┐
    │ Generate PDF│
    │ binary data │
    └─────────────┘
        ↓
    ┌─────────────┐
    │ Save to:    │
    │ /wp-content/│
    │ uploads/    │
    │ invoices/   │
    │ {id}.pdf    │
    └─────────────┘
        ↓
    ┌─────────────┐
    │ RETURN      │
    │ file path   │
    └─────────────┘
        ↓
        ⬭ END
```

**Output:** PDF file saved to server

---

## FC-09: SEARCH ALGORITHM 🔍

**Mục đích:** Search rooms với filters và sorting

### **Flowchart:**

```
        ⬭ START
        ↓
    ┌─────────────┐
    │ INPUT:      │
    │ • checkIn   │
    │ • checkOut  │
    │ • adults    │
    │ • children  │
    │ • roomType  │
    │ • minPrice  │
    │ • maxPrice  │
    │ • sortBy    │
    └─────────────┘
        ↓
    ┌─────────────┐
    │ Build SQL   │
    │ query       │
    └─────────────┘
        ↓
    ┌─────────────┐
    │ SELECT rooms│
    │ WHERE       │
    │ post_type = │
    │ 'hb_room'   │
    └─────────────┘
        ↓
        ◇ Has roomType?
       / \
      /   \
     No   Yes
     ↓     ↓
    Skip ┌─────────────┐
         │ AND type =  │
         │ roomType    │
         └─────────────┘
     ↓     ↓
     └──┬──┘
        ↓
    ┌─────────────┐
    │ AND capacity│
    │ >= adults + │
    │    children │
    └─────────────┘
        ↓
        ◇ Has price filter?
       / \
      /   \
     No   Yes
     ↓     ↓
    Skip ┌─────────────┐
         │ AND price   │
         │ BETWEEN min │
         │ AND max     │
         └─────────────┘
     ↓     ↓
     └──┬──┘
        ↓
    ┌─────────────┐
    │ Execute     │
    │ query       │
    └─────────────┘
        ↓
    ┌─────────────┐
    │ rooms = []  │
    └─────────────┘
        ↓
    ┌─────────────┐
    │ FOR each    │
    │ result      │
    └─────────────┘
        ↓
    ┌─────────────┐
    │ Check       │
    │ availability│
    │ for dates   │
    └─────────────┘
        ↓
        ◇ Available?
       / \
      /   \
     No   Yes
     ↓     ↓
    Skip ┌─────────────┐
         │ Add to      │
         │ rooms[]     │
         └─────────────┘
     ↓     ↓
     └──┬──┘
        ↓
    ┌─────────────┐
    │ END FOR     │
    └─────────────┘
        ↓
        ◇ sortBy?
       /│\
      / │ \
   Price│Rating
     ↓  │  ↓
     │  │ ┌─────────────┐
     │  │ │ Sort by     │
     │  │ │ rating DESC │
     │  │ └─────────────┘
     │  │     ↓
     │  │ ┌─────────────┐
     │  │ │ Sort by     │
     │  │ │ name ASC    │
     │  │ └─────────────┘
     │  ↓     ↓
     │ ┌─────────────┐
     │ │ Sort by     │
     │ │ price ASC   │
     │ └─────────────┘
     ↓  ↓     ↓
     └──┴──┬──┘
           ↓
    ┌─────────────┐
    │ RETURN      │
    │ rooms[]     │
    └─────────────┘
        ↓
        ⬭ END
```

**Filters:**
- Room type
- Capacity (adults + children)
- Price range
- Availability for dates

**Sorting:**
- By price (low to high)
- By rating (high to low)
- By name (A-Z)

---

## FC-10: REVIEW SUBMISSION ALGORITHM ⭐

**Mục đích:** Validate và submit review

### **Flowchart:**

```
        ⬭ START
        ↓
    ┌─────────────┐
    │ INPUT:      │
    │ • userId    │
    │ • roomId    │
    │ • rating    │
    │ • title     │
    │ • text      │
    │ • images[]  │
    └─────────────┘
        ↓
    ┌─────────────┐
    │ Check user  │
    │ has booked  │
    │ this room   │
    └─────────────┘
        ↓
    ┌─────────────┐
    │ Query DB:   │
    │ bookings    │
    │ WHERE       │
    │ user=userId │
    │ AND room=   │
    │ roomId AND  │
    │ status=     │
    │ 'completed' │
    └─────────────┘
        ↓
        ◇ Has booking?
       / \
      /   \
     No   Yes
     ↓     ↓
┌────────────┐ │
│ RETURN     │ │
│ "Must book │ │
│  first"    │ │
└────────────┘ │
     ↓         ↓
     │         ◇ rating valid?
     │         (1-5)
     │        / \
     │       /   \
     │      No   Yes
     │      ↓     ↓
┌────────────┐    │
│ RETURN     │    │
│ "Invalid   │    │
│  rating"   │    │
└────────────┘    │
     │            ↓
     │            ◇ Has text?
     │           / \
     │          /   \
     │         No   Yes
     │         ↓     ↓
┌────────────┐       │
│ RETURN     │       │
│ "Text      │       │
│  required" │       │
└────────────┘       │
     │               ↓
     │               ◇ Has images?
     │              / \
     │             /   \
     │            No   Yes
     │            ↓     ↓
     │           Skip ┌─────────────┐
     │                │ Validate    │
     │                │ images:     │
     │                │ • count ≤ 5 │
     │                │ • size OK   │
     │                │ • type OK   │
     │                └─────────────┘
     │                    ↓
     │                    ◇ Valid?
     │                   / \
     │                  /   \
     │                 No   Yes
     │                 ↓     ↓
┌────────────┐             Skip
│ RETURN     │
│ "Invalid   │
│  images"   │
└────────────┘
     │         ↓     ↓
     │         └──┬──┘
     │            ↓
     │        ┌─────────────┐
     │        │ Upload      │
     │        │ images to   │
     │        │ server      │
     │        └─────────────┘
     │            ↓
     │            └──┬──┘
     │               ↓
     │           ┌─────────────┐
     │           │ Insert      │
     │           │ review to   │
     │           │ DB:         │
     │           │ • roomId    │
     │           │ • userId    │
     │           │ • rating    │
     │           │ • title     │
     │           │ • text      │
     │           │ • images    │
     │           │ • status=   │
     │           │   'pending' │
     │           └─────────────┘
     │               ↓
     │           ┌─────────────┐
     │           │ Update room │
     │           │ avg rating  │
     │           └─────────────┘
     │               ↓
     │           ┌─────────────┐
     │           │ RETURN      │
     │           │ Success,    │
     │           │ reviewId    │
     │           └─────────────┘
     ↓               ↓
     └───────┬───────┘
             ↓
             ⬭ END
```

**Validations:**
1. User has completed booking
2. Rating 1-5
3. Text required
4. Images optional (max 5, valid types)
5. Insert with status='pending'

---

## ✅ CHECKLIST VẼ FLOWCHARTS

- [ ] Start/End ovals (⬭)
- [ ] Process rectangles rõ ràng
- [ ] Decision diamonds với Yes/No branches
- [ ] Input/Output parallelograms
- [ ] Arrows có hướng flow
- [ ] Variables được khai báo
- [ ] Logic đầy đủ và chính xác
- [ ] Loop có END condition
- [ ] No infinite loops
- [ ] All paths lead to END

---

## 🎨 MÀU SẮC FLOWCHARTS

```css
/* Shapes */
Start/End: #C8E6C9 (Light Green)
Process: #BBDEFB (Light Blue)
Decision: #FFF9C4 (Light Yellow)
Input/Output: #E1BEE7 (Light Purple)
Error/Return: #FFCDD2 (Light Red)

/* Lines */
Flow arrows: #424242 (Dark Gray), 2pt
Yes branch: #388E3C (Green), 1.5pt
No branch: #D32F2F (Red), 1.5pt

/* Text */
Labels: 10pt, Black
Variables: 9pt, Italic
```

---

## ⏱️ THỜI GIAN ƯỚC TÍNH

| Flowchart | Complexity | Decisions | Loops | Thời gian |
|-----------|------------|-----------|-------|-----------|
| FC-01: Price Calculation | High | 3 | 1 | 1.5-2 giờ |
| FC-02: Availability Check | High | 2 | 1 | 1.5 giờ |
| FC-03: Booking Validation | Medium | 8 | 0 | 1-1.5 giờ |
| FC-04: Coupon Validation | Medium | 5 | 0 | 1-1.5 giờ |
| FC-05: Inventory Mgmt | Medium | 2 | 2 | 1 giờ |
| FC-06: Date Blocking | Medium | 3 | 1 | 1 giờ |
| FC-07: Email Notification | Medium | 3 | 0 | 45-60 phút |
| FC-08: PDF Generation | Medium | 0 | 1 | 1 giờ |
| FC-09: Search Algorithm | High | 4 | 1 | 1.5 giờ |
| FC-10: Review Submission | Medium | 5 | 0 | 1 giờ |

**TỔNG:** 11-14 giờ cho 10 Flowcharts

---

## 💡 BEST PRACTICES

1. **One entry, one exit:** Mọi flowchart có 1 START và 1 END
2. **Clear decisions:** Decision diamonds có Yes/No rõ ràng
3. **No ambiguity:** Mọi condition phải explicit
4. **Show all paths:** Bao gồm cả error paths
5. **Use loops correctly:** FOR/WHILE có điều kiện kết thúc
6. **Variables named:** Khai báo và dùng variables consistent
7. **Comments when complex:** Thêm notes cho logic phức tạp

---

**HOÀN THÀNH TẤT CẢ 10 FLOWCHARTS! 🎉**

**File này được tạo bởi Claude AI - Ngày: 26/05/2026**
