
import os
import sys
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

print("📜 Arquivos modificados:")
for file in files:
    print(f"🔹 {file}")
print("-------------------------")

# Processar cada arquivo
for file in files:
    commit_msg = ai.generate_commit_message(file)
    if commit_msg:
        #subprocess.run(["git", "add", file])
        #subprocess.run(["git", "commit", "-m", commit_msg])
        print(f"✅ Committed: {file} -> {commit_msg}")

print("🎉 Todos os arquivos foram commitados individualmente.")
