# import all necessary libraries here
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

## Load the messy dataset ##
data = pd.read_csv("messy_data.csv")

from testing2 import impute_missing_values, remove_duplicates, normalize_data, remove_redundant_features

## Applying the preprocessing steps in order, updating 'data' each time to run through pipeline, then printing head() to see the changes ##
data = impute_missing_values(data)
data = remove_duplicates(data)
data = normalize_data(data, method='standard', target_column='target')
data = remove_redundant_features(data)

## Included this to manually revert target column as I was getting errors before ##
data['target'] = data['target'].round().astype(int)

data.to_csv("cleaned_data.csv", index=False)

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'data_preprocessor'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[3], line 2\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;66;03m# Import necessary modules\u001b[39;00m\n\u001b[0;32m----> 2\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mdata_preprocessor\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mdp\u001b[39;00m\n\u001b[1;32m      3\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mpandas\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mpd\u001b[39;00m\n\u001b[1;32m      4\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01msklearn\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mlinear_model\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m LogisticRegression\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'data_preprocessor'"
     ]
    }
   ],
   "source": [
    "# Import necessary modules\n",
    "import data_preprocessor as dp\n",
    "import pandas as pd\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.metrics import accuracy_score\n",
    "\n",
    "# 1. Load the dataset\n",
    "messy_data = pd.read_csv('../Data/messy_data.csv')\n",
    "clean_data = messy_data.copy()\n",
    "\n",
    "# 2. Preprocess the data\n",
    "clean_data = dp.impute_missing_values(clean_data, strategy='mean')\n",
    "clean_data = dp.remove_duplicates(clean_data)\n",
    "clean_data = dp.normalize_data(clean_data)\n",
    "clean_data = dp.remove_redundant_features(clean_data)\n",
    "\n",
    "# 3. Save the cleaned dataset\n",
    "# clean_data.to_csv('../Data/clean_data.csv', index=False)\n",
    "\n",
    "# 4. Train and evaluate the model\n",
    "simple_model(clean_data)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "default",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.21"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
