from flask import Flask,render_template, request, redirect, url_for,jsonify

from view import *

@app.errorhandler(401)
def unauthorized_error_handler(error):
    # Create a custom response object with custom headers
    unauthorized_headers = {"WWW-Authenticate": "Bearer"}
    response = jsonify(error="Could not validate credentials")
    response.status_code = 401
    for header, value in unauthorized_headers.items():
        response.headers[header] = value
    return response


if __name__ == "__main__":
    app.run(debug=True)
