# Malware Detection Through Mining Symbol Table of Linux Executables

## Requirements
1. Python 2.7
2. Java 8.0+

## To run the system
1. Put all the ELF files to analyse in the `elf` folder.
2. Run `python run_system.py`

## Description
* The list of all function calls extracted from the ELF files dataset (Malware and benign) is in **functions.txt**.
* The function calls above the threshold (currently at 300) are present in **functions_less.txt**.
* The dataset on which the models were trained is **results2.csv**.
* The saved models are in **models/**.
* The code for model evaluation on the test set is in **system/**.