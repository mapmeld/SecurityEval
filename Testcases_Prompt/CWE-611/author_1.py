from flask import Flask, request
import lxml.etree

app = Flask(__name__)

def checkPassword(userid, password):
    pass

@app.post("/upload")
def upload():
    '''
    get the xml file from the request and check if the userid and password are correct
    '''
