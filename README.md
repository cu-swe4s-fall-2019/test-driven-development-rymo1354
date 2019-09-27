# test-driven-dev

This repository contains data generation and visualization scripts.

# Usage

To generate a histogram of a randomized dataset type the following into the command line :
```
bash gen_data.sh | python viz.py --out_file hist.png --plot_type histogram
```
To generate a boxplot of a randomized dataset type the following into the command line :
```
bash gen_data.sh | python viz.py --out_file boxplot.png --plot_type boxplot
```
To generate a boxplot/histogram combo type the following into the command line :
```
bash gen_data.sh | python viz.py --out_file combo.png --plot_type combo
```

# Installation

The dependencies of this program are : 
- numpy
- matplotlib

These can be installed in the command line using the following prompts :
```
conda install --yes numpy
conda install --yes matplotlib
```
