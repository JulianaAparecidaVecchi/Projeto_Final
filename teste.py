import tkinter as tk
from PIL import Image, ImageTk

#indices = marca, modelo, velocidade máxima, potencia/cavalos, turbo talvez?
garagem = [
    ["Ferrari 812 gts", "Ferrari.png", 350, 789, 2016],
    ["Lamborguini Hurucan", "Lmaborguini.png", 325, 640, 1000],
    ["Bugatti Bolide","Bugatti.png", 499,1825,2000],
    ["Hennessey Venom F5", "Hennessey.png", 125, 2000, 200],
    ["McLaren Speedtail", "McLaren.png", 402,1050, 200]
]


#inicialização de uma janela
janela = tk.Tk()
janela.title("Jogos velozes")


#frame é uma região do layout (janela), onde algo irá aparecer
frame_left = tk.Frame(janela)
frame_left.pack(side=tk.LEFT, padx=10, pady=10)


#label serve para conversar, como se fosse um print, é um texto na tela
lbl_select = tk.Label(frame_left, text="Selecione um carro:")
lbl_select.pack()


#função para atualizar a exibição (imagem e dados)
def update_carro(event): #parametro evento exigencia do tkinter
    carro_selecionado = listbox_carros.curselection()
    if carro_selecionado:
        #a posição 0 retorna o index da listbox
        index = carro_selecionado[0]
        carro = garagem[index]


        #pegar a imagem
        img_carro = Image.open(carro[1])
        img_carro = img_carro.resize(200,200), Image.ANTIALIAS
        img_carro = ImageTk.PhotoImage(img_carro)


listbox_carros = tk.Listbox(frame_left) #janela é onde a listbox vai estar 

for carro in garagem:
    listbox_carros.insert(0,carro[0])
listbox_carros.pack()

#button é um botão, command é o que esse botão fará, pode ser quit(sair), soma, começar....
btn_exit = tk.Button(frame_left, text="Sair", command= janela.quit)
btn_exit.pack()

btn_comecar = tk.Button(text="Começar corrida!")
btn_comecar.pack()



#rodar janela
janela.mainloop()