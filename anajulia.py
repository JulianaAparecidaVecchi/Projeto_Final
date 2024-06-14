import customtkinter as ctk
import menu_principal

carros = [
    ["Volkswagen Gol", 180, 80, 12],
    ["Chevrolet Celta", 170, 78, 13],
    ["Chevrolet Corsa", 175, 82, 11],
    ["Fiat Palio", 165, 76, 14],
    ["Volkswagen Fox", 170, 79, 13],
    ["Fiat Siena", 160, 75, 15],
    ["Ford Fiesta", 180, 83, 12],
    ["Ford Ka", 170, 77, 13],
    ["HB20", 175, 80, 12],
    ["Chevrolet Onix", 180, 85, 11],
    ["Peugeot 208", 170, 82, 13],
    ["Renault Sandero", 165, 79, 14],
    ["Honda Fit", 160, 76, 15],
    ["Volkswagen Fusca", 155, 74, 15],
    ["Toyota Yaris", 170, 78, 13],
    ["Ford Belina", 150, 72, 15],
    ["Nissan March", 165, 77, 14],
    ["Renault Clio", 160, 75, 15],
    ["Fiat Punto", 175, 80, 12],
    ["Volkswagen Jetta", 220, 140, 15],
    ["Honda Civic", 210, 135, 15],
    ["Toyota Corolla", 215, 138, 15],
    ["Mitsubishi Lancer", 225, 145, 25],
    ["Nissan Sentra", 210, 133, 20],
    ["Hyundai Elantra", 215, 137, 8],
    ["Audi A4", 230, 150, 25],
    ["Bmw 320i", 240, 160, 25],
    ["Chevrolet Cruze", 220, 140, 15],
    ["Subaru Impreza", 225, 145, 20],
    ["Chevrolet Camaro amarelo", 250, 180, 40],
    ["Ford Mustang", 260, 190, 40],
    ["Nissan 370Z", 245, 175, 25],
    ["Subaru WRX", 240, 170, 30],
    ["Mazda MX-5 Miata", 235, 165, 40],
    ["Toyota Supra", 250, 180, 30],
    ["BMW M3", 255, 185, 35],
    ["Audi RS3", 260, 190, 40],
    ["Mercedes-Benz C63 AMG", 270, 200, 30],
    ["Porsche 911", 280, 210, 35],
    ["Bugatti Chiron", 420, 1500, 55],
    ["Bugatti Veyron", 410, 1200, 40],
    ["Porsche 718 Spyder RS", 310, 500, 75],
    ["Ferrari LaFerrari", 350, 950, 60],
    ["Ferrari 812 GTS", 340, 900, 45],
    ["Porsche 911 GT3 RS", 320, 520, 50],
    ["McLaren Senna", 330, 800, 45],
    ["Tesla Model S", 320, 1000, 60],
    ["Fiat Uno com Escada", 650, 750, 90]
]



 
def janela_garagem():
    garagem_janela=ctk.CTk()
    botao_proximo=ctk.CTkButton(garagem_janela,text='PRÓXIMO',width=100, height=50,command='Próximo')
    botao_proximo.grid(row=1,column=3)
    #carro atual = uma lista com um carro
    carro_mostrado=menu_principal.card_carro(garagem_janela,carro_atual)
    carro_mostrado.grid(row=1,column=3)
    botao_anterior=ctk.CTkButton(garagem_janela,text='ANTERIOR',width=100, height=50,command='Próximo')
    botao_anterior.grid(row=1,column=1)
    garagem_janela.mainloop()

janela_garagem()