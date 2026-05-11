# Enhanced Health Insurance Claims Analysis

## Project Overview

This project leverages big data management tools—specifically **Hadoop** and **Spark**—to analyze a health insurance claims dataset containing 4,500 records. The primary objective is to identify operational inefficiencies, financial risks, and demographic factors that influence claim approval outcomes.

## Problem Definition

The health insurance industry generates massive volumes of data that traditional relational databases struggle to manage efficiently. This project addresses:

- **Financial Exposure:** Quantifying the amount of capital tied up in pending claims.

- **Operational Bottlenecks:** Identifying provider specialties or submission methods that delay processing.

- **Predictive Factors:** Determining which patient demographics significantly impact approval rates.

## Dataset Description

The analysis uses the **Enhanced Health Insurance Claims Dataset**, which includes:

- **Claims Data:** Claim ID, amount, status (Approved, Pending, Denied), and submission metadata.

- **Provider Information:** ID, specialty (e.g., Orthopedics, Pediatrics), and location.

- **Patient Demographics:** Age, gender, income, and employment status.

## Technology Stack

The project employs a hybrid toolchain for robust analysis:

- **HDFS:** Distributed storage for the raw dataset.

- **PySpark:** Used for fast, in-memory distributed computation and descriptive statistics.

- **HiveSQL:** Utilized for patient segmentation, percentile calculations, and high-value claim analysis.

- **Hadoop MapReduce:** Used for validating PySpark results and calculating critical financial liabilities.

- **Tableau:** For final data visualization and insight interpretation.

## Key Insights

### 1. Provider Performance Gap

- **Highest Performer:** Orthopedics achieved the highest approval rate (36.4%).

- **Lowest Performer:** Pediatrics had the lowest approval rate (31.3%) and the highest pending financial exposure, totaling nearly \$1.75M.

### 2. Patient Segmentation

- **Predictors:** Employment status and age are strong predictors of approval, while gender and marital status have negligible impact.

- **Top Group:** Patients aged 19–35 had the highest approval rate at 36.8%.

### 3. Financial Risk Analysis

- **High-Value Claims:** Claims in the top 5th percentile (> \$9,510.27) face the highest denial rates (36.0%), suggesting stricter scrutiny for expensive claims.

### 4. Operational Inefficiencies

- **Submission Method:** Phone submissions (34.6%) are more effective than Online submissions (32.9%).

- **Temporal Trends:** Claims processed on Tuesdays show higher approval rates compared to Wednesdays.

## Repository Structure

- `ds8003_final_project_report.pdf`: Detailed technical analysis and findings.

- `ds8003_group6_project_proposal.pdf`: Initial project scope and objectives.

- `insight_1_mapper.py`: Python mapper script for calculating pending vs. total claims.

- `insight_1_reducer.py`: Python reducer script for final financial aggregation.

## How to Run the MapReduce Job

To execute the financial liability analysis (Insight 4) on a Hadoop cluster:

```bash
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-files insight_1_mapper.py,insight_1_reducer.py \
-mapper "python insight_1_mapper.py" \
-reducer "python insight_1_reducer.py" \
-input /user/root/claims_input/enhanced_health_insurance_claims.csv \
-output /user/root/claims_output_financial
```

> **Note:** Ensure `-D mapreduce.input.fileinputformat.split.minsize` is adjusted based on your dataset size for single-mapper consistency.

---

## Group 6 Members

- Samuel Ukoha  
- Surayia Rahman  
- Jakia Nowshin
