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
        return requests.get(url + 'montarDiarioEletronico.asp', headers=headers, params=params)

def md5_creator (file):
        return hashlib.md5(file).hexdigest()

def save_pdf (file):
        file_pdf = open(f'{md5_pdf_file}.pdf', 'wb')
        file_pdf.write(file)

response = get_page(main_url)

if response.status_code == 200:
        html_response = response.content

        table = BeautifulSoup(html_response, 'html.parser')
        link = table.find('a').get('href')

        #quando localizo a tag <a> com o href desejado, vem um grande espaço antes do link. Então utilizei o .strip() para retirar este espaço do início e não quebrar o meu get
        raw_pdf_file = requests.get(f'{main_url}/{link.strip()}', headers=headers, params=params).content

        md5_pdf_file = md5_creator(raw_pdf_file)
        print(md5_pdf_file)

        save = input('Deseja salvar o arquivo em pasta local? 1-Sim 2-Não: ')
        if save == '1':
                save_pdf(raw_pdf_file)
                print(f'Arquivo {md5_pdf_file} salvo com sucesso!')
        elif save == '2':
                print('Arquivo não salvo!')
        else:
                print('Opção inválida!')
else:
        print(f'ERROR {response.status_code}... Data inválida ou página não encontrado!')
