import requests
from bs4 import BeautifulSoup
import hashlib

data = input('Digite a Data de Publicação no formato dd/mm/aaaa: ')
main_url =  'http://www.stf.jus.br/portal/diariojusticaeletronico/'

#headers e params necessários para a autenticação da requisição no site. Caso contrário o servidor me retorna uma mensagem de operação ilegal e me "bloqueia".
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}
params = (
    ('tp_pesquisa', '0'),
    ('dataP', data)
)

def get_page (url):
        r = requests.get(url + 'montarDiarioEletronico.asp', headers=headers, params=params)
        return r

def md5_creator (file):
        hashlib.md5(file).hexdigest()
        return

def save_pdf (file):
        save_pdf = open('diario.pdf', 'wb')
        save_pdf.write(file)

response = get_page(main_url)
html_response = response.content


table = BeautifulSoup(html_response, 'html.parser')
link = table.find('a').get('href')

pdf_file = requests.get(f'{main_url}/{link.strip()}', headers=headers, params=params).content

pdf_file_md5 = md5_creator(pdf_file)

save_pdf(pdf_file)
