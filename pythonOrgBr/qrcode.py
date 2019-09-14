# -*- encoding: utf-8 -*- 
import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('''BEGIN:VCARD
VERSION:3.0
FN;CHARSET=UTF-8:Gaspar Carreira Júnior
N;CHARSET=UTF-8:;Gaspar Carreira Júnior;;;
EMAIL;CHARSET=UTF-8;type=WORK,INTERNET:gaspar@carreirajrconsultoria.com
TEL;TYPE=CELL:21988010159
TITLE;CHARSET=UTF-8:Business Advisor, Conselheiro, Consultor
ORG;CHARSET=UTF-8: Gestão empresarial e Financeira''')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.show()