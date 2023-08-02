#
# app.py
# Driver code for backend
#
# Author: Rin | Discord: Rin#0304
# https://github.com/ReallyAwesomeName/kf2-tools
#
# =========================================================================== #
#     This program provides tools to calculate things for Killing Floor 2     #
#     Copyright (C) 2023  Rin                                                 #
#                                                                             #
#     This file is part of kf2-tools                                          #
#                                                                             #
#     This program is free software: you can redistribute it and/or modify    #
#     it under the terms of the GNU General Public License as published by    #
#     the Free Software Foundation, either version 3 of the License, or       #
#     (at your option) any later version.                                     #
#                                                                             #
#     This program is distributed in the hope that it will be useful,         #
#     but WITHOUT ANY WARRANTY; without even the implied warranty of          #
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           #
#     GNU General Public License for more details.                            #
#                                                                             #
#     You should have received a copy of the GNU General Public License       #
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.  #
# =========================================================================== #

from flask import Flask, request
import flask
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/users", methods=["GET", "POST"])
def users():
    print("users endpoint reached...")
    if request.method == "GET":
        with open("data/users.json", "r") as f:
            data = json.load(f)
            data.append({"username": "user4", "pets": ["hamster"]})

            return flask.jsonify(data)
    if request.method == "POST":
        received_data = request.get_json()
        print(f"received data: {received_data}")
        message = received_data["data"]
        return_data = {"status": "success", "message": f"received: {message}"}
        return flask.Response(response=json.dumps(return_data), status=201)


if __name__ == "__main__":
    app.run("localhost", 6969)
