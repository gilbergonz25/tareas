import pymongo
from flask import Flask, render_template, request

app = Flask(__name__)

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["diccio"]
collection = db["diction"]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/agregar', methods=['GET', 'POST'])
def agregar_palabra():
    if request.method == 'POST':
        palabra = request.form['palabra']
        documento = collection.find_one({"palabra": palabra})
        if documento:
            mensaje = "la palabra " + palabra + " ya existe"
        else:
            significado = request.form['significado']
            collection.insert_one({"palabra": palabra, "significado": significado})
            mensaje = "La palabra " + palabra + " se ha agregado correctamente"
        return render_template('resultado.html', mensaje=mensaje)
    else:
        return render_template('agregar.html')

@app.route('/editar', methods=['GET', 'POST'])
def editar_palabra():
    if request.method == 'POST':
        palabra = request.form['palabra']
        documento = collection.find_one({"palabra": palabra})
        if documento:
            nuevo_significado = request.form['significado']
            collection.update_one({"palabra": palabra}, {"$set": {"significado": nuevo_significado}})
            mensaje = "La palabra " + palabra + " se ha actualizado correctamente"
        else:
            mensaje = "La palabra " + palabra + " no existe en el diccionario"
        return render_template('resultado.html', mensaje=mensaje)
    else:
        return render_template('editar.html')

@app.route('/eliminar', methods=['GET', 'POST'])
def eliminar_palabra():
    if request.method == 'POST':
        palabra = request.form['palabra']
        documento = collection.find_one({"palabra": palabra})
        if documento:
            collection.delete_one({"palabra": palabra})
            mensaje = "La palabra " + palabra + " se ha eliminado correctamente"
        else:
            mensaje = "La palabra " + palabra + " no existe en el diccionario"
        return render_template('resultado.html', mensaje=mensaje)
    else:
        return render_template('eliminar.html')

@app.route('/listado')
def listado_palabras():
    cursor = collection.find()
    palabras = []
    for documento in cursor:
        palabras.append(documento["palabra"])
    return render_template('listado.html', palabras=palabras)

@app.route('/buscar', methods=['GET', 'POST'])
def buscar_significado():
    if request.method == 'POST':
        palabra = request.form['palabra']
        documento = collection.find_one({"palabra": palabra})
        if documento:
            significado = documento["significado"]
            return render_template('resultado.html', mensaje=significado)
        else:
            mensaje = "La palabra " + palabra + " no existe en el diccionario"
            return render_template('resultado.html', mensaje=mensaje)
    else:
        return render_template('buscar.html')

if __name__ == '__main__':
    app.run(debug=True)
