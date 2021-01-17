Pyce Tools Manual
======================================

Introduction
------------

Ice Nucleating Particles (INP) are … One in a million particles act as INP at -20C

They are crucial to determining various properties of clouds, including precipitation rates, lifetime, shortwave reflectivity, and longwave emissivity. Since the effects of aerosols on cloud optical properties and radiative forcing is the single most uncertain component of radiative forcing of Earth’s climate, this makes understanding INP massively important.

The field is nascent and fast moving. Not only that, but uncertainty is on the scale of orders of magnitude.  Any time not spent wrangling and preprocessing data can be spent finding high impact results. Pyce Tools addresses these two problems. First, by offering a set of guidelines for INP data workup means less errors during data workup. Second, it’s easy to prepare, so you can spend less Spend less time working up your data, and more time finding high impact results.
This getting started guide briefly describes the Pyce Tools nomenclature, the raw data processing workflow, and the additional data analysis tools included in the package. Further details are found in the code documentation (in the pyce_tools.py file). Users can also reference the accompanying jupyter notebook tutorial file.

A final disclaimer: this code was written for the Sea2Cloud Tangaroa Cruise. As such, it assumes input files are organized in a certain way. I tried to keep things broad so that the code could be extended to future cases, but don’t be afraid tweak the source code as you see fit.

Important Definitions
---------------------
The Pyce Tools workflow has a very strict naming convention. For this reason, it’s important to first define some terms. INP samples come in various TYPES, which can be collected from a range of LOCATIONS, and are subject to different PROCESSES before analysis with the LINDA instrument.

.. py:attribute:: type

    [*aerosol, seawater, mq*] the category of the INP sample. This is most generally either seawater or aerosol. Note that if the sample is a seawater blank, it is defined as ‘mq’. If the sample is an aerosol blank, it is still classified as aerosol, since the blank used is a filter.


.. py:attribute:: location

    [*uway, wboatsml, wboatssw, bubbler, coriolis*] where the sample was collected. For instance, seawater type samples can come from the boat’s underway (uway) or from workboat deployments (wboat). Workboat measurements are further specified as either wboatsml or wboatssw depending on where in the water column the sample originated. Aerosol type INP samples can come from a bubbler, coriolis, or ambient measurements. For blanks samples, the location options are bubbler, Coriolis, mq, mq_wboat. This is kind of a weird naming convention. Sorry.


.. py:attribute:: process
    
     [*uf, f*] a technique used on an INP sample to gather more information. Possible processes include heating the sample or filtering it. Others include H2O2 but we do not do that in these samples. The way the code is written currently is that the process of either filtering or leaving samples unfiltered is described in the sample name, while heated and unheated is implicitly assumed to have been conducted during initial sample analysis. For this reason, only UF/F is specified in sample names.

These three terms defined above are used throughout the Pyce Tools workflow, which is described in the following section.

INP Analysis Workflow
---------------------
Throughout the workflow of an INP sample, several file types are made. They are termed raw, calculated, and cleaned. In general, the workflow and how each file type fits into it is generalized as follows:

1.	An INP sample of a specific :py:attr:`type` is collected from a specific :py:attr:`location`.
2.	The sample then undergoes whatever post-collection :py:attr:`process` the experimenter decides.
3.	The sample is analyzed with LINDA and raw data files are saved to their appropriate folder with the appropriate naming convention.
4.	Raw data files are then pre-processed into calculated report files using sample template spreadsheets. This step involves, among other things, subtraction of the blank (see `Blank Correction`_). Calculated report files are then saved to their appropriate folder.
5.	Calculated report files from the calculation step are then cleaned and saved as cleaned output files, which are ready for analysis. During this step, error bars can be calculated and saved in separate files as well.

The specifics of these steps are further described in the following sections.

Saving Raw Data Files
^^^^^^^^^^^^^^^^^^^^^^^^^^

It is imperative that raw files are saved in the correct location and with the correct names. The rules are described for the two sample :py:attr:`type` (i.e., aerosol or seawater).

**Seawater sample raw file are saved as**
    seawater_[location]_[process]_[DDMMYY]_[HHmm].csv

**Seawater sample type raw files are saved into the following folder**
    ..\\[PROJECT_ROOT]\\data\\raw\\IN\\[SAMPLE_TYPE]\\[FILE]

**Aerosol sample raw file are saved as** [#]_
    aerosol_[location]_[process]_[size]_[DDMMYYYY]_[HHmm].csv

**Aerosol sample type raw files are saved into the following folder** 
    ..\\[PROJECT_ROOT]\\data\\raw\\IN\\[SAMPLE_TYPE]\\[FILE]

   
|

.. [#] When I initially began creating this workflow for aerosol sample types, I named files using ‘dayXX’. This was bad and I should not have done it. For this reason, there’s a section of code that uses a hash table to allocate dayXX with specific dates and times. Unless you are analyzing these specific samples where I did this (i.e., Coriolis samples from Tan2020 S2C), you can ignore that section of code. Going forward, files should be saved using the convention outlined below.

Creating Calculated Sample Report Files from Raw Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Calculated report files are created by processing the raw data using either the calculate_raw_blank() or :py:func:`pyce_tools.calculate_raw` functions. Raw blank calculation is described in Section 3.3 below. Here we describe the process of creating a calculated sample report file for raw data, assuming that calculated blank data files are ready for use. [#]_

|

.. [#] Right now, only a single blank file is loaded. Eventually it would make sense to add functionality to average all relevant blank files into one file which is then subtracted from the data. For now, your best bet is to do this manually yourself by calculating several blank files individually (see Section 3.3 Blank Correction), and then averaging them into one blank file and passing that file as a parameter when calling the calculate_raw() function.

Raw data files are processed using template spreadsheets. There is a template for seawater and aerosol sample types which should be placed in your project root directory. These template spreadsheets have the necessary equations already inside of them so that the code simply needs to place the values in the correct locations. 
The overall process of calculating report files is as follows: 

1.	Raw file is loaded. 
2.	Metadata is calculated and listed for raw data source, type, location, process, sample source name, sample collection date, sample analysis date, number of tubes, ml per tube, issues, and sigma. Sigma is used for error bar calculation and should be left at 1.96 for confidence intervals of 95%.
3.	If the sample is aerosol type, additional metadata is calculated and used in INP calculation. These parameters are rinse volume, size, average flow, sample collection time (calculated from start and stop time) and total sampled air volume (calculated from sample collection time and average flow).
4.	Raw data is loaded into the template spreadsheet and calculations are made. 
5.	A blank data file is loaded into the template file and used to subtract from raw data. 

The calculated report file is then saved to its appropriate location according to the following convention:  
    \\[PROJECT_ROOT]\\data\\interim\\IN\\calculated\\[SAMPLE_TYPE]\\[SAMPLE_LOCATION]\\[type]_[location]_[process]_[date]_[time]_calculated.xlsx

You will want to check over the calculated report file yourself as the template may not calculate across all temperatures conducted in your specific experiment. Simply extending the equation further down to lower temperatures by dragging a cell should suffice. See the Tutorial in Section 6 for more information.


Blank Correction
-----------------