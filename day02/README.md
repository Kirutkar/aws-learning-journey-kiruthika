# Day 2 — AWS Account Setup, IAM, MFA, and Billing Awareness

## 📘 What I Studied
- How to create an AWS Account safely  
- Importance of using IAM Users instead of the Root Account  
- Multi-Factor Authentication (MFA)  
- Billing Dashboard and Free Tier usage  
- Creating a Billing Alarm using CloudWatch  

---

## ☁️ 1. AWS Account Setup
- Signed up for AWS using my verified email and card (for identity verification).  
- Selected the **Free Tier plan** to explore services safely without charges.  
- Verified identity using OTP and billing details (PAN, phone, etc.).  
- Once validated, the account was activated and ready to use.

🧠 *Learning takeaway:*  
> AWS needs billing verification even for Free Tier accounts. This ensures that users are genuine and can later pay for extra services if needed.

---

## 🔐 2. IAM — Identity and Access Management
- **IAM (Identity and Access Management)** allows us to create users and manage permissions safely.  
- Instead of working with the root account, I created a **new IAM user** with `AdministratorAccess`.

### 🪜 Steps:
1. Go to AWS Console → IAM → Users → Add User  
2. Enable “AWS Management Console access”  
3. Assign permissions → `AdministratorAccess`  
4. Download the access credentials (CSV file) safely

✅ Now, I log in using the IAM user credentials — not the root account.

---

## 🔑 3. MFA — Multi-Factor Authentication
- MFA adds an extra security layer beyond username/password.  
- I enabled MFA using the **Google Authenticator app** on my phone.  

🧭 Steps:
1. Go to **My Security Credentials** → Activate MFA  
2. Scan QR code using Google Authenticator  
3. Enter two codes shown in the app to verify  

Now, even if someone gets my password, they can’t log in without my MFA code. 🔒

---

## 💰 4. Billing Dashboard and Free Tier Monitoring
- Opened the **Billing and Cost Management Dashboard**.  
- Reviewed current Free Tier usage to ensure no hidden charges.  
- Learned about:
  - **Cost Explorer** – visualizes monthly spending
  - **Budgets** – set custom budget limits
  - **Free Tier Usage Alerts** – monitor free limits
  - **CloudWatch Billing Alarms** – email alerts when cost exceeds threshold  

---

### 🧾 Billing Alarm Setup
To avoid unexpected charges, I created a billing alarm:

1. Open **CloudWatch → Alarms → Billing**  
2. Set condition → when total estimated charges > `$1`  
3. Set notification → via **SNS (email)**  
4. Confirm subscription by clicking the link received in email  

✅ *Result:* I now get an email if my free tier usage goes beyond the limit.

---

## 🧩 5. Reflection (Brief)
- Understood the importance of working under IAM user, not root.  
- Learned how to keep my account secure with MFA.  
- Configured billing alarms for cost safety.  
- Now my AWS environment is fully secure and ready for EC2 instance creation.

---

## 🧠 6. Quiz (My Answers)

| Question | Answer |
|-----------|---------|
| 1️⃣ What is IAM used for? | To create and manage users, groups, and permissions securely. |
| 2️⃣ What is the root account? | The main AWS account with full access; should be used only for account-level tasks. |
| 3️⃣ Why enable MFA? | Adds extra security; requires OTP verification during login. |
| 4️⃣ What is a Billing Alarm? | A CloudWatch alert that notifies when your estimated cost exceeds a set amount. |
| 5️⃣ Why use IAM user for AWS Console? | To follow best practices and prevent accidental security or billing risks. |

---

## 🖼️ Screenshot
- ✅ AWS Login Page with MFA Enabled  
- ✅ Billing Dashboard Screenshot  
- ✅ Billing Alarm Confirmation Email  

---

## 🔗 Next Step
➡️ **Day 3:** Launch EC2 instance, learn AMI, Instance Types, Key Pairs, and Security Groups.  
➡️ Deploy Apache and access website from public IP.

---

## 💬 Reflection Quote
> “Security first, configuration next — that’s the real foundation of cloud computing.” ☁️

---
