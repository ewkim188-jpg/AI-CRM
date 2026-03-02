import numpy as np
import pandas as pd

def generate_hcp_data(n_hcps=500, seed=42):
    np.random.seed(seed)
    
    # --- HCP Basic Info ---
    specialties = np.random.choice(
        ['내과', '심장내과', '내분비내과', '신경과', '정형외과', '가정의학과'],
        n_hcps, p=[0.25, 0.15, 0.20, 0.15, 0.10, 0.15]
    )
    hospital_types = np.random.choice(
        ['대학병원', '종합병원', '개인병원', '의원'],
        n_hcps, p=[0.15, 0.25, 0.30, 0.30]
    )
    regions = np.random.choice(
        ['서울', '경기', '부산', '대구', '대전', '광주', '기타'],
        n_hcps, p=[0.30, 0.25, 0.10, 0.08, 0.07, 0.05, 0.15]
    )
    years_practice = np.random.randint(3, 35, n_hcps)

    # --- CRM Activity Data (recent 6m) ---
    visits_6m = np.random.poisson(lam=4, size=n_hcps)
    calls_6m = np.random.poisson(lam=3, size=n_hcps)
    emails_opened = np.random.poisson(lam=5, size=n_hcps)
    webinar_attended = np.random.binomial(3, 0.3, n_hcps)
    symposium_attended = np.random.binomial(2, 0.25, n_hcps)
    digital_engagement_score = np.clip(
        emails_opened * 2 + webinar_attended * 5 + np.random.normal(0, 3, n_hcps), 0, 50
    ).astype(int)

    # --- Prescription Data ---
    base_rx = np.where(np.isin(hospital_types, ['대학병원', '종합병원']),
                       np.random.normal(80, 25, n_hcps),
                       np.random.normal(35, 15, n_hcps))
    rx_last_6m = np.clip(base_rx + visits_6m * 3 + np.random.normal(0, 10, n_hcps), 5, 200).astype(int)
    rx_prev_6m = np.clip(rx_last_6m + np.random.normal(5, 15, n_hcps), 5, 200).astype(int)
    rx_change_pct = ((rx_last_6m - rx_prev_6m) / rx_prev_6m * 100).round(1)
    market_share = np.clip(np.random.normal(25, 12, n_hcps), 2, 65).round(1)

    # --- Churn (Target) ---
    churn_prob = 1 / (1 + np.exp(-(
        -0.3 
        + (-0.04 * rx_change_pct)
        + (-0.20 * visits_6m)
        + (-0.08 * digital_engagement_score)
        + (0.03 * years_practice)
        + np.random.normal(0, 0.5, n_hcps)
    )))
    churn = (np.random.random(n_hcps) < churn_prob).astype(int)

    # --- DataFrame ---
    df = pd.DataFrame({
        'hcp_id': [f'HCP_{i:04d}' for i in range(n_hcps)],
        'specialty': specialties,
        'hospital_type': hospital_types,
        'region': regions,
        'years_practice': years_practice,
        'visits_6m': visits_6m,
        'calls_6m': calls_6m,
        'emails_opened': emails_opened,
        'webinar_attended': webinar_attended,
        'symposium_attended': symposium_attended,
        'digital_engagement_score': digital_engagement_score,
        'rx_last_6m': rx_last_6m,
        'rx_prev_6m': rx_prev_6m,
        'rx_change_pct': rx_change_pct,
        'market_share': market_share,
        'churn': churn
    })
    
    return df

if __name__ == "__main__":
    df = generate_hcp_data()
    print(df.head())
    df.to_csv('hcp_raw_data.csv', index=False)
