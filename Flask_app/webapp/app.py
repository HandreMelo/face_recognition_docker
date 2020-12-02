from flask import Flask, jsonify
from flask import Flask, render_template, request, redirect, url_for
import facerec

#https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask
#https://www.compulsivecoders.com/tech/how-to-edit-a-file-on-heroku-dynos-using-nano-or-vim
app = Flask(__name__)

import random
import string
from flask import send_file
# get random string without repeating letters
def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.sample(letters, length))
    print("Random String is:", result_str)



@app.route('/')
def index():
    print("Face Recognition API")
    return render_template('index.html')

@app.route('/validar', methods=['POST'])
def validar(**post):

    upload_path_foto = request.files['file_foto']
    upload_path_cod = request.files['file_cod']
    result = facerec.validar_aluno(file_foto=upload_path_foto, file_cod=upload_path_cod)
    return jsonify({'result': repr(result)})

@app.route('/codificar', methods=['POST'])
def codificar(**post):

    upload_path_foto = request.files['file_foto']
    result = facerec.codificar_foto(file=upload_path_foto)
    result_string = str(list(result))
    return jsonify({'result': repr(result_string)})

if __name__ == '__main__':
    app.run(host='0.0.0.0')