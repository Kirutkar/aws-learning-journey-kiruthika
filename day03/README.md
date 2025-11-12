# Day 3 — EC2 Fundamentals + Launching My First Cloud Server (Apache)

## 📘 What I Studied
- What is AWS (in simple language)
- Why companies and developers use AWS
- What is EC2 (Elastic Compute Cloud)
- What are AMI, Instance Type, Key Pair, and Security Group
- How to create an EC2 instance
- How to connect to EC2 using SSH (PuTTY)
- How to install Apache web server
- How to edit the homepage and see it in the browser

---

## ☁️ 1. What is AWS? (Simple English)

AWS (Amazon Web Services) is like a **big online shop where we can rent computers and storage** instead of buying our own.

These computers live in Amazon’s data centres all around the world, and we can use them to:
- Run websites  
- Run apps  
- Store files  
- Process data  
- Build AI, APIs, and more  

We control everything from a browser, not from physical machines.

---

## ☁️ 2. Why AWS?

AWS is popular because:
- We **don’t need to buy hardware**
- We **pay only for what we use**
- It is available **24×7** from anywhere
- It is **scalable** (can grow as needed)
- It has a **Free Tier** which is very good for learning

---

## 🖥️ 3. What is EC2? (Very Simple Explanation)

EC2 = **Elastic Compute Cloud**.  
It is like a **computer that lives in the cloud**.

It is similar to buying a new PC:
- We choose the **operating system** (Linux or Windows)
- We choose the **CPU and RAM**
- We choose the **disk size**
- Then we **switch it on** and use it

But instead of being on our table, this computer runs inside Amazon’s data centre and we reach it over the internet.

---

## 🧩 4. Important EC2 Terms (in Plain English)

### 📌 AMI (Amazon Machine Image)
AMI = **ready-made OS template** for our cloud computer.

Examples:
- Amazon Linux 2  
- Ubuntu  
- Windows Server  

For this task, I used: **Amazon Linux 2 (Free Tier)**.

---

### 📌 Instance Type
Instance type = the **size and power** of the cloud computer.

Examples:
- `t2.micro` / `t3.micro` → small, free tier, 1 vCPU + 1 GB RAM  
- `c5` family → for more CPU power  
- `r5` family → for memory-heavy work  

For this task, I used: **t3.micro** (Free Tier).

---

### 📌 Key Pair (`.pem` and `.ppk`)
Key pair = **special key file** used to log in securely to the EC2 instance.

- `.pem` → created in AWS  
- `.ppk` → needed for PuTTY (Windows SSH client)

I:
- Created `kiru-key.pem` in AWS  
- Converted it to `kiru-key.ppk` using **PuTTYgen**  

---

### 📌 Security Group
Security group = **firewall rules** for the EC2 instance.

I allowed:
- **SSH (22)** → to log in to the server  
- **HTTP (80)** → to open the website in the browser  
- **HTTPS (443)** → for secure websites (optional but added)

Source for learning: **Anywhere (0.0.0.0/0)**

---

## 🧩 5. Task — Launching My EC2 Instance

### Steps I Followed:
1. Went to **EC2 → Launch Instance**
2. Gave name: `kiru-ec2-apache`
3. Selected AMI: **Amazon Linux 2**
4. Selected instance type: **t3.micro**
5. Chose key pair: `kiru-key` (`.pem`)
6. In Security Group:
   - Allowed **SSH (22)**
   - Allowed **HTTP (80)**
   - Allowed **HTTPS (443)**
7. Launched the instance and waited until:
   - Instance state = **Running**
   - Status checks = **3/3 checks passed**

---

## 🧩 6. Task — Connecting to EC2 Using PuTTY

To connect from my Windows laptop:

1. **Installed PuTTY** (64-bit version for Windows)
2. Opened **PuTTYgen**:
   - Loaded `kiru-key.pem`
   - Saved as `kiru-key.ppk`
3. Opened **PuTTY**:
   - Host name: `ec2-user@<my-public-ip>`
   - In SSH → Auth → selected my `kiru-key.ppk` file
4. Clicked **Open**, accepted the prompt  
5. Successfully logged in as `ec2-user` 🎉

---

## 🧩 7. Task — Installing Apache Web Server

Inside the EC2 terminal (PuTTY window), I ran:

```bash
sudo yum update -y
sudo yum install httpd -y

yum update → updated packages

yum install httpd → installed Apache web server

systemctl start httpd → started Apache

systemctl enable httpd → made Apache start automatically on boot

To confirm that Apache is running:

```bash
sudo systemctl status httpd

It showed active (running) ✅

---


##  🧩 8. Task — Editing the Homepage

The default Apache homepage file is:

```text
/var/www/html/index.html
````

I opened it using:

```bash
sudo nano /var/www/html/index.html
```

Then I replaced the content with:

```html
<h1>Welcome to Kiruthika’s AWS Cloud Server!</h1>
<p>Day 3 of my AWS learning journey 🚀</p>
```

To save in nano:

1. Press **Ctrl + O**, then Enter
2. Press **Ctrl + X** to exit

---

## 🧩 9. Task — Testing in the Browser

Then I opened my browser and typed:

```text
http://<my-public-ip>
```

Example:

```text
http://15.206.xx.xx
```

I saw:

* **First:** Apache default page (“It works!”)
* **After editing:** my own custom message from `index.html`

This confirmed my cloud server is serving a webpage live on the internet 🥳

---

## 🖼️ 10. Screenshot

(I took a screenshot of my Apache “It works!” / custom page and saved it as `aws-d3-apache.png`.)

<img width="800" alt="awsday2" src="https://github.com/user-attachments/assets/d1f66ee1-ccc8-4347-bf2b-1216d8cb66ca" />

---

## 🧠 11. Quiz (My Answers)

| Question                      | Answer                                                                       |
| ----------------------------- | ---------------------------------------------------------------------------- |
| 1️⃣ What is EC2?              | A virtual computer running in the AWS cloud.                                 |
| 2️⃣ What is an AMI?           | A ready-made operating system template used to launch EC2 instances.         |
| 3️⃣ What is a key pair?       | A special key file used to log in securely to the EC2 instance (SSH access). |
| 4️⃣ What is a security group? | A firewall that controls which traffic (ports) can reach my server.          |
| 5️⃣ Why did I install Apache? | To run a simple web server and show a webpage from my EC2 instance.          |

---

## ✨ 12. Reflection

Today I:

* Created my first EC2 instance
* Learned what AMI, instance type, key pair, and security group really mean
* Connected to a Linux server using SSH + PuTTY
* Installed Apache and hosted a webpage from the cloud

This made me feel like I am controlling a real production-style cloud server,
and it increased my confidence in working with AWS.

> **“Today I didn’t just learn AWS; I made the cloud show my own message.” ☁️✨**

```

---

If you want, I can now generate **Day 3 FULL README.md** in one block also (all sections 1–12).
```
















sudo systemctl start httpd
sudo systemctl enable httpd
