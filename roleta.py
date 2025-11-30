import tkinter as tk
from tkinter import messagebox, filedialog
import random
import time

def adicionar_item():
    item = entrada_item.get().strip()

    if not item:
        messagebox.showwarning("Erro", "Digite um item válido!")
        return

    lista_itens.insert(tk.END, item)
    entrada_item.delete(0, tk.END)

def limpar_itens():
    if messagebox.askyesno("Confirmação", "Deseja remover todos os itens?"):
        lista_itens.delete(0, tk.END)

def exportar_resultado():
    if len(historico_sorteados.get(0, tk.END)) == 0:
        messagebox.showwarning("Erro", "Nenhum sorteio realizado para exportar!")
        return

    caminho = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Arquivo de Texto", "*.txt")]
    )

    if caminho:
        with open(caminho, "w", encoding="utf-8") as arquivo:
            arquivo.write("Histórico de itens Sorteados\n")
            arquivo.write("---------------------------------\n\n")

            for item in historico_sorteados.get(0, tk.END):
                arquivo.write(f"{item}\n")

        messagebox.showinfo("Sucesso", "Arquivo exportado com sucesso!")

def animacao_sorteio(itens):
    """Animação rápida mostrando vários itens antes do sorteio final."""
    for _ in range(15):
        item_temp = random.choice(itens)
        label_sorteio.config(
            text=f"Sorteando...\n{item_temp}",
            fg="gray"
        )
        janela.update()
        time.sleep(0.05)

def sortear_item():
    itens = lista_itens.get(0, tk.END)

    if len(itens) == 0:
        messagebox.showwarning("Erro", "Nenhum item cadastrado!")
        return

    # Animação
    animacao_sorteio(itens)

    # Sorteia item final
    item_sorteado = random.choice(itens)

    # Remove da lista
    index = itens.index(item_sorteado)
    lista_itens.delete(index)

    # Mostra na tela
    label_sorteio.config(
        text=f"item Sorteado:\n{item_sorteado}",
        fg="blue"
    )

    # Adiciona ao histórico
    historico_sorteados.insert(tk.END, item_sorteado)

janela = tk.Tk()
janela.title("Sorteio de itens de TCC - Versão Avançada")
janela.geometry("520x800")
janela.resizable(False, False)

tk.Label(janela, text="Digite algo para ser sorteado:", font=("Arial", 11)).pack(pady=5)

entrada_item = tk.Entry(janela, width=45)
entrada_item.pack()

tk.Button(janela, text="Adicionar Item", command=adicionar_item, width=20).pack(pady=5)

tk.Label(janela, text="itens cadastrados:", font=("Arial", 11)).pack(pady=5)

lista_itens = tk.Listbox(janela, width=60, height=10)
lista_itens.pack()

tk.Button(janela, text="Limpar Itens", command=limpar_itens, width=20).pack(pady=5)

tk.Button(janela, text="Sortear Item", command=sortear_item, width=25, height=2).pack(pady=10)

label_sorteio = tk.Label(janela, text="", font=("Arial", 13, "bold"))
label_sorteio.pack(pady=10)

tk.Label(janela, text="Histórico de itens Sorteados:", font=("Arial", 11)).pack(pady=5)

historico_sorteados = tk.Listbox(janela, width=60, height=10)
historico_sorteados.pack()

tk.Button(janela, text="Exportar Resultado (TXT)", command=exportar_resultado, width=25).pack(pady=15)

janela.mainloop()
