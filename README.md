# 🏥 AI-Powered CRM Enhancement for Pharmaceutical SFE (Sales Force Effectiveness)

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/deploy?repository=ewkim188-jpg/AI-CRM&mainBranch=main&appFilePath=app.py)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**제약 영업 AI CRM 고도화 파이프라인**은 머신러닝(ML)을 활용하여 제약 산업의 영업 효율성을 극대화하는 **End-to-End 데이터 분석 솔루션**입니다. HCP(Healthcare Professional) 세분화, 처방 이탈 위험 예측, 그리고 데이터 기반의 차세대 영업 전략(Next Best Action)을 제공합니다.

---

## 🌟 Key Value Proposition

이 프로젝트는 제약사 CRM 데이터를 전략적 자산으로 전환하여 다음과 같은 비즈니스 가치를 창출합니다:

- **데이터 기반 HCP 타겟팅**: 감(感)이 아닌 행동 데이터를 기반으로 고객을 세분화합니다.
- **선제적 이탈 방지**: 처방이 감소하기 전, AI가 위험 신호를 감지하여 대응 기회를 제공합니다.
- **영업 생산성 극대화 (NBA)**: 매일 아침 어떤 고객에게, 어떤 채널로, 어떤 메시지를 전달할지 AI가 추천합니다.

---

## 📋 3-Step AI Pipeline Architecture

| Step  | Core Task                  | Algorithm / Method              | SEO Keywords                                  |
| ----- | -------------------------- | ------------------------------- | --------------------------------------------- |
| **1** | **HCP Segmentation**       | K-Means Clustering              | Customer Segmentation, Physician Targeting    |
| **2** | **Churn Prediction**       | Gradient Boosting (XGBoost/GBM) | Attrition Risk, Predictive Modeling           |
| **3** | **Next Best Action (NBA)** | Hybrid Rule-based + ML Scoring  | Omni-channel Strategy, Personalized Marketing |

---

## 🚀 Quick Start & Deployment

### Installation
```bash
git clone https://github.com/ewkim188-jpg/AI-CRM.git
cd AI-CRM
pip install -r requirements.txt
```

### Run Interactive Dashboard
Streamlit을 통해 로컬 환경에서 즉시 시뮬레이션 대시보드를 실행할 수 있습니다.
```bash
streamlit run app.py
```

---

## 🛠️ Tech Stack & Advanced Features

### Technologies
- **Core Logic**: `Python 3.10+`
- **Machine Learning**: `scikit-learn` (KMeans, GradientBoostingClassifier, RandomForest)
- **Data Engineering**: `pandas`, `numpy`
- **Interactive UI**: `Streamlit`
- **Visualization**: `matplotlib`, `seaborn` (Korean Font Optimized)

### Key Features
- **Real-time Simulation**: 500+ HCP 가상 데이터를 즉석에서 생성하고 분석합니다.
- **Predictive Scoring**: 각 의사별로 0~1 사이의 이탈 위험 점수(Churn Risk Score)를 산출합니다.
- **Personalized Recommendations**: 세그먼트와 이탈 위험도를 결합해 최적의 채널(대면, 디지털, 웨비나)을 추천합니다.
- **Data Export**: 분석 결과를 즉시 CSV로 내보내어 실제 영업 현장에서 활용 가능합니다.

---

## 📂 Project Structure

- `app.py`: **Streamlit Web Dashboard** 서비스의 메인 엔트리 포인트
- `pipeline.py`: 데이터 생성부터 NBA 추천까지 전체 로직의 **통합 실행 스크립트**
- `data_generator.py`: 제약 영업 현장의 특성을 반영한 **가상 CRM 데이터 엔진**
- `hcp_segmentation.py`: 행동 패턴 기반의 **고객 세분화 모듈**
- `churn_prediction.py`: **Gradient Boosting** 기반 처방 이탈 예측 모델
- `nba_recommender.py`: 개인화된 **영업 액션 추천 엔진**

---

## 📚 References
1. *Axtria*, "ML-Driven Physician Segmentation and Targeting" (2024)
2. *Cogent Engineering*, "Classification models for customer churn prediction" (2024)
3. *IntuitionLabs*, "A Guide to Next Best Action in Pharma Marketing" (2025)

---
Developed & Maintained by **Eun Woo Kim (김은우)**  
📧 Contact: chloewkim@gmail.com | [LinkedIn](https://www.linkedin.com/in/eunwookim/)  
*Last Updated: February 2026*
