import openai
import os
import subprocess

class GPTCommitMessageGenerator:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("Erro: OPENAI_API_KEY não definido no arquivo .env")
        openai.api_key = self.api_key

    def generate_commit_message(self, file):
        """Gera mensagens de commit em português usando GPT."""
        diff_content = subprocess.run(["git", "diff", "--", file], capture_output=True, text=True).stdout

        if not diff_content.strip():
            return None  # Nenhuma mudança detectada

        prompt = f"""
        Gere uma mensagem de commit curta e objetiva em português para as seguintes mudanças:\n
        {diff_content}
        Inclua um emoji apropriado conforme o tipo de modificação:
        - 🔧 Ajustes de código
        - 🐛 Correção de bugs
        - ✨ Nova funcionalidade
        - 📚 Atualização de documentação
        - 🛠 Refatoração
        - ⚡ Melhoria de performance
        """

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é um assistente que gera mensagens de commit concisas e informativas em português, incluindo emojis."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        return response['choices'][0]['message']['content'].strip()
