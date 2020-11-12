# Lazeye
 A kind of hands free lock mechanism software for laptop

Used model: effnetb2 : https://storage.googleapis.com/keras-applications/efficientnetb2_notop.h5

Image size: (224, 224)

Live Video capture: using OpenCV (opencv is used for video capturing **only** )

lazi.py: is main file.

## Built with

- [Tensorflow](https://www.tensorflow.org/api_docs/python/tf) Version = 2.3
- [OpenCV](https://pypi.org/project/opencv-python/)

## Installation

- The juptyter notebook can be opened in [colab](https://colab.research.google.com/) or [scratchpad colab](https://colab.research.google.com/notebooks/empty.ipynb)

- OpenCV doesnt work in jupyter notebooks for video capturing

So to install it locally

- Prepare a venv,

for example using conda,

`conda create -n name_of_new_venv python=3.7 anaconda`

- Activate the newly created environment

`activate name_of_new_venv`

-install tensorflow and Opencv-python

`pip install --upgrade tensorflow`

`pip install opencv-python`


## Disclaimer
> _All video capturing and classification is done locally and is not transmitted to any other whatsoever_

 # Contributions
 
 All contributions are ***highly appreciated***. To make any contribution:
 
 1. Fork the project
 2. Create your own branch `git checkout -b <anyName>`
 3. Commit your changes `git commit -m "Add something"`
 4. Push to branch `git push origin <theNameOfBranchYouCreated>`
 5. Open a pull request.
 
 Thank you.
