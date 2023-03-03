#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/')

def index():
    f = open('data.json')
    data = json.load(f)
    ret = []
    for i in data['theData']:
        ret.append(i)
    f.close()
    return jsonify(ret)