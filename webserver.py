from flask import Flask,render_template

app = Flask("website")

@app.route("/")
def mostrar_imagen():
   return render_template("index.html")

@app.route("/ruta_prueba")
def hello_world():
    return "Hello world"
    
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port='5000')
