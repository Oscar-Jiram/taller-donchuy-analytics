# 🛠️ Taller Don Chuy — End-to-End Analytics Engineering Pipeline

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-Executive_Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Data Architecture](https://img.shields.io/badge/Architecture-ETL_%7C_Data_Mart-success?style=for-the-badge)

An end-to-end Analytics Engineering solution designed to transform raw transactional data from an automotive service center into scalable, executive-level business intelligence. This project demonstrates full-stack data capabilities: building a modular Python ETL pipeline, engineering a robust MySQL relational database with custom analytical views, and deploying an interactive Power BI dashboard.

---

## 📊 Executive Dashboard Preview

> **Business Impact:** Translates over 50+ service records into actionable insights, enabling stakeholders to instantly identify that spare parts account for 65.45% of total revenue, driving better inventory forecasting and vendor negotiation.

![Executive Dashboard](Snapshots/Dashboard-donchuy.png)

---

## 🎯 The Business Challenge & Solution

Automotive repair centers often generate rich operational data across clients, vehicles, and services, but struggle to consolidate these siloed records into strategic visual metrics.

* **The Challenge:** Lack of centralized visibility into total billing, service line profitability, labor vs. parts cost split, and customer retention metrics.
* **The Engineering Solution:** 
  1. Developed a **custom Python ETL pipeline** to standardize and automate data ingestion with built-in logging and integrity constraints.
  2. Engineered a **MySQL Data Mart** using optimized SQL views (`v_fact_reparaciones`, `v_kpi_servicios`, `v_kpi_clientes`) to decouple complex data logic from the presentation layer.
  3. Deployed a **minimalist Power BI Dashboard** utilizing a standardized corporate UI/UX (`#1B365D` palette) to deliver immediate macro and micro financial insights.

---

## 🏗️ Technical Architecture & Data Flow

The project is built on a decoupled architecture, ensuring scalability, maintainability, and seamless debugging across the data lifecycle.

```mermaid
graph TD
    A[Raw Data Inputs] -->|Extraction| B[Modular Python ETL]
    B -->|Data validation, transformation & event logging| C[(MySQL Database)]
    C -->|Relational 3NF Schema| D[(Analytical SQL Views)]
    D -->|Dimensional Data Mart tailored for BI| E[Executive Power BI]
    E -->|Interactive Reporting, DAX Measures & KPI Tracking| F([Business Insights])
    
    style B fill:#3776AB,stroke:#fff,stroke-width:2px,color:#fff
    style C fill:#4479A1,stroke:#fff,stroke-width:2px,color:#fff
    style D fill:#4479A1,stroke:#fff,stroke-width:2px,color:#fff
    style E fill:#F2C811,stroke:#333,stroke-width:2px,color:#000
```

## 🔑 Key Analytics & Insights Derived
Macro Financial Health: Continuous tracking of Total Revenue ($145.86K), Total Completed Services (50), and Average Ticket Size ($2.92K).

Service Line Profitability: Automated ranking of top revenue-generating services (e.g., Oil Changes, Clutch Replacements).

Cost Center Analysis: Accurate evaluation of the total income ratio between Labor (~34.55%) vs. Spare Parts (~65.45%).

Customer Intelligence: Identification and ranking of VIP clients by total lifetime expenditure to drive loyalty programs.

--

## 📂 Repository Structure

DonChuy/
├── config/             # Connection configurations & environment variables
├── logs/               # Automated pipeline execution logs for debugging
├── models/             # Analytical SQL views & database schema scripts
│   ├── v_fact_reparaciones.sql
│   ├── v_kpi_clientes.sql
│   └── v_kpi_servicios.sql
├── PowerBI/            # Power BI Desktop report files (.pbix)
├── Snapshots/          # High-resolution documentation images & visual assets
├── src/                # Core ETL pipeline Python modules (Extraction & Loading)
│   └── pipeline.py
├── .gitignore          # Git exclusion rules (.venv, local credentials)
├── main.py             # ETL pipeline execution entry point
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies (mysql-connector-python, pandas, etc.)

--

## 🚀 Getting Started (Local Deployment)

### 1.-Clone the repository:
git clone [https://github.com/Oscar-Jiram/taller-donchuy-analytics.git](https://github.com/Oscar-Jiram/taller-donchuy-analytics.git)
cd taller-donchuy-analytics

### 2.-Set up the virtual environment:
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt

### 3.-Run the ETL Pipeline:
python main.py


--

Deploy the BI Layer:

Execute the SQL scripts located in models/ within MySQL Workbench to generate the analytical views.

Open PowerBI/Don_ChuyBI.pbix to interact with the executive dashboard.

## 👤 Author

**Oscar Jiram**  
*Analytics & Data Engineer*  

I build the infrastructure that makes data actionable. Experienced in orchestrating data workflows, deploying relational data marts, and crafting executive UI/UX BI reporting. Currently seeking 100% remote positions to contribute to high-performing technical teams.

[**LinkedIn**](https://www.linkedin.com/in/TU_USUARIO) | [**GitHub**](https://github.com/Oscar-Jiram)
