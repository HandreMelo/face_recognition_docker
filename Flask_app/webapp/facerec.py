#mod by André :)
import face_recognition
import numpy as np
import os
#from reconhecimento.models import Alunos
# https://pythonhosted.org/dataIO/pk.html
#https://medium.com/rafaeltardivo/python-entendendo-o-uso-de-args-e-kwargs-em-fun%C3%A7%C3%B5es-e-m%C3%A9todos-c8c2810e9dc8
#https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/
#funciona o reconhecimento, basta escolher, se arquivo ou codificação. Mas tem que ser trabsformado a codificação em lista antes de colar lá...

def codificar_foto(file,**kwargs):
    
    loaded_file = face_recognition.load_image_file(file)
    return face_recognition.face_encodings(loaded_file)[0]

def ajustar_codificacao(file_cod,cod_aluno):

    if file_cod != None:
        cod_aluno = (file_cod.read()).decode('ascii')
    else:
        cod_aluno=cod_aluno
        
    cod_aluno = cod_aluno.replace("[","")
    cod_aluno = cod_aluno.replace("]","")
    lista_numeros_cod_aluno = []
    for num in cod_aluno.split(","):
        lista_numeros_cod_aluno.append(float(num))
    
    cod_aluno_ajustada = np.array(lista_numeros_cod_aluno)
    
    return cod_aluno_ajustada
    
def validar_aluno(**kwargs):
    match=False
    file_foto,file_cod  = None,None
    
    if kwargs.get('file_foto') != None:
        file_foto = kwargs.get('file_foto')
    if kwargs.get('file_cod') != None:
        file_cod = kwargs.get('file_cod')
    cod_aluno = kwargs.get('cod_aluno')
    
    foto_codificada = codificar_foto(file_foto)
    cod_aluno_ajustada = ajustar_codificacao(cod_aluno=cod_aluno,file_cod=file_cod)
    
    match = face_recognition.compare_faces([cod_aluno_ajustada], foto_codificada)
    
    print("Printando match", match)
    if True in match:
        print("retornando True")
        return True
    return False