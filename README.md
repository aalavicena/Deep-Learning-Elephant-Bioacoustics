# Deep learning models performance in examining Asian elephant (_Elephas maximus_) sounds from Sri Lanka and Malaysia with considerations for applications

This repository is provided as a supplementary material to Avicena et al. (in review). Data can be obtained under formal request to the authors. 

## Pre-requisites
### Software requirements
Before starting, you will need to have Python installed in your system:
https://www.python.org/downloads/

Since the codes are embedded in Jupyter Notebook, we suggest to install Jupyter Lab to run them:
<p>Install Jupyter Lab via pip in Python</p>
<pre><code>pip install jupyterlab</code></pre>

<p>You can also install it via Conda</p>
<pre><code>conda install -c conda-forge jupyterlab</code></pre>

Please refer to the Jupyter Lab documentation for more information:
https://jupyterlab.readthedocs.io/en/stable/user/index.html

### Module requirements
We use [PyTorch]([url](https://pytorch.org/))'s TorchAudio to build the CNN model in our study. You will need to install it in your system:
<p>Install PyTorch via pip</p>
<pre><code>pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu</code></pre>

Other required modules are listed in each notebook. Please install accordingly.

## Contents
The repositories include the following materials:
  1. Model training.ipynb [Contains codes for data pre-processing, CNN architecture, training loop, and model evaluation]
  2. Inference on unseen data.ipynb [Contains codes for inferring unseen data using the trained model]


Part of the codes were adopted from several repositories:
1. https://towardsdatascience.com/audio-deep-learning-made-simple-sound-classification-step-by-step-cebc936bbe5 (Main Architecture)
2. https://github.com/kuangliu/pytorch-metrics (Performance Metrics)
3. https://medium.com/dataseries/k-fold-cross-validation-with-pytorch-and-sklearn-d094aa00105f (K-Fold Cross Validation)

## Acknowledgments
We are sincerely grateful for the support given by Yayasan Sime Darby, Department of Wildlife and National Parks Peninsular Malaysia, Forest Department Peninsular Malaysia, and Trunks and Leaves Inc. This study is funded by Yayasan Sime Darby and Microsoft AI for Earth.
