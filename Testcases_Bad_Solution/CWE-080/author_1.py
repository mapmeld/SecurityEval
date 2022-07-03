from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/renderhtml")
def renderHTML():
    '''
    get name from request and render html to response
    '''
    name = request.args.get('name', '')
    response = make_response('<h1>Hello '+name+'</h1>')
    return response
    