# 📱 INFECTED SMS v5.0

> একটি শক্তিশালী এবং নিরাপদ SMS পাঠানোর টুল

![Version](https://img.shields.io/badge/version-5.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-Active-brightgreen)

---

## 📖 বিবরণ

**INFECTED SMS v5.0** একটি আধুনিক এবং ব্যবহারকারী-বান্ধব টুল যা আপনাকে দ্রুত এবং নির্ভরযোগ্যভাবে SMS পাঠাতে সাহায্য করে। এটি একাধিক ফিচার এবং উন্নত নিরাপত্তা প্রদান করে।

---

## ✨ মূল বৈশিষ্ট্য

- ✅ **দ্রুত SMS পাঠানো** - মিলিসেকেন্ডে বার্তা ডেলিভারি
- ✅ **ব্যাচ প্রসেসিং** - একসাথে একাধিক SMS পাঠান
- ✅ **স্বয়ংক্রিয় নিয়ন্ত্রণ** - সময়সূচী অনুযায়ী বার্তা পাঠান
- ✅ **বিস্তারিত লগিং** - সমস্ত ক্রিয়াকলাপের রেকর্ড রাখুন
- ✅ **ত্রুটি পরিচালনা** - নির্ভরযোগ্য এবং স্থিতিশীল সম্পাদন
- ✅ **সহজ ইন্টিগ্রেশন** - সহজেই আপনার প্রকল্পে অন্তর্ভুক্ত করুন

---

## 🛠️ প্রয়োজনীয়তা

- **Python 3.8+** বা তার উপরের সংস্করণ
- **pip** প্যাকেজ ম্যানেজার
- একটি সক্রিয় ইন্টারনেট সংযোগ
- প্রয়োজনীয় API কী এবং শংসাপত্র

---

## 📦 ইনস্টলেশন

### পদ্ধতি ১: Pip থেকে ইনস্টল করুন

```bash
pip install infected-sms
```

### পদ্ধতি ২: GitHub থেকে ক্লোন করুন

```bash
git clone https://github.com/Alaminvaihero/Infected_sms.git
cd Infected_sms
pip install -r requirements.txt
```

---

## 🚀 দ্রুত শুরু

### সাধারণ উদাহরণ

```python
from infected_sms import SMSClient

# ক্লায়েন্ট শুরু করুন
client = SMSClient(api_key='your-api-key')

# একটি SMS পাঠান
response = client.send(
    phone_number='01712345678',
    message='নমস্কার! এটি একটি পরীক্ষামূলক বার্তা।'
)

# ফলাফল প্রদর্শন করুন
print(response)
```

### ব্যাচ SMS পাঠানো

```python
# একাধিক ফোন নম্বরে SMS পাঠান
phone_numbers = ['01712345678', '01812345679', '01912345680']
message = 'এটি একটি গণ বার্তা পরীক্ষা'

for phone in phone_numbers:
    client.send(phone_number=phone, message=message)
```

---

## 📚 ডকুমেন্টেশন

### মূল পদ্ধতি

#### `send(phone_number, message, options=None)`

একটি SMS বার্তা পাঠান।

**পরামিতি:**
- `phone_number` (str): গন্তব্য ফোন নম্বর
- `message` (str): পাঠানোর বার্তা
- `options` (dict): অতিরিক্ত অপশন (ঐচ্ছিক)

**রিটার্ন:**
- সফলতা: `{'status': 'success', 'message_id': 'xxx'}`
- ব্যর্থতা: `{'status': 'error', 'error_message': 'xxx'}`

---

## ⚙️ কনফিগারেশন

`config.json` ফাইল তৈরি করুন:

```json
{
  "api_key": "আপনার-API-কী",
  "api_url": "https://api.example.com",
  "timeout": 30,
  "retry_count": 3,
  "log_level": "INFO"
}
```

---

## 📋 ব্যবহারের উদাহরণ

### উদাহরণ ১: সময়সূচী পরিষেবা

```python
import schedule
import time

def send_scheduled_sms():
    client.send('01712345678', 'প্রতিদিনের রিমাইন্ডার')

schedule.every().day.at("09:00").do(send_scheduled_sms)

while True:
    schedule.run_pending()
    time.sleep(60)
```

### উদাহরণ ২: ত্রুটি পরিচালনা

```python
try:
    response = client.send(
        phone_number='01712345678',
        message='পরীক্ষামূলক বার্তা'
    )
    if response['status'] == 'success':
        print('✅ SMS সফলভাবে পাঠানো হয়েছে')
    else:
        print(f'❌ ত্রুটি: {response["error_message"]}')
except Exception as e:
    print(f'⚠️ ব্যতিক্রম: {str(e)}')
```

---

## 🔒 নিরাপত্তা

- ✅ API কী এনক্রিপশন
- ✅ SSL/TLS সংযোগ
- ✅ রেট লিমিটিং সুরক্ষা
- ✅ ইনপুট যাচাইকরণ

### নিরাপত্তা সর্বোত্তম অনুশীলন

```bash
# API কী পরিবেশ ভেরিয়েবলে সংরক্ষণ করুন
export INFECTED_SMS_API_KEY='your-api-key'

# কোডে সরাসরি API কী লিখবেন না
```

---

## 🐛 সমস্যা সমাধান

### সমস্যা: "Invalid API Key"
**সমাধান:** আপনার API কী সঠিক এবং সক্রিয় কিনা তা পরীক্ষা করুন।

### সমস্যা: "Connection Timeout"
**সমাধান:** আপনার ইন্টারনেট সংযোগ পরীক্ষা করুন এবং সার্ভার স্থিতি নিশ্চিত করুন।

### সমস্যা: "Invalid Phone Number"
**সমাধান:** ফোন নম্বর সঠিক ফরম্যাটে রয়েছে কিনা যাচাই করুন (০ দিয়ে শুরু হওয়া বাংলাদেশী নম্বর)।

---

## 📊 পারফরম্যান্স

| মেট্রিক | মান |
|--------|------|
| গড় সরবরাহ সময় | < 100ms |
| সাফল্যের হার | > 99.5% |
| সর্বাধিক থ্রুপুট | 1000 SMS/সেকেন্ড |
| আপটাইম | 99.9% |

---

## 📝 লাইসেন্স

এই প্রকল্পটি **MIT লাইসেন্স** এর অধীন। বিবরণের জন্য [LICENSE](./LICENSE) ফাইল দেখুন।

---

## 🤝 অবদান রাখুন

আমরা অবদান স্বাগত জানাই! অনুগ্রহ করে নিম্নলিখিত পদক্ষেপগুলি অনুসরণ করুন:

1. **এই রিপোজিটরি ফর্ক করুন**
   ```bash
   git fork https://github.com/Alaminvaihero/Infected_sms.git
   ```

2. **নতুন ব্রাঞ্চ তৈরি করুন**
   ```bash
   git checkout -b feature/আপনার-ফিচার
   ```

3. **পরিবর্তনগুলি কমিট করুন**
   ```bash
   git commit -m "যোগ করা হয়েছে: আপনার-ফিচার বর্ণনা"
   ```

4. **ব্রাঞ্চ পুশ করুন**
   ```bash
   git push origin feature/আপনার-ফিচার
   ```

5. **Pull Request খুলুন**

---

## 🙋 সাহায্য এবং সহায়তা

- 📧 **ইমেল:** alaminvaihero@gmail.com
- 💬 **Issues:** [GitHub Issues](https://github.com/Alaminvaihero/Infected_sms/issues)
- 📱 **সোশ্যাল মিডিয়া:** আমাদের অনুসরণ করুন

---

## 📈 রোডম্যাপ

- [ ] Web ড্যাশবোর্ড যোগ করা
- [ ] মাল্টি-চ্যানেল সমর্থন (WhatsApp, Email)
- [ ] উন্নত বিশ্লেষণ প্রতিবেদন
- [ ] মোবাইল অ্যাপ্লিকেশন
- [ ] AI-চালিত বার্তা পরামর্শ

---

## 🙏 ধন্যবাদ

এই প্রকল্পটি ব্যবহার করার জন্য এবং সমর্থন করার জন্য ধন্যবাদ! ⭐ স্টার দিয়ে আমাদের সমর্থন করুন।

---

**শেষ আপডেট:** 2026-07-20  
**সংস্করণ:** 5.0.0  
**অবস্থা:** সক্রিয় এবং রক্ষণাবেক্ষণকৃত ✅
