from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bellman1')
def bellman1():
    return render_template('bellman1.html')

@app.route('/bellman2')
def bellman2():
    return render_template('bellman2.html')

@app.route('/dijkstra1')
def dijkstra1():
    return render_template('dijkstra1.html')

@app.route('/dijkstra2')
def dijkstra2():
    return render_template('dijkstra2.html')

@app.route('/comparison')
def comparison():
    return render_template('comparison.html')

if __name__ == "__main__":
    app.run(debug=True)