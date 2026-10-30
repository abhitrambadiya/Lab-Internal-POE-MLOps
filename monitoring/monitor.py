"""
Evidently AI Model & Data Quality Monitoring Script.
Evaluates baseline dataset vs current inference dataset to detect:
1. Feature Drift (DataDriftPreset)
2. Summary statistics & data distribution characteristics (DataSummaryPreset)
"""
import os
import numpy as np
import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset, DataSummaryPreset

def run_evidently_monitoring(output_dir="monitoring/reports"):
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Generate baseline reference data (Simulating normal production distribution)
    np.random.seed(42)
    n_samples = 200
    reference_data = pd.DataFrame({
        "feature_x": np.random.normal(loc=20.0, scale=3.5, size=n_samples),
        "feature_y": np.random.normal(loc=50.0, scale=8.0, size=n_samples),
        "target": np.random.choice([0, 1], size=n_samples, p=[0.6, 0.4])
    })
    
    # 2. Generate current data (Simulating distribution drift in feature_x)
    current_data = pd.DataFrame({
        "feature_x": np.random.normal(loc=26.5, scale=4.0, size=n_samples), # drifted
        "feature_y": np.random.normal(loc=50.2, scale=8.1, size=n_samples), # stable
        "target": np.random.choice([0, 1], size=n_samples, p=[0.55, 0.45])
    })
    
    # 3. Configure and execute Evidently Report
    report = Report([DataDriftPreset(), DataSummaryPreset()])
    
    print("[INFO] Computing Data Drift and Quality metrics across datasets...")
    snapshot = report.run(reference_data=reference_data, current_data=current_data)
    
    html_file = os.path.join(output_dir, "evidently_drift_report.html")
    json_file = os.path.join(output_dir, "evidently_drift_report.json")
    
    snapshot.save_html(html_file)
    snapshot.save_json(json_file)
    
    print(f"[SUCCESS] Evidently Drift HTML Report generated at: {html_file}")
    print(f"[SUCCESS] Evidently Drift JSON Metrics generated at: {json_file}")
    return html_file, json_file

if __name__ == "__main__":
    run_evidently_monitoring()
