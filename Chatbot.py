import os


def processar_resposta(resposta,nome):
    if resposta ==   '1':
        print(f'{os.linesep}{nome} na minha opinião sim, visto que os veiculos antigos tiveram uma valorização acima de 400% nos ultimos 10 anos.Além de ser um hobby muito legal, pode ser visto também como um investimento pois os veiculos antigos tendemsempre a valorizar com o passar dos anos.{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome} os modelos que ainda possuem um preço mais em conta são Chevrolet Chevette, Vw Fusca, Ford Corcel. Dependendo do ano de fabricação, ainda é possível encontrar veiculos com bons preços{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome} as chances são maiores em cidades do interior. Lá é possível encontrar veículos em bom estado de conservação por um preço interessante {os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome} sim, existem lojas especializadas porém recomendamos que sempre pesquise bastante e busque um recomendações positivas da loja ou do vendedor.{os.linesep}')
    else:
        print('Digite apenas 1, 2, 3 ou 4')


def start():
    print("Olá! Seja bem-vindo ao guia de compra de veiculos antigos")
    nome = input('Digite seu nome:')

    email = input('Digite seu email:')
    while True:
     resposta = input(
         f'O que voce gostaria de saber?{os.linesep}[1] - Vale a pena comprar um veiculo antigo?{os.linesep}[2] - Quais modelos tem o melhor preço?{os.linesep}[3] - Onde encontrar esses veículos com um preço mais em conta?{os.linesep}[4] - Existe alguma loja confiavel que venda esse tipo de veiculo?{os.linesep}')
     processar_resposta(resposta,nome)
    
 
 
 
 
 
if __name__ == '__main__':
     start()
 








