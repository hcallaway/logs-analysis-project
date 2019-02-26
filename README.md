# Logs Analysis Project

This project is to utilize a news article database to find the top 3 articles of all time, list the authors in descending order, from most read to least, and find the days where errors occured at a rate higher than 1%

This grouping of files -- specifically this README.md, analyze_logs.py, and Logs Analysis.txt -- is to satisfy the submission requirements for the Udacity Full Stack Nanodegree programs "Logs Analysis" project.

## Requirements
* [Vagrant](https://www.vagrantup.com/downloads.html)
* [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
* [Vagrant Configuration](https://github.com/udacity/fullstack-nanodegree-vm) - provided by Udacity

## Getting Started
### Can run with Python 2.7 or Python 3.x
* Install [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) -- You do not need to launch VirtualBox after installing
    * Note: **Ubuntu 14.04 Users** you will need to install VirtualBox using the Ubuntu Software Center, due to a reported bug
* Install [Vagrant](https://www.vagrantup.com/downloads.html)
    * Confirm Vagrant install is successful by running `vagrant --version`
* Download the VM configuration: [FSND-Virtual-Machine.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) or fork and clone the [Github Repository](https://github.com/udacity/fullstack-nanodegree-vm)
* After extracting .zip or cloning repo into desire directory, `cd` into the folder, then `cd` into the **/vagrant** directory
* Start the subdirectory by running the command `vagrant up` within the **/vagrant** directory
* Once `vagrant up` has completed, run `vagrant ssh` to log in to the newly installed Linux VM
* Download the data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
* Unzip the file after downloading, and locate **newsdata.sql**
* Place **newsdata.sql** in the **/vagrant** directory
* Run command `psql -d news -f newsdata.sql` to import data into the `news` database
* Move the **analyze_logs.py** file to the **/vagrant** directory on your computer (it is shared with the VM)
* Within the **/vagrant** directory within the VM, run `python analyze_logs.py` and look for the output file **logs_analysis.txt** in the same directory
* Running **analyze_logs.py** again will replace any existing logs_analysis.txt files with updated data when appropriate

## Running without Vagrant & Virtual Box
* If you like, you can run without Vagrant or Virtual box
* Requrements:
    * Python 2.7 or 3.x
    * PostgreSQL
    * News database file, found [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

### Setup        
* Set up a PSQL database named **news**
* Run `psql -d news -f newsdata.sql` to insert data into the **news** database
* Move the **analyze_logs.py** file to the **/vagrant** directory on your computer (it is shared with the VM)
* Within the **/vagrant** directory within the VM, run `python analyze_logs.py` and look for the output file **logs_analysis.txt** in the same directory
* Running **analyze_logs.py** again will replace any existing logs_analysis.txt files with updated data when appropriate
