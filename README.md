# Pyce Tools

A PYthon library for calculating, cleaning, and analyzing iCE nucleating particle (INP) data. :ice_cube:

Pyce Tools allows users to easily:

* Create experiment report files (xlsx format) by loading and processing raw experiment (or blank) csv data files of seawater or filter extract samples obtained from the LED-based Ice Nucleation Detection Apparatus (LINDA).
* Create cleaned, combined time series files from experiment report files for further processing and analysis in Python.
* Load and wrangle inverted differential mobility particle sizer (DMPS) data from LAMP's Scanotron instrument and condensation particle counter (CPC, TSI Inc.) time series data files into single time series files which are readily manipulated for further exploratory data analysis (EDA).
* Plot time series of particle surface area and number size distributions.
* Create plots of common INP graphs, including comparison with literature values.
* Normalize INP concentrations by particle surface area.
* Calculate and plot correlations between seawater parameters and INP concentrations.

## Getting Started

See the getting_started guide for a general overview and introduction to Pyce Tools.

## Installation

For now, Pyce Tools is installed simply by cloning this repository into your workspace.

## Requirements

* Pandas
* openpyxl
* datetime
* Plotly
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


## Planned Updates

* :heavy_check_mark: Clean and prep LINDA experiment report files into a single time series dataset for exploratory analysis (error bars and data) 
* :heavy_check_mark: Include functions for plotting surface area and number size distribution timeseries (error bars included)
* :heavy_check_mark: Include function for plotting common INP plots
* :heavy_check_mark: Improve time zone handling
* :heavy_check_mark: Include function for creating error bars for ice nucleating particles 
* :heavy_check_mark: Include function for calculating INP concentrations normalized by particle surface area
* :heavy_check_mark: Include function for calculating correlations
* :heavy_check_mark: Include function for calculating particle surface areas 
* :construction: Update documentation
* :heavy_check_mark: Include function for calculating and loading uncertainties
* :construction: update clean_aqualog function


## Contributing

Feel free to download the source code and alter for your specific needs.

## License

MIT License