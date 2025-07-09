import tkinter as tk
from tkinter import font, colorchooser
from PIL import Image, ImageTk
import random
import os
import sys

'''
TKINTER
É uma biblioteca que fornece uma Interface Gráfica (GUI) que já vem por padrão no Python.
Ela quem vai fornecer uma maneira de criar os botões, janelas, caixa de texto, áreas de imagens e os outros elementos visuais do aplicativo.

--FONT: É usado para para obter uma lista de todas as famílias de fontes disponíveis no sistema do usuário.
Isso permite que o usuário escolha uma fonte instalada em seu computador para o texto da frase.

--COLORCHOOSER: É usado para abrir a caixa de diálogo de seleção de cores, permitindo que o usuário escolha a cor do texto da frase.

PILLOW (PIL)
É uma biblioteca para processamento e imagens

--IMAGE: É a classe principal da Pillow que representa uma imagem.
Ela fornece métodos para abrir, manipular (redimensionar, cortar, etc.) e salvar imagens.

--IMAGETK: É um submódulo da Pillow que fornece a ponte entre os objetos de imagem do Pillow (PIL.Image) e os objetos de imagem que o tkinter pode exibir (tk.PhotoImage).
É usado pois o Tkinter por padrão só suporta os formatos GIF e PPM/PGM

RANDOM
É um módulo padrão do Python que implementa geradores de números pseudoaleatórios.

OS
É um módulo padrão do Python que fornece uma maneira de interagir com o sistema operacional (Operating System).
Ele oferece funções para trabalhar com caminhos de arquivo e diretório, variáveis de ambiente, processos, etc.

SYS
O módulo sys é um módulo embutido no Python que fornece acesso a variáveis e funções que interagem diretamente com o interpretador Python e o ambiente em que o script está sendo executado.
No código ele é necessario para indica quando o código está rodando pelo interpretador ou quando está rodando como ececutável
'''

frases_por_tema = {}
pastas_por_tema = {}
config_fonte = {}
caminho_imagens_base = ""
cor_texto_atual = "white"
janela_principal = None
tela = None
id_imagem_fundo = None
texto_frase = None
botao_gerar_frase = None
botao_mudar_fonte = None
id_janela_moldura_botoes = None
caminho_imagem_atual = None
imagem_tk = None

def inicializar_app(): # função que inicializa o aplicativo
    '''
    Essa é a função que inicializa o aplicativo.

    '''
    global janela_principal, frases_por_tema, pastas_por_tema, caminho_imagens_base, \
           config_fonte, cor_texto_atual, tela, id_imagem_fundo, texto_frase, \
           botao_gerar_frase, botao_mudar_fonte, id_janela_moldura_botoes, imagem_tk

    janela_principal = tk.Tk() # Cria a janela principal
    janela_principal.title("Motivação Verde") # Define o texto que aparecerá na barra de título da janela principal.
    janela_principal.geometry("960x540") #  Define as dimensões iniciais em pixels.
    janela_principal.resizable(True, True) # Controla se a janela pode ser redimensionada nos eixos X e Y (X, Y).
    
    caminho_base_app = "" # essa é a variável que indica onde o aplicativo vai encontrar as imagens

    if getattr(sys, 'frozen', False):
        caminho_base_app = sys._MEIPASS
        '''
        getattr tenta conseguir o valor de 'frozen' de sys
        Se não existir significa que o aplicativo não foi empacotado e está rodando como um script Python normal.
        Se existir o caminho para as imagens está em sys._MEIPASS que é o diretorio temporado gerado pelo PyInstaller.
        '''

    else:
        caminho_base_app = os.path.dirname(os.path.abspath(__file__))
        '''
        Caso o aplicativo não esteja rodando como um executável, o caminho para as imagens é onde o script está localizado
        os.path.abspath(__file__): Retorna o caminho absoluto do arquivo do script atual.
        os.path.dirname(...): Retorna o diretório que contém o caminho especificado.
        '''

    frases_por_tema.update({
        "Mudanças Climáticas": [
            "O futuro do planeta está em nossas mãos; cada ação conta.",
            "Pequenas escolhas diárias somam-se a um grande impacto contra as mudanças climáticas.",
            "A inação de hoje é o arrependimento de amanhã. Aja pelo clima!",
            "Proteger o clima é proteger a vida.",
            "Nosso lar é só um. Vamos defendê-lo das mudanças climáticas.",
            "O tempo de agir é agora. O clima não espera.",
            "Seja a mudança que você quer ver no clima do mundo.",
            "Sustentabilidade é a chave para um futuro sem crises climáticas.",
            "A ciência nos alerta. A consciência nos move.",
            "O planeta pede socorro. Nossa responsabilidade é responder.",
            "Menos carbono, mais vida.",
            "Cada árvore plantada é um sopro de esperança para o clima.",
            "O clima não é uma questão política, é uma questão de sobrevivência.",
            "Que a esperança no futuro inspire nossas ações pelo clima hoje.",
            "Juntos podemos reverter o curso. O clima agradece."
        ],
        "Educação Ambiental": [
            "Conhecimento ambiental liberta e transforma.",
            "Educar para preservar é semear um futuro verde.",
            "A semente da mudança começa na educação ambiental.",
            "Cuidar do meio ambiente é um aprendizado contínuo.",
            "Quem aprende a respeitar a natureza, aprende a respeitar a si mesmo.",
            "Invista em educação ambiental e colha um planeta mais saudável.",
            "A melhor herança que podemos deixar é a consciência ambiental.",
            "Transforme informação em ação: eduque-se, eduque a todos.",
            "A educação é a base para um mundo mais sustentável.",
            "Despertar a consciência ambiental é o primeiro passo para a mudança.",
            "Não há futuro sem educação ambiental.",
            "Que a curiosidade pela natureza inspire nosso aprendizado.",
            "A natureza ensina, nós aprendemos a cuidar.",
            "Um futuro verde se constrói com mentes conscientes.",
            "Educar ambientalmente é plantar respeito pela vida."
        ],
        "Urbanização e Meio Ambiente": [
            "Cidades verdes são cidades que respiram.",
            "O crescimento urbano pode ser sustentável. É nossa escolha.",
            "Transforme sua cidade em um oásis de sustentabilidade.",
            "Menos concreto, mais verde. Cidades do futuro!",
            "Uma cidade sustentável é um direito e um dever de todos.",
            "Respeite o verde da cidade. Ele é o pulmão da nossa vida urbana.",
            "Construa com consciência, preserve a natureza da cidade.",
            "Cidades para pessoas, não só para carros.",
            "Cuidar da cidade é cuidar de você.",
            "Cidades inteligentes pensam verde.",
            "Menos poluição, mais qualidade de vida nas cidades.",
            "Que cada esquina urbana reflita nosso compromisso ambiental.",
            "O futuro das cidades é ser parte da natureza.",
            "Planejamento urbano sustentável: a chave para o bem-estar.",
            "Por cidades que floresçam, em harmonia com o meio ambiente."
        ],
        "Resíduos/Reciclagem": [
            "Seja a solução, não a poluição. Recicle!",
            "Lixo que vira luxo: a mágica da reciclagem.",
            "Descarte certo, futuro garantido.",
            "Reduza, reutilize, recicle: os pilares de um mundo sem lixo.",
            "Cada embalagem reciclada é um pedaço de futuro salvo.",
            "Não jogue fora o que pode ser transformado.",
            "Lixo é recurso fora do lugar. Recicle!",
            "Sua atitude de hoje define o amanhã dos resíduos.",
            "Reciclar é alimentar um ciclo de vida sustentável.",
            "O planeta não é um lixão. Faça sua parte!",
            "Menos aterro, mais transformação.",
            "Que o ato de reciclar seja um hábito diário.",
            "Separe seu lixo, una-se ao futuro.",
            "A reciclagem é um presente para as próximas gerações.",
            "Pense no ciclo: nada se perde, tudo se transforma."
        ],
        "Recursos Naturais": [
            "Nossa riqueza maior está nos recursos naturais; vamos protegê-los.",
            "Cada gota de água, cada pedaço de floresta: são tesouros a serem preservados.",
            "A terra nos dá tudo. Nossa responsabilidade é devolver cuidado.",
            "Consumir com consciência é garantir que os recursos naturais durem.",
            "Sem recursos naturais, não há vida. Preserve!",
            "O futuro que queremos depende dos recursos naturais que conservamos hoje.",
            "A natureza não é um presente infinito. Use os recursos naturais com sabedoria.",
            "De cada nascente à vastidão do oceano, a vida pede proteção dos seus recursos.",
            "O bem mais precioso do planeta está nos seus recursos naturais.",
            "Preservar é o único caminho para que a natureza continue nos provendo.",
            "Menos exploração, mais renovação.",
            "Que a gratidão pelos recursos naturais inspire nossa conservação.",
            "O ar que respiramos, a água que bebemos: recursos naturais essenciais, não descartáveis.",
            "Cuidar dos recursos naturais é garantir a vida das próximas gerações.",
            "Seja um guardião da natureza. Nossos recursos naturais dependem de você."
        ]
    })
    '''
    frases_por_tema.update({...}) preenche o dicionário com os temas e as frases criadas
    '''
        
    pastas_por_tema.update({
        "Mudanças Climáticas": "mudancas-climaticas",
        "Educação Ambiental": "educacao-ambiental",
        "Urbanização e Meio Ambiente": "urbanizacao-e-meio-ambiente",
        "Resíduos/Reciclagem": "residuos-reciclagem",
        "Recursos Naturais": "recursos-naturais",
        "Introdução": "introducao"
    })
    '''
    pastas_por_tema.update({...}) preenche o dicionário com os temas e as respectivas pastas onde estão as imagens daquele tema
    '''
    caminho_imagens_base = os.path.join(caminho_base_app, "imagens") # inidica onde estão as pastas com as imagens temas

    config_fonte.update({
        "fonte_da_frase": "Helvetica",
        "tamanho_da_fonte": 28
    })
    '''
    Esse dicionário define a fonte e o seu tamanho
    Nesse trecho são definidos os valores iniciais para a fonte ("Helvetica") e o seu tamanho (28)
    '''
    cor_texto_atual = "white" # cor inicial do texto

    tela = tk.Canvas(janela_principal, bg="black") # cria uma tela preta dentro da janela principal
    tela.pack(fill="both", expand=True) # (fill="both") faz com que a tela preencha toda a janela principal e (expand=True) se expanda junto com ela
    id_imagem_fundo = None # guarda o ID da imagem do fundo

    texto_frase = tela.create_text( # cria um objeto de texto
        480, 270, # coordenadas do centro do texto
        text="Qual a sua frase do dia?", # texto inicial
        width=700, # largura máxima da caixa de texto
        font=(config_fonte["fonte_da_frase"], config_fonte["tamanho_da_fonte"], "bold"), # fonte, tamanho e estilo (negrito) do texto
        fill=cor_texto_atual, # cor do texto
        justify="center" # centraliza o texto
    )

    moldura_botoes = tk.Frame(janela_principal) # lugar (frame) onde ficaram os botões
    
    botao_gerar_frase = tk.Button(moldura_botoes, text="Nova Frase", command=gerar_nova_frase_e_imagem, font=("Arial", 14), bg="#4CAF50", fg="white", relief="raised", bd=3) # Dá ao botão uma aparência "elevada"
    botao_gerar_frase.pack(side="left", padx=10, pady=10) 
    '''
    Configuração do botão para gerar novas frases
    '''

    botao_mudar_fonte = tk.Button(moldura_botoes, text="Mudar Fonte e Cor", command=abrir_config_fonte, font=("Arial", 14), bg="#2196F3", fg="white",relief="raised", bd=3) # Dá ao botão uma aparência "elevada"
    botao_mudar_fonte.pack(side="left", padx=10, pady=10) 
    '''
    Configuração do botão para mudar a fonte
    '''

    id_janela_moldura_botoes = tela.create_window(
        400, 500, 
        window=moldura_botoes 
    )
    '''
    Configuração a moldura dos botões
    '''

    carregar_imagem_inicial()
    janela_principal.bind("<Configure>", redimencionar)
    '''
    <Configure>: É um evento Tkinter que é disparado sempre que a janela é movida, redimensionada ou tem suas propriedades alteradas.
    redimencionar: É a função que será chamada automaticamente sempre que o evento <Configure> ocorrer na janela_principal.
    Isso garante que os elementos se ajustem a tela.
    '''

def carregar_imagem_inicial(): # Carrega a imagem inicial do aplicativo.
    caminho_pasta_imagem_inicial = os.path.join(caminho_imagens_base, pastas_por_tema["Introdução"])
    nome_arquivo_imagem_inicial = "imagem_inicial.jpg" 
    caminho_completo_imagem_inicial = os.path.join(caminho_pasta_imagem_inicial, nome_arquivo_imagem_inicial)
    carregar_imagem_fundo(caminho_completo_imagem_inicial)

def redimencionar(evento): # Função que ajusta os elementos da tela, qunado ela é redimencionada ou movimentada.
    global tela, texto_frase, caminho_imagem_atual, id_janela_moldura_botoes
    largura_tela = tela.winfo_width() # Largura da tela
    altura_tela = tela.winfo_height() # Altura da tela
    
    '''
    largura_tela e altura_tela são os valores usados como base para ajustar os demais elementos
    '''
    
    largura_texto_frase = largura_tela * 0.9 
    tela.itemconfigure(texto_frase, width=largura_texto_frase) # Define a largura máxima do texto
    tela.coords(texto_frase, largura_tela*0.5 , altura_tela*0.5) # Reposiciona o texto na tela
    
    if caminho_imagem_atual: # Carrega a imagem novamente, quando a tela é redimencionada, ou pela primeira vez, ao iniciar o aplicativo.
        carregar_imagem_fundo(caminho_imagem_atual)

    if id_janela_moldura_botoes: # Reposiciona a moldura dos botões quando a tela é redimencionada.
        tela.coords(
            id_janela_moldura_botoes, 
            largura_tela*0.5, 
            altura_tela - 60 
        )

def caminhos_imagens_do_tema(tema): # Lista o caminho para todas as imagens associadas ao tema.
    global pastas_por_tema, caminho_imagens_base
    pasta_do_tema = pastas_por_tema.get(tema)

    caminho_completo_pasta = os.path.join(caminho_imagens_base, pasta_do_tema)
    
    lista_imagens = [i for i in os.listdir(caminho_completo_pasta) if i.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    
    return [os.path.join(caminho_completo_pasta, img) for img in lista_imagens]

def carregar_imagem_fundo(caminho_imagem): # Carrega a imagem e garante que ela preencha a tela inteira.
    global caminho_imagem_atual, imagem_tk, id_imagem_fundo, janela_principal, tela
    caminho_imagem_atual = caminho_imagem 

    imagem_original = Image.open(caminho_imagem) # Abre o arquivo de imagem usando a biblioteca Pillow.
        
    largura_tela = tela.winfo_width()
    altura_tela = tela.winfo_height()

    proporcao_original = imagem_original.width / imagem_original.height # Calcula a proporção da imagem original.
    proporcao_tela = largura_tela / altura_tela # Calcula a proporção da tela.

    # Lógica para redimensionar a imagem mantendo a proporção e cobrindo a tela.
    if proporcao_original > proporcao_tela: # Se a imagem original for mais "larga" que a tela.
        nova_altura = altura_tela # A nova altura da imagem será igual à altura da tela.
        nova_largura = int(nova_altura * proporcao_original) # A nova largura é calculada para manter a proporção original.
    else: # Se a imagem original for mais "alta" ou tiver a mesma proporção que a tela.
        nova_largura = largura_tela # A nova largura da imagem será igual à largura da tela.
        nova_altura = int(nova_largura / proporcao_original) # A nova altura é calculada para manter a proporção original.

    imagem_redimensionada = imagem_original.resize((nova_largura, nova_altura), Image.LANCZOS) # Redimensiona a imagem original para as novas dimensões. LANCZOS é um filtro para melhorar a qualidade da imagem.
    imagem_tk = ImageTk.PhotoImage(imagem_redimensionada) # Converte a imagem redimensionada (Pillow Image) para um formato que o Tkinter pode exibir (PhotoImage).
    
    if id_imagem_fundo: # Verifica se já existe uma imagem de fundo na tela.
        tela.delete(id_imagem_fundo) # Remove a imagem de fundo anterior da tela para evitar sobreposição e liberar memória.
        
    deslocamento_x = (largura_tela - nova_largura)*0.5 # Calcula o deslocamento X para centralizar a imagem horizontalmente na tela.
    deslocamento_y = (altura_tela - nova_altura)*0.5 # Calcula o deslocamento Y para centralizar a imagem verticalmente na tela.
    
    id_imagem_fundo = tela.create_image( # Cria um novo item de imagem na tela.
        deslocamento_x, deslocamento_y, image=imagem_tk, anchor="nw" # Posiciona a imagem usando os deslocamentos e define o ponto de ancoragem sendo como o canto superior esquerdo (north-west).
    )
    tela.tag_lower(id_imagem_fundo) # Move a imagem para a camada mais baixa da tela, garantindo que o texto e os botões apareçam sobre ela.


def gerar_nova_frase_e_imagem(): # Função que gera uma nova frase e uma nova imagem de fundo aleatoriamente.
    global frases_por_tema, tela, texto_frase, id_imagem_fundo
    temas_disponiveis = list(frases_por_tema.keys()) # Obtém uma lista de todos os temas disponíveis no dicionário frases_por_tema.

    tema_escolhido = random.choice(temas_disponiveis) # Escolhe aleatoriamente um tema da lista de temas disponíveis.
    
    frases_do_tema = frases_por_tema.get(tema_escolhido) # Obtém a lista de frases para o tema escolhido.
  
    frase_aleatoria = random.choice(frases_do_tema) # Escolhe aleatoriamente uma frase da lista de frases associadas ao tema.
    tela.itemconfigure(texto_frase, text=frase_aleatoria) # Atualiza o texto exibido na tela com a nova frase.

    imagens_do_tema = caminhos_imagens_do_tema(tema_escolhido) # Obtém uma lista de caminhos completos para as imagens associadas ao tema escolhido.
    imagem_aleatoria = random.choice(imagens_do_tema) # Escolhe aleatoriamente um caminho de imagem da lista.
    carregar_imagem_fundo(imagem_aleatoria) # Carrega a imagem aleatória como o novo plano de fundo da tela.

def abrir_config_fonte(): # Abre uma nova janela para configurar a fonte e a cor do texto.
    global janela_principal, config_fonte, cor_texto_atual
    
    janela_config = tk.Toplevel(janela_principal) # Cria uma nova janela de nível superior (pop-up) que é filha da janela principal.
    janela_config.title("Configurar Fonte e Cor") # Define o título da nova janela.
    janela_config.geometry("400x350") # Define o tamanho inicial da janela de configuração (largura x altura).
    janela_config.transient(janela_principal) # Faz com que a janela de configuração seja dependente da janela principal (ela será minimizada/fechada junto com a principal).
    janela_config.grab_set() # Captura todos os eventos de entrada (mouse e teclado) para esta janela, bloqueando a interação com a outra janela do aplicativo.

    todas_familias_fonte = sorted(list(font.families())) # Obtém uma lista de todas as famílias de fontes disponíveis no sistema e as ordena alfabeticamente.
    
    tk.Label(janela_config, text="Fonte da Frase:").pack(pady=5) # Cria um rótulo de texto "Fonte da Frase:" na janela de configuração e o empacota com preenchimento vertical.
    var_fonte_frase_local = tk.StringVar(janela_config) # Cria uma variável especial Tkinter para armazenar a seleção da fonte pelo usuário.
    var_fonte_frase_local.set(config_fonte["fonte_da_frase"]) # Define o valor inicial da fonte com a fonte atual configurada.
    menu_fonte_frase = tk.OptionMenu(janela_config, var_fonte_frase_local, *todas_familias_fonte) # Cria um menu para seleção da família da fonte.
    menu_fonte_frase.pack() # Empacota o menu na janela de configuração.

    tk.Label(janela_config, text="Tamanho da Frase:").pack(pady=5) # Cria um rótulo "Tamanho da Frase:" e o empacota.
    escala_tamanho_frase_local = tk.Scale(janela_config, from_=10, to=60, orient="horizontal", variable=tk.IntVar(value=config_fonte["tamanho_da_fonte"])) # Cria um controle deslizante para ajustar o tamanho da fonte.
    escala_tamanho_frase_local.pack() # Empacota o controle deslizante.

    tk.Label(janela_config, text="Cor da Letra:").pack(pady=5) # Cria um rótulo "Cor da Letra:" e o empacota.
    moldura_cor_exibicao = tk.Frame(janela_config, bg=cor_texto_atual, width=50, height=20, bd=2, relief="sunken") # Cria uma moldura que exibe a cor atual do texto. (outras opções para relief - flat, raised, ridge)
    moldura_cor_exibicao.pack(pady=5) # Empacota a moldura de exibição de cor.
    tk.Button(janela_config, text="Escolher Cor", command=lambda: escolher_cor(janela_config, moldura_cor_exibicao)).pack(pady=5) # Cria um botão "Escolher Cor" que, ao ser clicado, chama a função escolher_cor.

    botao_aplicar = tk.Button(janela_config, text="Aplicar", command=lambda: aplicar_config_fonte(janela_config, var_fonte_frase_local, escala_tamanho_frase_local)) # Cria o botão "Aplicar" que, ao ser clicado, chama a função aplicar_config_fonte para aplicar as alterações.
    botao_aplicar.pack(pady=20) # Empacota o botão "Aplicar".
    
    janela_config.protocol("WM_DELETE_WINDOW", lambda: [janela_config.grab_release(), janela_config.destroy()]) # Configura um protocolo para lidar com o fechamento da janela de configuração.

def escolher_cor(janela_nivel_superior, moldura_cor_exibicao): # Abre o seletor de cores e atualiza a cor do texto e a moldura de exibição.
    global cor_texto_atual
    codigo_cor = colorchooser.askcolor(title="Escolha a cor da letra", initialcolor=cor_texto_atual)[1] # Abre a caixa de diálogo do seletor de cores; [1] pega o código hexadecimal da cor.
    if codigo_cor: # Verifica se o usuário realmente selecionou uma cor (não cancelou).
        cor_texto_atual = codigo_cor # Atualiza a variável global da cor do texto com a cor escolhida.
        moldura_cor_exibicao.config(bg=cor_texto_atual) # Atualiza a cor de fundo da moldura de exibição de cor para a cor escolhida.

def aplicar_config_fonte(janela_nivel_superior, var_fonte_frase_local, escala_tamanho_frase_local): # Aplica as configurações de fonte e cor selecionadas pelo usuário.
    global config_fonte, cor_texto_atual, tela, texto_frase
    config_fonte["fonte_da_frase"] = var_fonte_frase_local.get() # Atualiza a família da fonte no dicionário de configurações global com o valor selecionado no menu suspenso.
    config_fonte["tamanho_da_fonte"] = escala_tamanho_frase_local.get() # Atualiza o tamanho da fonte no dicionário de configurações global com o valor do controle deslizante.

    tela.itemconfigure(texto_frase, font=(config_fonte["fonte_da_frase"], config_fonte["tamanho_da_fonte"], "bold"), fill=cor_texto_atual) # Atualiza a fonte (família, tamanho, estilo) e a cor do texto da frase na tela principal.
    
    janela_nivel_superior.grab_release() # Libera o "grab" de entrada da janela de configuração, permitindo a interação com a janela principal novamente.
    janela_nivel_superior.destroy() # Fecha e destrói a janela de configuração.


inicializar_app()
janela_principal.mainloop()
