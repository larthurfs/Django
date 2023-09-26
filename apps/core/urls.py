"""
As URLS criam rotas em um sistema web, em um projeto Django o arquivo urls.py que vem por padrão dentro do diretório do projeto
são responsáveis por mapear as URLs acessadas pelos usuários para as views correspondentes, que processam as requisições e retornam as respostas apropriadas.
Uma rota de URL consiste em um padrão de URL e uma view associada a esse padrão.
Apesar do Django não criar um arquivo de moelo urls.py dentro da app Django, recomendo fortemente que você sempre crie dentro de suas apps.
Ter um arquivo de modelo urls.py em cada app vai facilitar a organização do seu código e você vai conseguir configurar as rotas de seu projeto de uma forma muito mais organizada.



Por padrão dentro do urls.py você vai encontrar a variável urlpatterns que é uma lista que contém as definições das rotas de URL do sistema.
Cada rota é definida como uma instância da função path() ou re_path(),
cada instância da função path() ou re_path() especifica um padrão de URL e uma view a ser associada a esse padrão.
O padrão de URL pode ser uma string literal ou um padrão regex.

"""



from django.urls import path #importa a função path do módulo django.urls. A função path é usada para definir as rotas de URL no Django.
from apps.core.views import home, ferramenta_qrcode #importa a view home do módulo views dentro da app core. A view home será associada à rota de URL definida.

urlpatterns = [
    path('', home, name='home'), #Esta é uma definição de rota de URL. O primeiro parâmetro vazio '' indica o padrão de URL raiz, que corresponde à página inicial do sistema. A view associada a essa rota é a home, importada anteriormente. O parâmetro name é opcional e define o nome da rota, neste caso, 'home'.
    path('qrcode', ferramenta_qrcode, name='ferramenta_qrcode'), #define o padrão da URL que será mapeada. Neste caso, quando o usuário acessar a rota "qrcode" no navegador, essa rota será ativada. No contexto de um servidor local, essa rota será chamada quando a URL http://127.0.0.1:8000/qrcode for acessada.
]







from apps.core.views import home, ferramenta_qrcode, ferramenta_recibos, ferramenta_senha, ferramenta_numeros, guru_inativo,ferramenta_guru

urlpatterns = [
    path('', home, name='home'),
    path('qrcode', ferramenta_qrcode, name='ferramenta_qrcode'),
    path('recibos', ferramenta_recibos, name='ferramenta_recibos'),
    path('senha', ferramenta_senha, name='ferramenta_senha'),
    path('numeros', ferramenta_numeros, name='ferramenta_numeros'),
    path('guru/dormindo', guru_inativo, name='guru_inativo'),
    path('guru', ferramenta_guru, name='ferramenta_guru'),

]




