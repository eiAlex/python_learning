# -*- encoding: utf-8 -*- 


import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=15,
    border=1,
)
qr.add_data('''BEGIN:VCARD
VERSION:3.0
FN;CHARSET=UTF-8:Pedro Canalini
N;CHARSET=UTF-8:;Pedro Canalini;;;
EMAIL;CHARSET=UTF-8;type=WORK,INTERNET:pedroc@montreal.com.br
TEL;TYPE=CELL:21975395588 
TEL;TYPE=WORK,VOICE:2122764093 
TITLE;CHARSET=UTF-8:Gerente Comercial | Diretoria Regional RJ
ORG;CHARSET=UTF-8: Montreal Informática
URL;type=WORK;CHARSET=UTF-8:https://www.montreal.com.br/
END:VCARD
''')
qr.make(fit=True)

img = qr.make_image(fill_color="#7e171d", back_color = "#dddddc")
img.show()
img.save('QrcodePedro_1.png', 'PNG')