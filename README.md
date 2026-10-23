**KnZ (Domain 1)**

is an AI-powered career intelligence and psychological career counselling platform that combines resume analysis, RIASEC profiling, labour-market insights, and personalised reskilling pathways to help individuals discover suitable careers, develop future-ready skills, and navigate a changing world of work.


## Team Information

| **Field** | **Details** |
|---|---|
| **Team Name** | K&Z |
| **Team Domain** | Domain 1 |
| **SDG Track (1–17)** | SDG 4 – Quality Education<br>SDG 8 – Decent Work and Economic Growth<br>SDG 9 – Industry, Innovation and Infrastructure |
| **Team Leader** | Chong Wen Kai |
| **University** | Xiamen University Malaysia<br>International Medical University (IMU) |
| **Number of Members** | 2 |



## Links
| **Resource** | **Link** |
|---|---|
| GitHub Repository | [https://github.com/Kai9932/KnZ](https://github.com/Kai9932/KnZ) |
| Replit Project | [https://replit.com/@chongwenkai0/KnZ-2](https://replit.com/@chongwenkai0/KnZ-2) |
| Live Demo | [https://kn-z-2.replit.app](https://kn-z-2.replit.app) |
| RunPod Endpoint | [https://api.runpod.ai/v2/your-endpoint-id](https://api.runpod.ai/v2/your-endpoint-id) |
| Slide Deck | [Google Slides presentation](https://docs.google.com/presentation/d/1Lo44FWxnSBqrD3SAJnhQveEWhVN7jXu3/edit?usp=sharing&ouid=103189924867479152597&rtpof=true&sd=true) |
| Demo Video | [https://example.com/demo-video](https://example.com/demo-video) |



## Overview

### Problem

Many students, graduates, and career changers struggle to identify careers that fit their skills, interests, and strengths. At the same time, AI and automation are changing job requirements, making it difficult to know which skills to develop next. Traditional career resources may not provide the personalised, evidence-informed guidance and ongoing learning support people need to plan confidently for the future.

### Solution

**K&Z** is an AI-powered career intelligence and psychological career counselling platform that connects resume analysis and RIASEC career-interest profiling with career matching, labour-market insights, and personalised reskilling. It aims to explain why a career may fit a user, highlight skills to improve, and guide users through a structured learning pathway with quizzes and progress tracking. Future-skills insights and scenario planning help users consider possible changes in the world of work, while SDG mapping links career development to sustainable development goals.

### Key Features

- **Skills Profile Intake** — Users upload a resume and complete a RIASEC assessment to build a career profile.
- **Career Matches** — Combines resume information and RIASEC interests to suggest suitable occupations and show relevant skills, industries, and Malaysian salary information where data is available.
- **Future Skills** — Highlights skills that may be relevant to a target career, with sources and publication dates to be shown for trend information.
- **Personalised Reskilling Pathway** — Recommends learning modules based on a user's career goals and skills gaps; quizzes can be used to check learning before unlocking later modules.
- **Psychological Career Counselling** — Provides a conversational space for career reflection, strengths exploration, and navigating uncertainty; it is not a clinical diagnostic service.
- **Scenario Simulator** — Presents multiple possible future job-market scenarios, making assumptions and uncertainty clear rather than treating estimates as guaranteed predictions.
- **SDG Impact** — Connects relevant careers and skills to SDG 4 (Quality Education), SDG 8 (Decent Work and Economic Growth), and SDG 9 (Industry, Innovation and Infrastructure).
- **Learning Progress** — Helps users track completed modules and quiz progress and adapt their study plan.

### Tech Stack

| **Layer** | **Technology** |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, FastAPI |
| Data files | CSV files for labour-market and occupational data; CSV files are data storage, not a relational database |
| AI / Machine Learning | DistilBERT-based resume classification (checkpoint/version to be confirmed), RIASEC scoring and career-matching logic, DeepSeek API for AI-generated explanations |
| AI Compute / Model Hosting | RunPod GPU endpoint, if enabled and connected to the application |
| Development / Hosting | Replit; source-code version control through GitHub |



## How We Use Replit

Our team used **Replit** to develop, manage, and deploy our KnZ AI Career Guidance System.

- **Development:** We connected our GitHub repository to Replit and continued modifying, improving, and debugging the application's code directly in Replit.
- **Replit Agent:** We used Replit Agent to assist with development tasks, including adding CSV files and making necessary code modifications.
- **Secrets Management:** Sensitive information, such as API keys and credentials, is securely stored in **Replit Secrets** instead of being exposed in the source code.
- **Hosting and Deployment:** We used Replit's **Publish** feature to deploy our application, making it publicly accessible without requiring a local computer to run.



