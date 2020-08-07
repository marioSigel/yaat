# yaat - Yet Another Annotation Tool

*Italic* commands have to be executed in command line, e.g. iTerm (Mac), Powershell (Windows).   

## Install
* Install python 3
  * Mac: *brew install python3*
	* You can check if it works by typing *python3*. And *exit()* to leave python.
	  * If *python3* is not found for some reason use */usr/local/bin/python3* instead, same for pip3 below.
  * Linux: *apt install python3.7*
  * Windows: 
    * Download "Windows x86-64 executable installer" ("Windows x86 executable installer" for 32-bit windows) from https://www.python.org/downloads/release/python-378/
	* Install with standard settings
  
* Install requirements
  * Mac/Linux:
    * go to yaat folder and type *pip3 install -r requirements.txt* 
  * Windows:
    * open yaat folder
	* double click setup.bat
  
## Download images
  * *aws configure* -> insert credentials you will receive from mario.sigel@sociovestix.com via email. 
    * For Default output format: just hit enter
  * go to (command line, Powershell) yaat folder next to app.py and type *mkdir images*
  * *cd images*
  * ``` aws s3 sync s3://rem-sens-data/sen2-gt-2019-cpp0.5/sentinel2/data_corrected/ . ```
  * append ``` --exclude "*" --include "<number prefix, eg. 1>_*" ``` to get a subset of images. This should be discussed with Mario/Florian.
    * append ``` --exclude '*' --include '<number prefix, eg. 1>_*' ``` on Windows. 
	
  * Windows: if aws is not found in Powershell use installer:
    https://docs.aws.amazon.com/cli/latest/userguide/install-windows.html

  
## Start application:
* Insert your user_name (unique id, e.g. your name) host, passw (yaat database credentials from email) in config.py
* Mac:
  * PYTHONPATH=. python3 app.py
* Windows:
  * double click start_app.bat


## Any issues:
* contact mario.sigel@sociovestix.com
  
