import os
from flask import Flask, request
from flask_cors import CORS
import gets_posts_requests
from bs4 import BeautifulSoup
import json

class live_games_post(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)
        
class retorno_post(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)
        
app = Flask(__name__)
CORS(app, resource={r"/*":{"origins":"*"}})

def games_live_func(lg_post):
    rtn = retorno_post('{}')
    rtn.lista_de_jogos = []
    
    pagina = "https://www.matchendirect.fr/live-score/"
    htmlPagina = gets_posts_requests.get_list_games_live(pagina)
    soup = BeautifulSoup(htmlPagina, 'html.parser')
    tabela_eventos = soup.find_all('div', {'class','panel panel-info'})
    for te in tabela_eventos:
        try:
            qtd_jogos_campeonato = len(te.find_all("td", {"class","lm3"}))
            for i in range(0,qtd_jogos_campeonato):
                campeonato = te.find_all("div", {'class','lienCompetition'})[0].text
                tempo_de_jogo = te.find_all("td", {'class','lm2 lm2_1'})
                tempo_de_jogo = str(tempo_de_jogo[i]).split('</span>')[1].split('\'''</td>')[0].replace('Mi-Tps</td>','45')
                info_confronto = te.find_all("td", {"class","lm3"})[i]
                time_casa = info_confronto.find_all("a")[0].find_all("span", {"class","lm3_eq1"})[0].text
                time_visitante = info_confronto.find_all("a")[0].find_all("span", {"class","lm3_eq2"})[0].text
                placar_casa = info_confronto.find_all("a")[0].find_all("span", {"class","lm3_score"})[0].text.split(' - ')[0]
                placar_visitante = info_confronto.find_all("a")[0].find_all("span", {"class","lm3_score"})[0].text.split(' - ')[1]
                
                if (int(tempo_de_jogo) >= int(lg_post.min_inicio) and int(tempo_de_jogo) < int(lg_post.min_fim)):
                    if (str(lg_post.totalgols) != ''):                        
                        if ((int(placar_casa) + int(placar_visitante)) == int(lg_post.totalgols)):
                            result_jogos = json.loads('{"competicao": "'+campeonato+'","confronto": "'+time_casa+" x "+time_visitante+'", "placar": "'+placar_casa+" - "+placar_visitante+'", "tempo_de_jogo": "'+tempo_de_jogo+'"}')
                            rtn.lista_de_jogos.append(result_jogos)
                            print('''
                                Campeonato: {}
                                Confronto: {} x {}
                                placar: {} - {}
                                Tempo de jogo: {}'''.format(campeonato,time_casa,time_visitante,placar_casa,placar_visitante,tempo_de_jogo))
                    else:
                        result_jogos = json.loads('{"competicao": "'+campeonato+'","confronto": "'+time_casa+" x "+time_visitante+'", "placar": "'+placar_casa+" - "+placar_visitante+'", "tempo_de_jogo": "'+tempo_de_jogo+'"}')
                        rtn.lista_de_jogos.append(result_jogos)
                        print('''
                            Campeonato: {}
                            Confronto: {} x {}
                            placar: {} - {}
                            Tempo de jogo: {}'''.format(campeonato,time_casa,time_visitante,placar_casa,placar_visitante,tempo_de_jogo))
        except Exception as ex:
            print("Descrição do erro:\n" + str(ex))
    return json.dumps(rtn.__dict__)

@app.route("/live_games/", methods=['POST'])
def games_live():
    lg_post = live_games_post(json.dumps(request.get_json()))
    rtn = games_live_func(lg_post)
    return rtn

def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == '__main__':
    main()
    