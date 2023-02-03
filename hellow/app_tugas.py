from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Steven Gerrard</h1><br><p>Steven George Gerrard MBE (lahir di Whiston, Merseyside, Inggris, 30 Mei 1980; umur 39 tahun) adalah seorang mantan pemain sepak bola asal Inggris, dan manajer klub sepak bola asal Skotlandia, Rangers. Dia telah memainkan sebagian besar kariernya di posisi pusat lini tengah, tetapi ia juga pernah diposisikan sebagai second striker, gelandang bertahan, bek kanan, dan pemain sayap kanan.[3][4] Pemain asli kota Liverpool atau Liverpudlian ini mengidolakan John Barnes, yang sama-sama memainkan peran playmaker di lapangan tengah. Ia menikah dengan Alex Curran dan dianugerahi empat anak, yakni: Lourdes Gerrard, Lexie Gerrard, Lilly-Ella Gerrard, dan Lio Gerrard. Pada tahun 2015, Stevie G, demikian ia kerap dipanggil, menerbitkan buku "My Story" yang ditulisnya sendiri dan berkisah soal perjalanan kariernya.<p><br><a href="gelar">gelar</a> <a href="kawal">kehidupan awal</a>';

@app.route('/gelar')
def gelar():
	return '<h2>gelar</h2><br><ul><li>Piala FA: 2000–01, 2005–06</li><li>Piala Liga Inggris: 2000–01, 2002–03, 2011–12</li><li>FA Community Shield: 2006</li><li>Liga Champions UEFA: 2004–05</li><li>Piala UEFA: 2000–01</li><li>Piala Super UEFA: 2001</li></ul><a href="/">home</a>  <a href="kawal">kehidupan awal</a>';

@app.route('/kawal')
def kawal():
	return '<h2>kehidupan awal</h2><br><p>Gerrard mulai bermain bersama tim lokal, Whiston Juniors. Dia mendapat perhatian dari pencari bakat Liverpool dan bergabung dengan akademi junior The Reds saat usianya 9 tahun.[14] Dia hanya bermain dalam beberapa pertandingan, karena perkembangannya yang lambat membuat dia hanya bermain dalam 20 pertandingan saat berusia 14 hingga 16.[butuh rujukan] Diusia 14, Gerrard memperoleh kesempatan bertanding dengan beberapa klub, termasuk Manchester United. Dalam autobiografinya, dia mengatakan "untuk menekan Liverpool agar memberi saya YTS kontrak." selama masa tersebut dia sempat mengalami kecelakaan yang disebabkan garpu taman yang berkarat yang dapat menyebabkan dia kehilangan jari kakinya.[15] Gerrard menandatangani kontrak profesional pertamanya bersama Liverpool pada 5 November 1997.[15]</p><a href="gelar">gelar</a> <a href="/">home</a>';

if __name__ == '__main__':
	app.run(debug = True)
