#!flask/bin/python

from flask import Flask, jsonify, request, abort

import requests, json

# from flask.ext.httpauth import HTTPBasicAuth

app = Flask(__name__)

@app.route('/rackhd/login', methods=['POST'])
def rackhd_login():
	if not request.json or not 'username' in request.json:
		abort(400)

	username = request.json['username']
	password = request.json['password']


	url = "https://localhost:8443/login"

	headers = {
			"Content-Type": "application/json"
	}

	data = '{"username": "' + username + '", "password": "' + password + '"}'
	res = requests.post(url, headers=headers, data=data, verify=False)
	return res.text

@app.route('/rackhd/obms/read', methods=['GET'])
def readobms():
	url = "https://localhost:8443/api/current/obms"
	token = request.headers.get('token')

	headers = {
		"Content-Type" : "application/json",
		"Authorization":"JWT " + token

	}

	res = requests.get(url, headers=headers, verify=False)
	return res.text

@app.route('/rackhd/obms/create', methods=['PUT'])
def createobms():
	nodeId = request.json['nodeId']
	service = request.json['service']
	user = request.json['user']
	password = request.json['password']
	host = request.json['host']

	url = "https://localhost:8443/api/current/obms"
	token = request.headers.get('token')
	headers = {
		"Content-Type":"application/json",
		 "Authorization":"JWT " + token

	}

	data = '{"nodeId": "' + nodeId + '", "service":"' + service + '", "config":{"user":"' + user + '", "password":"' + password + '", "host":"' + host + '"}}'

	res = requests.put(url, headers=headers, data=data, verify=False)
	return res.text


@app.route('/rackhd/obms/update', methods=['PATCH'])
def updateobms():
	nodeId = request.json['nodeId']
	service = request.json['service']
	user = request.json['user']
	password = request.json['password']
	host = request.json['host']

	url = "https://localhost:8443/api/current/obms/" + nodeId
	token = request.headers.get('token')

	headers = {
		"Content-Type": "application/json",
		"Authorization": "JWT " + token
	}


	data = '{"nodeId":"' + nodeId +'", "service":"' + service + '", "config":{"user":"' + user +'", "password":"' + password + '", "host":"' + host + '"}}'

	res = requests.patch(url, headers=headers, data=data, verify=False)
	return res.text


@app.route('/rackhd/obms/delete', methods=['DELETE'])
def deleteobms():
	nodeId = request.json['nodeId']
	url = "https://localhost:8443/api/current/obms/" + nodeId

	token = request.headers.get('token')

	headers = {
		"Content-Type": "application/json",
		"Authorization": "JWT " + token
	}

	res = requests.delete(url, headers=headers, verify=False)

	return res.text


@app.route('/rackhd/skus/read', methods=['GET'])
def readskus():
	url = "https://localhost:8443/api/current/skus"
	token = request.headers.get('token')

	headers = {
		"Content-Type": "application/json",
		"Authorization": "JWT " + token
	}

	res = requests.get(url, headers=headers, verify=False)

	return res.text

@app.route('/rackhd/skus/create', methods=['PUT'])
def createskus():
	url = "https://localhost:8443/api/current/skus"
	token = request.headers.get('token')
	headers = {
		"Content-Type": "application/json",
		"Authorization": "JWT " + token
	}

	name = request.json['name']
	path = request.json['path']
	contains = request.json['contains']
	path = request.json['path']

	data = '{}'

	res = requests.put(url, headers=headers, data=data, verify=False)
	print res.text

@app.route('/rackhd/skus/delete', methods=['DELETE'])
def deleteskus():
	skuid = request.json['skuid']
	url = "https://localhost:8443/api/current/skus/" + skuid

	token = request.headers.get('token')

	headers = {
		"Content-Type": "application/json",
		"Authorization": "JWT " + token
	}

	res = requests.delete(url, headers=headers, verify=False)


if __name__ == '__main__':
	app.run(debug=True)
