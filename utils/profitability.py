def calculate_profitability(price, airbnb_metrics, risk_score=3):
    revenue = airbnb_metrics['Annual_Revenue']
    expenses = 0.5 * revenue
    noi = revenue - expenses
    cap_rate = (noi / price) * 100

    return {
        'Home Price': round(price),
        'ADR': airbnb_metrics['ADR'],
        'Occupancy Rate': airbnb_metrics['Occupancy'],
        'Annual Revenue': revenue,
        'NOI': noi,
        'Cap Rate': round(cap_rate, 2),
        'Risk Score': risk_score
    }
