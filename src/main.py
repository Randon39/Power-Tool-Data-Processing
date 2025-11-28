import os
from dataparser import (
    load_datalogger_file,
    compute_torque,
    filter_working_points,
    export_outputs
)

# Main Path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_FOLDER = os.path.join(PROJECT_ROOT, "data", "raw")
PROCESSED_FOLDER = os.path.join(PROJECT_ROOT, "data", "processed")

# Linear Regression
K_T = 0.28 # Slope
B_T = 2.2  # Intercept

def process_all_files():
    print("RAW_FOLDER =", RAW_FOLDER)
    print("PROCESSED_FOLDER =", PROCESSED_FOLDER)

    if not os.path.isdir(RAW_FOLDER):
        raise FileNotFoundError(f" Folder not found: {RAW_FOLDER}")

    os.makedirs(PROCESSED_FOLDER, exist_ok=True)

    for file in os.listdir(RAW_FOLDER):
        if not file.endswith(".dat"):
            continue

        print(f"\nProcessing: {file}")

        path = os.path.join(RAW_FOLDER, file)
        df = load_datalogger_file(path)
        df = compute_torque(df, K_T, B_T)
        df = filter_working_points(df)

        csv_out = os.path.join(PROCESSED_FOLDER, file.replace(".dat", ".csv"))
        excel_out = os.path.join(PROCESSED_FOLDER, file.replace(".dat", ".xlsx"))

        export_outputs(df, csv_out, excel_out)

        print(f"→ Arquivos gerados:\n   {csv_out}\n   {excel_out}")

if __name__ == "__main__":
    process_all_files()
