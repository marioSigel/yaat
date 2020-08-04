# yaat - Yet Another Annotation Tool

## Install
* Install python 3
  * Mac: *brew install python3*
  * Linux: *apt install python3.7*
  * You can check if it works by typing *python3*. And *exit()* to leave python.
    * If *python3* is not found for some reason use */usr/local/bin/python3* instead, same for pip3 below.
* Install requirements
  * go to yaat folder and type *pip3 install -r requirements.txt* 
  
## Download images
* install awscli 
  * *pip install awscli*
  * *aws configure* -> insert credentials you will receive from mario.sigel@sociovestix.com via email. 
  * go to yaat folder next to app.py and type *mkdir images*
  * *cd images*
  * ``` aws s3 sync s3://rem-sens-data/sen2-gt-2019-cpp0.5/sentinel2/data_corrected/ . ```
  * append ``` --exclude "*" --include "<number prefix, eg. 1>_*" ``` to get a subset of images. This should be discussed with Mario/Florian.
  
## Start application:
* Insert your user_name (unique id, e.g. your name) host, passw (yaat database credentials from email) in config.py
* PYTHONPATH=. python3 app.py


## Any issues:
* contact mario.sigel@sociovestix.com
  
