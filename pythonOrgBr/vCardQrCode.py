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
FN;CHARSET=UTF-8:Vinícius Marcílio
N;CHARSET=UTF-8:;Vinícius Marcílio;;;
EMAIL;CHARSET=UTF-8;type=WORK,INTERNET: vinicius.marcilio@montreal.com.br
TEL;TYPE=CELL:55 21 98758-4534
TITLE;CHARSET=UTF-8:Gerente de Novos Negócios
ORG;CHARSET=UTF-8: Montreal Informática
''')
qr.make(fit=True)

img = qr.make_image(fill_color="#7e171d", back_color = "#dddddc")
img.show()
img.save('qrVinícius.png', 'PNG')