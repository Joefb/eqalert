# eqalert

Play Everquest on Linux?! Cant get GINA to work but would really like voice notifications like GINA
provides? Me too!!! Thats why I made eqalert.

Eqalert will give voice notifications for events that are defined in the `alert_dict.py`

### Features
* Voice notifications for events you define
* Automatically detect the active toon
* Automatically swap log file to the active toon

### Requirements:
* `python 3`
* `espeak` command line text to speech program

### Set Up
1. Install `python3` -  Skip already installed
2. Install `espeak` - Use your package manager to install
4. Open `eqalery.py` with your favorite text editor and set the `log_path` variable to your EQ log dir 
3. Open `alert_dict.py` with your favorite text editor to define alerts

### Usage:
`python3 eqalert.py`
