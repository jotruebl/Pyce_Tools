# Pyce Tools

A PYthon library for loading, cleaning, and analyzing iCE nucleating particle (INP) data. :ice_cube:

Pyce Tools allows users to easily:

* Create experiment report files (xlsx format) by loading and processing raw experiment (or blank) csv data files from the LED-based Ice Nucleation Detection Apparatus (LINDA).
* Load and wrangle inverted differential mobility particle sizer (DMPS) data from LAMP's Scanotron instrument and condensation particle counter (CPC, TSI Inc.) time series data files into single time series files which are readily manipulated for further exploratory data analysis (EDA).
* Load pre-processed DMPS data files for EDA.

## Installation

For now, Pyce Tools is installed simply by cloning this repository into your workspace.

## Requirements

* Pandas
* openpyxl
* datetime
* *Recommended:* Jupyter Notebooks

## Usage

In your Jupyter Notebook (or equivalent workspace), alter your system path to include pyce_tools root folder:
```
import sys
sys.path.append('PATH\\TO\\PYCE_TOOLS')
```

Then, import Pyce Tools by typing the following:
```
import pyce_tools.pyce_tools as pt
```


## TO DO

* Load LINDA experiment report files into a single time series dataset for exploratory analysis.
* Include function for plotting DMPS timeseries (see scanotron_magic_BHS) and downsampling to average of user-selected time periods.
* Include function for plotting common INP plots
* Include function for creating error bars for scanotron and ice nucleating particles (the INP uncertainties are created in spreadsheet, but more needs to be done before they can be plotted with plotly..see PEACETIME Revised Plots notebook)
* Include function for calculating INP concentrations normalized by particle surface area (see nz2020 in_bio_analysis notebook)
* Include function for calculating correlation terms (see PEACETIME notebooks)
* Include function for calculating particle surface areas (see nz2020 in_bio_analysis notebook)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)