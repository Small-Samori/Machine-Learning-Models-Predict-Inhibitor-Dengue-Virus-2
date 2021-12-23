**Machine Learning Models Predict Inhibitiorys of Dengue Virus 2**


This repository is the code implementation of the paper: Machine Learning Models Predict Inhibitiorys of Dengue Virus 2. Random Forest came out as the best performing(**accuracy = 0.94**, **precision = 0.94**, **recall = 0.94**, **F1-score = 0.94**). It had an **AUC of 0.8** and **Mathew Correlation Coefficient (MCC) of 0.61**.

The methodology employed in the the figure is summerized in the figure below:

<p align = "center">
<img align="center" src="methodology.png"/>
</p>

The dataset utillized in this project is a dataset of compound screened against the Dengue Virus 2 (DENV2). It can be found [here](https://pubchem.ncbi.nlm.nih.gov/bioassay/651640#section=Result-Definitions).
The script for each step of the project is saved in separate folders. To reproduce this work rerun the .py files in each folder (except the Molecular Descriptors step that require running PaDEL) as follows:
1. Download the SMILES structure dataset (as a .txt file) and compounds datatable from [PubChem](https://pubchem.ncbi.nlm.nih.gov/bioassay/651640#section=Result-Definitions).
2. Copy the two files in to the `1. Data Preparation` folder and run the scripts in the order they are numbered. Make sure the filenames match those in the scripts.
3. Copy the `smile_activity_data.csv` csv file that will be generated into the `2. Molecular Descriptors` folder
4. Run the `csv_smi_format_conversion.py` script to the copied file from a csv file to a smi file. This will generate three smi files: actives.smi, inactives_1.smi and inactives_2.smi
5. Download [PaDEL Descriptors](http://www.yapcwsoft.com/dd/padeldescriptor/) and use it to compute the molecular descriptors.
6. Copy the generated descriptor files into the `3. Train test split/Imputation` folder.
7. Within the `Imputation` folder, run `combine_inactives.py` to combine the inactives into one file and then the `impute.py` script to impute all NaNs
8. Copy the generated files into the `3. Train test split/Dataset` folder and run the `train_test_split_df.py` script. NOTE: Edit filename and paths where necessary.
9. Copy the generated training and testing data into the `4. SMOTE analysis/Dataset` folder and run the `SMOTE analysis.py` to perform SMOTE.
10. Copy the generated files into the `5. EDA/Dataset` folder and run the `PCA.py` script
11. Copy the data from step 10 into the `6. Data Preprocessing/Dataset` and run the `mannwhitney_test_feature_selection.py` to perform feautre selection.
12. Copy the reduced dataset into the `7. Build Models/Dataset` folder and run the models.py script to train and evaulate the models.

To run just the training and evaluation of the models, run the `models.py` script in the `7. Build Models folder`. The performance of the model will be saved as text files the `Evaluation` folder.
The path of the datasets in the `models.py` script can be changed to train and/or test the algorithms on a new dataset.
The trained models are saved in the `7. Build Models/Models` folder

**Credit**


[Data Professor YouTube Channel](https://www.youtube.com/c/DataProfessor) 
