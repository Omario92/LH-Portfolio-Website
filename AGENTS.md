# AGENTS.md

## Rules
- Luôn ưu tiên giữ code sạch, tuân thủ rules đã định sẵn.
- Phát triển giao diện tĩnh (HTML/CSS/JS) chất lượng cao tập trung vào AI Vibe Coding tại thư mục `front-end/`.
- Không cập nhật hay phát triển thêm cho thư mục `elementor/` (được giữ lại làm legacy backup).

## Commands
- N/A

## Recent Changes
- Tổ chức lại cấu trúc thư mục, di chuyển toàn bộ giao diện tĩnh vào thư mục `front-end/`.
- Cấu hình lại `package.json` và script check path tương thích với cấu trúc mới.
- Loại bỏ các mục tiêu và hướng dẫn đồng bộ Elementor trong tài liệu dự án.
- Cập nhật layout Hero chồng lớp (overlapping) và hiệu ứng portrait hạt halftone hạt nhỏ (cream highlights + dark shadows) trên nền glow teal-cyan theo mẫu thiết kế.
- Tích hợp trang chi tiết dự án động (`project-detail.html`) bằng client-side JS và liên kết toàn bộ thẻ dự án trên trang chủ và portfolio đến các trang chi tiết tương ứng (Thay thế bởi trang tĩnh riêng ở bước sau).
- Phát sinh 13 trang chi tiết dự án tĩnh riêng biệt trong thư mục `front-end/` bằng script `generate_projects.py` dựa trên 4 mẫu thiết kế (TVC video, Album ảnh nghệ thuật, UI thiết kế hệ thống, và CGI Hybrid kết hợp ảnh & video lặp).
- Cập nhật liên kết thẻ dự án trên trang chủ (`index.html`) và trang portfolio (`portfolio.html`) trỏ trực tiếp đến các trang tĩnh `.html` tương ứng và xóa trang `project-detail.html` cũ.
- Chạy script kiểm tra `check_paths.py` xác thực tính toàn vẹn của tất cả các liên kết tĩnh và đường dẫn tài nguyên.
- Thêm smooth page transition (fade + scale) khi chuyển trang, bao gồm CSS transition classes trên `.lh-page`, JS intercept link click với exit animation, và BFcache `pageshow` handler cho nút Back/Forward.
- Đồng bộ hóa thành công giao diện trang chủ `index.html` hiện tại (bao gồm hiệu ứng portrait halftone canvas, các smooth transitions, and dynamic menu navigation logic) cùng file Custom CSS (`styles.css`) và JS (`main.js`) đã xử lý đường dẫn tương đối thành `/assets/...` lên trang WordPress Elementor page ID `998`.
- Tích hợp hiệu ứng Heading Text Reveal cuộn trang (scroll reveal) theo dòng chữ (line-by-line reveal) cho các tiêu đề chính (`h1`, `.lh-section-title`, `.lh-cta h2`). Sử dụng giải thuật tách dòng tự động (dynamic line splitting) dựa trên `offsetTop` và thẻ `<br>` có sẵn, hỗ trợ co giãn màn hình (debounced resize recalculation) mượt mà và tối ưu hóa khả năng tiếp cận (Accessibility `aria-label` & `aria-hidden`).
- Tinh chỉnh tốc độ hiệu ứng Heading Text Reveal: tăng thời gian chuyển động lên `1.6s`, nâng độ trễ giữa các dòng (stagger delay) lên `0.15s`, và tách bộ quan sát IntersectionObserver riêng biệt cho tiêu đề với khoảng đệm lề dưới `rootMargin: '0px 0px -12% 0px'` kết hợp bộ đệm trễ `150ms` giúp hiệu ứng xuất hiện rõ rệt, sang trọng và dễ cảm nhận hơn khi cuộn.
- Khắc phục lỗi hiển thị tiêu đề bị cắt ngang (từ "CINEMATIC" bị xén thành "CINEMA1") bằng cách thiết lập `width: max-content` trên container `.lh-reveal-line` kết hợp nâng `max-width` của `.lh-hero-body` lên `75%` ở màn hình lớn để mở rộng không gian hiển thị và cho phép chữ tràn chồng lớp (overlap) tự nhiên lên canvas halftone. Đồng thời nâng dịch chuyển ẩn lên `translateY(140%)` để triệt tiêu hoàn toàn hiện tượng lồi nét đỉnh chữ trước khi chuyển động xuất hiện do chênh lệch chiều cao đệm lề dưới (`padding-bottom`).
- Cấu hình lại chiều rộng tiêu đề cho Desktop: Loại bỏ hẳn thuộc tính `max-width: 100%` trên `.lh-reveal-line` để các từ dài không bị bóp nghẹt bởi chiều rộng cột nội dung. Thêm truy vấn `@media (min-width: 1200px)` mở rộng `max-width` của `.lh-hero-body` lên `85%` để tiêu đề hiển thị trọn vẹn ở các độ phân giải lớn.
- Khắc phục lỗi chữ đầu dòng (như chữ "C" trong "CINEMATIC") bị xén mất cạnh trái bằng cách thêm `padding-inline: 0.08em` và bù lại bằng `margin-inline: -0.08em` trên `.lh-reveal-line`, tạo vùng đệm biên (sidebearing padding) giúp bảo vệ toàn vẹn hình dáng chữ khi sử dụng `overflow: hidden`.
- Tích hợp hiệu ứng cuộn Parallax so le (staggered scroll parallax) cho danh sách dự án `.lh-work-card` trong `.lh-work-grid`. Các thẻ được tính toán số lượng cột thực tế (3 cột ở Desktop, 2 cột ở Tablet, 1 cột ở Mobile) để gán hệ số so le tương ứng. Các thẻ tự động căn bằng nhau khi cuộn tới gần giữa màn hình (`translateY` tiệm cận `0` khi `distance <= 0`), đồng bộ mượt mà với hiệu ứng hover và được tối ưu hóa bằng `requestAnimationFrame` triệt tiêu độ trễ cuộn (scroll lag).
- Cải tiến hiệu ứng Parallax cuộn so le: Tăng cường hệ số so le (factor) lên `0.1` (desktop) và `0.07` (tablet) để hiệu ứng chuyển động rõ rệt hơn. Chuyển đổi sang giải thuật Parallax liên tục (continuous) trên toàn bộ khung nhìn thay vì dừng hẳn ở giữa màn hình, giúp các thẻ (đặc biệt là các thẻ ở hàng đầu) chuyển động mượt mà và cuộn lên chậm rõ rệt trong suốt quá trình cuộn trang, trong khi vẫn giao thoa căn bằng nhau chính xác tại trục giữa màn hình.








