# 💰 Projeto de Cotação de Moedas com Python + API

Este é um projeto simples e educativo criado para praticar conceitos fundamentais de desenvolvimento Python, como:

- Criação e uso de ambiente virtual (`venv`)
- Gerenciamento de pacotes com `pip`
- Uso de arquivos `requirements.txt`
- Armazenamento seguro de variáveis de ambiente com `.env`
- Consumo de API real de cotação de moedas (`https://www.exchangerate-api.com`)

---

## 📦 Requisitos

- Python 3.10+ instalado
- Conta gratuita na [ExchangeRate API](https://www.exchangerate-api.com)

---

## 🚀 Passo a passo do projeto

### 1. Clone o repositório

git clone https://github.com/marreiro204/API-VENV.git
cd API-VENV

2. Crie um ambiente virtual com seu nome
python -m venv sua_venv

3. Ative o ambiente virtual
   sua_venv\Scripts\activate

4. Instale os pacotes necessários
   pip install requests python-dotenv

5. Gere o arquivo requirements.txt
pip freeze > requirements.txt

6. Crie o arquivo .env
Este arquivo não deve ser versionado (adicionado ao Git) e deve conter:
API_KEY=sua_chave_aqui
Substitua sua_chave_aqui pela chave que você obteve no site da ExchangeRate API.

7. Execute o script consulta.py
python consulta.py

