
# 🏥 VidaPlus - Sistema de Gestão Hospitalar e de Serviços de Saúde (SGHSS)

O **VidaPlus** é um sistema desenvolvido em **Django** com o objetivo de oferecer uma plataforma moderna, segura e escalável para gerenciar processos hospitalares e de saúde.  

Com ele é possível organizar consultas, pacientes, funcionários e outros aspectos essenciais para uma gestão eficiente no ambiente hospitalar.

---

## 🚀 Tecnologias Utilizadas
- **Python 3.11.9**
- **Django 5.2.5**
- **SQLite** 
- **TailwindCSS**
- **HTML5**

---

## ⚙️ Como Rodar o Projeto Localmente

### 1. Clone o Repositório
```bash
git clone https://github.com/Figueiraa/vidaplus-sghss.git
cd vidaplus-sghss
```

### 2. Crie e Ative um Ambiente Virtual
```bash
python -m venv venv
# No Windows
venv\Scripts\activate
# No Linux/Mac
source venv/bin/activate
```

### 3. Instale as Dependências
```bash
pip install -r requirements.txt
```

### 4. Configure o Banco de Dados
Execute as migrações:
```bash
python manage.py migrate
```

### 5. Crie um Superusuário (Administrador)
```bash
python manage.py createsuperuser
```
- Não é necessário inserir um CPF real, pois o projeto é apenas um protótipo.

### 6. Rode o Servidor de Desenvolvimento
```bash
python manage.py runserver
```

Acesse o sistema em:  
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  

---

## 🔑 Acesso ao Admin
O Django Admin estará disponível em:  
👉 [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)  

Use o **usuário e senha** criados no passo anterior para acessar.

---

## 📌 Funcionalidades Desenvolvidas
O sistema possui três perfis de acesso: Paciente, Funcionário e Administrador.

👤 Pacientes
- Agendar consultas
- Consultar consultas

🧑‍⚕️ Funcionários
- Visualizar consultas disponíveis (em aberto por Pacientes) e selecionar para atender
- Consultar consultas atribuídas a si e concluir consultas
- Visualizar histórico de consultas concluídas

👨‍💼 Administradores
- Cadastro de Funcionários
- Cadastro de Administradores
- Visualização e gerenciamento de Usuários
- Cadastro de Pacientes
- Visualização de Pacientes
- Visualização de Consultas

---

## Licença
Este projeto é de uso educacional e interno.  
