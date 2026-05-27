# 📐 HƯỚNG DẪN VẼ SEQUENCE DIAGRAMS - 10 UC QUAN TRỌNG

**Dự án:** Quan Trọng Hotel (Parkside Sunline Hotel)  
**Loại sơ đồ:** Sequence Diagrams (UML)  
**Số lượng diagrams:** 10 Sequence Diagrams cho UC quan trọng  
**Công cụ đề xuất:** Visual Paradigm, StarUML, Draw.io, PlantUML

---

## 🎯 MỤC TIÊU

Sequence Diagram mô tả:
- **Interaction** giữa các objects theo thời gian
- **Messages** (method calls) trao đổi giữa objects
- **Lifelines** (vòng đời) của objects
- **Activation boxes** (khi object đang xử lý)
- **Return messages** (nếu có)

---

## 🎨 CẤU TRÚC SEQUENCE DIAGRAM

### **Các thành phần:**

```
Actor    Object1    Object2   Object3
  |         |          |          |
  |─────────>|          |          |  ← Message
  |         |────────────>|         |
  |         |          |──────────>|
  |         |          |<──────────|  ← Return
  |         |<──────────|          |
  |<─────────|          |          |
  |         |          |          |
```

### **Ký hiệu:**
- **Actor/Object:** Box ở đầu
- **Lifeline:** Vertical dashed line (- - -)
- **Activation:** Narrow rectangle trên lifeline
- **Message:** Solid arrow (→)
- **Return:** Dashed arrow (⇢)
- **Self-call:** Arrow quay lại chính nó

---

## 📋 10 SEQUENCE DIAGRAMS CHI TIẾT

---

## SD-01: SEARCH ROOMS (UC-01) 🔍

**Actors/Objects:**
- Guest
- SearchForm (UI)
- SearchController
- RoomRepository
- Database

### **Sequence:**

```
Guest   SearchForm  SearchController  RoomRepository  Database
  |         |              |                 |            |
  |─enter dates──>|        |                 |            |
  |         |              |                 |            |
  |─enter guests─>|        |                 |            |
  |         |              |                 |            |
  |─click Search─>|        |                 |            |
  |         |──validate()──>|                |            |
  |         |              |                 |            |
  |         |<─────OK──────|                 |            |
  |         |              |                 |            |
  |         |      searchRooms(criteria)──────>|          |
  |         |              |                 |            |
  |         |              |        query(SQL)────────────>|
  |         |              |                 |            |
  |         |              |        <───results───────────|
  |         |              |                 |            |
  |         |              |<────roomList────|            |
  |         |              |                 |            |
  |         |      applyFilters(roomList)    |            |
  |         |              |                 |            |
  |         |<───displayRooms(filteredList)──|            |
  |         |              |                 |            |
  |<─show results─────────|                 |            |
  |         |              |                 |            |
```

**Messages:**
1. `enter dates`, `enter guests` - User input
2. `validate()` - Check dates valid
3. `searchRooms(criteria)` - Controller → Repository
4. `query(SQL)` - Repository → Database
5. `applyFilters()` - Filter by price, rating
6. `displayRooms()` - Show results to Guest

**Timing:** ~2 seconds total (0.5s UI, 1s DB query, 0.5s render)

---

## SD-02: VIEW ROOM DETAILS (UC-02) 🏨

**Actors/Objects:**
- Guest
- RoomPage (UI)
- RoomController
- Room (Entity)
- ReviewRepository
- Database

### **Sequence:**

```
Guest   RoomPage  RoomController  Room  ReviewRepository  Database
  |        |            |          |           |              |
  |─click room────>|    |          |           |              |
  |        |            |          |           |              |
  |        |──getRoomDetails(id)──>|           |              |
  |        |            |          |           |              |
  |        |            |    loadFromDB()──────────────────────>|
  |        |            |          |           |              |
  |        |            |    <────data─────────────────────────|
  |        |            |          |           |              |
  |        |<─────roomData────────|           |              |
  |        |            |          |           |              |
  |        |    getReviews(roomId)─────────────>|             |
  |        |            |          |           |              |
  |        |            |          |     query(SQL)───────────>|
  |        |            |          |           |              |
  |        |            |          |     <───reviews──────────|
  |        |            |          |           |              |
  |        |<─────reviews─────────────────────|              |
  |        |            |          |           |              |
  |<─display page──────|          |           |              |
  |  (gallery,         |          |           |              |
  |   details,         |          |           |              |
  |   reviews)         |          |           |              |
  |        |            |          |           |              |
```

**Messages:**
1. `getRoomDetails(id)` - Load room data
2. `loadFromDB()` - Room entity fetches from DB
3. `getReviews(roomId)` - Load reviews for room
4. `display page` - Render full page with all data

---

## SD-03: ADD TO CART (UC-03) 🛒

**Actors/Objects:**
- Guest
- BookingForm (UI)
- CartController
- Cart (WooCommerce)
- InventoryChecker
- Database

### **Sequence:**

```
Guest  BookingForm  CartController  Cart  InventoryChecker  Database
  |        |              |          |           |              |
  |─enter dates──>|       |          |           |              |
  |        |              |          |           |              |
  |─add extras─>|         |          |           |              |
  |        |              |          |           |              |
  |─click Add─>|          |          |           |              |
  |        |              |          |           |              |
  |        |──addToCart(data)────>  |           |              |
  |        |              |          |           |              |
  |        |        checkAvailability(room,dates)────>|         |
  |        |              |          |           |              |
  |        |              |          |     query(inventory)─────>|
  |        |              |          |           |              |
  |        |              |          |     <───available────────|
  |        |              |          |           |              |
  |        |        <───TRUE─────────────────────|              |
  |        |              |          |           |              |
  |        |              |    addItem(cartItem)>|              |
  |        |              |          |           |              |
  |        |              |    <───cartUpdated───|              |
  |        |              |          |           |              |
  |        |<─────success message───|           |              |
  |        |              |          |           |              |
  |<─show notification───|          |           |              |
  |  "Added to cart"     |          |           |              |
  |        |              |          |           |              |
```

**Messages:**
1. `addToCart(data)` - Room, dates, guests, extras
2. `checkAvailability()` - Verify room available for dates
3. `addItem()` - Add to WooCommerce cart
4. `success message` - Confirm added

**Alternative Flow:** If not available, return error instead

---

## SD-04: VIEW CART (UC-06) 🛍️

**Actors/Objects:**
- Guest
- CartPage (UI)
- CartController
- Cart (WooCommerce)
- PriceCalculator

### **Sequence:**

```
Guest   CartPage  CartController  Cart  PriceCalculator
  |        |            |          |           |
  |─click cart icon──>  |          |           |
  |        |            |          |           |
  |        |──getCartContents()──>|           |
  |        |            |          |           |
  |        |            |  <───items───────|   |
  |        |            |          |           |
  |        |    calculateTotals(items)─────────>|
  |        |            |          |           |
  |        |            |      calculate():    |
  |        |            |      • basePrice     |
  |        |            |      • extras        |
  |        |            |      • nights        |
  |        |            |      • subtotal      |
  |        |            |      • discount      |
  |        |            |      • total         |
  |        |            |          |           |
  |        |            |      <───totals──────|
  |        |            |          |           |
  |        |<─────renderCart(items,totals)────|
  |        |            |          |           |
  |<─display:          |          |           |
  |  • cart table      |          |           |
  |  • coupon input    |          |           |
  |  • totals          |          |           |
  |  • checkout button |          |           |
  |        |            |          |           |
```

**Messages:**
1. `getCartContents()` - Fetch all items
2. `calculateTotals()` - Sum up prices
3. `renderCart()` - Display table and totals

---

## SD-05: CHECKOUT & PAYMENT (UC-08, UC-09, UC-10) 💳

**Actors/Objects:**
- Guest
- CheckoutPage (UI)
- CheckoutController
- OrderManager
- BookingManager
- EmailService
- Database

### **Sequence:**

```
Guest  CheckoutPage  CheckoutController  OrderManager  BookingManager  EmailService  Database
  |         |                |                |              |              |           |
  |─enter info────>|         |                |              |              |           |
  |         |                |                |              |              |           |
  |─select payment>|         |                |              |              |           |
  |         |                |                |              |              |           |
  |─click Place Order───>    |                |              |              |           |
  |         |                |                |              |              |           |
  |         |────validate()──>|               |              |              |           |
  |         |                |                |              |              |           |
  |         |<─────OK────────|                |              |              |           |
  |         |                |                |              |              |           |
  |         |        createOrder(data)────────>|              |              |           |
  |         |                |                |              |              |           |
  |         |                |          insert(order)─────────────────────────────────>|
  |         |                |                |              |              |           |
  |         |                |          <───orderID──────────────────────────────────|
  |         |                |                |              |              |           |
  |         |                |<─────order─────|              |              |           |
  |         |                |                |              |              |           |
  |         |            createBooking(order)─────────────────>|             |           |
  |         |                |                |              |              |           |
  |         |                |                |        insert(booking)───────────────>|
  |         |                |                |              |              |           |
  |         |                |                |        <───bookingID────────────────|
  |         |                |                |              |              |           |
  |         |                |                |<───booking───|              |           |
  |         |                |                |              |              |           |
  |         |            sendConfirmationEmail(booking)──────────────────────>|         |
  |         |                |                |              |              |           |
  |         |                |                |              |        send(SMTP)───>   |
  |         |                |                |              |              |   External|
  |         |                |                |              |              |   SMTP    |
  |         |<─────redirect to confirmation page─────|        |              |           |
  |         |                |                |              |              |           |
  |<─show order received────|                |              |              |           |
  |  Order #1598            |                |              |              |           |
  |         |                |                |              |              |           |
```

**Messages:**
1. `validate()` - Check all required fields
2. `createOrder()` - Create WooCommerce order
3. `createBooking()` - Create hotel booking
4. `sendConfirmationEmail()` - Email with invoice
5. `redirect` - Navigate to confirmation page

**Key Points:**
- Order created BEFORE booking (WooCommerce flow)
- Email sent asynchronously
- Multiple database inserts in transaction

---

## SD-06: WRITE REVIEW (UC-17) ⭐

**Actors/Objects:**
- Guest
- ReviewForm (UI)
- ReviewController
- ReviewRepository
- Database

### **Sequence:**

```
Guest  ReviewForm  ReviewController  ReviewRepository  Database
  |        |              |                  |              |
  |─click Write Review──>|                  |              |
  |        |              |                  |              |
  |        |──checkEligibility(guest,room)──>|              |
  |        |              |                  |              |
  |        |              |       query(hasBooked)──────────>|
  |        |              |                  |              |
  |        |              |       <───TRUE────────────────|
  |        |              |                  |              |
  |        |<─────show form────────|         |              |
  |        |              |                  |              |
  |─enter rating──>|     |                  |              |
  |        |              |                  |              |
  |─enter title─>|        |                  |              |
  |        |              |                  |              |
  |─enter text──>|        |                  |              |
  |        |              |                  |              |
  |─upload images>|       |                  |              |
  |        |              |                  |              |
  |─click Submit────>     |                  |              |
  |        |              |                  |              |
  |        |──submitReview(data)──────────────>|            |
  |        |              |                  |              |
  |        |              |         insert(review)──────────>|
  |        |              |         status='pending'        |
  |        |              |                  |              |
  |        |              |         <───reviewID───────────|
  |        |              |                  |              |
  |        |              |<─────review──────|              |
  |        |              |                  |              |
  |        |<─────success message────────|   |              |
  |        |              |                  |              |
  |<─show notification───|                  |              |
  |  "Review submitted   |                  |              |
  |   for approval"      |                  |              |
  |        |              |                  |              |
```

**Messages:**
1. `checkEligibility()` - Verify guest has booked this room
2. `submitReview()` - Submit with rating, text, images
3. `insert(review)` - Save with status='pending'
4. `success message` - Awaiting admin approval

---

## SD-07: ADMIN MANAGE BOOKINGS (UC-21) 🔧

**Actors/Objects:**
- Admin
- AdminUI
- BookingManager
- BookingRepository
- EmailService
- Database

### **Sequence:**

```
Admin  AdminUI  BookingManager  BookingRepository  EmailService  Database
  |       |            |                |               |           |
  |─navigate to Bookings──>|            |               |           |
  |       |            |                |               |           |
  |       |──getBookings(filters)───────>|              |           |
  |       |            |                |               |           |
  |       |            |       query(bookings)──────────────────────>|
  |       |            |                |               |           |
  |       |            |       <───bookingList──────────────────────|
  |       |            |                |               |           |
  |       |            |<───bookings────|               |           |
  |       |            |                |               |           |
  |       |<─display table─────|        |               |           |
  |       |            |                |               |           |
  |─click Edit booking─────>   |        |               |           |
  |       |            |                |               |           |
  |       |──getBookingDetails(id)──────>|              |           |
  |       |            |                |               |           |
  |       |            |       query(booking)───────────────────────>|
  |       |            |                |               |           |
  |       |            |       <───booking──────────────────────────|
  |       |            |                |               |           |
  |       |            |<───booking─────|               |           |
  |       |            |                |               |           |
  |       |<─display edit form─|        |               |           |
  |       |            |                |               |           |
  |─change status──>   |                |               |           |
  |  (Pending→Confirmed)|                |              |           |
  |       |            |                |               |           |
  |─click Update────>  |                |               |           |
  |       |            |                |               |           |
  |       |──updateBooking(id,status)───>|              |           |
  |       |            |                |               |           |
  |       |            |       update(booking)──────────────────────>|
  |       |            |                |               |           |
  |       |            |       <───success──────────────────────────|
  |       |            |                |               |           |
  |       |            |<───updated─────|               |           |
  |       |            |                |               |           |
  |       |    sendStatusEmail(booking)──────────────────────────>  |
  |       |            |                |               |           |
  |       |            |                |         send(SMTP)────>   |
  |       |            |                |               |    External|
  |       |<─show success msg─|         |               |           |
  |       |            |                |               |           |
  |<─"Booking updated"─────|            |               |           |
  |       |            |                |               |           |
```

**Messages:**
1. `getBookings()` - Fetch list with filters
2. `getBookingDetails()` - Load specific booking
3. `updateBooking()` - Change status
4. `sendStatusEmail()` - Notify customer of status change

---

## SD-08: ADMIN EDIT ROOM (UC-22) 🏨

**Actors/Objects:**
- Admin
- RoomEditPage (UI)
- RoomManager
- RoomRepository
- Database

### **Sequence:**

```
Admin  RoomEditPage  RoomManager  RoomRepository  Database
  |         |             |              |            |
  |─click Edit room───>   |              |            |
  |         |             |              |            |
  |         |──loadRoom(id)─────────────>|            |
  |         |             |              |            |
  |         |             |       query(room)──────────>|
  |         |             |              |            |
  |         |             |       <───roomData────────|
  |         |             |              |            |
  |         |             |<───room──────|            |
  |         |             |              |            |
  |         |<─display tabs────|         |            |
  |         |  (General,Pricing,         |            |
  |         |   BlockDates,etc)          |            |
  |         |             |              |            |
  |─edit General tab──>   |              |            |
  |  • Name, Type        |              |            |
  |  • Capacity          |              |            |
  |  • Inventory: 18→20  |              |            |
  |         |             |              |            |
  |─edit Pricing tab──>  |              |            |
  |  • Base: 3,000,000đ  |              |            |
  |         |             |              |            |
  |─click Update────>     |              |            |
  |         |             |              |            |
  |         |──updateRoom(id,data)───────>|           |
  |         |             |              |            |
  |         |             |       update(room)────────>|
  |         |             |              |            |
  |         |             |       <───success────────|
  |         |             |              |            |
  |         |             |<───updated───|            |
  |         |             |              |            |
  |         |<─show success msg─|        |            |
  |         |             |              |            |
  |<─"Room updated"─────|              |            |
  |         |             |              |            |
```

**Messages:**
1. `loadRoom(id)` - Fetch room data for all tabs
2. `updateRoom()` - Save changes to multiple fields
3. Success confirmation

---

## SD-09: ADMIN BLOCK DATES (UC-24) 🚫

**Actors/Objects:**
- Admin
- BlockDateTab (UI)
- AvailabilityManager
- AvailabilityRepository
- Database

### **Sequence:**

```
Admin  BlockDateTab  AvailabilityManager  AvailabilityRepository  Database
  |         |                |                     |                  |
  |─click Block Special Date tab──>|               |                  |
  |         |                |                     |                  |
  |         |──loadCalendar(roomId,month)──────────>|                 |
  |         |                |                     |                  |
  |         |                |            query(availability)──────────>|
  |         |                |                     |                  |
  |         |                |            <───dates────────────────────|
  |         |                |                     |                  |
  |         |                |<───calendar─────────|                  |
  |         |                |                     |                  |
  |         |<─display May 2026 calendar─|         |                  |
  |         |  (show blocked dates)       |         |                  |
  |         |                |                     |                  |
  |─select date 26th───>    |                     |                  |
  |         |                |                     |                  |
  |         |  (date highlights in yellow)         |                  |
  |         |                |                     |                  |
  |─[Optional] enter reason>|                     |                  |
  |  "Maintenance"          |                     |                  |
  |         |                |                     |                  |
  |─click Update────>        |                     |                  |
  |         |                |                     |                  |
  |         |──blockDates(roomId,dates,reason)─────>|                 |
  |         |                |                     |                  |
  |         |                |            update(availability)─────────>|
  |         |                |            SET is_blocked=1             |
  |         |                |            SET block_reason='...'       |
  |         |                |                     |                  |
  |         |                |            <───success─────────────────|
  |         |                |                     |                  |
  |         |                |<───blocked──────────|                  |
  |         |                |                     |                  |
  |         |<─refresh calendar────|               |                  |
  |         |  (26th now shows blocked)            |                  |
  |         |                |                     |                  |
  |<─show notification──────|                     |                  |
  |  "Dates blocked"        |                     |                  |
  |         |                |                     |                  |
```

**Messages:**
1. `loadCalendar()` - Load month view with availability
2. `blockDates()` - Mark dates as blocked
3. `update(availability)` - Set `is_blocked=1` in database
4. Refresh calendar to show changes

---

## SD-10: GENERATE INVOICE PDF (UC-27) 📄

**Actors/Objects:**
- System (triggered)
- InvoiceGenerator
- InvoiceSettings
- PDFLibrary (TCPDF)
- FileSystem

### **Sequence:**

```
System  InvoiceGenerator  InvoiceSettings  PDFLibrary  FileSystem
  |            |                  |             |           |
  |─booking confirmed─>           |             |           |
  |  (trigger)         |          |             |           |
  |            |                  |             |           |
  |            |──getSettings()───>|            |           |
  |            |                  |             |           |
  |            |<───companyInfo───|             |           |
  |            |  (logo,name,     |             |           |
  |            |   address,etc)   |             |           |
  |            |                  |             |           |
  |            |──getBookingData()>             |           |
  |            |  from Database   |             |           |
  |            |                  |             |           |
  |            |<───bookingData───|             |           |
  |            |  (order,customer,|             |           |
  |            |   room,dates)    |             |           |
  |            |                  |             |           |
  |            |──loadTemplate()──>             |           |
  |            |                  |             |           |
  |            |<───template──────|             |           |
  |            |                  |             |           |
  |            |──createPDF()─────────────────>|           |
  |            |  pass:companyInfo,             |           |
  |            |       bookingData,             |           |
  |            |       template                 |           |
  |            |                  |             |           |
  |            |                  |    build():            |
  |            |                  |    • header(logo)      |
  |            |                  |    • company info      |
  |            |                  |    • invoice #         |
  |            |                  |    • customer details  |
  |            |                  |    • items table       |
  |            |                  |    • totals            |
  |            |                  |    • footer            |
  |            |                  |             |           |
  |            |                  |<───pdfData──|           |
  |            |                  |             |           |
  |            |──savePDF(pdfData,filename)─────────────>  |
  |            |                  |             |    write()|
  |            |                  |             |    to disk|
  |            |                  |             |           |
  |            |                  |             |<───path───|
  |            |                  |             |    /wp-   |
  |            |                  |             |    content|
  |            |                  |             |    /invoic|
  |            |                  |             |    es/    |
  |            |                  |             |    1598.pdf|
  |            |<─────pdfPath─────────────────────────|    |
  |            |                  |             |           |
  |<───invoice URL─────|          |             |           |
  |  (for download     |          |             |           |
  |   & email attach)  |          |             |           |
  |            |                  |             |           |
```

**Messages:**
1. `getSettings()` - Load company info for header
2. `getBookingData()` - Fetch order and booking details
3. `loadTemplate()` - Get invoice layout
4. `createPDF()` - Generate PDF with TCPDF library
5. `savePDF()` - Write to filesystem
6. Return path for download/email

**Key Points:**
- PDF generated synchronously after booking
- Saved to `/wp-content/uploads/invoices/`
- Used for both download and email attachment

---

## ✅ CHECKLIST VẼ SEQUENCE DIAGRAMS

- [ ] Actors/Objects ở đầu với boxes
- [ ] Lifelines là vertical dashed lines
- [ ] Messages có arrows với labels rõ ràng
- [ ] Activation boxes khi object processing
- [ ] Return messages dùng dashed arrows
- [ ] Method parameters trong parentheses
- [ ] Thứ tự messages từ trên xuống dưới (time flows down)
- [ ] Self-calls (nếu có) quay về chính object
- [ ] Notes/comments cho phần phức tạp

---

## 🎨 MÀU SẮC & STYLES

```css
/* Actor/Object Boxes */
Actor (Human): #FFF9C4 (Light Yellow)
UI Components: #E3F2FD (Light Blue)
Controllers: #BBDEFB (Blue)
Repositories: #C8E6C9 (Light Green)
Database: #A5D6A7 (Green)
External Services: #E1BEE7 (Light Purple)

/* Lines */
Lifeline: #9E9E9E (Gray), dashed
Activation: #BBDEFB (Light Blue), filled rectangle
Message arrow: #424242 (Dark Gray), solid
Return arrow: #424242 (Dark Gray), dashed

/* Labels */
Message labels: 10pt, Black
```

---

## ⏱️ THỜI GIAN ƯỚC TÍNH

| Sequence Diagram | Actors/Objects | Messages | Complexity | Thời gian |
|------------------|----------------|----------|------------|-----------|
| SD-01: Search | 5 | 8 | Medium | 1-1.5 giờ |
| SD-02: View Room | 6 | 8 | Medium | 1-1.5 giờ |
| SD-03: Add to Cart | 6 | 9 | Medium | 1-1.5 giờ |
| SD-04: View Cart | 5 | 6 | Simple | 45-60 phút |
| SD-05: Checkout | 7 | 12 | High | 1.5-2 giờ |
| SD-06: Review | 5 | 8 | Medium | 1 giờ |
| SD-07: Admin Bookings | 6 | 11 | High | 1.5-2 giờ |
| SD-08: Edit Room | 5 | 7 | Medium | 1 giờ |
| SD-09: Block Dates | 5 | 9 | Medium | 1-1.5 giờ |
| SD-10: Invoice PDF | 5 | 8 | Medium | 1-1.5 giờ |

**TỔNG:** 11-16 giờ cho 10 Sequence Diagrams

---

## 💡 BEST PRACTICES

1. **Keep it focused:** Mỗi diagram cho 1 UC hoặc 1 scenario
2. **Show key interactions:** Không cần vẽ mọi method call
3. **Use clear names:** Message labels phải rõ ràng (getBookingDetails, not get)
4. **Time flows down:** Thời gian chảy từ trên xuống dưới
5. **Activation boxes:** Show khi nào object đang xử lý
6. **Return messages optional:** Chỉ vẽ khi cần thiết để hiểu flow
7. **Notes for complex logic:** Thêm notes giải thích phần phức tạp

---

**HOÀN THÀNH! 🎉**

**File này được tạo bởi Claude AI - Ngày: 26/05/2026**
