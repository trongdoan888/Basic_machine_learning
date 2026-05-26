# 🏨 Quan Tròng Hotel — Hệ thống Đặt phòng Khách sạn trực tuyến

> Dự án WordPress hotel booking sử dụng plugin **WP Hotel Booking v2.3.0** (ThimPress) tích hợp **WooCommerce** và **PayPal**.

---

## 📋 Danh sách Use Cases (UC)

### 👥 UC dành cho Khách hàng (Guest)

| Mã UC | Tên Use Case | Mô tả chi tiết |
|-------|-------------|----------------|
| **UC-01** | Tìm kiếm phòng | Khách nhập ngày check-in / check-out, lọc theo loại phòng (`hb_room_type`) và sức chứa (`hb_room_capacity`). Hệ thống kiểm tra tính khả dụng theo thời gian thực. |
| **UC-02** | Xem chi tiết phòng | Khách xem trang phòng đơn lẻ: ảnh gallery, mô tả, giá/đêm, sức chứa người lớn / trẻ em, tiện nghi, phòng liên quan. |
| **UC-03** | Thêm phòng vào giỏ hàng | Khách chọn phòng với ngày cụ thể và thêm vào `WPHB_Cart`. Hỗ trợ nhiều phòng trong một lần đặt. |
| **UC-04** | Thêm dịch vụ bổ sung (Extra) | Khách chọn các dịch vụ extra (`hb_extra_room`): ăn sáng, đỗ xe, spa, v.v. Tính thêm phí theo số đêm. |
| **UC-05** | Áp dụng mã giảm giá (Coupon) | Khách nhập mã coupon (`hb_coupon`). Hệ thống validate: hạn sử dụng, giá trị đơn tối thiểu/tối đa, số lần dùng còn lại. |
| **UC-06** | Xem giỏ hàng | Khách xem toàn bộ giỏ: danh sách phòng, ngày check-in/out, extra services, coupon đã áp dụng, tổng tiền. |
| **UC-07** | Xóa sản phẩm khỏi giỏ | Khách xóa phòng hoặc dịch vụ extra ra khỏi giỏ trước khi thanh toán. |
| **UC-08** | Tiến hành Checkout | Khách nhấn "Đặt phòng" — hệ thống chuyển đến trang checkout (`WPHB_Checkout`). |
| **UC-09** | Nhập thông tin khách | Khách điền: họ tên, email, số điện thoại, địa chỉ, yêu cầu đặc biệt. |
| **UC-10** | Chọn phương thức thanh toán | Khách chọn: **PayPal** (online) hoặc **Offline** (thanh toán tại quầy). |
| **UC-11** | Hoàn tất thanh toán | Hệ thống tạo booking (`hb_booking`), xử lý thanh toán, cập nhật trạng thái đặt phòng. |
| **UC-12** | Xem trang xác nhận | Khách xem trang thank-you: mã booking, chi tiết đặt phòng, thông tin thanh toán. |
| **UC-13** | Nhận email xác nhận | Hệ thống gửi email xác nhận tự động đến khách và admin sau khi đặt phòng thành công. |
| **UC-14** | Đăng ký tài khoản | Khách mới tạo tài khoản để quản lý lịch sử đặt phòng. |
| **UC-15** | Đăng nhập tài khoản | Khách đã có tài khoản đăng nhập để xem / quản lý đơn đặt phòng. |
| **UC-16** | Xem lịch sử đặt phòng | Khách đã đăng nhập xem danh sách các booking đã thực hiện, trạng thái từng đơn. |
| **UC-17** | Đánh giá phòng | Khách gửi đánh giá sao và nhận xét về phòng đã ở. Review được kiểm duyệt trước khi hiển thị. |
| **UC-18** | Chat hỗ trợ trực tuyến | Khách khởi tạo live chat với nhân viên hỗ trợ qua **3CX Live Chat**. |
| **UC-19** | Xuất dữ liệu cá nhân (GDPR) | Khách yêu cầu xuất toàn bộ dữ liệu cá nhân của mình (tuân thủ GDPR). |
| **UC-20** | Xóa dữ liệu cá nhân (GDPR) | Khách yêu cầu xóa tài khoản và toàn bộ dữ liệu liên quan (tuân thủ GDPR). |

---

### 🔑 UC dành cho Quản trị viên (Admin)

| Mã UC | Tên Use Case | Mô tả chi tiết |
|-------|-------------|----------------|
| **UC-21** | Quản lý đặt phòng | Admin xem danh sách tất cả booking, xác nhận / hủy / hoàn thành từng đơn. Lọc theo trạng thái: `hb-pending`, `hb-confirmed`, `hb-cancelled`. |
| **UC-22** | Quản lý phòng | Admin thêm mới / chỉnh sửa / xóa phòng (`hb_room`): tên, mô tả, ảnh gallery, giá/đêm, sức chứa. |
| **UC-23** | Quản lý tồn kho phòng | Admin cấu hình số lượng phòng có sẵn (inventory) cho từng loại phòng. |
| **UC-24** | Khóa ngày không cho đặt | Admin block các ngày cụ thể khi phòng bảo trì hoặc đã được đặt trước. |
| **UC-25** | Quản lý dịch vụ bổ sung | Admin thêm / sửa / xóa extra services (`hb_extra_room`) kèm theo phòng: giá và mô tả. |
| **UC-26** | Tạo và quản lý Coupon | Admin tạo mã giảm giá (`hb_coupon`): loại giảm (cố định / %), hạn dùng, giá trị đơn min/max, số lần dùng tối đa. |
| **UC-27** | Tạo hóa đơn PDF | Hệ thống tự động tạo hóa đơn PDF cho mỗi booking hoàn thành (WooCommerce PDF Invoices). |
| **UC-28** | Cấu hình hệ thống | Admin cấu hình: trang mặc định (cart, checkout, account), phương thức thanh toán, mẫu email, cài đặt phòng. |
| **UC-29** | Tạo form tùy chỉnh | Admin xây dựng form liên hệ / hỏi giá bằng **SureForms** và nhúng vào các trang. |
| **UC-30** | Quảng cáo & SEO | Admin thiết lập Google Listings & Ads, tối ưu SEO với SureRank, kết nối mạng xã hội (Pinterest, Snapchat, Reddit). |

---

## 📊 Tổng quan Use Cases

```
Tổng số UC:   30
├── Khách hàng (Guest):      20 UC  (UC-01 → UC-20)
└── Quản trị viên (Admin):   10 UC  (UC-21 → UC-30)
```

### Luồng chính của Khách hàng

```
[UC-01] Tìm kiếm phòng
        ↓
[UC-02] Xem chi tiết phòng
        ↓
[UC-03] Thêm vào giỏ hàng ──→ [UC-04] Thêm Extra Services
        ↓                      [UC-05] Áp dụng Coupon
[UC-06] Xem giỏ hàng
        ↓
[UC-08] Checkout ──→ [UC-09] Nhập thông tin khách
        ↓
[UC-10] Chọn thanh toán ──→ [UC-11] Hoàn tất thanh toán
        ↓
[UC-12] Xem xác nhận + [UC-13] Nhận email
```

---

## 🛠️ Tech Stack

| Thành phần | Chi tiết |
|---|---|
| **Nền tảng** | WordPress 6.9 |
| **Theme** | Astra v4.13.0 |
| **Booking Engine** | WP Hotel Booking v2.3.0 (ThimPress) |
| **E-commerce** | WooCommerce 10.7.0 |
| **Thanh toán** | PayPal + Offline Payment |
| **Hóa đơn** | WooCommerce PDF Invoices & Packing Slips |
| **Live Chat** | 3CX Live Chat |
| **Form Builder** | SureForms |
| **Email** | MailPoet + SureMails |
| **SEO** | SureRank + Google Listings & Ads |
| **Backup** | All-in-One WP Migration |
| **Database** | MySQL (`hotel_booking_db`) |

---

## 📁 Custom Post Types

| Post Type | Slug | Mục đích |
|---|---|---|
| Phòng | `hb_room` | Danh sách phòng khách sạn |
| Đặt phòng | `hb_booking` | Đơn đặt phòng của khách |
| Coupon | `hb_coupon` | Mã giảm giá |
| Dịch vụ bổ sung | `hb_extra_room` | Extra services đi kèm phòng |

---

## 📌 Ghi chú

- File `wp-config.php` **không được commit** vì chứa thông tin nhạy cảm (DB password, secret keys).
- Thư mục `wp-content/uploads/` và `wp-content/ai1wm-backups/` không được commit do dung lượng lớn (>3 GB).
- Khi clone về, cần tạo lại `wp-config.php` và import database riêng.
