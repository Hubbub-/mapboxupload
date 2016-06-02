# mapboxupload
Uploading data to mapbox

Javascript using npm:

1. install Nodejs from https://nodejs.org/en/download/
2. run in terminal in whatever location for examples: git clone https://github.com/mapbox/mapbox.js.git
3. term: cd mapbox.js
4. term: npm install
5. term: make
6. term: npm install -g serve
7. term: cd ../mapboxupload/basic-map/
8. term: serve
9. Serve will create a local server on http://localhost:3000/basic-map.html 
10. Open in browser
11. Enjoy!

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
