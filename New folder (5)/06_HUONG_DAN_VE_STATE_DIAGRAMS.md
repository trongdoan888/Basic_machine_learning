# 📐 HƯỚNG DẪN VẼ STATE DIAGRAMS - HỆ THỐNG HOTEL BOOKING

**Dự án:** Quan Trọng Hotel (Parkside Sunline Hotel)  
**Loại sơ đồ:** State Diagrams (UML State Machine Diagrams)  
**Số lượng diagrams:** 5 State Diagrams chính  
**Công cụ đề xuất:** Visual Paradigm, StarUML, Draw.io, Lucidchart

---

## 🎯 MỤC TIÊU

Vẽ State Diagrams để hiển thị:
- **States (Trạng thái):** Các trạng thái khác nhau của objects
- **Transitions (Chuyển trạng thái):** Events/Actions gây ra chuyển đổi
- **Initial State:** Trạng thái ban đầu (●)
- **Final State:** Trạng thái kết thúc (◎)
- **Guard Conditions:** Điều kiện để chuyển trạng thái [condition]
- **Actions:** Hành động khi transition (do / entry / exit)

---

## 📏 CẤU TRÚC MỘT STATE DIAGRAM

### **Các thành phần cơ bản:**

```
    ●  ← Initial State (filled circle)
    ↓
┌─────────────────┐
│  State Name     │  ← State (rounded rectangle)
├─────────────────┤
│ entry / action1 │  ← Entry action (optional)
│ do / action2    │  ← Do action (optional)
│ exit / action3  │  ← Exit action (optional)
└─────────────────┘
    ↓ event [guard] / action  ← Transition
┌─────────────────┐
│  Next State     │
└─────────────────┘
    ↓
    ◎  ← Final State (bull's eye)
```

### **Ký hiệu:**
- **●** : Initial state (solid circle, 0.5cm diameter)
- **◎** : Final state (bull's eye, 0.8cm diameter)
- **→** : Transition (arrow)
- **[condition]** : Guard condition
- **event** : Trigger event
- **/ action** : Action to perform

---

## 📦 DANH SÁCH 5 STATE DIAGRAMS CHÍNH

1. **Booking State Diagram** - Quan trọng nhất (UC-10, UC-11, UC-21)
2. **Payment State Diagram** - Luồng thanh toán
3. **Review State Diagram** - Quy trình đánh giá (UC-17)
4. **Room State Diagram** - Trạng thái phòng (UC-22, UC-23)
5. **Order State Diagram** - WooCommerce order states

---

# STATE DIAGRAM 1: BOOKING STATE DIAGRAM 🏨

**Đây là sơ đồ QUAN TRỌNG NHẤT của hệ thống!**

## 🎯 Mục đích

Mô tả vòng đời của một Booking từ khi tạo đến khi hoàn tất hoặc hủy.

---

## 📊 CÁC TRẠNG THÁI (8 states)

### **1. [Initial State]** ●
- Solid circle, đường kính 0.5cm
- Màu đen (#000000)
- Không có label

---

### **2. Pending (Chờ xử lý)**

**Hình dạng:** Rounded rectangle  
**Kích thước:** 6cm x 3cm  
**Màu nền:** #FFF9C4 (Light Yellow)  
**Viền:** 2pt, #F57C00 (Orange)

```
┌────────────────────────────────┐
│         Pending                │
│      (Chờ xử lý)              │
├────────────────────────────────┤
│ entry / createBookingRecord()  │
│ entry / reserveInventory()     │
│ entry / generateOrderNumber()  │
│                                │
│ do / waitingForConfirmation()  │
└────────────────────────────────┘
```

**Mô tả:** 
- Booking vừa được tạo
- Chờ admin xác nhận hoặc khách thanh toán
- Inventory đã được reserve tạm thời

**Metadata (wp_postmeta):**
```
hb_booking_status = 'hb-pending'
hb_payment_status = 'pending'
```

---

### **3. Processing (Đang xử lý)**

**Kích thước:** 6cm x 3.5cm  
**Màu nền:** #BBDEFB (Light Blue)  
**Viền:** 2pt, #1976D2 (Blue)

```
┌────────────────────────────────┐
│       Processing               │
│     (Đang xử lý)              │
├────────────────────────────────┤
│ entry / notifyAdmin()          │
│ entry / sendConfirmationEmail()│
│                                │
│ do / verifyPayment()           │
│ do / checkAvailability()       │
└────────────────────────────────┘
```

**Mô tả:**
- Admin đang xem xét booking
- Hoặc đang verify payment information
- Chờ xác nhận cuối cùng

**Metadata:**
```
hb_booking_status = 'hb-processing'
hb_payment_status = 'pending' hoặc 'processing'
```

---

### **4. Confirmed (Đã xác nhận)**

**Kích thước:** 6cm x 4cm  
**Màu nền:** #C8E6C9 (Light Green)  
**Viền:** 2pt, #388E3C (Green)

```
┌────────────────────────────────┐
│        Confirmed               │
│      (Đã xác nhận)            │
├────────────────────────────────┤
│ entry / lockInventory()        │
│ entry / sendConfirmationEmail()│
│ entry / generateInvoice()      │
│ entry / updateRoomCalendar()   │
│                                │
│ do / waitingForCheckIn()       │
└────────────────────────────────┘
```

**Mô tả:**
- Booking đã được xác nhận
- Phòng đã được lock chắc chắn
- Invoice đã được tạo
- Chờ khách check-in

**Metadata:**
```
hb_booking_status = 'hb-confirmed'
hb_payment_status = 'paid' (nếu đã thanh toán) hoặc 'pending'
```

---

### **5. Checked-In (Đã nhận phòng)**

**Kích thước:** 6cm x 3cm  
**Màu nền:** #B2DFDB (Teal)  
**Viền:** 2pt, #00796B (Teal Dark)

```
┌────────────────────────────────┐
│       Checked-In               │
│     (Đã nhận phòng)           │
├────────────────────────────────┤
│ entry / recordCheckInTime()    │
│ entry / notifyHousekeeping()   │
│                                │
│ do / guestStaying()            │
└────────────────────────────────┘
```

**Mô tả:**
- Khách đã check-in
- Đang ở trong phòng
- Chờ check-out

**Metadata:**
```
hb_booking_status = 'hb-checked-in'
hb_check_in_actual_time = '2026-05-26 14:00:00'
```

---

### **6. Checked-Out (Đã trả phòng)**

**Kích thước:** 6cm x 3cm  
**Màu nền:** #D1C4E9 (Purple Light)  
**Viền:** 2pt, #7E57C2 (Purple)

```
┌────────────────────────────────┐
│      Checked-Out               │
│     (Đã trả phòng)            │
├────────────────────────────────┤
│ entry / recordCheckOutTime()   │
│ entry / releaseRoom()          │
│ entry / requestReview()        │
│                                │
│ do / finalizeCharges()         │
└────────────────────────────────┘
```

**Mô tả:**
- Khách đã check-out
- Phòng được release
- Email yêu cầu review được gửi
- Chờ hoàn tất thanh toán (nếu chưa)

**Metadata:**
```
hb_booking_status = 'hb-checked-out'
hb_check_out_actual_time = '2026-05-28 12:00:00'
```

---

### **7. Completed (Hoàn tất)**

**Kích thước:** 6cm x 3.5cm  
**Màu nền:** #A5D6A7 (Green Light)  
**Viền:** 3pt, #2E7D32 (Dark Green)

```
┌────────────────────────────────┐
│       Completed                │
│       (Hoàn tất)              │
├────────────────────────────────┤
│ entry / markAsComplete()       │
│ entry / updateStatistics()     │
│ entry / archiveBooking()       │
│                                │
│ do / allowReview()             │
└────────────────────────────────┘
```

**Mô tả:**
- Booking hoàn tất hoàn toàn
- Thanh toán đã xong
- Khách có thể viết review
- Trạng thái cuối cùng (không thể thay đổi)

**Metadata:**
```
hb_booking_status = 'hb-completed'
hb_payment_status = 'paid'
completed_date = '2026-05-28 12:30:00'
```

---

### **8. Cancelled (Đã hủy)**

**Kích thước:** 6cm x 4cm  
**Màu nền:** #FFCDD2 (Red Light)  
**Viền:** 2pt, #D32F2F (Red)

```
┌────────────────────────────────┐
│       Cancelled                │
│        (Đã hủy)               │
├────────────────────────────────┤
│ entry / releaseInventory()     │
│ entry / sendCancellationEmail()│
│ entry / processRefund()        │
│ entry / updateCalendar()       │
│                                │
│ do / calculateCancellationFee()│
└────────────────────────────────┘
```

**Mô tả:**
- Booking đã bị hủy (bởi khách hoặc admin)
- Inventory được release
- Refund được xử lý (nếu có)

**Metadata:**
```
hb_booking_status = 'hb-cancelled'
cancellation_date = '2026-05-25 10:00:00'
cancellation_reason = 'Customer request'
cancelled_by = 'admin' hoặc 'customer'
```

---

### **9. No-Show (Không đến)**

**Kích thước:** 6cm x 3cm  
**Màu nền:** #FFCCBC (Orange Light)  
**Viền:** 2pt, #E64A19 (Deep Orange)

```
┌────────────────────────────────┐
│        No-Show                 │
│      (Không đến)              │
├────────────────────────────────┤
│ entry / markAsNoShow()         │
│ entry / releaseRoom()          │
│ entry / chargeNoShowFee()      │
│                                │
│ do / notifyManagement()        │
└────────────────────────────────┘
```

**Mô tả:**
- Khách không đến check-in
- Sau 24h từ check-in time
- No-show fee có thể được áp dụng

**Metadata:**
```
hb_booking_status = 'hb-no-show'
no_show_recorded_at = '2026-05-27 15:00:00'
```

---

### **10. [Final State]** ◎
- Bull's eye circle
- Outer diameter: 0.8cm
- Inner dot: 0.4cm
- Màu đen (#000000)

---

## 🔗 TRANSITIONS (Các chuyển trạng thái)

### **Transition 1: Initial → Pending**
```
● ──────→ [Pending]
   "Create Booking"
   / createBooking()
```

**Event:** Create Booking (UC-10)  
**Action:** createBooking(), reserveInventory()  
**Trigger:** User submits checkout form

---

### **Transition 2: Pending → Processing**
```
[Pending] ──────→ [Processing]
   "Admin Reviews" / notifyAdmin()
```

**Event:** Admin clicks "Process" button  
**Guard:** [inventory available]  
**Action:** notifyAdmin(), sendConfirmationEmail()

---

### **Transition 3: Processing → Confirmed**
```
[Processing] ──────→ [Confirmed]
   "Admin Confirms"
   [payment verified] / lockInventory()
```

**Event:** Admin confirms booking (UC-21)  
**Guard:** [payment verified OR payment method = 'bank_transfer']  
**Action:** lockInventory(), generateInvoice(), sendConfirmationEmail()

---

### **Transition 4: Confirmed → Checked-In**
```
[Confirmed] ──────→ [Checked-In]
   "Guest Arrives"
   [check-in date reached] / recordCheckIn()
```

**Event:** Guest checks in at hotel  
**Guard:** [check-in date = today OR today >= check-in date]  
**Action:** recordCheckInTime(), notifyHousekeeping()

---

### **Transition 5: Checked-In → Checked-Out**
```
[Checked-In] ──────→ [Checked-Out]
   "Guest Leaves"
   [check-out time reached] / recordCheckOut()
```

**Event:** Guest checks out  
**Guard:** [check-out date >= today]  
**Action:** recordCheckOutTime(), releaseRoom(), requestReview()

---

### **Transition 6: Checked-Out → Completed**
```
[Checked-Out] ──────→ [Completed]
   "Finalize Payment"
   [payment completed] / markComplete()
```

**Event:** Final payment confirmed  
**Guard:** [payment_status = 'paid']  
**Action:** markAsComplete(), updateStatistics(), archiveBooking()

---

### **Transition 7: Completed → [Final State]**
```
[Completed] ──────→ ◎
   "Archive"
```

**Event:** Booking archived  
**Action:** None

---

### **Transition 8: Pending → Cancelled**
```
[Pending] ──────→ [Cancelled]
   "Cancel Request"
   [cancellation allowed] / processRefund()
```

**Event:** Customer or Admin cancels  
**Guard:** [cancellation policy allows]  
**Action:** releaseInventory(), sendCancellationEmail(), processRefund()

---

### **Transition 9: Processing → Cancelled**
```
[Processing] ──────→ [Cancelled]
   "Admin Rejects"
   [reason provided] / notifyCustomer()
```

**Event:** Admin rejects booking  
**Guard:** [reason != empty]  
**Action:** releaseInventory(), sendCancellationEmail()

---

### **Transition 10: Confirmed → Cancelled**
```
[Confirmed] ──────→ [Cancelled]
   "Cancel Booking"
   [before check-in] / calculateFee()
```

**Event:** Cancellation before check-in  
**Guard:** [today < check-in date]  
**Action:** releaseInventory(), calculateCancellationFee(), processRefund()

---

### **Transition 11: Confirmed → No-Show**
```
[Confirmed] ──────→ [No-Show]
   "No Check-In"
   [24h after check-in time] / chargeNoShowFee()
```

**Event:** Automatic after 24h past check-in  
**Guard:** [now > check-in time + 24h]  
**Action:** markAsNoShow(), releaseRoom(), chargeNoShowFee()

---

### **Transition 12: Cancelled → [Final State]**
```
[Cancelled] ──────→ ◎
   "Archive"
```

---

### **Transition 13: No-Show → [Final State]**
```
[No-Show] ──────→ ◎
   "Archive"
```

---

## 📐 LAYOUT BOOKING STATE DIAGRAM

**Khổ giấy:** A4 Landscape (30cm x 21cm)

```
    ● Initial (1cm, 3cm)
    ↓
┌─────────┐ (4cm, 5cm)
│ Pending │
└─────────┘
    ↓           ↓ (cancel)
┌───────────┐   ┌───────────┐
│Processing │   │ Cancelled │ (22cm, 10cm)
└───────────┘   └───────────┘
(4cm, 10cm)          ↓
    ↓                ◎ (24cm, 16cm)
┌───────────┐
│ Confirmed │
└───────────┘
(4cm, 15cm)
    ↓           ↓ (no-show)
┌──────────┐    ┌─────────┐
│Checked-In│    │ No-Show │ (22cm, 15cm)
└──────────┘    └─────────┘
(10cm, 15cm)         ↓
    ↓                ◎
┌───────────┐
│Checked-Out│
└───────────┘
(16cm, 15cm)
    ↓
┌───────────┐
│ Completed │
└───────────┘
(22cm, 5cm)
    ↓
    ◎ (24cm, 3cm)
```

**Main flow (left to right):**
- Initial → Pending → Processing → Confirmed → Checked-In → Checked-Out → Completed → Final

**Alternative flows:**
- Pending/Processing/Confirmed → Cancelled → Final
- Confirmed → No-Show → Final

---

## 🎨 MÀU SẮC CHO BOOKING STATE DIAGRAM

```css
/* States */
Pending: #FFF9C4 (Yellow Light)
Processing: #BBDEFB (Blue Light)
Confirmed: #C8E6C9 (Green Light)
Checked-In: #B2DFDB (Teal Light)
Checked-Out: #D1C4E9 (Purple Light)
Completed: #A5D6A7 (Green)
Cancelled: #FFCDD2 (Red Light)
No-Show: #FFCCBC (Orange Light)

/* Transitions */
Normal flow: #424242 (Dark Gray), 2pt solid
Cancel flow: #D32F2F (Red), 2pt dashed
System trigger: #1976D2 (Blue), 2pt solid
```

---

# STATE DIAGRAM 2: PAYMENT STATE DIAGRAM 💳

## 🎯 Mục đích

Mô tả các trạng thái của Payment từ khi tạo đến khi hoàn tất.

---

## 📊 CÁC TRẠNG THÁI (5 states)

### **1. [Initial State]** ●

---

### **2. Unpaid (Chưa thanh toán)**

```
┌────────────────────────────────┐
│          Unpaid                │
│     (Chưa thanh toán)         │
├────────────────────────────────┤
│ entry / createPaymentRecord()  │
│ entry / setPaymentMethod()     │
│                                │
│ do / waitingForPayment()       │
└────────────────────────────────┘
```

**Màu:** #FFF9C4 (Yellow)  
**Metadata:** `hb_payment_status = 'pending'`

---

### **3. Processing (Đang xử lý)**

```
┌────────────────────────────────┐
│       Processing               │
│      (Đang xử lý)             │
├────────────────────────────────┤
│ entry / verifyPaymentInfo()    │
│                                │
│ do / checkBankTransfer()       │
└────────────────────────────────┘
```

**Màu:** #BBDEFB (Blue)  
**Metadata:** `hb_payment_status = 'processing'`

---

### **4. Paid (Đã thanh toán)**

```
┌────────────────────────────────┐
│          Paid                  │
│      (Đã thanh toán)          │
├────────────────────────────────┤
│ entry / recordPaymentDate()    │
│ entry / sendReceipt()          │
│ entry / updateBookingStatus()  │
└────────────────────────────────┘
```

**Màu:** #C8E6C9 (Green)  
**Metadata:** `hb_payment_status = 'paid'`  
**Actions:** Update booking status to 'confirmed'

---

### **5. Failed (Thất bại)**

```
┌────────────────────────────────┐
│         Failed                 │
│       (Thất bại)              │
├────────────────────────────────┤
│ entry / notifyCustomer()       │
│ entry / logFailureReason()     │
│                                │
│ do / allowRetry()              │
└────────────────────────────────┘
```

**Màu:** #FFCDD2 (Red)  
**Metadata:** `hb_payment_status = 'failed'`

---

### **6. Refunded (Đã hoàn tiền)**

```
┌────────────────────────────────┐
│       Refunded                 │
│     (Đã hoàn tiền)            │
├────────────────────────────────┤
│ entry / processRefund()        │
│ entry / sendRefundNotice()     │
│ entry / updateBooking()        │
└────────────────────────────────┘
```

**Màu:** #FFE082 (Orange)  
**Metadata:** `hb_payment_status = 'refunded'`

---

### **7. [Final State]** ◎

---

## 🔗 TRANSITIONS

```
● → [Unpaid]
   "Create Payment"

[Unpaid] → [Processing]
   "Submit Payment Info"
   [bank transfer selected]

[Processing] → [Paid]
   "Payment Verified"
   [admin confirms] / sendReceipt()

[Processing] → [Failed]
   "Verification Failed"
   [invalid info]

[Failed] → [Unpaid]
   "Retry Payment"
   [retry allowed]

[Paid] → [Refunded]
   "Process Refund"
   [booking cancelled]

[Paid] → ◎
   "Complete"

[Refunded] → ◎
   "Archive"
```

---

# STATE DIAGRAM 3: REVIEW STATE DIAGRAM ⭐

## 🎯 Mục đích

Mô tả quy trình đánh giá phòng từ khi viết đến khi được approve (UC-17).

---

## 📊 CÁC TRẠNG THÁI (4 states)

### **1. [Initial State]** ●

---

### **2. Draft (Nháp)**

```
┌────────────────────────────────┐
│          Draft                 │
│          (Nháp)               │
├────────────────────────────────┤
│ entry / createReviewDraft()    │
│                                │
│ do / allowEditing()            │
└────────────────────────────────┘
```

**Màu:** #FFF9C4 (Yellow)  
**Metadata:** `comment_approved = '0'`  
**Mô tả:** Review đang được viết, chưa submit

---

### **3. Pending (Chờ duyệt)**

```
┌────────────────────────────────┐
│        Pending                 │
│      (Chờ duyệt)              │
├────────────────────────────────┤
│ entry / submitReview()         │
│ entry / notifyAdmin()          │
│                                │
│ do / waitingForApproval()      │
└────────────────────────────────┘
```

**Màu:** #BBDEFB (Blue)  
**Metadata:** `comment_approved = '0'` + `review_submitted = true`  
**Mô tả:** Review đã submit, chờ admin duyệt

---

### **4. Approved (Đã duyệt)**

```
┌────────────────────────────────┐
│        Approved                │
│       (Đã duyệt)              │
├────────────────────────────────┤
│ entry / publishReview()        │
│ entry / updateRoomRating()     │
│ entry / notifyAuthor()         │
│                                │
│ do / displayPublicly()         │
└────────────────────────────────┘
```

**Màu:** #C8E6C9 (Green)  
**Metadata:** `comment_approved = '1'`  
**Mô tả:** Review được approve, hiển thị public

---

### **5. Rejected (Bị từ chối)**

```
┌────────────────────────────────┐
│       Rejected                 │
│     (Bị từ chối)              │
├────────────────────────────────┤
│ entry / rejectReview()         │
│ entry / notifyAuthorWithReason()│
│                                │
│ do / allowResubmit()           │
└────────────────────────────────┘
```

**Màu:** #FFCDD2 (Red)  
**Metadata:** `comment_approved = 'spam'` hoặc `'trash'`  
**Mô tả:** Review không phù hợp, bị reject

---

### **6. [Final State]** ◎

---

## 🔗 TRANSITIONS

```
● → [Draft]
   "Start Writing Review"

[Draft] → [Pending]
   "Submit Review"
   [all fields filled]

[Pending] → [Approved]
   "Admin Approves"
   [content appropriate] / updateRating()

[Pending] → [Rejected]
   "Admin Rejects"
   [inappropriate content]

[Rejected] → [Draft]
   "Edit & Resubmit"
   [user edits]

[Approved] → ◎
   "Published"
```

---

# STATE DIAGRAM 4: ROOM STATE DIAGRAM 🛏️

## 🎯 Mục đích

Mô tả trạng thái sẵn sàng của phòng (UC-22, UC-23).

---

## 📊 CÁC TRẠNG THÁI (5 states)

### **1. [Initial State]** ●

---

### **2. Available (Sẵn sàng)**

```
┌────────────────────────────────┐
│       Available                │
│      (Sẵn sàng)               │
├────────────────────────────────┤
│ entry / markAsAvailable()      │
│ entry / updateInventory()      │
│                                │
│ do / acceptBookings()          │
└────────────────────────────────┘
```

**Màu:** #C8E6C9 (Green)  
**Metadata:** `hb_room_status = 'publish'`  
**Mô tả:** Phòng sẵn sàng cho booking

---

### **3. Reserved (Đã đặt)**

```
┌────────────────────────────────┐
│       Reserved                 │
│       (Đã đặt)                │
├────────────────────────────────┤
│ entry / decrementInventory()   │
│ entry / blockDates()           │
│                                │
│ do / waitingForCheckIn()       │
└────────────────────────────────┘
```

**Màu:** #FFF9C4 (Yellow)  
**Mô tả:** Phòng đã có booking, chờ check-in

---

### **4. Occupied (Đang sử dụng)**

```
┌────────────────────────────────┐
│       Occupied                 │
│    (Đang sử dụng)             │
├────────────────────────────────┤
│ entry / assignGuest()          │
│ entry / markAsOccupied()       │
│                                │
│ do / monitorUsage()            │
└────────────────────────────────┘
```

**Màu:** #BBDEFB (Blue)  
**Mô tả:** Khách đang ở

---

### **5. Cleaning (Đang dọn dẹp)**

```
┌────────────────────────────────┐
│        Cleaning                │
│     (Đang dọn dẹp)            │
├────────────────────────────────┤
│ entry / notifyHousekeeping()   │
│                                │
│ do / cleanRoom()               │
└────────────────────────────────┘
```

**Màu:** #FFE082 (Orange)  
**Mô tả:** Sau check-out, đang dọn dẹp

---

### **6. Maintenance (Bảo trì)**

```
┌────────────────────────────────┐
│      Maintenance               │
│       (Bảo trì)               │
├────────────────────────────────┤
│ entry / blockAllDates()        │
│ entry / notifyMaintenance()    │
│                                │
│ do / performMaintenance()      │
└────────────────────────────────┘
```

**Màu:** #FFCDD2 (Red)  
**Metadata:** `hb_room_status = 'draft'` hoặc blocked  
**Mô tả:** Phòng đang sửa chữa, không available

---

### **7. Blocked (Bị khóa)**

```
┌────────────────────────────────┐
│         Blocked                │
│        (Bị khóa)              │
├────────────────────────────────┤
│ entry / blockSpecificDates()   │
│ entry / setBlockReason()       │
│                                │
│ do / preventBooking()          │
└────────────────────────────────┘
```

**Màu:** #B0BEC5 (Gray)  
**Metadata:** Availability table with `is_blocked = 1`  
**Mô tả:** Admin khóa ngày cụ thể (UC-24)

---

### **8. [Final State]** ◎

---

## 🔗 TRANSITIONS

```
● → [Available]
   "Create Room"

[Available] → [Reserved]
   "Booking Confirmed"
   [inventory > 0]

[Reserved] → [Occupied]
   "Guest Checks In"

[Occupied] → [Cleaning]
   "Guest Checks Out"

[Cleaning] → [Available]
   "Cleaning Complete"
   [room inspected]

[Available] → [Blocked]
   "Admin Blocks Dates"

[Blocked] → [Available]
   "Unblock Dates"

[Available] → [Maintenance]
   "Maintenance Required"
   [issue reported]

[Maintenance] → [Available]
   "Maintenance Complete"
   [inspection passed]

[Reserved] → [Available]
   "Booking Cancelled"
   / incrementInventory()
```

---

# STATE DIAGRAM 5: ORDER STATE DIAGRAM (WooCommerce) 🛒

## 🎯 Mục đích

Mô tả trạng thái đơn hàng WooCommerce (tích hợp với Booking).

---

## 📊 CÁC TRẠNG THÁI (6 states)

### **1. [Initial State]** ●

---

### **2. Pending Payment (Chờ thanh toán)**

```
┌────────────────────────────────┐
│    Pending Payment             │
│    (Chờ thanh toán)           │
├────────────────────────────────┤
│ entry / createOrder()          │
│ entry / sendOrderEmail()       │
│                                │
│ do / waitingForPayment()       │
└────────────────────────────────┘
```

**Màu:** #FFF9C4 (Yellow)  
**WooCommerce status:** `pending`

---

### **3. On Hold (Tạm giữ)**

```
┌────────────────────────────────┐
│        On Hold                 │
│       (Tạm giữ)               │
├────────────────────────────────┤
│ entry / markAsOnHold()         │
│                                │
│ do / awaitingConfirmation()    │
└────────────────────────────────┘
```

**Màu:** #FFE082 (Orange)  
**WooCommerce status:** `on-hold`

---

### **4. Processing (Đang xử lý)**

```
┌────────────────────────────────┐
│       Processing               │
│      (Đang xử lý)             │
├────────────────────────────────┤
│ entry / processOrder()         │
│ entry / notifyHotel()          │
└────────────────────────────────┘
```

**Màu:** #BBDEFB (Blue)  
**WooCommerce status:** `processing`

---

### **5. Completed (Hoàn thành)**

```
┌────────────────────────────────┐
│       Completed                │
│      (Hoàn thành)             │
├────────────────────────────────┤
│ entry / markComplete()         │
│ entry / sendCompletionEmail()  │
└────────────────────────────────┘
```

**Màu:** #C8E6C9 (Green)  
**WooCommerce status:** `completed`

---

### **6. Cancelled (Đã hủy)**

```
┌────────────────────────────────┐
│       Cancelled                │
│        (Đã hủy)               │
├────────────────────────────────┤
│ entry / cancelOrder()          │
│ entry / restoreInventory()     │
│ entry / processRefund()        │
└────────────────────────────────┘
```

**Màu:** #FFCDD2 (Red)  
**WooCommerce status:** `cancelled`

---

### **7. Refunded (Đã hoàn tiền)**

```
┌────────────────────────────────┐
│       Refunded                 │
│     (Đã hoàn tiền)            │
├────────────────────────────────┤
│ entry / processRefund()        │
│ entry / sendRefundEmail()      │
└────────────────────────────────┘
```

**Màu:** #D1C4E9 (Purple)  
**WooCommerce status:** `refunded`

---

### **8. [Final State]** ◎

---

## 🔗 TRANSITIONS

```
● → [Pending Payment]
   "Create Order"

[Pending Payment] → [On Hold]
   "Bank Transfer Selected"

[On Hold] → [Processing]
   "Payment Received"

[Pending Payment] → [Processing]
   "Payment Confirmed"

[Processing] → [Completed]
   "Order Fulfilled"

[Pending Payment] → [Cancelled]
   "Cancel Before Payment"

[On Hold] → [Cancelled]
   "Cancel During Hold"

[Processing] → [Cancelled]
   "Cancel Order"

[Completed] → [Refunded]
   "Process Refund"

[Completed] → ◎

[Cancelled] → ◎

[Refunded] → ◎
```

---

## ✅ CHECKLIST VẼ STATE DIAGRAMS

### **Cho mỗi State Diagram:**

- [ ] Initial state (●) được vẽ ở góc trên trái
- [ ] Final state (◎) được vẽ ở cuối
- [ ] Tất cả states có rounded rectangles
- [ ] Mỗi state có entry/do/exit actions (nếu có)
- [ ] Màu sắc consistent với loại state
- [ ] Tất cả transitions có arrows
- [ ] Mỗi transition có label (event [guard] / action)
- [ ] Guard conditions trong [] nếu có
- [ ] Actions sau / nếu có
- [ ] Layout rõ ràng, không overlap
- [ ] Legend giải thích màu sắc

---

## 🎨 MÀU SẮC CHUNG CHO TẤT CẢ STATE DIAGRAMS

```css
/* State Colors by Type */
Initial state (active): #C8E6C9 (Green Light)
In-progress states: #BBDEFB (Blue Light)
Waiting states: #FFF9C4 (Yellow Light)
Completed states: #A5D6A7 (Green)
Error/Failed states: #FFCDD2 (Red Light)
Cancelled states: #FFCDD2 (Red Light)
Maintenance states: #FFE082 (Orange Light)

/* Transition Colors */
Normal flow: #424242 (Dark Gray), 2pt solid
Cancel/Error flow: #D32F2F (Red), 2pt dashed
System trigger: #1976D2 (Blue), 2pt solid
User action: #388E3C (Green), 2pt solid
```

---

## 📝 MẪU TEXT MÔ TẢ (Cho báo cáo)

> **Hình X.X: Booking State Diagram**
>
> State Diagram mô tả vòng đời của một Booking từ khi tạo đến khi hoàn tất. Booking có thể trải qua 8 trạng thái chính:
>
> 1. **Pending:** Booking vừa tạo, chờ xác nhận
> 2. **Processing:** Admin đang xem xét
> 3. **Confirmed:** Đã xác nhận, chờ check-in
> 4. **Checked-In:** Khách đã nhận phòng
> 5. **Checked-Out:** Khách đã trả phòng
> 6. **Completed:** Hoàn tất toàn bộ
> 7. **Cancelled:** Đã hủy
> 8. **No-Show:** Khách không đến
>
> Transitions chính bao gồm: Create Booking → Pending → Processing → Confirmed → Checked-In → Checked-Out → Completed. Các luồng phụ có thể dẫn đến Cancelled (bất cứ lúc nào trước check-in) hoặc No-Show (nếu khách không đến sau 24h).

---

## ⏱️ THỜI GIAN ƯỚC TÍNH

| State Diagram | Số states | Transitions | Thời gian |
|---------------|-----------|-------------|-----------|
| Booking | 9 states | 13 transitions | 1.5-2 giờ |
| Payment | 6 states | 8 transitions | 45-60 phút |
| Review | 5 states | 6 transitions | 30-45 phút |
| Room | 7 states | 10 transitions | 1-1.5 giờ |
| Order | 7 states | 9 transitions | 45-60 phút |

**TỔNG:** 5-6.5 giờ cho tất cả 5 State Diagrams

---

## 💡 BEST PRACTICES

1. **States nên là nouns (danh từ):** "Pending", "Confirmed", không phải "Waiting", "Confirming"
2. **Transitions nên có events rõ ràng:** "Admin Confirms" thay vì chỉ arrow
3. **Guard conditions trong []:** `[payment verified]`
4. **Actions sau /:** `/ sendEmail()`
5. **Màu sắc consistent:** Cùng loại state cùng màu
6. **Layout top-to-bottom hoặc left-to-right:** Dễ follow
7. **Tránh crossing arrows:** Dùng điểm uốn nếu cần

---

**HOÀN THÀNH! 🎉**

**File này được tạo bởi Claude AI - Ngày: 26/05/2026**
