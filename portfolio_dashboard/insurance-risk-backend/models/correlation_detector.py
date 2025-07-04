# backend/models/correlation_detector.py
import pandas as pd
import numpy as np

def detect_correlations(policy_data):
    """
    Detects correlations between policy types.
    This is a placeholder. In a real scenario, this would involve
    feature engineering and statistical correlation methods.
    """
    # Return a dummy correlation matrix for demonstration
    policy_types = ['Auto', 'Home', 'Life', 'Commercial', 'Health']
    matrix = []
    for r_idx, r_type in enumerate(policy_types):
        row_data = {"name": r_type}
        for c_idx, c_type in enumerate(policy_types):
            if r_idx == c_idx:
                row_data[c_type] = 1.0
            elif r_idx < c_idx:
                # Generate random correlation for upper triangle
                corr_val = round(np.random.uniform(-0.4, 0.4), 2)
                row_data[c_type] = corr_val
            else:
                # Ensure symmetry by copying from the transposed position
                # This requires knowing the structure of the matrix
                # For simplicity, we'll just generate a random value too,
                # but in a real system, you'd ensure symmetry.
                # A more robust way would be to build a full numpy array and then convert.
                row_data[c_type] = round(np.random.uniform(-0.4, 0.4), 2) # simplified for this conceptual example
        matrix.append(row_data)

    # A more correct way to ensure symmetry for a DataFrame conversion:
    data_for_df = {}
    for r_type in policy_types:
        data_for_df[r_type] = {}
        for c_type in policy_types:
            if r_type == c_type:
                data_for_df[r_type][c_type] = 1.0
            elif r_type in data_for_df and c_type in data_for_df[r_type]:
                pass # Already set by symmetric counterpart
            else:
                val = round(np.random.uniform(-0.4, 0.4), 2)
                data_for_df[r_type][c_type] = val
                data_for_df[c_type][r_type] = val # Set symmetric value

    # Convert to the list of dicts format expected by the frontend
    final_matrix = []
    for r_type in policy_types:
        row_dict = {"name": r_type}
        for c_type in policy_types:
            row_dict[c_type] = data_for_df[r_type][c_type]
        final_matrix.append(row_dict)

    return final_matrix