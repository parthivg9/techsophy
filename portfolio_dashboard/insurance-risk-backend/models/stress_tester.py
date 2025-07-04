# backend/models/stress_tester.py
import random

def run_stress_test(policy_data, scenario):
    """
    Runs a stress test for a given scenario.
    This is a placeholder. Real implementation would involve
    complex simulations and financial modeling.
    """
    # Simulate loss based on scenario
    loss_multiplier = {
        'Major Hurricane': 0.15,
        'Economic Downturn': 0.10,
        'Cyber Attack': 0.07,
        'Pandemic Outbreak': 0.18,
        'Interest Rate Hike': 0.03,
        'default': 0.05
    }
    base_loss = sum(p.get('insured_value', 0) for p in policy_data) * loss_multiplier.get(scenario, loss_multiplier['default'])
    simulated_loss = base_loss * (1 + random.uniform(-0.1, 0.1)) # Add some randomness

    return {
        "scenario": scenario,
        "estimated_loss": round(simulated_loss, 0),
        "impact_description": f"Simulated impact of {scenario} on portfolio."
    }