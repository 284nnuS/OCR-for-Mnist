from flask import Flask , render_template , request 
import os 
from modules import model_ocr
app = Flask(__name__)
model_ocr = model_ocr()
@app.route('/',methods=['GET','POST'])
def main():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        upload()
        res = model_ocr.predict_model()
        return render_template('result.html',result=res)
    
def upload():
    f = request.files['filename']
    file_path = os.getcwd()+'/static'
    f.save(file_path+'/'+'result.png')

if __name__ =='__main__':
    app.run(host='0.0.0.0',port='2804',debug='True')