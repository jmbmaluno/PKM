from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from pkm import *

def mostrar_dados(pokemom):
    global Status

    ttk.Label(window, text = pokemom.nome, font = (25), ).grid(column=0, row=3)
    
    tipo = ""
    for i in range(len(pokemon.tipo)):
        tipo = tipo + pokemon.tipo[i] + "   "
    ttk.Label(window, text = tipo, justify=LEFT).grid(column=0, row = 4)

    hab = ""
    for i in range(len(pokemom.habilidade)):
        hab = hab + pokemom.habilidade[i] + "   "
    ttk.Label(window, text = hab).grid(column=0, row = 5)

    for i in range(6):
        ttk.Label(window, text = Status[i] + ": " + str(pokemom.status[i])).grid(column = 0, row = 6+i)


#Evento que ocorre quando eu seleciono So pokemon na combobox
def pkm_changed(event):
    global selected_pkm
    global url_selected
    global pokemon

    showinfo(
        title = "Result",
        message = f'Você escolheu {selected_pkm.get()}'
    )
    
    #caso do nidoran femea e macho
    if str(selected_pkm.get()) == "Nidoran♂":  
        selected_pkm = "nidoran-m"
    elif str(selected_pkm.get()) == "Nidoran♀":
        selected_pkm = "nidoran-f"
    
    if(type(selected_pkm) != str):
        pokemon.set_nome(selected_pkm.get())
        url_selected = url_selected + str(selected_pkm.get()).lower()
    else:
        pokemon.set_nome(selected_pkm)
        url_selected = url_selected + selected_pkm
    
    pokemon.set_url_pkm(url_selected)

    if type(selected_pkm) != str:
        pokemon.set_nome(selected_pkm.get())
    else:
        pokemon.set_nome(selected_pkm)

    pokemon.set_url_pkm(url_selected)
    pokemon.atualizar_dados()
    print(pokemon.tipo)
    print(pokemon.habilidade)
    print(pokemon.status)

    mostrar_dados(pokemon)

site_menu = Site("https://pokemondb.net/pokedex/game/firered-leafgreen")
url_selected = "https://pokemondb.net/pokedex/"


#inforcard-lg-data text-muted
pkm_html = site_menu.get_doc().find_all("a", {"class" : "ent-name"})
lista_pkm = []
for i in pkm_html:
    lista_pkm.append(str(i.string))

pokemon = Pkm()

window = Tk()
window.title("Moveset")
window.geometry('500x500')

#photo = PhotoImage(data = raw_data)
#ttk.Label(window, image = photo).grid(column=0, row = 0)
ttk.Label(window, text = "Escolha o Pokemon").grid(column = 0, row = 0)
#ttk.Button(window, text = "Quit", command=window.destroy).grid(column=2, row=2, padx = 100, pady = 30)

selected_pkm = StringVar()
combobox_pkm = ttk.Combobox(window, textvariable=selected_pkm)
combobox_pkm['values'] = lista_pkm
combobox_pkm.grid(column=1, row = 0, padx= 10)
combobox_pkm.current()
combobox_pkm.bind('<<ComboboxSelected>>', pkm_changed)

window.mainloop()