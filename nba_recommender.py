import pandas as pd

def recommend_channel(row):
    high_risk = row['churn_risk_score'] > 0.6
    high_digital = row['digital_engagement_score'] > 15
    if high_risk and not high_digital:
        return '대면 방문 (Face-to-face)'
    elif high_risk and high_digital:
        return '화상 미팅 + 이메일'
    elif not high_risk and high_digital:
        return '이메일 + 웨비나'
    else:
        return '전화 + 대면 방문'

def recommend_content(row):
    if row['rx_change_pct'] < -10:
        return '경쟁 제품 비교 데이터 + 리텐션 오퍼'
    elif row['rx_change_pct'] > 10:
        return '신규 임상 데이터 + 처방 확대 프로그램'
    elif row['market_share'] < 20:
        return '효능/안전성 핵심 데이터 + KOL 동영상'
    else:
        return '최신 가이드라인 업데이트 + 환자 케이스'

def recommend_frequency(row):
    if row['churn_risk_score'] > 0.6:
        return '주 1회 (긴급)'
    elif row['churn_risk_score'] > 0.3:
        return '격주 1회'
    else:
        return '월 1회'

def apply_nba(df):
    df['priority_score'] = (
        df['rx_last_6m'] / df['rx_last_6m'].max() * 0.4 +
        df['churn_risk_score'] * 0.4 +
        df['market_share'] / df['market_share'].max() * 0.2
    ).round(3)
    
    df['nba_channel'] = df.apply(recommend_channel, axis=1)
    df['nba_content'] = df.apply(recommend_content, axis=1)
    df['nba_frequency'] = df.apply(recommend_frequency, axis=1)
    
    return df

if __name__ == "__main__":
    # Mocking data for test
    data = {
        'churn_risk_score': [0.8, 0.2],
        'digital_engagement_score': [5, 20],
        'rx_change_pct': [-15, 5],
        'market_share': [10, 30],
        'rx_last_6m': [100, 50]
    }
    df = pd.DataFrame(data)
    df = apply_nba(df)
    print(df[['nba_channel', 'nba_content']])
