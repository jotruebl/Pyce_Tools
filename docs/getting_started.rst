Getting Started with Pyce Tools
======================================

1.0 Introduction
-----------------

Ice Nucleating Particles (INP) are crucial to determining various properties of clouds, including precipitation rates, lifetime, shortwave reflectivity, and longwave emissivity. Since the effects of aerosols on cloud optical properties and radiative forcing is the single most uncertain component of radiative forcing of Earth’s climate, this makes understanding INP massively important.

The field is nascent and fast moving. Not only that, but uncertainty is on the scale of orders of magnitude. Any time not spent wrangling and preprocessing data can be spent finding high impact results. Pyce Tools addresses these two problems. First, by offering a set of guidelines for INP data workup means less errors during data workup. Second, it’s easy to prepare, so you can spend less Spend less time working up your data, and more time finding high impact results.
This getting started guide briefly describes the Pyce Tools nomenclature, the raw data processing workflow, and the additional data analysis tools included in the package. Further details are found in the code documentation (in the pyce_tools.py file). Users can also reference the accompanying jupyter notebook tutorial file.

**A final disclaimer:** this code was written for the Sea2Cloud Tangaroa Cruise. As such, it assumes input files are organized in a certain way. I tried to keep things broad so that the code could be extended to future cases, but don’t be afraid tweak the source code as you see fit.

2.0 Important Definitions
-------------------------
The Pyce Tools workflow has a very strict naming convention. For this reason, it’s important to first define some terms. INP samples come in various TYPES, which can be collected from a range of LOCATIONS, and are subject to different PROCESSES before analysis with the LINDA instrument.

.. py:attribute:: type

    [*aerosol, seawater, mq*] the category of the INP sample. This is most generally either seawater or aerosol. Note that if the sample is a seawater blank, it is defined as ‘mq’. If the sample is an aerosol blank, it is still classified as aerosol, since the blank used is a filter.


.. py:attribute:: location

    [*uway, wboatsml, wboatssw, bubbler, coriolis*] where the sample was collected. For instance, seawater type samples can come from the boat’s underway (uway) or from workboat deployments (wboat). Workboat measurements are further specified as either wboatsml or wboatssw depending on where in the water column the sample originated. Aerosol type INP samples can come from a bubbler, coriolis, or ambient measurements. For blanks samples, the location options are bubbler, Coriolis, mq, mq_wboat. This is kind of a weird naming convention. Sorry.


.. py:attribute:: process
    
     [*uf, f*] a technique used on an INP sample to gather more information. Possible processes include heating the sample or filtering it. Others include H2O2 but we do not do that in these samples. The way the code is written currently is that the process of either filtering or leaving samples unfiltered is described in the sample name, while heated and unheated is implicitly assumed to have been conducted during initial sample analysis. For this reason, only UF/F is specified in sample names.

These three terms defined above are used throughout the Pyce Tools workflow, which is described in the following section.

3.0 INP Pre-processing Workflow
--------------------------------
Throughout the workflow of an INP sample, several file types are made. They are termed raw, calculated, and cleaned. In general, the workflow and how each file type fits into it is generalized as follows:

1.	An INP sample of a specific :py:attr:`type` is collected from a specific :py:attr:`location`.
2.	The sample then undergoes whatever post-collection :py:attr:`process` the experimenter decides.
3.	The sample is analyzed with LINDA and raw data files are saved to their appropriate folder with the appropriate naming convention.
4.	Raw data files are then pre-processed into calculated report files using sample template spreadsheets. This step involves, among other things, subtraction of the blank (see `3.3 Blank Correction`_). Calculated report files are then saved to their appropriate folder.
5.	Calculated report files from the calculation step are then cleaned and saved as cleaned output files, which are ready for analysis. During this step, error bars can be calculated and saved in separate files as well.

The specifics of these steps are further described in the following sections.

3.1 Saving Raw Data Files
^^^^^^^^^^^^^^^^^^^^^^^^^^

It is imperative that raw files are saved in the correct location and with the correct names. The rules are described for the two sample :py:attr:`type` (i.e., aerosol or seawater).

**Seawater sample raw file are saved as**
    seawater_[LOCATION]_[PROCESS]_[DDMMYY]_[HHmm].csv

**Seawater sample type raw files are saved into the following folder**
    \\[PROJECT_ROOT]\\data\\raw\\IN\\[SAMPLE_TYPE]\\[FILE]

**Aerosol sample raw file are saved as** [#]_
    aerosol_[LOCATION]_[PROCESS]_[SIZE]_[DDMMYY]_[HHmm].csv

**Aerosol sample type raw files are saved into the following folder** 
    \\[PROJECT_ROOT]\\data\\raw\\IN\\[SAMPLE_TYPE]\\[FILE]

   
|

.. [#] When I initially began creating this workflow for aerosol sample types, I named files using ‘dayXX’. This was bad and I should not have done it. For this reason, there’s a section of code that uses a hash table to allocate dayXX with specific dates and times. Unless you are analyzing these specific samples where I did this (i.e., Coriolis samples from Tan2020 S2C), you can ignore that section of code. Going forward, files should be saved using the convention outlined here.

3.2 Creating Calculated Sample Report Files from Raw Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Calculated report files are created by processing the raw data using either the :py:func:`.calculate_raw_blank` or :py:func:`.calculate_raw` functions. Raw blank calculation is described in Section `3.3 Blank Correction`_ below. Here we describe the process of creating a calculated sample report file for raw data, assuming that calculated blank data files are ready for use. [#]_

|

.. [#] Right now, only a single blank file is loaded. Eventually it would make sense to add functionality to average all relevant blank files into one file which is then subtracted from the data. For now, your best bet is to do this manually yourself by calculating several blank files individually (see Section `3.3 Blank Correction`_), and then averaging them into one blank file and passing that file as a parameter when calling the :py:func:`.calculate_raw` function.

Raw data files are processed using template spreadsheets. There is a template for seawater and aerosol sample :py:attr:`type` which should be placed in your project root directory. These template spreadsheets have the necessary equations already inside of them so that the code simply needs to place the values in the correct locations. 

The overall process of calculating report files is as follows: 

1.	Raw file is loaded. 
2.	Metadata is calculated and listed for raw data source, :py:attr:`type`, location, process, sample source name, sample collection date, sample analysis date, number of tubes, ml per tube, issues, and sigma. Sigma is used for error bar calculation and should be left at 1.96 for confidence intervals of 95%.
3.	If the sample is of :py:attr:`type` aerosol, additional metadata is calculated and used in INP calculation. These parameters are rinse volume, size, average flow, sample collection time (calculated from start and stop time) and total sampled air volume (calculated from sample collection time and average flow).
4.	Raw data is loaded into the template spreadsheet and calculations are made. 
5.	A blank data file is loaded into the template file and used to subtract from raw data. 

The calculated report file is then saved to its appropriate location according to the following convention:  
    *\\[PROJECT_ROOT]\\data\\interim\\IN\\calculated\\[SAMPLE_TYPE]\\[SAMPLE_LOCATION]\\[TYPE]_[LOCATION]_[PROCESS]_[DDMMYY]_[HHmm]_calculated.xlsx*

You will want to check over the calculated report file yourself as the template may not calculate across all temperatures conducted in your specific experiment. Simply extending the equation further down to lower temperatures by dragging a cell should suffice. See the Tutorial in Section 6 for more information.


3.3 Blank Correction
^^^^^^^^^^^^^^^^^^^^
As mentioned in the previous section, INP raw data files from the LINDA need to be blank corrected. To do this, blanks are collected, analyzed with LINDA, calculated with :py:func:`.calculate_raw_blank`, and finally subtracted from experiment raw data files using the :py:func:`.calculate_raw` function.

When conducting LINDA experiments, the name of the blank file should follow this naming template specified below.

For seawater :py:attr:`type` samples:
    mq_blank_[PROCESS]_[DDMMYY].csv

For aerosol :py:attr:`type` samples:
    [TYPE]_blank_[PROCESS]_[SIZE]_[DDMMYY].csv


The calculated report file will include metadata on the following: raw data source, :py:attr:`type`, :py:attr:`location`, :py:attr:`process`, sample source name, sample collection date, sample analysis date, number of tubes, volume per tube in mL.

If the sample is of :py:attr:`type` aerosol, the metadata will also include rinse volume and aeorosol size regime.

The calculated report file is then saved to the appropriate folder. See :py:func:`.calculate_raw` for specifics.

3.4 Cleaning Calculated Report Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :py:func:`.clean_calculated_in` function loads and cleans each calculated report file into a format that’s easier to use in Python. Some processes carried out by this function include renaming columns, reshaping the dataframes, and most importantly, combining all the calculated report files into a single time series file. This means you will want to ensure each project or experiment has its own folder so that results from different projects don't get combined into a single time series. 

The output of this function is a csv file where each row is an observation and each column is a temperature. Seawater sample types will also have columns for datetime, time, process, type, location, and filtered/unfiltered indicator. The IN values are given in IN/mL of water.
 
 In addition to the columns listed above, aerosol sample types from the bubbler or Coriolis will also have size (bubbler only), start_date and stop_date. IN values are given in INP/L of air.

Cleaned files are saved to: 
    *\\[PROJECT_ROOT]\\data\\interim\\IN\\cleaned\\combinedtimeseries\\[SAMPLE_TYPE]\\[LOCATION]_[START_DATE]_[END_DATE].csv*

3.4.1 Calculating Confidence Intervals
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Error bars are usually given as xxx. This is carried out using :py:func:`.calculate_wilson_errors`. The function itself is not pretty but it gets the job done. The output csv file is saved in the same location as the cleaned combined time series data file described in Section `3.4 Cleaning Calculated Report Files`_ and with the same naming convention, but with ‘wilson_error’ appended to the end.

Lower and upper bounds for blank subtracted frozen fraction of tubes (upperBound, lowerBound) are calculated using subfunctions (:py:func:`.wilsonLower` and :py:func:`.wilsonUpper`). These fractions are then converted to a number of blank subtracted tubes that are frozen (upper_N-BLNK, lower_N-BLNK, respectively). These bounds are then converted into INP/tube upper and lower bounds. Then they are converted to IN/mL and IN/L upper and lower bounds. Finally, the difference between each bound and the original observed value is calculated to determine the size of the error bars and saved as error_y and error_minus_y. The confidence interval of the uncertainty can be changed by using a different sigma value in the template spreadsheets.

For seawater samples, the units are INP/L seawater. For aerosol samples, the units are INP/L air.

3.5 Loading and Final Pre-Preprocessing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

While Pyce Tools does a bulk of the necessary manipulations and pre-processing, there’s a few steps that should still be completed after loading the cleaned combined timeseries files. This is left to the user’s discretion as the specifics of each experiment will vary considerably. For reference, the preprocessing steps carried out for S2C data are shown below:

- Convert datetime column to a pandas datetime index
- Melt the dataframe 
- Calculate different units
- Round to nearest hour
- Set to NZ time zone
- Merge uncertainty and concentration dataframes

The code for these steps can be found in the jupyter notebook that accompanies the Section XX Tutorial.

4.0 Handling Particle Size Distribution Data
---------------------------------------------
Particle size distribution data is crucial as it is needed to calculate surface area normalized INP concentrations of SSA. Pyce Tools includes some functions for loading, visualizing, and preparing size distribution data for normalization of INP.

Inverted data from the scanotron is cleaned and concatenated into a single combined timeseries file  using :py:func:`.clean_inverted` function. For processing, all inverted files should be saved into a single folder. 

Here, we choose the following directory path:
    *\\[PROJECT_ROOT]\\data\\interim\\scanotron\\inverted\\pro\\[FILE]*
The output path for the cleaned size distribution file can be defined by the user. Here we choose the following:
    *\\[PROJECT_ROOT]\\data\\interim\\scanotron\\combinedtimeseries\\*

Inverted concentrations from the scanotron are usually lognormalized. As such, the :py:func:`.clean_inverted` function accepts the number of size bins as a parameter for calculation of raw counts.

After cleaning inverted scanotron data, it can be loaded into a workspace using :py:func:`.load_scano_data` and further manipulated. Parameters for the :py:func:`.load_scano_data` function include dates, which is the name of the combined time series file you want to load, and instr, which tells where the file is located. 
The :py:func:`pyce_tools` modules for further information on the rest of the functions, which include:

- Surface area can be calculated using :py:func:`.surface_area`
- Magic CPC data can be cleaned using :py:func:`.clean_magic`
- Create plots using :py:func:`.plot_number_dist` and :py:func:`.plot_surface_dist`

5.0 Analysis
-------------

Pyce Tools currently has functions for several basic analyses. In the following section, we will describe them. See the tutorial attached for a complete overview of how to use them.

5.1 Creating INP Objects
^^^^^^^^^^^^^^^^^^^^^^^^^
Analysis of INP data is achieved using the INP class. An INP class object consists of INP data of a single type from a single location, a uway_bio dataframe consisting of observations from the ships underway, and a cyto_bio dataframe which can have further biology data from any location. In this way, we have a final INP object consisting of INP data from a specific location and of a certain type, which will contain multiple processes and temperatures and filtered/unfiltered states. 

See the tutorial for how to construct an INP class object from data. INP objects are instantiated when given an inp_type, inp_location, cyto_location, a cyto_data dataframe, a uway_bio dataframe, and an inp_data dataframe. See the pyce_tools.py file for in depth details.

It is important that the index in the INP dataframe be titled ‘datetime’ and be a datetime object. Code for how to do this is found in the tutorial section. Note that you can pass in a dataframe consisting of multiple locations and types, but the code will automatically keep only the data that corresponds to your selected type and location as defined when instantiating the object.

The uway_bio dataframe can include any data. The only requirements are that the index is a datetime object with the name ‘datetime’ so that it can be lined up correctly with the INP observations and a location column is defined.

The cyto_data dataframe will look similar to the uway_bio dataframe. Again, you can pass in a cyto_bio dataframe that contains a mixture of locations, but the function will automatically only keep data from your specified location. This means you need to make multiple objects if you have cyto data from multiple locations.

5.2 Calculating Surface Area Normalized INP Concentrations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Surface area normalized INP concentrations are calculated using the inp object’s :py:func:`pyce_tools.pyce_tools.inp.sa_normalize` method. The dA_total dataframe, which is returned from the :py:func:`.surface_area` function, is passed as a parameter. This function assumes you have already organized dA_total to line up with your INP collection periods. See the tutorial for specifics.

5.3 Plotting with error bars and previous studies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A plot of aerosol INP vs literature values is done through the :py:func:`pyce_tools.pyce_tools.inp.plot_ins_inp` method. Note that seawater INP (ssw and sml) plots are not object methods but rather Pyce Tools functions (:py:func:`.plot_sml_inp`, :py:func:`.plot_ssw_inp`). 

5.4 Correlations and correlation scatter plots
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Correlations are calculated using INP object’s :py:func:`pyce_tools.pyce_tools.inp.correlations` method. A list of temperatures as strings are sent, as well as a specific process (H, or UH) and inp_units string, which indicates the column containing your INP concentrations. See tutorial and code documentation for more details.
The correlations can also be viewed with scatter plots by using the :py:func:`pyce_tools.pyce_tools.inp.plot_corr_scatter` method, which returns a figure object which can be further stylized.
