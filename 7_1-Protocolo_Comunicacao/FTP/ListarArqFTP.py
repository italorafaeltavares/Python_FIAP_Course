from ftplib import *

ftp_ativo = False
ftp = FTP('ftp.ibiblio.org')

print(ftp.getwelcome())
usuario = input("Digite o usuário:")
senha = input("Digite a senha: ")

ftp.login(username, senha)
print("Diretório atual de trablaho: ", ftp.pwd())
ftp.cwd('pub')

print("Diretório corrente: ", ftp.pwd())
print(ftp.retrlines('LIST'))

ftp.quit()

