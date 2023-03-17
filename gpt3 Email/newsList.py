import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import openai
from bs4 import BeautifulSoup
import requests

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

openai.api_key = "sua chave openAI" 
url = "https://olhardigital.com.br" # site para extrair
response = requests.get(url) #request html
html = response.content

soup = BeautifulSoup(response.content, 'html.parser') #configurao beautifulsoup

textSend = [] #corpo do email ja tratado
noticias_tratadas = []

#funçao para resumir utilizando chat gpt
def gpt3(prompt):
    completions = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = completions.choices[0].text
    return message.strip()

#funçao para enviar email
def sendEmailGmail():
  email_de_origem = "seu email"
  senha = "sua senha"
  email_de_destino = "email de destino"

  mensagem = MIMEMultipart()
  mensagem['Subject'] = "Suas Noticias"

  corpo = string_concatenada = ' '.join(textSend)
  mensagem.attach(MIMEText(corpo, 'plain'))

  servidor = smtplib.SMTP('smtp.gmail.com', 587)
  servidor.starttls()
  servidor.login(email_de_origem, senha)

  servidor.sendmail(email_de_origem, email_de_destino, mensagem.as_string())

  servidor.quit()


#funçao que executa o tudo
def executeFile():
    for news in soup.find_all('div', class_='home-featured'):
        noticias = news.find_all('a')
        for link in noticias:
            link_href = link.get('href')
            if link_href:
                link_response = requests.get(link_href)
                link_html = link_response.content
                link_soup = BeautifulSoup(link_html, 'html.parser')
                titulo = link_soup.find('h1').text
                escopo = link_soup.find_all('p')
                conteudo_noticia = []
                for p in escopo:
                    if p.text:
                        conteudo_noticia.append(p.text)
                noticia = [titulo, ''.join(conteudo_noticia)]
                noticias_tratadas.append(noticia)
sendEmailGmail()

executeFile();