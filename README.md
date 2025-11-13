# ☁️ AWS Cloud Automation Portfolio  
### **Tech Stack:** AWS · Python · boto3 · Docker · GitHub Actions · Linux · CloudWatch

---

## 🚀 Summary
I am Scott, an aspiring Cloud Support / Junior DevOps engineer based in New Zealand.  
This portfolio demonstrates my ability to automate AWS workflows, containerize applications,  
deploy global static sites, and build CI/CD pipelines.  

---

## 📑 Table of Contents

- [🚀 Summary](#-summary)
- [🌟 Project Highlights](#-project-highlights)
- [💼 What I Can Do (Job-Ready Skills)](#-what-i-can-do-job-ready-skills)
- [🚀 Projects Overview](#-projects-overview)
  - [1️⃣ AWS Automation Manager (Python + boto3)](#1️⃣-aws-automation-manager-python--boto3)
  - [2️⃣ Dockerized AWS Automation Manager](#2️⃣-dockerized-aws-automation-manager)
  - [3️⃣ Static Website + CloudFront Distribution](#3️⃣-static-website--cloudfront-distribution)
  - [4️⃣ GitHub Actions CI/CD Pipeline](#4️⃣-github-actions-cicd-pipeline)
- [🧩 Core Skills Demonstrated](#-core-skills-demonstrated)
  - [🟦 AWS Cloud Support Skills](#-aws-cloud-support-skills)
  - [🐍 Python Automation (boto3)](#-python-automation-boto3)
  - [🐳 Docker & Containerization](#-docker--containerization)
  - [⚙️ GitHub & CI/CD](#️-github--cicd)
- [📚 Learning Journey (Day 1–16)](#-learning-journey-day-1--day-16)
- [🤝 About Me](#-about-me)
- [📬 Contact](#-contact)

---

## 🌟 Project Highlights
- **AWS Automation Manager** — Python boto3 tool for EC2/S3 automation (with simulation mode)
- **Dockerized Automation Tool** — Packaged and published as a reusable Docker image
- **Global Static Website** — S3 + CloudFront CDN project with caching/invalidation testing

---

## 💼 What I Can Do (Job-Ready Skills)
- Deploy and troubleshoot AWS infrastructure (EC2, S3, CloudFront, IAM)
- Automate AWS operations using Python + boto3
- Build, run, and publish Docker containers
- Set up GitHub Actions CI/CD workflows
- Create CloudWatch alarms and basic Linux troubleshooting

---

## 🚀 Projects Overview  

## 📂 Repository Structure
```
.
├── automation_manager/   # AWS Automation Manager (boto3 scripts for EC2 + S3)
├── docker/               # Dockerfile and notes for building/running the image
├── cicd_demo/            # GitHub Actions CI/CD workflow examples
├── screenshots/          # CLI, Docker, CloudFront, CloudWatch screenshots
└── README.md             # Project overview (this file)
```

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
#### 📸 Screenshots
**1. Boto3 Automation Output (EC2 + S3 Listing)** 
This screenshot shows the Python automation tool successfully listing real AWS resources  
using `python -m automation_manager.main` in simulation mode.

![CLI showing EC2/S3 listing](./screenshots/boto3_run_output.png)

**2. Simulated EC2 Start Action**  
![Sim Start](screenshots/boto3_sim_start.png)

---

**3. Simulated EC2 Stop Action**  
![Sim Stop](screenshots/boto3_sim_stop.png)

---

**4. Simulated S3 File Upload**  
![Sim Upload](screenshots/boto3_sim_upload.png)

---

**5. Automation Manager Project Structure**  
Shows the modular Python package layout (main.py, EC2/S3 managers, utils).

![Project Structure](screenshots/boto3_project_structure.png)

---

### **2️⃣ Dockerized AWS Automation Manager**  
This project packages my AWS Automation Manager (Python + boto3) into a fully portable Docker image.

**What I built:**  
- A custom **Dockerfile** that installs Python, boto3, and all project dependencies  
- A reproducible runtime environment that runs identically on any machine  
- A published Docker image on Docker Hub (`soliscottude/aws-automation:v2`)  
- AWS credential injection via environment variables  
- Support for AWS Profile binding using local `~/.aws`  

**Why Docker matters:**  
Docker ensures that my automation tool:  
- Runs consistently across macOS, Linux, and Windows  
- Avoids “it works on my machine” issues  
- Bundles all dependencies so users don’t need to install Python or boto3  
- Makes deployment & automation more professional and scalable  

**Key Learnings:**  
- How to write production-style Dockerfiles  
- Understanding image layers, caching, and how build contexts work  
- Publishing images to Docker Hub  
- Using environment variables securely inside containers  

**Run the container (with AWS Profile):**  
```bash
docker run --rm --name automation-demo \
  -v ~/.aws:/root/.aws:ro \
  -e AWS_PROFILE=default \
  -e AWS_DEFAULT_REGION=ap-southeast-2 \
  soliscottude/aws-automation:v2
```

🛳️ Docker Hub: https://hub.docker.com/r/soliscottude/aws-automation

#### 📸 Screenshots
**1. Docker Container Running AWS Automation Manager**  
This screenshot shows the Docker image pulling from Docker Hub and successfully  
running the automation tool inside a container using the local AWS Profile.

![Docker Run Output](screenshots/docker_run_output.png) 

---

**2. Docker Hub Repository (Published Image)**  
This screenshot shows the public Docker Hub repository for my automation tool.  
The image `soliscottude/aws-automation:v2` can be pulled and run on any machine,  
demonstrating that the project is fully containerized and shareable.

![Docker Hub Page](screenshots/docker_hub_page.png)

---

### **3️⃣ Static Website + CloudFront Distribution**  
This project demonstrates a complete **global static website deployment** using S3 + CloudFront.

**What I implemented:**  
- Created an S3 bucket with **Static Website Hosting** enabled  
- Uploaded a custom `index.html` and tested direct S3 access  
- Configured a **CloudFront distribution** using the S3 website endpoint  
- Verified global CDN acceleration using the CloudFront URL  
- Tested cache behaviour and performed manual **invalidation**  
- Confirmed HTTP → HTTPS redirection and default root object settings  

**Key Learnings:**  
- Difference between S3 bucket endpoint vs website endpoint  
- How CloudFront caches content at edge locations  
- How invalidation refreshes outdated content  
- Understanding TTL and global latency reduction  

🌍 **CloudFront URL:** https://d3hd4jq824wa7l.cloudfront.net/

#### 📸 Screenshots

**1. S3 Static Website Hosting Configuration**  
This screenshot shows the S3 bucket with *Static Website Hosting* enabled,  
including the index document setup (`index.html`) and the public website endpoint.

![S3 Static Hosting](screenshots/s3_static_hosting.png)

---

**2. CloudFront Distribution Settings**  
This screenshot shows the CloudFront distribution connected to the S3 website endpoint,  
with the distribution status marked as *Enabled* and the domain name displayed.

![CloudFront Distribution](screenshots/cloudfront_distribution.png)

---

**3. CloudFront Global URL (Deployed Website)**  
This screenshot shows the CloudFront URL opened successfully in the browser—  
demonstrating global CDN caching and HTTPS delivery through CloudFront.

![CloudFront Website](screenshots/cloudfront_website.png)

---

### **4️⃣ GitHub Actions CI/CD Pipeline**

This project includes a simple CI/CD pipeline built with **GitHub Actions**,  
designed to demonstrate automated workflows for cloud environments.

**What the pipeline does:**  
- Automatically triggers on every `push` to the repository  
- Installs Python + boto3 inside the GitHub runner  
- Validates the project structure (linting / syntax checks)  
- (Optional) Uploads files to S3 or executes boto3 automation scripts  
- Logs workflow results directly inside GitHub Actions

**Why it matters:**  
- Shows the ability to create automated build/test/deploy workflows  
- Demonstrates understanding of workflow triggers (`on: push`)  
- Shows awareness of secure use of AWS credentials in CI/CD environments  
- A core DevOps skill used in real cloud migration & automation teams

📁 **Workflow file:**  
`/.github/workflows/main.yml`

#### 📸 Screenshots  

**1. GitHub Actions Workflow Run**  
Shows the workflow triggered on push, with green checkmark status.

![CI/CD Workflow Run](screenshots/cicd_workflow_run.png)

---

**2. Workflow YAML Summary**  
Shows the structure of the GitHub Actions script used to automate tasks.

![CI/CD YAML File](screenshots/cicd_yaml.png)

---

## 🧩 Core Skills Demonstrated

### 🟦 AWS Cloud Support Skills
- Deploy and troubleshoot EC2 instances (SSH access, security groups, key pairs)
- Deploy static websites using S3 + CloudFront CDN
- Understand IAM permissions, access keys, and least-privilege principles
- Use AWS CLI to diagnose region, credential, and permission issues
- Create and test CloudWatch alarms (CPU, metric filters)

### 🐍 Python Automation (boto3)
- Automate EC2 start/stop workflows
- Automate S3 uploads with error handling and logging
- Read/write JSON, manage file operations, and format CLI output
- Build modular Python applications (separated managers for EC2/S3)
- Use logging module to record system actions

### 🐳 Docker & Containerization
- Write production-style Dockerfiles
- Build and publish images to Docker Hub (`soliscottude/aws-automation:v2`)
- Inject AWS credentials into containers using env variables
- Bind local AWS profiles using volume mounts
- Run reproducible automation inside containers

### ⚙️ GitHub & CI/CD
- Push and version control project code using Git
- Write GitHub Actions workflows (build/test/deploy)
- Automate deployment steps (S3 upload, boto3 scripts)
- Maintain a clean, professional portfolio structure
- Document projects clearly for technical reviewers 

---

## 📚 Learning Journey (Day 1 – Day 16)

---

### **Day 1 — AWS Account Setup & Fundamentals**
**Topic:** Region, IAM, VPC Basics  
**What I Did:** Created AWS account, configured IAM, learned core concepts  
**Output:** AWS CLI configured locally

---

### **Day 2 — EC2 Basics**
**Topic:** Launching & Managing EC2  
**What I Did:** Created first EC2 instance, learned instance types and pricing  
**Output:** Running EC2 with security group settings  

---

### **Day 3 — SSH & Security Groups**
**Topic:** Connecting to EC2  
**What I Did:** SSH into EC2, explored inbound/outbound rules  
**Output:** Successful EC2 login via SSH key  

---

### **Day 4 — S3 Concepts**
**Topic:** Bucket, object storage, access patterns  
**What I Did:** Created S3 bucket, uploaded files  
**Output:** Working S3 bucket with uploaded objects  

---

### **Day 5 — Static Website Hosting**
**Topic:** S3 Website Hosting  
**What I Did:** Enabled static hosting, uploaded index.html  
**Output:** Public website running on S3  

---

### **Day 6 — CloudFront CDN**
**Topic:** Global Content Delivery  
**What I Did:** Created CloudFront distribution, connected to S3  
**Output:** CloudFront URL delivering S3 site globally  

---

### **Day 7 — Documentation & GitHub**
**Topic:** Recording progress  
**What I Did:** Added README + screenshots to GitHub  
**Output:** Organized repo with Day1–Day7 updates  

---

### **Day 8 — Python Basics**
**Topic:** Variables, loops, functions  
**What I Did:** Wrote practice scripts  
**Output:** Python fundamentals ready for automation  

---

### **Day 9 — File & JSON Handling**
**Topic:** Python data processing  
**What I Did:** Read/write files, parsed JSON  
**Output:** Helper functions for later boto3 scripts  

---

### **Day 10 — boto3 AWS Connection**
**Topic:** Connecting to AWS programmatically  
**What I Did:** Wrote boto3 scripts to list S3 buckets & EC2 instances  
**Output:** boto3 connection test uploaded to GitHub  

---

### **Day 11 — EC2 & S3 Automation**
**Topic:** Automating AWS workflows  
**What I Did:** Built EC2 start/stop + S3 upload automation  
**Output:** AWS Automation Manager v1 (Python)  

---

### **Day 12 — Dockerize the Automation Tool**
**Topic:** Containers & portability  
**What I Did:** Wrote Dockerfile, built/published image  
**Output:** Docker image `soliscottude/aws-automation:v2` on Docker Hub  

---

### **Day 13 — CI/CD with GitHub Actions**
**Topic:** Automation pipeline  
**What I Did:** Created workflow files, added triggers  
**Output:** Working CI/CD pipeline (build/test/deploy)  

---

### **Day 14 — CloudWatch & Linux Essentials**
**Topic:** Monitoring & troubleshooting  
**What I Did:** Created CPU alarm, practised Linux tools  
**Output:** CloudWatch alarm + troubleshooting cheat sheet  

---

### **Day 15 — System Review & Certification Prep**
**Topic:** Review AWS Core Services  
**What I Did:** Consolidated knowledge, practised exam questions  
**Output:** Finalized Automation + Docker + CloudWatch understanding  

---

### **Day 16 — Mock Interview & Portfolio Completion**
**Topic:** Interview readiness  
**What I Did:** Practised technical/behavioral questions, polished GitHub  
**Output:** Job-ready portfolio and improved README  


---

## 🤝 About Me  
I'm Scott from New Zealand 🇳🇿 — transitioning into Cloud Support / DevOps.  
I enjoy automation, cloud services, and building practical tools that help people work smarter.

---

## 📬 Contact  
**LinkedIn:** www.linkedin.com/in/scottyangnz
**GitHub:** https://github.com/soliscottude

---
