from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        with open('bookings.txt', 'a') as f:
            f.write(f"{name},{email},{phone}\n")
        return redirect(url_for('index'))
    return render_template('book.html')

if __name__ == '__main__':
    app.run(debug=True)
