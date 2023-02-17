from flask import Flask , render_template , request 
import os 

UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/',methods=['GET','POST'])
def main():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        upload()
        return render_template('result.html')

def upload():
    f = request.files['filename']
    file_path = os.getcwd()+'/static'
    print(file_path)
    f.save(file_path+'/'+'result.png')

if __name__ =='__main__':
    app.run(host='0.0.0.0',port='2804',debug='True')