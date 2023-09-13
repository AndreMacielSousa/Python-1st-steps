import shutil
import tempfile

local = r"C:\Sivacom\fdmssiva\CFC00086"  # Use 'r' antes da string para tratar o caminho como raw string

# Lê do arquivo e escreve em outro arquivo temporário
with open(local, 'r') as xfile, \
     tempfile.NamedTemporaryFile('w', delete=False) as fout:
    for linha in xfile:
        if not linha.startswith("C"):
            linha = linha[:39] + "78" + linha[41:]  # Remonta a linha
        fout.write(linha)  # Escreve no arquivo temporário

# Move o arquivo temporário para o original
shutil.move(fout.name, local)  # Use a variável 'local' para especificar o caminho do arquivo original
