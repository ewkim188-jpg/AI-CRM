# 🏥 AI-Powered CRM Enhancement for Pharmaceutical SFE

> **제약 영업 AI CRM 고도화 파이프라인**  
> AI/ML을 활용하여 HCP(Healthcare Professional) 세분화, 이탈 위험 예측, 그리고 최적의 영업 활동(Next Best Action)을 추천하는 End-to-End 시스템입니다.

---

## 📋 Project Overview

이 프로젝트는 제약사 CRM 데이터를 분석하여 영업 성과를 최적화하는 **3단계 AI 파이프라인**을 구현합니다:

| Step | Task                 | Method                  | Business Value                 |
| ---- | -------------------- | ----------------------- | ------------------------------ |
| 1    | **HCP Segmentation** | K-Means Clustering      | 고객 그룹별 차별화된 전략 수립 |
| 2    | **Churn Prediction** | Gradient Boosting       | 처방 감소 위험 HCP 사전 식별   |
| 3    | **Next Best Action** | Rule-based + ML Scoring | 최적 채널/타이밍/콘텐츠 추천   |

## 🛠️ Tech Stack

- **Language**: Python 3.10+
- **Framework**: Streamlit (Dashboard)
- **ML Libraries**: scikit-learn, pandas, numpy
- **Visualization**: matplotlib, seaborn

## 📁 Project Structure

```text
├── app.py                # Streamlit 대시보드 (실행 파일)
├── pipeline.py           # 전체 분석 파이프라인 오케스트레이션
├── data_generator.py     # 가상 HCP CRM 데이터 생성 모듈
├── hcp_segmentation.py   # Step 1: HCP 세분화 모듈
├── churn_prediction.py   # Step 2: 이탈 위험 예측 모델 모듈
├── nba_recommender.py    # Step 3: NBA 추천 엔진 모듈
└── requirements.txt      # 필요 라이브러리 목록
```

## 🚀 Quick Start

### 1. 환경 설정
```bash
pip install -r requirements.txt
```

### 2. 대시보드 실행
```bash
streamlit run app.py
```

## 🔬 Key Features

- **Interactive Modeling**: 대시보드에서 직접 AI 파이프라인을 실행하고 시뮬레이션 데이터를 생성할 수 있습니다.
- **Churn Risk Analysis**: Gradient Boosting 모델을 통해 각 HCP의 이탈 확률(Churn Risk Score)을 산출합니다.
- **Actionable Insights**: 세그먼트와 이탈 위험도를 결합하여 즉시 실행 가능한 영업 가이드(채널, 콘텐츠, 빈도)를 제공합니다.

---
*Developed by Eun Woo Kim | February 2026*
