import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import roc_auc_score

def train_churn_model(df):
    le_spec = LabelEncoder()
    le_hosp = LabelEncoder()
    le_region = LabelEncoder()
    
    df['specialty_enc'] = le_spec.fit_transform(df['specialty'])
    df['hospital_type_enc'] = le_hosp.fit_transform(df['hospital_type'])
    df['region_enc'] = le_region.fit_transform(df['region'])
    
    df['rx_per_visit'] = (df['rx_last_6m'] / (df['visits_6m'] + 1)).round(1)
    df['total_touchpoints'] = df['visits_6m'] + df['calls_6m'] + df['emails_opened']
    
    feature_cols = [
        'specialty_enc', 'hospital_type_enc', 'region_enc', 'years_practice',
        'visits_6m', 'calls_6m', 'emails_opened', 'webinar_attended',
        'symposium_attended', 'digital_engagement_score',
        'rx_last_6m', 'rx_prev_6m', 'rx_change_pct', 'market_share',
        'rx_per_visit', 'total_touchpoints'
    ]
    
    X = df[feature_cols]
    y = df['churn']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    model = GradientBoostingClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    prob = model.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, prob)
    print(f"Model AUC: {auc:.4f}")
    
    # Assign scores to all
    df['churn_risk_score'] = model.predict_proba(X[feature_cols])[:, 1].round(3)
    df['churn_risk_level'] = pd.cut(df['churn_risk_score'],
                                    bins=[0, 0.3, 0.6, 1.0],
                                    labels=['🟢 Low Risk', '🟡 Medium Risk', '🔴 High Risk'])
    
    return df, model, feature_cols

if __name__ == "__main__":
    df = pd.read_csv('hcp_raw_data.csv')
    # Mocking pre-processing for standalone test
    df['specialty'] = df['specialty'].astype(str)
    df['hospital_type'] = df['hospital_type'].astype(str)
    df['region'] = df['region'].astype(str)
    df, _, _ = train_churn_model(df)
    print(df['churn_risk_level'].value_counts())
