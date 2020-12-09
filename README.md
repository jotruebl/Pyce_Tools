# Pyce Tools

A PYthon library for loading, cleaning, and analyzing iCE nucleating particle (INP) data. :ice_cube:

Pyce Tools allows users to easily:

* Create experiment report files (xlsx format) by loading and processing raw experiment (or blank) csv data files of seawater or filter extract samples obtained from the LED-based Ice Nucleation Detection Apparatus (LINDA).
* Create cleaned, combined time series files from experiment report files for further processing and analysis in Python.
* Load and wrangle inverted differential mobility particle sizer (DMPS) data from LAMP's Scanotron instrument and condensation particle counter (CPC, TSI Inc.) time series data files into single time series files which are readily manipulated for further exploratory data analysis (EDA).
* Load pre-processed DMPS data files for EDA.
* Plot time series of particle surface area and number size distributions.
* Create plots of common INP graphs, including comparison with literature values.
* Normalize INP concentrations by particle surface area.
* Calculate and plot correlations between seawater parameters and INP concentrations.


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

* :heavy_check_mark: Clean and prep LINDA experiment report files into a single time series dataset for exploratory analysis (error bars and data) --> clean_calculated_in;calculate_wilson_errors
* :heavy_check_mark: Include functions for plotting surface area and number size distribution timeseries (error bars included) --> plot_number_dist; plot_surface_dist
* Function for downsampling to average of user-selected time periods.
* :heavy_check_mark: Include function for plotting common INP plots
* :heavy_check_mark: Improve time zone handling
* :heavy_check_mark: Include function for creating error bars for ice nucleating particles --> calculate_wilson_errors
* :heavy_check_mark: Include function for calculating INP concentrations normalized by particle surface area
* :heavy_check_mark: Include function for calculating correlations
* :heavy_check_mark: Include function for calculating particle surface areas --> surface_area
* :construction: Update documentation
* :heavy_check_mark: Include function for calculating and loading uncertainties
* update clean_aqualog function


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

MIT License

Copyright (c) 2020 Jonathan V. Trueblood

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.