from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def ana_sayfa():
    return render_template('index.html')

if __name__ == '__main__':
    # host='0.0.0.0' sayesinde site hem bilgisayarında hem aynı Wi-Fi'daki telefonlarda çalışır
    app.run(host='0.0.0.0', port=5000, debug=True)