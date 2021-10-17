# Desafio Justiça Fácil :rocket:

Desafio em Python para a vaga de estágio da Justiça Fácil

## Relatório :orange_book:

Confesso que foi um desafio e tanto para mim. Como não tinha quase nenhum conhecimento em Python e em requisições http, passei a maior parte do tempo estudando e buscando algumas documentações sobre as ferramentas que eu iria usar.
No início tentei entender como eu iria fazer para dar um input com a data direto na página a partir do código, por estar mais familiarizado com o JS e a manipulação do DOM.
Então, depois de apanhar e não sair do lugar, fui para a página e verifiquei no DevTools a aba de network. Tentei entender de uma forma agnóstica à linguagem como funcionava o processo de requisição a partir do momento em que jogamos uma data no input. Após isso, tive uma considerável evolução no meu entendimento e na codificação do algorítmo.
Identifiquei a requisição e copiei a cURL para simular o mesmo no Python. Vi que todas as requisições usavam uma url padrão e a partir do momento que recebia o response da requisição ele me devolvia uma table contendo as informações do PDF. Então a partir dessa table eu consegui capturar o link complementar para acesso do PDF (para isso utilizei o BeautifulSoup e consegui capturar o link da tag desejada).

## Documentação :blue_book:

O projeto foi desenvolvido para fazer uma requisição de diários oficiais do **Supremo Tribunal Federal**. Após execução do algoritmo no terminal, será solicitado um input de uma data no formato (dd/mm/aaaa), que será a **data de publicação** do diário. Logo que inserido a data, ele irá retornar uma hash MD5 do mesmo e te dar uma opção de salvar ou não, e encerrará o programa.

### :alien: Fontes :flying_saucer:

- Requests (https://docs.python-requests.org/en/latest/)
- BeautifulSoup (https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- hashlib (https://pythonhelp.wordpress.com/tag/md5/)
- Stackoverflow
- Alguns vídeos no YouTube
