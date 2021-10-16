import requests
from requests.sessions import Session

cookies = {
    '__utmz': '60534895.1633476064.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'ASPSESSIONIDQCARDTDC': 'KLOJNHOADEIDMHEPMIGJBBBH',
    '__utma': '60534895.950547131.1633476064.1634081690.1634326503.8',
    '__utmc': '60534895',
    'ASPSESSIONIDQABTDQCB': 'EGPJNHOADIFNGEBGOJDGHAFO',
    'ASPSESSIONIDQABABRRD': 'EBCEEIOANLNJJGBBOCMHNKFM',
    'ASPSESSIONIDSAAQDRDA': 'OCGBOOOAHKPKDPKLAELJPNAB',
    'ASPSESSIONIDSACQDSDC': 'MKPBOOOALLFFEIDGBKIOLKNM',
    'ASPSESSIONIDQACQDTCD': 'OECJOFPAKMLMGPLIGAFAGIIE',
    'ASPSESSIONIDSAACARRC': 'POEDFGPAJOPOFGJEGHKDIFOA',
    'ASPSESSIONIDSACQDRCA': 'JJGJOFPAIAMNEANNJLFCCEKP',
}

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-GPC': '1',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
}

params = (
    ('tp_pesquisa', '0'),
    ('numDj', ''),
    ('anoDj', ''),
    ('dataD', ''),
    ('dataP', '15/10/2021'),
    ('argumento', ''),
)

session = requests.Session()

session.get('http://www.stf.jus.br/portal/diariojusticaeletronico/pesquisardiarioeletronico.asp', headers=headers)

response = requests.get('http://www.stf.jus.br/portal/diariojusticaeletronico/montarDiarioEletronico.asp', headers=headers, params=params)

main_url =  'http://www.stf.jus.br/portal/diariojusticaeletronico/'

response2 = requests.get(main_url + 'verDiarioEletronico.asp?seq=757632168&data=05/10/2021&ano=2021&numero=199', headers=headers, params=params)

pdf = open('file.pdf', 'wb')
pdf.write(response2.content)
