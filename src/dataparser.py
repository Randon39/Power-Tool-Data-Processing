import pandas as pd
from torque_model import electrical_to_mechanical_torque

def load_datalogger_file(path):
    """Reads a .dat file from the datalogger (semicolon-separated) and returns a processed DataFrame."""
    df = pd.read_csv(path, header=None, sep=';')

    df.columns = ['datetime', 'current', 'voltage', 'watts', 'work']

    df['datetime'] = pd.to_datetime(df['datetime'], format='%d.%m.%Y:%H:%M:%S.%f', errors='coerce')
    df['current'] = pd.to_numeric(df['current'], errors='coerce')
    df['voltage'] = pd.to_numeric(df['voltage'], errors='coerce')
    df['watts']  = pd.to_numeric(df['watts'], errors='coerce')
    df['work']   = pd.to_numeric(df['work'], errors='coerce')

    return df


def compute_torque(df, K_T, B_T):
    """Adds a mechanical torque column to the DataFrame."""
    df['Torque'] = electrical_to_mechanical_torque(df['current'], K_T, B_T )
    df = df[df['Torque'] >= 0]  # removes negative values
    return df


def filter_working_points(df):
    """Keeps only the data points where the tool is actually curring (work == 1)."""
    df = df[df['work'] == 1].reset_index(drop=True)
    df['tempo_s'] = df.index / 50.0  # 50 Hz → 50 samples per second
    return df


def export_outputs(df, csv_path, excel_path):
    """Exports the final file to .CSV (for MATLAB/Simulink) and Excel (for auditing)."""
    df[['tempo_s','Torque']].to_csv(csv_path, index=False, header=False)
    df.to_excel(excel_path, index=False)
