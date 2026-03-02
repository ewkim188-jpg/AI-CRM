import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

def perform_segmentation(df, n_clusters=4):
    seg_features = ['rx_last_6m', 'rx_change_pct', 'visits_6m', 'calls_6m',
                    'digital_engagement_score', 'market_share', 'years_practice']
    
    scaler = StandardScaler()
    X_seg = scaler.fit_transform(df[seg_features])
    
    km = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    df['segment'] = km.fit_predict(X_seg)
    
    # Define Segment Labels
    seg_summary = df.groupby('segment').agg({
        'rx_last_6m': 'mean',
        'digital_engagement_score': 'mean',
        'churn': 'mean'
    }).sort_values('rx_last_6m', ascending=False)
    
    label_names = ['🏆 Champions (고처방/고인게이지)', '⭐ Growth Potential (중처방/성장가능)',
                   '⚠️ At Risk (중처방/이탈위험)', '🔻 Low Priority (저처방/저인게이지)']
    
    seg_labels = {seg_id: label_names[min(i, len(label_names)-1)] 
                  for i, seg_id in enumerate(seg_summary.index)}
    
    df['segment_name'] = df['segment'].map(seg_labels)
    
    return df, km, scaler

if __name__ == "__main__":
    df = pd.read_csv('hcp_raw_data.csv')
    df, _, _ = perform_segmentation(df)
    print(df['segment_name'].value_counts())
