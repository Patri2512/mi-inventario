from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configuración de la base de datos SQLite
# Creamos un archivo llamado 'inventario.db' en la carpeta raíz
db_path = os.path.join(os.path.dirname(__file__), 'inventario.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Definimos el modelo de la tabla de Inventario
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Float, nullable=False)

# Crear la base de datos físicamente al arrancar
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    # Consultamos todos los productos de la base de datos
    todos_los_productos = Producto.query.all()
    return render_template('index.html', lista=todos_los_productos)

@app.route('/api/productos', methods=['POST'])
def agregar_producto():
    nombre = request.form.get('nombre')
    stock = request.form.get('stock')
    precio = request.form.get('precio')

    if nombre and stock and precio:
        # Creamos un nuevo objeto Producto y lo guardamos
        nuevo_item = Producto(nombre=nombre, stock=int(stock), precio=float(precio))
        db.session.add(nuevo_item)
        db.session.commit()
    
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)