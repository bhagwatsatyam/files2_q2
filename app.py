from flask import Flask, render_template, request

app = Flask(__name__)

registrations = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        if name and email:
            registrations.append({'name': name, 'email': email})

    return render_template('index.html', registrations=registrations)

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3003)