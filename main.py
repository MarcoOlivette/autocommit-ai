import os
import sys
import openai
import subprocess
from dotenv import load_dotenv
from ai.gpt import GPTCommitMessageGenerator

# Carregar variáveis de ambiente do .env
load_dotenv()

# Verificar argumentos
if len(sys.argv) < 3:
    print("Uso: python main.py <caminho_do_repositorio> <modelo_ia>")
    sys.exit(1)

repo_path = sys.argv[1]
ai_model = sys.argv[2].lower()

# Validar se é um repositório Git
if not os.path.isdir(os.path.join(repo_path, ".git")):
    print(f"Erro: '{repo_path}' não é um repositório Git válido.")
    sys.exit(1)

# Instanciar a IA escolhida (por enquanto, apenas GPT)
if ai_model == "gpt":
    ai = GPTCommitMessageGenerator()
else:
    print(f"Erro: Modelo de IA '{ai_model}' não suportado.")
    sys.exit(1)

# Mudar para o diretório do repositório
os.chdir(repo_path)

# Obter arquivos modificados
files = subprocess.run(["git", "status", "--short"], capture_output=True, text=True).stdout
files = [line.split()[1] for line in files.splitlines() if line]

print("📜 Mudanças detectadas:")
print("-------------------------")

# Processar cada arquivo
for file in files:
    # Obter as mudanças do arquivo
    diff_output = subprocess.run(["git", "diff", "--", file], capture_output=True, text=True).stdout

    if not diff_output.strip():
        continue  # Pular se não houver mudanças

    # Mostrar as mudanças no terminal
    #print(f"🔹 Arquivo: {file}")
    #print(diff_output)  # Exibe as alterações no terminal
    #print("-------------------------")

    # Gerar mensagem de commit usando a IA
    commit_msg = ai.generate_commit_message(file)

    if commit_msg:
        #subprocess.run(["git", "add", file])
        #subprocess.run(["git", "commit", "-m", commit_msg])
        print(f"✅ Committed: {file} -> {commit_msg}")
        print("-------------------------")

print("🎉 Todos os arquivos foram commitados individualmente.")
