# mapboxupload
Uploading data to mapbox

running mapboxTest:

1. install Nodejs from https://nodejs.org/en/download/
2. cd into mapboxTest
3. Install bower: npm install -g bower
4. term: npm install
5. term: bower install
6. install ruby here: https://www.ruby-lang.org/en/downloads/
7. update ruby package manager: gem update --system
8. Install compass: gem install compass
9. run: grunt serve
10. Enjoy

Python:

Installation:

1. Install python 3.5.1 from https://www.python.org/downloads/
2. Download virtual ENV from https://virtualenv.pypa.io/en/stable/installation.html
3. Using Command Line, change directory into this repository "cd path/to/this/folder/"
4. Initialise the virtual environment "virtualenv -p python3.5 ENV"
5. Activate the virtual environment "source ENV/bin/activate"
6. Upgrade pip "pip install -U pip"
7. Install mapbox dependencies "pip install mapbox"
8. Install more mapbox deps "pip install mapboxcli"
9. Deactivate the virtual environment by using "deactivate"

To use the upload command, you will need to make a secret key from Mapbox. https://www.mapbox.com/studio/account/tokens/
Create a new token with upload:write scope.

Run Upload:

1. cd into the folder "cd path/to/this/folder/"
2. Activate the virtual environment "source ENV/bin/activate"
3. Enter the token "export MAPBOX_ACCESS_TOKEN=sk.blah-blah-blah"
4. Upload data "mapbox upload username.data data.geojson --name somename" <br>
For example, to upload data from the file "geotest.geojson" to my profile "creativereubs" with the name "firstupload"...<br>
"mapbox upload creativereubs.data geotest.geojson -name firstupload"<br>
You can run this step as many times as you want without running the first 3 steps.
5. Deactivate the virtual environment by using "deactivate"
