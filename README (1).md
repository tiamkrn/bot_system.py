# 📱 سیستم ۷ بات تلگرام

راهنمای کامل برای نصب و استفاده سیستم مدیریت تراکنش‌ها و کش‌اوت

---

## 📋 فهرست مطالب

1. [آماده‌سازی اولیه](#آماده‌سازی-اولیه)
2. [نصب Python](#نصب-python)
3. [ایجاد بات‌های تلگرام](#ایجاد-بات‌های-تلگرام)
4. [تنظیم پروژه](#تنظیم-پروژه)
5. [نصب کتابخانه‌ها](#نصب-کتابخانه‌ها)
6. [اجرای برنامه](#اجرای-برنامه)

---

## 🚀 آماده‌سازی اولیه

### **۱. دانلود و نصب Python**

1. برید به: **https://www.python.org/downloads/**
2. دانلود **Python 3.9** یا بالاتر
3. نصب کنید با این گام‌ها:
   - ✅ **گزینه "Add Python to PATH" را انتخاب کنید**
   - بقیه گزینه‌ها: بگذاری روی پیش‌فرض

### **۲. بررسی نصب**

درون **Command Prompt** (Windows) یا **Terminal** (Mac/Linux) بنویسید:

```bash
python --version
```

باید نتیجه‌ای مثل `Python 3.11.0` بدهد.

---

## 🤖 ایجاد بات‌های تلگرام

### **۳. ایجاد بات اول (ترون)**

1. درون **Telegram**:
   - پیدا کنید: **@BotFather**
   - بفرستید: `/newbot`
   
2. **BotFather** می‌پرسد:
   - اسم بات: `Tron Bot` (یا هر نامی دلخواه)
   - username: `my_tron_bot` (باید منحصر به‌فرد باشد)

3. **BotFather** می‌دهد:
   ```
   Here is your bot token:
   123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
   ```

   ✅ **این توکن رو کپی کنید!**

### **۴. تکرار برای ۵ بات دیگر**

همین مراحل را برای بات‌های دیگر تکرار کنید:
- بات تتر
- بات کش‌اوت بالای 10م
- بات کش‌اوت زیر 10م
- بات کش‌اوت ترون/تتر
- بات بدهی

---

## 📁 تنظیم پروژه

### **۵. ایجاد پوشه پروژه**

1. **برای Windows:**
   - کلیک راست روی دسکتاپ
   - انتخاب: New → Folder
   - نام: `telegram_bot`
   - دو بار کلیک برای باز کردن

2. **برای Mac/Linux:**
   ```bash
   mkdir telegram_bot
   cd telegram_bot
   ```

### **۶. ایجاد فایل‌های پروژه**

درون پوشه `telegram_bot`، ۳ فایل ایجاد کنید:

**فایل ۱: `requirements.txt`**
```
python-telegram-bot==20.3
openpyxl==3.10.10
pandas==2.0.3
python-dotenv==1.0.0
APScheduler==3.10.4
requests==2.31.0
```

**فایل ۲: `config.json`**
```json
{
  "bots": {
    "tron": {
      "token": "YOUR_TRON_TOKEN_HERE",
      "channel_id": -1001234567890
    },
    "tether": {
      "token": "YOUR_TETHER_TOKEN_HERE",
      "channel_id": -1001234567890
    },
    "cashout_10plus": {
      "token": "YOUR_CASHOUT_10PLUS_TOKEN_HERE",
      "channel_id": -1001234567890
    },
    "cashout_10minus": {
      "token": "YOUR_CASHOUT_10MINUS_TOKEN_HERE",
      "channel_id": -1001234567890
    },
    "cashout_crypto": {
      "token": "YOUR_CASHOUT_CRYPTO_TOKEN_HERE",
      "channel_id": -1001234567890
    },
    "debt": {
      "token": "YOUR_DEBT_TOKEN_HERE",
      "channel_id": -1001234567890
    }
  }
}
```

**فایل ۳: `bot_system.py`**
(کد اصلی - دانلود کنید از فایل‌های فوق)

### **۷. شماسه کانال را بدست آورید**

برای یافتن شماسه کانال:

1. کانال را در تلگرام باز کنید
2. کلیک روی نام کانال (بالا)
3. کپی شماسه (معمولاً شامل `-100` است)

---

## 📦 نصب کتابخانه‌ها

### **۸. باز کردن Command Prompt/Terminal**

**Windows:**
- کلیک راست درون پوشه `telegram_bot`
- انتخاب: Open PowerShell here

**Mac/Linux:**
```bash
cd /path/to/telegram_bot
```

### **۹. نصب وابستگی‌ها**

درون Command Prompt/Terminal بنویسید:

```bash
pip install -r requirements.txt
```

**صبر کنید تا تمام بشه...** (۲-۳ دقیقه)

---

## 🚀 اجرای برنامه

### **۱۰. اجرای برنامه**

درون Command Prompt/Terminal:

```bash
python bot_system.py
```

اگر درست باشد، باید ببینید:
```
🚀 بات شروع شد...
```

### **۱۱. تست کنید!**

1. به کانال‌های خود برید
2. یک پیام نمونه بفرستید (مثل: `kakajan@1998. 8trx. 634 zh h`)
3. بات باید پیام مرتب‌شده رو بفرسته

---

## ⚠️ مشکلات رایج

### مشکل: `ModuleNotFoundError: No module named 'telegram'`

**حل:** بازگردید به مرحله نصب کتابخانه‌ها
```bash
pip install -r requirements.txt
```

### مشکل: `FileNotFoundError: config.json`

**حل:** فایل `config.json` را در پوشه صحیح ذخیره کنید (کنار `bot_system.py`)

### مشکل: توکن غلط است

**حل:** توکن را از **BotFather** دوباره کپی کنید (کپی دقیق)

### مشکل: کانال شناسه غلط است

**حل:** شماسه کانال را دوباره چک کنید (باید شامل `-100` باشد)

---

## 📊 داده‌های ذخیره‌شده

برنامه داده‌ها را در پوشه `data/` ذخیره می‌کند:

```
data/
├── tron_data.json
├── tether_data.json
├── debt_data.json
├── cashout_10plus.json
├── cashout_10minus.json
└── cashout_crypto.json
```

اکسل‌های روزانه در پوشه `excel_reports/` ذخیره می‌شوند.

---

## 🔧 تنظیمات پیشرفته

### تغییر زمان ارسال اکسل

در `config.json`:
```json
"excel_time": "06:00"
```

تغییر دهید به: `"07:00"` (ساعت ۷ صبح) یا هر ساعت دیگری

### تغییر منطقه زمانی

```json
"timezone": "Asia/Tehran"
```

تغییر دهید به:
- `"Europe/London"` (لندن)
- `"America/New_York"` (نیویورک)
- و غیره...

---

## 📞 نیاز به کمک؟

اگر مشکلی داشتید:

1. بررسی کنید **Python نصب است**
2. بررسی کنید **کتابخانه‌ها نصب هستند**
3. بررسی کنید **فایل‌ها در جای صحیح هستند**
4. بررسی کنید **توکن‌ها صحیح هستند**

---

**موفق باشید!** 🎉
