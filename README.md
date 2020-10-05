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