import tkinter as tk
from tkinter import font, messagebox, colorchooser
from PIL import Image, ImageTk
import random
import os
import sys

class AplicativoFrases:
    def __init__(self, master):
        self.master = master
        master.title("Motivação Verde") # Título do aplicativo que aparece na barra quando ele é iniciado
        master.geometry("960x540") # Tamanho inicial da tela do aplicativo
        master.resizable(True, True) # Permite colocar o aplicativo em tela cheia e redimencionar manualmente a tela. "True" desbloqueia aquele eixo (x,y)
        
        '''
        Em Python, __init__ é um método especial (dunder method) que atua como o construtor de uma classe.
        Ele é chamado automaticamente sempre que você cria uma nova instância (objeto) daquela classe.
        A principal função do __init__ é inicializar os atributos do objeto.
        '''
        
        # Determina o caminho base para recursos (imagens)
        # Isso é crucial para que o PyInstaller encontre os arquivos no executável
        if getattr(sys, 'frozen', False):
            self.base_path = sys._MEIPASS
        else:
            self.base_path = os.path.dirname(os.path.abspath(__file__))

        # --- Dados das frases: Dicionário de listas de frases por tema ---
        self.frases_por_tema = {
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
        }
        
        # --- Mapeamento de temas para subpastas de imagem ---
        self.tema_para_pasta_imagens = {
            "Mudanças Climáticas": "mudancas-climaticas",
            "Educação Ambiental": "educacao-ambiental",
            "Urbanização e Meio Ambiente": "urbanizacao-e-meio-ambiente",
            "Resíduos/Reciclagem": "residuos-reciclagem",
            "Recursos Naturais": "recursos-naturais",
            "Introdução": "introducao"
        }
        self.caminho_imagens_base = os.path.join(self.base_path, "imagens")

        # Configurações de Fonte e Cor Padrão
        self.font_config = {
            "frase_family": "Helvetica",
            "frase_size": 28
        }
        self.current_text_color = "white" # Cor de texto padrão

        # Widget para a Imagem de Fundo (Canvas)
        self.canvas = tk.Canvas(master, bg="black") # Cor de fundo padrão caso não haja imagem
        self.canvas.pack(fill="both", expand=True)
        self.bg_image_id = None # ID da imagem no canvas para referência

        # Widget de Texto Único sobre o Canvas
        self.label_frase = self.canvas.create_text(
            400, 300, # Posição X, Y (centro do canvas)
            text="Qual a sua frase do dia?", # Frase inicial personalizada
            width=700, # Use 'width' para quebra de linha em Canvas
            font=(self.font_config["frase_family"], self.font_config["frase_size"], "bold"),
            fill=self.current_text_color, # Usa a cor padrão
            justify="center" # Centraliza o texto
        )

        # Frame para os botões (agrupa todos os botões na parte inferior)
        button_frame = tk.Frame(master)
        
        # Botão para gerar nova frase
        self.btn_gerar_frase = tk.Button(button_frame, text="Nova Frase", command=self.gerar_nova_frase,
                                         font=("Arial", 14), bg="#4CAF50", fg="white",
                                         relief="raised", bd=3)
        self.btn_gerar_frase.pack(side="left", padx=10, pady=10) # Empacota dentro do frame

        # Botão para mudar fonte e cor
        self.btn_mudar_fonte = tk.Button(button_frame, text="Mudar Fonte e Cor", command=self.abrir_config_fonte,
                                         font=("Arial", 14), bg="#2196F3", fg="white",
                                         relief="raised", bd=3)
        self.btn_mudar_fonte.pack(side="left", padx=10, pady=10) # Empacota dentro do frame

        # Posiciona o frame de botões no canvas (abaixo do texto) e armazena o ID da janela
        self.button_frame_window_id = self.canvas.create_window(
            400, 500, # Coordenadas iniciais
            window=button_frame # O frame de botões
        )

        # --- Carrega a imagem inicial personalizada ---
        self.carregar_imagem_inicial()
        
        # Liga o evento de redimensionamento da janela ao método _on_resize
        self.master.bind("<Configure>", self._on_resize)

    def carregar_imagem_inicial(self):
        """Carrega e exibe a imagem de introdução."""
        caminho_imagem_inicial_pasta = os.path.join(self.caminho_imagens_base, self.tema_para_pasta_imagens["Introdução"])
        nome_arquivo_imagem_inicial = "imagem_inicial.jpg" # Nome da sua imagem inicial (altere se for diferente)
        caminho_completo_imagem_inicial = os.path.join(caminho_imagem_inicial_pasta, nome_arquivo_imagem_inicial)

        if os.path.exists(caminho_completo_imagem_inicial):
            self._carregar_imagem_fundo(caminho_completo_imagem_inicial)
        else:
            messagebox.showwarning("Aviso", f"Imagem inicial '{nome_arquivo_imagem_inicial}' não encontrada na pasta 'introducao'.")
            print(f"Aviso: Imagem inicial '{caminho_completo_imagem_inicial}' não encontrada.")


    def _on_resize(self, event):
        """
        Atualiza a posição do texto e recarrega a imagem de fundo quando a janela é redimensionada
        (incluindo a maximização/restauração pela barra de título).
        """
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        # Ajusta a largura do texto para que ele quebre a linha corretamente
        self.canvas.itemconfigure(self.label_frase, width=canvas_width * 0.9) 
        # Centraliza o texto no canvas
        self.canvas.coords(self.label_frase, canvas_width / 2, canvas_height * 0.5)
        
        # Recarrega a imagem para preencher o novo tamanho do canvas
        if hasattr(self, 'current_image_path') and self.current_image_path:
            self._carregar_imagem_fundo(self.current_image_path)

        # Atualiza a posição do frame de botões para mantê-lo centralizado na parte inferior
        if self.button_frame_window_id: # Verifica se o ID da janela dos botões existe
            # O centro do frame de botões será:
            # X: Centro horizontal do canvas
            # Y: Altura do canvas menos uma margem (ex: 60 pixels do fundo)
            self.canvas.coords(
                self.button_frame_window_id, 
                canvas_width / 2, 
                canvas_height - 60 
            )


    def _get_imagens_do_tema(self, tema):
        """
        Retorna uma lista de caminhos de imagem para o tema especificado.
        """
        pasta_do_tema = self.tema_para_pasta_imagens.get(tema)
        # Se o tema for "Introdução", a imagem já é específica, não precisamos listar
        if tema == "Introdução":
            return [os.path.join(self.caminho_imagens_base, pasta_do_tema, "imagem_inicial.png")] # Caminho fixo para a imagem inicial

        if not pasta_do_tema:
            print(f"Aviso: Não há pasta de imagem mapeada para o tema '{tema}'.")
            return []
        
        # Constrói o caminho completo para a pasta do tema dentro do diretório de imagens base
        caminho_completo_pasta = os.path.join(self.caminho_imagens_base, pasta_do_tema)
        
        # Verifica se a pasta existe
        if not os.path.isdir(caminho_completo_pasta):
            print(f"Aviso: Pasta de imagens '{caminho_completo_pasta}' não encontrada. Verifique sua estrutura de arquivos.")
            return []
        
        # Lista todos os arquivos na pasta e filtra por extensões de imagem comuns
        imagens = [f for f in os.listdir(caminho_completo_pasta) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        
        # Retorna o caminho completo para cada imagem
        return [os.path.join(caminho_completo_pasta, img) for img in imagens]

    def _carregar_imagem_fundo(self, imagem_path):
        """
        Carrega e exibe a imagem de fundo no canvas, redimensionando-a para cobrir toda a área.
        """
        self.current_image_path = imagem_path # Armazena o caminho da imagem atual para recarregamento

        try:
            original_image = Image.open(imagem_path)
            
            # Obtém o tamanho atual do canvas. Se ainda não estiver renderizado, usa o tamanho da janela principal.
            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()
            
            if canvas_width == 0 or canvas_height == 0:
                # Usa o tamanho da janela principal se o canvas ainda não tiver tamanho definido
                canvas_width = self.master.winfo_width()
                canvas_height = self.master.winfo_height()
                if canvas_width == 1 or canvas_height == 1: # Prevenção para caso seja 1x1 antes de renderizar
                     canvas_width, canvas_height = 800, 600 # Fallback para tamanho inicial

            # Calcula a proporção da imagem original e do canvas
            original_aspect = original_image.width / original_image.height
            canvas_aspect = canvas_width / canvas_height

            # Redimensiona a imagem para cobrir o canvas, mantendo a proporção
            if original_aspect > canvas_aspect:
                # A imagem é mais larga que o canvas, ajusta pela altura
                new_height = canvas_height
                new_width = int(new_height * original_aspect)
            else:
                # A imagem é mais alta que o canvas, ajusta pela largura
                new_width = canvas_width
                new_height = int(new_width / original_aspect)

            # Redimensiona usando o algoritmo LANCZOS para melhor qualidade
            resized_image = original_image.resize((new_width, new_height), Image.LANCZOS)
            self.tk_image = ImageTk.PhotoImage(resized_image) # Converte para formato Tkinter
            
            # Remove a imagem anterior do canvas (se houver)
            if self.bg_image_id:
                self.canvas.delete(self.bg_image_id)
            
            # Centraliza a imagem no canvas (calculando offsets para o canto superior esquerdo)
            x_offset = (canvas_width - new_width) / 2
            y_offset = (canvas_height - new_height) / 2
            
            self.bg_image_id = self.canvas.create_image(
                x_offset, y_offset, image=self.tk_image, anchor="nw" # Posiciona pelo canto superior esquerdo
            )
            self.canvas.tag_lower(self.bg_image_id) # Envia a imagem para o fundo
        except Exception as e:
            print(f"Erro ao carregar imagem: {imagem_path} - {e}")
            messagebox.showerror("Erro de Imagem", f"Não foi possível carregar a imagem: {os.path.basename(imagem_path)}\nDetalhes: {e}")
            self.tk_image = None # Limpa a referência em caso de erro
            if self.bg_image_id: self.canvas.delete(self.bg_image_id) # Remove qualquer imagem antiga em caso de erro

    def gerar_nova_frase(self):
        """
        Seleciona aleatoriamente um tema, uma frase desse tema e uma imagem desse tema, e as exibe.
        """
        temas_disponiveis = list(self.frases_por_tema.keys())
        if not temas_disponiveis:
            messagebox.showinfo("Informação", "Nenhum tema configurado para exibir.")
            return

        # 1. Escolhe um tema aleatoriamente
        tema_escolhido = random.choice(temas_disponiveis)
        
        # 2. Escolhe uma frase aleatória DESSE tema
        frases_do_tema = self.frases_por_tema.get(tema_escolhido, [])
        if not frases_do_tema:
            messagebox.showinfo("Informação", f"Nenhuma frase encontrada para o tema '{tema_escolhido}'.")
            self.canvas.itemconfigure(self.label_frase, text=f"Tema: {tema_escolhido}\nNenhuma frase disponível.")
            if self.bg_image_id: self.canvas.delete(self.bg_image_id)
            return
            
        frase_aleatoria = random.choice(frases_do_tema)
        self.canvas.itemconfigure(self.label_frase, text=frase_aleatoria)

        # 3. Escolhe uma imagem aleatória DESSE MESMO tema
        imagens_do_tema = self._get_imagens_do_tema(tema_escolhido)
        if imagens_do_tema:
            imagem_aleatoria = random.choice(imagens_do_tema)
            self._carregar_imagem_fundo(imagem_aleatoria)
        else:
            print(f"Aviso: Nenhuma imagem encontrada para o tema '{tema_escolhido}'.")
            messagebox.showwarning("Aviso", f"Nenhuma imagem encontrada para o tema '{tema_escolhido}'.")
            if self.bg_image_id:
                self.canvas.delete(self.bg_image_id) # Remove imagem se não houver para o tema atual

    def abrir_config_fonte(self):
        """
        Abre uma nova janela para configurar a fonte (família, tamanho) e a cor da frase.
        """
        top = tk.Toplevel(self.master)
        top.title("Configurar Fonte e Cor") # Título da janela de configuração
        top.geometry("400x350") # Tamanho da janela
        top.transient(self.master) # Mantém esta janela acima da principal
        top.grab_set() # Torna a janela modal (bloqueia interação com a principal)

        all_font_families = sorted(list(font.families())) # Lista todas as fontes disponíveis no sistema
        
        tk.Label(top, text="Fonte da Frase:").pack(pady=5)
        self.frase_font_var = tk.StringVar(top)
        self.frase_font_var.set(self.font_config["frase_family"]) # Define a fonte atual como valor inicial
        frase_font_menu = tk.OptionMenu(top, self.frase_font_var, *all_font_families)
        frase_font_menu.pack()

        tk.Label(top, text="Tamanho da Frase:").pack(pady=5)
        self.frase_size_scale = tk.Scale(top, from_=10, to=60, orient="horizontal", # Escala de 10 a 60 pontos
                                              variable=tk.IntVar(value=self.font_config["frase_size"]))
        self.frase_size_scale.pack()

        # --- Opção para Cor da Letra ---
        tk.Label(top, text="Cor da Letra:").pack(pady=5)
        # Frame para exibir a cor atual selecionada
        self.color_display_frame = tk.Frame(top, bg=self.current_text_color, width=50, height=20, bd=2, relief="sunken")
        self.color_display_frame.pack(pady=5)
        # Botão que abre o seletor de cores
        tk.Button(top, text="Escolher Cor", command=self._pick_color).pack(pady=5)

        btn_aplicar = tk.Button(top, text="Aplicar", command=self.aplicar_config_fonte)
        btn_aplicar.pack(pady=20)
        
        # Define o comportamento ao fechar a janela (libera grab_set e destrói)
        top.protocol("WM_DELETE_WINDOW", lambda: [top.grab_release(), top.destroy()])

    def _pick_color(self):
        """
        Abre o seletor de cores do sistema e atualiza a cor de texto selecionada.
        """
        # colorchooser.askcolor retorna (RGB_tuple, '#hex_code')
        color_code = colorchooser.askcolor(title="Escolha a cor da letra", initialcolor=self.current_text_color)[1]
        if color_code: # Se o usuário escolheu uma cor (não clicou em Cancelar)
            self.current_text_color = color_code
            # Atualiza a cor de fundo do frame de visualização para mostrar a cor escolhida
            self.color_display_frame.config(bg=self.current_text_color)

    def aplicar_config_fonte(self):
        """
        Aplica as configurações de fonte e cor escolhidas ao texto no canvas e fecha a janela de configuração.
        """
        # Atualiza as configurações de fonte
        self.font_config["frase_family"] = self.frase_font_var.get()
        self.font_config["frase_size"] = self.frase_size_scale.get()

        # Aplica as novas fontes E a nova cor ao texto no canvas
        self.canvas.itemconfigure(self.label_frase,
                                  font=(self.font_config["frase_family"],
                                        self.font_config["frase_size"], "bold"),
                                  fill=self.current_text_color) # Atualiza a cor aqui
        
        # Libera o grab_set e destrói a janela Toplevel
        # Verificação para evitar erro caso a janela já tenha sido fechada por outro meio
        if hasattr(self, 'frase_font_var') and self.frase_font_var.winfo_exists():
            self.master.winfo_children()[-1].grab_release()
            self.master.winfo_children()[-1].destroy()

    # As funções 'toggle_fullscreen_key' e 'exit_fullscreen' foram removidas, pois a maximização será nativa.

if __name__ == "__main__":
    # Cria a janela principal do Tkinter
    root = tk.Tk()
    # Instancia e executa o aplicativo
    app = AplicativoFrases(root)
    root.mainloop()