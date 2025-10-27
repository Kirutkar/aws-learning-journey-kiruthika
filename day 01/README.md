# Day 1 — Cloud Foundations

## 📚 What I studied
- What is cloud & why it’s needed
- On-prem vs Cloud
- Evolution: distributed → mainframe → cluster → grid → virtualization → utility computing → cloud
- **Service models:** IaaS, PaaS, SaaS
- **Deployment models:** Public, Private, Hybrid

## 🧪 Task: On-Prem vs Cloud Cost Simulation
I wrote a small Python script that compares a simplified monthly cost for on-prem infrastructure vs an AWS-style setup (EC2 + S3).  
> Run: `python cost_simulation.py` (or paste into Google Colab).

## 📝 Reflection (brief)
- Cloud shifts CapEx → OpEx and adds elasticity.
- Not every workload is cheaper by default; architecture & usage patterns matter.
- Today I focused on clarity of concepts before touching the AWS Console.

## 🧠 Quiz (my answers are below)
1. List the 3 cloud service models and one example each.  
2. Public vs Private vs Hybrid cloud — one-line definitions.  
3. Why does virtualization matter in cloud history?  
4. One scenario that still prefers on-prem.  
5. In simple terms, difference between a **web server**, **app server**, **database server**.

### ✅ My Answers
1. *IaaS:* EC2; *PaaS:* AWS Elastic Beanstalk; *SaaS:* Gmail/Google Docs.  
2. *Public:* third-party provider over internet; *Private:* dedicated to one org; *Hybrid:* mix with secure connectivity.  
3. Virtualization lets multiple isolated VMs share the same physical hardware efficiently → foundational for cloud multi-tenancy and scaling.  
4. Strict data residency/compliance with low-latency on-site equipment (e.g., factory floor control systems).  
5. **Web server** serves HTTP/static content; **App server** runs business logic; **DB server** stores/queries data.

