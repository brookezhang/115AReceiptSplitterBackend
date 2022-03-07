Backend: https://github.com/brookezhang/115AReceiptSplitterBackend <br/>
Documentation: https://drive.google.com/drive/u/2/folders/1QTqF__bsyIr11Gcu4JZSCo2Ajwaxjqv6


This API is deployed on https://tabdropbackend.herokuapp.com/.<br/>

Instructions to deploy locally as well:

1. Clone the repository.
2. Create a python virtual environment and activate it.
3. Enter on the console/terminal, "pip install -r requirements.txt", within the folder with the repository to install all dependencies.
4. Create a file named ".env" with your Azure API information with the format below:
```
    API_KEY=<Azure api key>
    ENDPOINT=<Azure api endpoint>
```
4. IF ON WINDOWS: in console, enter "set FLASK_APP=flaskapi.py".<br/>
IF ON MAC: in console, enter "export FLASK_APP=flaskapi.py".
5. in console, enter "flask run". The backend should be running locally.<br/>

To deploy on Heroku yourself, use this tutorial: https://devcenter.heroku.com/articles/git.
