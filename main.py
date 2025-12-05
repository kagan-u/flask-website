from flask import Flask , render_template
import random
app = Flask(__name__)
gercekler = ["Elon Musk ayrıca sosyal ağların düzenlenmesini ve kullanıcıların kişisel verilerinin korunmasını savunmaktadır. Sosyal ağların hakkımızda büyük miktarda bilgi topladığını ve bu bilgilerin daha sonra düşüncelerimizi ve davranışlarımızı manipüle etmek için kullanılabileceğini iddia ediyor."," Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.", "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor." ]

@app.route("/")
def hello_world():
    return f'<h1>{random.choice(gercekler)}</h1>'
@app.route("/homepage")
def homepage():
    return render_template("index.html")
@app.route("/sifreolusturucu")
def sifreolsuturucu():
    return render_template("sifreolusturucu.html")
app.run(debug=True)