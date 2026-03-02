import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_generator import generate_hcp_data
from hcp_segmentation import perform_segmentation
from churn_prediction import train_churn_model
from nba_recommender import apply_nba

def run_pipeline():
    print("--- 🏥 AI-Powered CRM Enhancement Pipeline Starting ---")
    
    # Step 0: Data Generation
    print("\n[Step 0] Generating Synthetic HCP Data...")
    df = generate_hcp_data(n_hcps=500)
    
    # Step 1: Segmentation
    print("[Step 1] Performing HCP Segmentation (K-Means)...")
    df, km, scaler = perform_segmentation(df, n_clusters=4)
    
    # Step 2: Churn Prediction
    print("[Step 2] Training Churn Prediction Model (Gradient Boosting)...")
    df, model, features = train_churn_model(df)
    
    # Step 3: NBA
    print("[Step 3] Applying Next Best Action Recommender...")
    df = apply_nba(df)
    
    # Save Results
    output_file = 'hcp_nba_results.csv'
    df.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(f"\n✅ Pipeline Complete! Results saved to '{output_file}'")
    
    # Visualizations (Simplified representation)
    print("\n[Step 4] Generating Visualizations...")
    plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.rcParams['axes.unicode_minus'] = False
    sns.set_style('whitegrid')
    
    # Plot 1: Segmentation and Churn Risk
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    # Segment Distribution
    df['segment_name'].value_counts().plot(kind='bar', ax=axes[0], color='skyblue')
    axes[0].set_title('HCP 세그먼트 분포', fontweight='bold')
    axes[0].tick_params(axis='x', rotation=30)
    
    # Churn Risk Distribution
    risk_counts = df['churn_risk_level'].value_counts()
    axes[1].pie(risk_counts, labels=risk_counts.index, autopct='%1.1f%%', colors=['lightgreen', 'orange', 'red'])
    axes[1].set_title('이탈 위험군 분포', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('pipeline_summary.png', dpi=150)
    print("📈 Visualization saved as 'pipeline_summary.png'")
    
    # Top 10 High Priority HCPs
    print("\n--- 🚨 Top 10 High Priority HCPs ---")
    top10 = df.nlargest(10, 'priority_score')[['hcp_id', 'segment_name', 'churn_risk_level', 'nba_channel', 'nba_content']]
    print(top10.to_string(index=False))

if __name__ == "__main__":
    run_pipeline()
