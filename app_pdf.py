import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# ---------------- FUNÇÃO ----------------
def gerar_pdf():
    texto = entrada_texto.get("1.0", tk.END).strip()

    if not texto:
        messagebox.showwarning("Aviso", "Digite algum texto para gerar o PDF!")
        return

    nome_arquivo = "pdf_gerado_pelo_app.pdf"

    c = canvas.Canvas(nome_arquivo, pagesize=A4)
    largura, altura = A4

    x = 50
    y = altura - 50

    for linha in texto.split("\n"):
        c.drawString(x, y, linha)
        y -= 20

        if y < 50:
            c.showPage()
            y = altura - 50

    c.save()

    messagebox.showinfo("Sucesso", f"PDF gerado com sucesso!\nArquivo: {nome_arquivo}")

# ---------------- INTERFACE ----------------
janela = tk.Tk()
janela.title(" Gerador de PDF - Bernardo")
janela.geometry("500x400")
janela.resizable(False, False)
janela.configure(bg="#0f172a")

# Título
titulo = tk.Label(
    janela,
    text="Gerador de PDF",
    font=("Arial", 16, "bold"),
    fg="white",
    bg="#0f172a"
)
titulo.pack(pady=10)

# Área de texto
entrada_texto = tk.Text(
    janela,
    width=55,
    height=12,
    font=("Arial", 11)
)
entrada_texto.pack(pady=10)

entrada_texto.insert("1.0", "Digite o texto que irá para o PDF...")

# Botão
botao = tk.Button(
    janela,
    text="Gerar PDF",
    font=("Arial", 12, "bold"),
    bg="#2563eb",
    fg="white",
    padx=15,
    pady=5,
    command=gerar_pdf
)
botao.pack(pady=15)

# Rodar app
janela.mainloop()
