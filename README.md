# mapboxupload
Uploading data to mapbox

Installation:

1. Download virtual ENV (https://virtualenv.pypa.io/en/stable/installation.html)
2. Using Command Line, change directory into this repository "cd path/to/this/folder/"
3. Initialise the virtual environment "virtualenv -p python3.5 ENV"
4. Activate the virtual environment "source ENV/bin/activate"
5. Upgrade pip "pip install -U pip"
6. Install mapbox dependencies "pip install mapbox"
7. Install more mapbox deps "pip install mapboxcli"
8. Deactivate the virtual environment by using "deactivate"

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
