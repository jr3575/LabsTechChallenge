from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/jr3575', methods=['GET'])
def wtf():
    return render_template('jr3575.html')


if __name__ == '__main__':
    app.run()
