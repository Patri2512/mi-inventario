from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Por ahora, usamos esta lista como nuestra "base de datos" temporal
inventario = [
    {'nombre': 'Café Moca', 'stock': 10, 'precio': 5.50}
]

@app.route('/')
def home():
    return render_template('index.html', lista=inventario)

# Esta es la API para anexar productos
@app.route('/api/productos', methods=['POST'])
def agregar_producto():
    # Obtenemos los datos del formulario
    nombre = request.form.get('nombre')
    stock = request.form.get('stock')
    precio = request.form.get('precio')

    # Validamos que no vengan vacíos y creamos el nuevo objeto
    if nombre and stock and precio:
        nuevo_item = {
            'nombre': nombre,
            'stock': int(stock),
            'precio': float(precio)
        }
        inventario.append(nuevo_item) # Lo anexamos a la lista
    
    # Redirigimos al inicio para ver el cambio
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)