# Power-Tool-Data-Processing
This repository contains a modular Python workflow developed for processing laboratory measurement data of electric power tools.
The pipeline loads raw datalogger .dat files, parses time-series data (current, voltage, power, work flag), and converts electrical current into mechanical torque using a linear electromechanical model obtained via regression during brake-dynamometer experiments.
The system automatically filters active cutting intervals, removes invalid values, generates clean torque traces sampled at 50 Hz, and exports them in both CSV (for MATLAB/Simulink integration) and Excel formats.
The project is part of a broader effort to characterize material-dependent usage profiles and support synthetic signal generation for dynamic modelling of electromechanical systems.

# DataLogger 
The raw data from the datalogger are '.dat' files containing:
- datetime
- current
- voltage
- watts
- work flag

(There is a sample data as example in this repository structure and it's to change the variables to atend your needs)

The main objetctive is to generate:
- Processed CSV (Torque x Time) for Simulink
- Excel for review of output
- Dataset processed for the sutudy of usage profiles (Neural Network training)


# Structure
```text
power-tools-data-processing/
│
├── src/
│   ├── torque_model.py       # Current → torque conversion model (linear regression from brake dynamometer)
│   ├── dataparser.py         # Loader and parser for .dat files
│   └── main.py               # Main processing script: filtering, export, pipeline execution
│
├── data/
│   ├── raw/                  # Put your raw .dat files here
│   └── processed/            # Automatically generated CSV and Excel outputs
│
├── notebooks/                # Optional exploratory analysis notebooks
│
├── README.md                 # Project documentation
└── requirements.txt          # Python dependencies
```
