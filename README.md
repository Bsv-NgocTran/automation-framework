# pytest cache directory #

This directory contains data from the pytest's cache plugin,
which provides the `--lf` and `--ff` options, as well as the `cache` fixture.

**Do not** commit this to version control.

See [the docs](https://docs.pytest.org/en/stable/how-to/cache.html) for more information.
# Playwright Python Automation Framework

# 1. Cấu trúc Framework

```
automation-framework/
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── product_page.py
│   └── cart_page.py
│
├── tests/
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_product.py
│   └── test_cart.py
│
├── test_data/
│   └── users.json
│
├── pytest.ini
└── README.md
```

### Ý nghĩa từng thư mục

#### pages/

Chứa các Page Object.

Mỗi màn hình của hệ thống được xây dựng thành một class riêng.

Ví dụ:

* LoginPage
* ProductPage
* CartPage

Mỗi Page chỉ quản lý:

* Locator
* Action
* Method thao tác

Không viết locator trực tiếp trong test case.

#### tests/

Chứa toàn bộ testcase.

Các testcase được chia theo từng chức năng:

* Login
* Product
* Cart

#### test_data/

Chứa dữ liệu test.

Ví dụ:

* Username
* Password
* Dữ liệu hợp lệ
* Dữ liệu không hợp lệ

#### conftest.py

Quản lý Fixture.

Có nhiệm vụ:

* Khởi tạo Browser
* Đăng nhập trước khi chạy các test cần login
* Tái sử dụng fixture cho nhiều testcase


# 2. Cách chạy Test

## Cài đặt thư viện

pip install -r requirements.txt

## Cài browser Playwright

```
playwright install
```

## Chạy toàn bộ testcase

```
python3 -m pytest
```

## Chạy kèm log chi tiết

```
python3 -m pytest -v
```

## Chạy một file

```
python3 -m pytest tests/test_login.py
```

## Chạy một testcase

```
python3 -m pytest tests/test_login.py::TestLogin::test_login_success
```


# 3. Cách thêm Test Data

Framework sử dụng file JSON để quản lý dữ liệu test.

Ví dụ:

```
test_data/users.json
```

Nội dung:

```json
{
    "validUser": {
        "username": "standard_user",
        "password": "secret_sauce"
    },
    "invalidPassword": {
        "username": "standard_user",
        "password": "123456"
    },
    "invalidUsername": {
        "username": "abcxyz",
        "password": "secret_sauce"
    }
}
```

Khi muốn thêm dữ liệu mới chỉ cần bổ sung object vào file `users.json` mà không cần sửa testcase.

Sau đó testcase chỉ cần đọc dữ liệu từ file JSON.

---

# 4. Giải thích cách áp dụng Page Object Model (POM)

Framework áp dụng mô hình **Page Object Model**.

Mỗi màn hình được xây dựng thành một class riêng.

Ví dụ:

### LoginPage

Quản lý:

* Username textbox
* Password textbox
* Login button
* Error message

Cung cấp các method:

* login()
* goto_login_page()

---

### ProductPage

Quản lý:

* Danh sách sản phẩm
* Add to Cart
* Remove
* Shopping Cart

Cung cấp các method:

* add_backpack_to_cart()
* remove_backpack_from_cart()
* click_backpack()
* open_cart()

---

### CartPage

Quản lý:

* Cart Item
* Checkout
* Continue Shopping

Cung cấp các method:

* checkout()
* continue_shopping()
* remove_backpack()

---

# 5. Best Practices đã áp dụng

* Áp dụng Page Object Model (POM).
* Không viết locator trực tiếp trong testcase.
* Dữ liệu test được tách riêng bằng file JSON.
* Sử dụng Fixture (`conftest.py`) để tái sử dụng bước đăng nhập.
* Các testcase độc lập, không phụ thuộc vào nhau.
* Không sử dụng `wait_for_timeout()`.
* Sử dụng cơ chế chờ của Playwright thông qua Locator và Assertion để tăng độ ổn định khi chạy test.

---

# 6. Chức năng đã Automation

## Login

* Login thành công
* Login sai password
* Login sai username
* Login bỏ trống dữ liệu

## Product

* Hiển thị danh sách sản phẩm
* Xem thông tin sản phẩm
* Add sản phẩm vào Cart
* Remove sản phẩm khỏi Cart

## Cart

* Kiểm tra danh sách sản phẩm trong Cart
* Continue Shopping
* Checkout
* Remove sản phẩm khỏi Cart

