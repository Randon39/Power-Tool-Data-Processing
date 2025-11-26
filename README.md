# Power-Tool-Data-Processing
This repository contains a modular Python workflow developed for processing laboratory measurement data of electric power tools.
The pipeline loads raw datalogger .dat files, parses time-series data (current, voltage, power, work flag), and converts electrical current into mechanical torque using a linear electromechanical model obtained via regression during brake-dynamometer experiments.

The code automatically:
- Identifies active cutting intervals
- removes invalid values
- generates clean torque traces sampled at 50 Hz
- exports them in both CSV (for MATLAB/Simulink integration) and Excel formats.

The project is part of a broader effort to characterize material-dependent usage profiles and support synthetic signal generation for dynamic modelling of electromechanical systems.

# DataLogger 
The raw data from the datalogger are '.dat' files containing:
- datetime
- current
- voltage
- watts
- work flag

A sample .dat file is included in the repository structure.
Adapt the parser or variable names as needed for your specific datalogger format.

The main objetctive is to generate:
- Processed CSV (Torque x Time) for Simulink
- Excel for review of output
- Clean datasets suitable for usage-profile studies or machine-learning applications (e.g., neural network training)


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
│
├── README.md                 # Project documentation
└── requirements.txt          # Python dependencies
```
