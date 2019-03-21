# WARNING
### This script will overwrite any web.config file in the same folder or directory, backup your web.config file by either saving a copy in another folder or renaming the one in the current folder to something other than web.config.

# Instructions

Place wconf_app.py in an empty folder or directory if you want to create the web.config file from scratch.

wconf_app.py has two modes argument only and interactive only

For interactive only mode use the following switch exactly and follow the prompts instructions:

wconf_app.py -i

For argument only mode using all of the following arguments, replacing "value" with your desired value respectively:

wconf_app.py dbname=value envname=value webname=value

The envname= argument only recognizes three enviroment types:

Dev, Stage, prod

Both dbname= and webname= can be any legal name value for each respectively.