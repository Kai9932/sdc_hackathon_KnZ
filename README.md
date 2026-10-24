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
| GitHub Repository | [https://github.com/Kai9932/KnZ-SDC](https://github.com/Kai9932/KnZ-SDC) |
| Replit Project | [https://replit.com/@chongwenkai0/KnZ-2](https://replit.com/@chongwenkai0/KnZ-2) |
| Live Demo | [https://kn-z-2.replit.app](https://kn-z-2.replit.app) |
| RunPod Endpoint | [https://api.runpod.ai/v2/your-endpoint-id](https://api.runpod.ai/v2/your-endpoint-id) |
| Slide Deck | [Google Slides presentation](https://docs.google.com/presentation/d/1Lo44FWxnSBqrD3SAJnhQveEWhVN7jXu3/edit?usp=sharing&ouid=103189924867479152597&rtpof=true&sd=true) |
| Demo Video | [https://youtu.be/J0ueaD0c3So](https://youtu.be/J0ueaD0c3So) |



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



## How We Use RunPod

Our team used **RunPod** to store, deploy, and run our AI models for the KnZ AI Career Guidance System.

- **Model Storage:** We used RunPod to store and manage our trained AI models, including our DistilBERT-based resume classification model.
- **Development and Testing:** We initially experimented with **Jupyter Notebook** and **Visual Studio Code (VS Code)** to configure the environment, manage model files, and troubleshoot deployment issues.
- **GPU Pod:** We then used a **RunPod GPU Pod** to set up the required dependencies, test our models, and run AI inference in a GPU-powered environment.
- **Serverless Deployment:** After testing our models on a GPU Pod, we transitioned to **RunPod Serverless** to enable on-demand AI inference without keeping a GPU Pod running continuously.
- **Integration with Replit:** Our Replit application communicates with the RunPod Serverless Endpoint through API requests using `RUNPOD_API_KEY` and `RUNPOD_ENDPOINT_ID`. These credentials are securely stored in Replit Secrets.

### RunPod Workflow

**Jupyter Notebook & VS Code → RunPod GPU Pod → RunPod Serverless Endpoint → Replit Web Application**

This setup allows our application to process AI model predictions through RunPod while Replit handles the website, user interactions, and backend functionality.



## Challenges & Learnings

### Challenges We Faced

One of the biggest challenges our team faced was learning how to use **RunPod** and **Replit**, as both platforms were completely new to us. We had limited experience with cloud deployment, GPU environments, and integrating AI models with web applications.

- **RunPod Setup and Deployment:** Initially, we struggled to understand how RunPod worked, especially when setting up Jupyter Notebook and VS Code, uploading model files, managing the GPU Pod environment, and transitioning from Pods to Serverless Endpoints.

- **Replit Development:** Since it was our first time using Replit, we faced difficulties navigating the platform, creating new files, understanding the file tree structure, uploading project files, and connecting our existing GitHub repository to Replit.

- **Learning New Tools:** Understanding the different features, configurations, and deployment processes of both platforms required considerable time, experimentation, and troubleshooting.

### How We Overcame These Challenges

To overcome these difficulties, our team took the initiative to learn through different resources and practical experimentation.

- **YouTube Tutorials:** We watched YouTube tutorials to understand how to set up RunPod GPU Pods, upload model files, configure Serverless Endpoints, and navigate the Replit environment.

- **AI Assistance:** We used AI tools to guide us step by step through unfamiliar processes, troubleshoot errors, and understand how to configure and deploy our application.

- **Trial and Error:** We continuously tested different approaches, identified errors, and made adjustments until we successfully deployed our AI models and web application.

### What We Learned

Through this experience, our team gained valuable technical knowledge and practical skills.

- Learned how to use **RunPod GPU Pods and Serverless Endpoints** to host and run AI models.
- Gained experience using **Replit** for web development, GitHub integration, file management, and application deployment.
- Understood how to connect a **Replit web application to a RunPod Serverless Endpoint** through API integration.
- Improved our **problem-solving, debugging, and independent learning skills** by exploring tutorials, using AI assistance, and experimenting with unfamiliar technologies.
- Learned the importance of **teamwork, patience, and adaptability** when working with new development platforms.

Overall, although we faced many challenges as first-time users of RunPod and Replit, the experience helped us develop a better understanding of cloud-based AI deployment and strengthened our confidence in learning and applying new technologies.



## Future Improvements

Our team plans to continuously improve the KnZ AI Career Guidance System by introducing new features that enhance user engagement, motivation, and the overall user experience.

- **Achievement and Reward System:** Introduce a gamification system where users can earn achievement badges and points by completing activities such as career assessments, resume analysis, and career development tasks.

- **Points-to-Token Redemption:** Integrate the achievement system with our pricing model, allowing users to redeem accumulated points for tokens. For example, users who earn **100 points** can exchange them for tokens to access selected AI-powered features




## Team

| **Name** | **Role** | **GitHub** |
|----------|----------|------------|
| Chong Wen Kai | Team Lead / Backend & Frontend Developer | [@Kai9932](https://github.com/Kai9932) |
| Chong Wen Zhi | RunPod & Replit Deployment / Cloud Infrastructure | — |



## Submission Checklist

- [x] Team name, domain Domain 1 and SDG track filled in
- [x] Slide deck link added
- [x] Demo video link added
- [x] Replit used, with proof of use in `submission/`
- [x] RunPod used, with proof of use in `submission/`
- [x] Preliminary submission completed (`SDC2026_TeamName_Preliminary.pdf`)
- [x] Technology declaration completed (`SDC2026_TeamName_TechDeclaration.pdf`)
- [x] Submission files renamed with your team name (replace `TeamName`)
- [x] "How to Run" steps verified
- [x] No API keys or secrets committed to the repository
