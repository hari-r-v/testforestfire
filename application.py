import pickle
from flask import Flask, request, jsonify,render_template,url_for
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

## import ridge regressor and standard scaler pickle

ridge_model = pickle.load(open('model/ridge.pkl','rb'))
standardscaler = pickle.load(open('model/scaler.pkl','rb'))

@app.route("/")
def Index():
    return render_template('home.html')

@app.route('/predictdata', methods=['GET','POST'])
def predict_datapoint():
    if request.method=="POST":
        pass
    else:
        return render_template('home.html')

if __name__=="__main__":
    app.run(host ="0.0.0.0")