from flask import Flask,render_template,request
import pickle
import numpy as np

model = pickle.load(open('dt_model.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_placement():
    a = int(request.form.get('a'))
    b = int(request.form.get('b'))
    c = int(request.form.get('c'))
    d = int(request.form.get('d'))
    e = int(request.form.get('e'))
    f = int(request.form.get('f'))
    g = int(request.form.get('g'))
    h = int(request.form.get('h'))
    i = int(request.form.get('i'))
    j = int(request.form.get('j'))
    k = int(request.form.get('k'))
    l = int(request.form.get('l'))
    m = int(request.form.get('m'))

    result = model.predict(np.array([a,b,c,d,e,f,g,h,i,j,k,l,m]).reshape(1,13))

    if result == 0:
        result = 'type 0'
    elif result == 1:
        result = 'type 1'
    elif result == 2:
        result = 'type 2'

    return render_template('index.html',result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)