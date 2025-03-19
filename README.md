# 🤖 Auto Commit Bot

Um **bot de commits automatizados** que gera mensagens de commit em **português** com **inteligência artificial**. Ele analisa as mudanças nos arquivos e cria mensagens descritivas usando **GPT** (ou outros modelos no futuro).

---

## 🚀 Como Usar

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seu-usuario/auto-commit-bot.git
cd auto-commit-bot
```

### 2️⃣ Criar e ativar um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar a chave da OpenAI
Copie o arquivo `.env.example` e edite:
```bash
cp .env.example .env
nano .env  # Adicione sua chave da OpenAI
```

---

## 🛠 Uso do Script

Para rodar o bot, basta fornecer o caminho do repositório e escolher a IA que deseja usar (atualmente só suporta `gpt`):

```bash
python main.py /caminho/do/repositorio gpt
```
---

## 📦 Funcionalidades
✅ **Gera mensagens de commit automaticamente** 📝  
✅ **Usa IA para analisar mudanças no código** 🤖  
✅ **Aceita diferentes modelos de IA (atualmente GPT)** 🔄  
✅ **Inclui emojis apropriados para cada tipo de mudança** 🚀  

---

## 🔜 Roadmap
- [ ] Adicionar suporte para outros modelos de IA (Claude, Llama, etc.)
- [ ] Melhorar a análise do código-fonte para commits mais precisos
- [ ] Adicionar um modo interativo para revisão das mensagens

---

## 📜 Licença
Este projeto está licenciado sob a **MIT License**.