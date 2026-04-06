# app.py - Backend em Python usando Flask

from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Configurações de email (substitua pelas suas)
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'devitifree36@gmail.com'  # Seu email
SENDER_PASSWORD = 'sua_senha_aqui'  # Substitua pela sua senha ou use app password
RECEIVER_EMAIL = 'tpnunes2025@gmail.com'  # Email para receber as mensagens

def send_email(name, email, message):
    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = f'Nova mensagem do blog: {name}'

        body = f'Nome: {name}\nEmail: {email}\n\nMensagem:\n{message}'
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        text = msg.as_string()
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, text)
        server.quit()
        return True
    except Exception as e:
        print(f'Erro ao enviar email: {e}')
        return False

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('posts.html')

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        if send_email(name, email, message):
            return redirect(url_for('home'))
        else:
            return 'Erro ao enviar mensagem. Tente novamente.'
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)