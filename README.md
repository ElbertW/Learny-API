# Learny-API
A simple Flask-based API for parsing user statements.

## Setting Up Your Python Virtual Environment
It is recommended to have the latest version of Python (3.6) installed. Follow the steps below to set up your Python virtual environment. Learny-API requires the Flask and Pyparsing libraries.

```
git clone https://github.com/ElbertW/Learny-API.git
cd Learny-API
python3 -m venv flask
flask/bin/pip install flask
flask/bin/pip install pyparsing
```

To start a local server for Learny-API, do:
```
./run.py
```

Your local server is now running at http://localhost:5000. Debug mode is enabled by default.

## Sending User Queries
This simple API only has 1 method: POST.

POST is used to submit a compact JSON object to the API of the form:
```javascript
{'statement': '1+1=2'}
```

POST returns a response in the form of another compact JSON object:
```javascript
{"result": "yes"}
```

To test queries on your local server, open up a new terminal and use `curl` to submit a POST request. Edit the inline JSON to see the different possible outcomes!
```
curl -i -H "Content-Type: application/json" -X POST -d '{"statement":"1+1=3"}' http://localhost:5000/learny/api/v1.0/eval
```

If the JSON input contains no `=`, then the API will perform a Bing Image search and return the top hit in the form of a URL.