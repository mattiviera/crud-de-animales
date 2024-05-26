from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simula una base de datos en memoria
animals = []

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', animals=animals)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        photo = request.form['photo']
        characteristic1 = request.form['characteristic1']
        characteristic2 = request.form['characteristic2']
        characteristic3 = request.form.get('characteristic3', '')
        characteristic4 = request.form.get('characteristic4', '')

        # Validar que el nombre sea único
        if any(animal['name'] == name for animal in animals):
            return 'El nombre debe ser único'

        animals.append({
            'name': name,
            'photo': photo,
            'characteristic1': characteristic1,
            'characteristic2': characteristic2,
            'characteristic3': characteristic3,
            'characteristic4': characteristic4
        })

        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/animal/<name>')
def detail(name):
    animal = next((animal for animal in animals if animal['name'] == name), None)
    if animal is None:
        return 'Animal no encontrado'
    return render_template('detail.html', animal=animal)

@app.route('/update/<name>', methods=['GET', 'POST'])
def update(name):
    animal = next((animal for animal in animals if animal['name'] == name), None)
    if animal is None:
        return 'Animal no encontrado'

    if request.method == 'POST':
        animal['photo'] = request.form['photo']
        animal['characteristic1'] = request.form['characteristic1']
        animal['characteristic2'] = request.form['characteristic2']
        animal['characteristic3'] = request.form.get('characteristic3', '')
        animal['characteristic4'] = request.form.get('characteristic4', '')

        return redirect(url_for('index'))

    return render_template('update.html', animal=animal)

@app.route('/delete/<name>')
def delete(name):
    user = name.query.get(name)
    if user:
        try:
            animals.delete(user)
            animals.commit()
        except Exception as e:
            print(f'Error al eliminar. {e}')
    return redirect('/home')

if __name__ == '__main__':
    app.run(debug=True)
