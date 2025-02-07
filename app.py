from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def beranda():
    return render_template('beranda.html')

@app.route('/tentang')
def tentang():
    return render_template('tentang_kami.html')

@app.route('/program')
def program():
    return render_template('program_kerja.html')

@app.route('/berita')
def berita():
    return render_template('berita_kegiatan.html')

@app.route('/galeri')
def galeri():
    return render_template('galeri.html')

@app.route('/kontak')
def kontak():
    return render_template('kontak.html')

if __name__ == '__main__':
    app.run(debug=True)
