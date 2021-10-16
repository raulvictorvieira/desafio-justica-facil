import requests
from requests.sessions import Session

main_url =  'http://www.stf.jus.br/portal/diariojusticaeletronico/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

params = (
    ('tp_pesquisa', '0'),
    ('dataP', '15/10/2021')
)

response = requests.get(main_url + 'verDiarioEletronico.asp?seq=757749531&amp;data=14/10/2021&amp;ano=2021&amp;numero=205', headers=headers, params=params)

pdf = open('file.pdf', 'wb')
pdf.write(response.content)
