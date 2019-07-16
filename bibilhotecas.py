# -*- coding utf-8 -*- 


import math 
x = 5
print(math.sqrt(5))
print(math.sin(x))
print(math.log(x))
print(math.cos(x))


import smtplib
server = smtplib.SMTP('mail.xx.net')

# Envio de e-mail da conta @xy para a conta @xx
server.sendmail 
('leonardo@xy.com', 'leonardo@xx.net',

"""To: leonardo@xx.net

From: leonardo@xy.com

Subject: Teste de envio de email

Estou lhe enviando este email como um teste.

""")
server.quit()
print('Envio ok')

import time

for i in range(1,6):
    time.sleep(1)
    print( f'Se passou {i} segundo(s).')

