# Mass-decorrelated Xbb Tagger using Adversarial Neural Networks
For training and evaluating mass-decorrelated Hbb vs. Dijets tagger and Hbb vs. Top tagger.

# Setup
1. Clone the package:
````
$ git clone https://github.com/allenshihlung/mass_decorrelated_hbb_tagger.git
$ cd adversarial-master
````

2. Install miniconda and other dependencies to create the appropriate software environments:
````
$ source install.sh
````

3. Add path to .bashrc in your ~ directory
````
$ cd ~
$ cat "export PATH=<path to your the bin directory of your miniconda installation>:$PATH"
````

4. Activate the conda environment
````
$ cd <path to your adversarial-master directory>
$ source activate.sh
````

# Data-preprocessing
1. Gather all .h5 datasets into hbbDijetsDatasets/ or hbbTopDatasets/ On PDSF, this can be done by
````
$ python dataprocessing/getHbbDijetsDatasets.py
````
or
````
$ python dataprocessing/getHbbTopDatasets.py
````

Note that the name of each dataset has to follow the following format:

<original data source name>_<dsid>_<H if isHbbSamples else N>.h5
For example:
````
user.dguest.15830754._000001.output_301498_H.h5
````
and
````
user.dguest.15830705._000040.output_361027_N.h5
````
  
2. Label the datasets
````
$ python dataprocessing/labelDatasets.py
````
This will place the labelled datasets into labelledHbbDijetsDatasets/ or labelledHbbTopDatasets/

3. Extract necessary columns for reweighting (we will add the other columns back after reweighting)
````
$ python dataprocessing/extractPtAndWeight.py
````
This will place the labelled datasets into extractedHbbDijetsDatasets/ or extractedHbbTopDatasets/

4. Reweight and subsample
````
$ python -m prepro.reweightData --train <test events to subsample in millions> --test <test events to subsample in millions> --max-processes <max concurrent processes to be spun off>
````
This will place the processed extractedData.h5 file in reweightDatasets/

5. Append all other columns back
````
$ python dataprocessing/appendData.py
````
This will place the processed data.h5 file in input/

Ready to go for training!

# Training
For training with the default configuration:
````
$ python -m run.adversarial.train --train
````
To make any changes to the configurations, locate the default.json file in the configs/.

# Performance tests
Locate the perform_studies function in tests/comparison.py and comment out or uncomment any study. Then run
````
$ python -m tests.comparison
````
The plots will be saved in figures/
