# 6 - Menu de Hierarquia
# Crie um programa que mostre o seguinte menu:
# Constituição
# Leis
# Decretos
# Resoluções
# Normas Técnicas
# Sair
# O usuário escolhe a opção
# O programa mostra a descrição da Fonte do Direito correspondente
# Repete até que a opção seja 6 (sair)

def Leis():
    print('LEIS:\n '
          'As leis ordinárias e complementares compõem a base prática do \n'
          'ordenamento jurídico brasileiro.\n'
          'Leis complementares detalham aspectos mais específicos \n'
          'e sensíveis, exigindo um processo legislativo mais rigoroso.')


def Constituicao():
    print('Constituicao:\n '
          'Garante direitos essenciais no mundo digital, como privacidade \n'
          'de dados, liberdade de expressãonas redes, acesso à informação \n'
          'e proteção contra abusos do poder público ou de empresas \n'
          'de tecnologia.')


def Decretos():
    print('DECRETOS:\n'
          'Os decretos são instrumentos normativos criados pelo Poder\n'
          'Executivo com o objetivo de detalhar e regulamentar a aplicação \n'
          'das leis aprovadas pelo Legislativo. Embora não tenham força para\n'
          'criar novas obrigações além da lei, são fundamentais para definir\n'
          ' como a norma será colocada em prática no dia a dia. Na área da \n'
          ' informática, muitos decretos trazem orientações específicas \n'
          'sobre a implementação de leis voltadas para tecnologia e \n'
          'proteção de dados.')


def Resolucoes():
    print('RESOLUÇÕES:\n '
          'As resoluções são normas criadas por órgãos públicos e entidades\n'
          'reguladoras para disciplinar situações específicas dentro de \n'
          'suas áreas de atuação. Diferentemente das leis e decretos, elas \n'
          'não abrangem toda a sociedade, mas têm força normativa sobre\n'
          ' setores determinados. Na área da informática e telecomunicações\n'
          ' as resoluções são especialmente relevantes, pois estabelecem \n'
          'regras técnicas e operacionais que impactam diretamente \n'
          'endempresas e usuários.')


def normas_tecnicas():
    print('NORMAS TÉCNICAS:\n '
          'As normas técnicas são documentos elaborados por instituições\n'
          'especializadas que definem padrões, requisitos e boas práticas\n'
          ' para diferentes áreas do conhecimento. Embora não tenham a mesma\n'
          ' força de uma lei, desempenham papel essencial na padronização de\n'
          ' processos e na garantia de qualidade e segurança. No campo da\n'
          ' informática, essas normas são indispensáveis, pois estabelecem\n'
          'critérios técnicos que impactam diretamente o desenvolvimento de\n'
          'softwares, a segurança da informação e até a ergonomia no uso de\n'
          ' equipamentos.')


while True:
    menu = input('1-leis, '
                 '2-Constituição, '
                 '3-Decretos, '
                 '4-Resoluções, '
                 '5-Normas Técnicas, '
                 '6-Sair: ')
    try:
        opcao = int(menu)
    except ValueError:
        print('por favor somente numeros inteiros')
        continue

    if opcao == 1:
        Leis()
    elif opcao == 2:
        Constituicao()
    elif opcao == 3:
        Decretos()
    elif opcao == 4:
        Resolucoes()
    elif opcao == 5:
        normas_tecnicas()
    elif opcao == 6:
        print('saindo...')
        break
    else:
        print('opção invalinda! escolha de 1 a 6.')
