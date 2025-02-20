import pdfplumber;
pdf_path = r"C:\Users\ruand\Desktop\lista-deferidos\lista-deferidos.pdf"; #essa linha ainda da erro


# Lista para armazenar todas as palavras do PDF
palavras = []

# Extrair texto de cada página e dividir em palavras
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            # Quebrar o texto em palavras e adicionar à lista
            palavras += text.upper().split()


contagem_todos = palavras.count("INDEFERIDO")
contagem_exata = palavras.count("DEFERIDO")
contagem_soma = contagem_todos + contagem_exata

print(f"Total de ocorrências de 'DEFERIDO': {contagem_exata}")
print(f"Total de ocorrências de 'INDEFERIDO': {contagem_todos}")
print(f"Total de pessoas': {contagem_soma}")