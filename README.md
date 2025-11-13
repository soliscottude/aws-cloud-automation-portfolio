# ☁️ AWS Cloud Automation Portfolio  
### Automation · AWS · Python · Docker · CI/CD  

Hi, I'm **Scott Yang**, an aspiring **Cloud Support / Junior DevOps Engineer**.  
This portfolio showcases the hands-on projects I built during my Cloud Support learning journey, including AWS automation, Dockerization, and infrastructure workflows.

---

## 🚀 Projects Overview  

### **1️⃣ AWS Automation Manager (Python + boto3)**  
A command-line automation tool that interacts with AWS services using boto3.

**Features:**  
- List EC2 instances (ID, state, tags)  
- List S3 buckets  
- Simulate EC2 Start / Stop  
- Simulate S3 file uploads  
- Safe mode: all real AWS-changing actions commented out  
- Modular Python structure  

**Tech Stack:**  
`Python` · `boto3` · `AWS EC2` · `AWS S3`

📂 Source Code: `Day10–Day12`  
📸 Screenshots: *(add later)*

---

### **2️⃣ Dockerized AWS Automation Manager**  
The Python automation project was packaged into a portable Docker image.

**Highlights:**  
- Custom `Dockerfile`  
- Image published to Docker Hub  
- Supports passing AWS credentials via env variables  
- Fully portable & reproducible runtime environment  

**Run (with AWS Profile):**
```bash
docker run --rm --name automation-demo \
  -v ~/.aws:/root/.aws:ro \
  -e AWS_PROFILE=default \
  -e AWS_DEFAULT_REGION=ap-southeast-2 \
  soliscottude/aws-automation:v2
```

🛳️ Docker Hub: *(insert link later)*  
📸 Screenshots: *(add later)*

---

### **3️⃣ Static Website + CloudFront Distribution**  
A simple static website deployed via **Amazon S3 + CloudFront**.

**What I built:**  
- S3 bucket (static hosting enabled)  
- CloudFront global distribution  
- Tested caching, invalidation, edge URL  
- Demonstrated real-world CDN setup  

🌍 CloudFront URL: *(insert later)*  
📸 Screenshots: *(add later)*

---

## 🧩 Skills Demonstrated  

### 🟦 **AWS Fundamentals**  
- EC2 (instances, SSH, security groups)  
- S3 (buckets, hosting, upload, versioning)  
- CloudFront CDN  
- IAM & Access Keys  
- AWS CLI & boto3 SDK  

### 🟨 **Python Automation**  
- boto3 AWS automation  
- File handling & JSON  
- Logging  
- Error handling  
- Modular scripting  

### 🟧 **Docker & Containers**  
- Build, run, and publish Docker images  
- Use environment variables  
- Bind AWS credentials into containers  
- Create production-ready images  

### 🟩 **GitHub & CI/CD**  
- Version control workflow  
- GitHub Actions basics  
- Repository organization  
- Writing clean README documentation  

---

## 📚 Learning Journey Summary (Day1–Day15)

| Day | Topic | Output |
|-----|-------|--------|
| 1–6 | EC2, S3, CloudFront | Static website deployment |
| 7 | Documentation | GitHub README + screenshots |
| 8–10 | Python + boto3 | AWS automation scripts |
| 11–12 | Automation Project | EC2/S3 automation + error handling |
| 13–15 | Dockerization | Docker Hub image + tests |

---

## 🤝 About Me  
I'm Scott from New Zealand 🇳🇿 — transitioning into Cloud Support / DevOps.  
I enjoy automation, cloud services, and building practical tools that help people work smarter.

---

## 📬 Contact  
**LinkedIn:** *(add later)*  
**GitHub:** https://github.com/scottatlas  

---
