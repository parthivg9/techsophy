# backend/services/risk_service.py
from models.portfolio_analyzer import analyze_portfolio
from models.risk_concentration_model import identify_concentrations
import random

def get_risk_summary(policy_data):
    """
    Aggregates risk summary data.
    """
    portfolio_analysis = analyze_portfolio(policy_data)

    # Simulate VaR and Expected Loss based on total portfolio value
    total_portfolio_value = portfolio_analysis["total_portfolio_value"]
    value_at_risk = total_portfolio_value * (0.02 + random.uniform(0, 0.03)) # 2-5%
    expected_loss = total_portfolio_value * (0.005 + random.uniform(0, 0.01)) # 0.5-1.5%

    return {
        "total_portfolio_value": total_portfolio_value,
        "total_insured_value": total_portfolio_value * 1.1, # Dummy higher insured value
        "value_at_risk": value_at_risk,
        "expected_loss": expected_loss,
    }

def get_alerts():
    """
    Generates dummy alerts. In a real system, these would come from
    monitoring concentration models, stress test thresholds, etc.
    """
    return [
        { "id": 1, "type": "concentration", "message": "High exposure detected in Florida region for Home policies.", "severity": "High", "timestamp": "2025-07-04T10:00:00Z" },
        { "id": 2, "type": "correlation", "message": "Increased correlation between Auto and Commercial lines observed.", "severity": "Medium", "timestamp": "2025-07-03T14:30:00Z" },
        { "id": 3, "type": "stress_test", "message": "Economic downturn scenario shows potential losses exceeding threshold.", "severity": "High", "timestamp": "2025-07-02T09:15:00Z" },
    ]