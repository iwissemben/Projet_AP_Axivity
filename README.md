
# Projet Activité Physique: Tracker Axivity
![Hiking photo as physical activity illustration](illustrations/physical_activity_2.jpg)

## Description

 This repository is for a group project dedicated to the Activity tracker Axivity AX3 as part of the HAH913E "Activité Physique" course. 

 With this project we aim to:
  - Learn to collect and handle accelerometric data.
  - Analyze it in regard to scientific findings (publications).
  - Draw educated guesses on the level of physicial activity and global health of the participants.

### Scientific question
The scientific question we aimed to investigate was how the use of an  accelerometer can allow us to evaluate the physical activity level (<b>PAL</b>) of a subject. 

Our work, informed by the publications listed in the [Bibliography](##Bibliography) led us to use the Euclidian Norm Minus One (<b>ENMO</b>) and the Mean Amplitude Deviation (<b>MAD</b>) as they are good indicators of the level of physical activity (<b>PAL</b>).


![Results data as physical activity illustration](illustrations/results_hiking_short.png)


 ### Tools
 1. The [Axivity AX3 ](https://axivity.com/product/ax3) tracker, a data logger containing a 3-axis accelerometer used to collect longitudinal movement data.
 2. OpenLab's [AX3 GUI](https://github.com/digitalinteraction/openmovement/wiki/AX3-GUI) software for windows was used to configure the axivity tracker (recording start, frequency sampling, sensitivity, etc.) access, read and export the data as `.CSV` files.   
 3. Python scripts 
    - [`Resampler.py`](src/Resampler.py) To resample the raw accelerometer data.
    - [`main.py`](src/main.py) To use the acceleration data, calculate the variables of interest related to physical activity, segment the data into activity periods, classifiy these periods according to activity intensity using tresholds, and plot the results.


<p align="center">
  <img src="illustrations/logos/axivity_logo.png" height="100" alt="Python logo illustration" />
  <img src="illustrations/logos/python_logo.svg" height="80" alt="Axivity logo illustration" />
</p>

### Data collection

<p align="center">
  <img src="illustrations/ax3_band_1.jpg" height="300" alt="Python logo illustration" />
  <img src="illustrations/ax3_hand_1.jpg" height="300" alt="Axivity logo illustration" />
  <img src="illustrations/ax3_orientation.jpg" height="300" alt="Axivity logo illustration" />
</p>

The Axivity tracker was used to record physical activity directly on two of the project members.

Each participant wore the tracker as a bracelet following the "wrist mounting consideration" convention detailled in the tracker's [user guide](https://axivity.com/userguides). The recording sampling rate was 100Hz. The data was initially saved as a voluminous `.cwa` file, then converted to a `.csv` file before resampling at 10Hz using the [`Resampler.py`](src/Resampler.py) script.

### Tested conditions
The participants wore the tracker for 1 day (also during sleep) in different setups, one was sedentary (attending class, small trips and walks), the other one was more active (whole saturday hiking, walking).


## Usage
Follow the instructions of src's [README](src/README.md)

## Repository structure
The AP_Axivity project is organized as a directory with the following structure: 

- 3 Subfolders
    - src
    - dat 
    - res
- 1 `readme.md` per folder 
- Files specific to each folder

Each of the 3 sub-folders contains its own readme file explaining the contents of the folder in which it is located.

The src folder contains source/code files in `.ipynb` or `.py` format.
The dat folder contains two subfolders 
- Raw: Should contain data files in `.cwa` format
- Converted: Should contain converted data files in `.csv` format


## Contributors

Contributions are always welcome!

This project was carried out by Wissem Ben Romdhane, Meriem Sebbata and Matthieu Molina  

Please adhere to this project's `code of conduct`.

### Feedback

If you have any suggestions, or discover information that might be of relevance to everyone, don't hesitate to edit the FAQ in the 'readme.md' file so that everyone can benefit.

You can always make Pull Requests to alert other contributors to changes and pique their curiosity.


## FAQ

#### What is the AX3 tracker? What does it record?

AX3 is an automatic recorder featuring a 3-axis accelerometer. When worn, it records acceleration values over time.

#### What is the tracker model we were working on?

We were working on Axivity's AX3 tracker. See the [AX3 tracker web page](https://axivity.com/product/ax3) for more details on the sensor.


#### Where can I find the tracker user guide?

A user manual can be found [here](https://axivity.com/userguides/ax3/).

#### Can the AX3 sensor be programmed?

Yes! that's the whole idea. Axivity has developed software to communicate with the tracker and configure it.
This software is called OmGui, and a [GitHub](https://github.com/digitalinteraction/openmovement/wiki/AX3-GUI) page has been specially written to help you get to grips with the software and configure the AX3 tracker.

#### How can I retrieve the data recorded by the tracker?

Follow the guide [GitHub](https://github.com/digitalinteraction/openmovement/wiki/AX3-GUI)


## Bibliography

- Ahmadi, Matthew N., et Stewart G. Trost. « Device-Based Measurement of Physical Activity in Pre-Schoolers: Comparison of Machine Learning and Cut Point Methods ». PLOS ONE 17, nᵒ 4 (13 avril 2022): e0266970. https://doi.org/10.1371/journal.pone.0266970.

- Bai, Jiawei, Chongzhi Di, Luo Xiao, Kelly R. Evenson, Andrea Z. LaCroix, Ciprian M. Crainiceanu, et David M. Buchner. « An Activity Index for Raw Accelerometry Data and Its Comparison with Other Activity Metrics ». PLOS ONE 11, nᵒ 8 (11 août 2016): e0160644. https://doi.org/10.1371/journal.pone.0160644.

- Bakrania, Kishan, Thomas Yates, Alex V. Rowlands, Dale W. Esliger, Sarah Bunnewell, James Sanders, Melanie Davies, Kamlesh Khunti, et Charlotte L. Edwardson. « Intensity Thresholds on Raw Acceleration Data: Euclidean Norm Minus One (ENMO) and Mean Amplitude Deviation (MAD) Approaches ». PLOS ONE 11, nᵒ 10 (5 octobre 2016): e0164045. https://doi.org/10.1371/journal.pone.0164045.

- Marin, Frédéric, Kevin Lepetit, Laetitia Fradet, Clint Hansen, et Khalil Ben Mansour. « Using accelerations of single inertial measurement units to determine the intensity level of light-moderate-vigorous physical activities: Technical and mathematical considerations ». Journal of Biomechanics 107 (juin 2020): 109834. https://doi.org/10.1016/j.jbiomech.2020.109834.

- Tsanas, Athanasios. « Investigating Wrist-Based Acceleration Summary Measures across Different Sample Rates towards 24-Hour Physical Activity and Sleep Profile Assessment ». Sensors (Basel, Switzerland) 22, nᵒ 16 (17 août 2022): 6152. https://doi.org/10.3390/s22166152.

- Vähä-Ypyä, Henri, Tommi Vasankari, Pauliina Husu, Ari Mänttäri, Timo Vuorimaa, Jaana Suni, et Harri Sievänen. « Validation of Cut-Points for Evaluating the Intensity of Physical Activity with Accelerometry-Based Mean Amplitude Deviation (MAD) ». PLOS ONE 10, nᵒ 8 (20 août 2015): e0134813. https://doi.org/10.1371/journal.pone.0134813.

- Walmsley, Rosemary, Shing Chan, Karl Smith-Byrne, Rema Ramakrishnan, Mark Woodward, Kazem Rahimi, Terence Dwyer, Derrick Bennett, et Aiden Doherty. « Reallocation of Time between Device-Measured Movement Behaviours and Risk of Incident Cardiovascular Disease ». British Journal of Sports Medicine 56, nᵒ 18 (6 septembre 2021): 1008‑17. https://doi.org/10.1136/bjsports-2021-104050.
