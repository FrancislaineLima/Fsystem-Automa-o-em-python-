# 🌸 Fsystem - Cadastro de Produtos & Automação RPA (Android)

Projeto desenvolvido com base na **Jornada Python** da Hashtag Programação. Para ir além do exercício tradicional (que utiliza uma aplicação web), decidi adaptar a solução para um cenário corporativo mais próximo da realidade de muitas empresas: **a automação em um aplicativo Android para simular um sistema próprio da empresa**.

Criei o **Fsystem**, um aplicativo mobile para cadastro e gestão de produtos, e desenvolvi um script de automação (RPA) em Python capaz de interagir diretamente com o emulador do Android Studio.

---

## 💡 O Diferencial do Projeto
Em vez de manipular um formulário web no navegador da propria Hashtag Programação forneceu, esta automação lida com os desafios de interagir com um aplicativo rodando em um emulador Android (`Android Studio`), gerenciando foco de janela, eventos de toque e simulação de entradas de teclado.

---

## 🚀 Funcionalidades

- **Aplicativo Mobile (Fsystem):** Interface customizada em tom rosa pastel para login e cadastro de itens.
- **Leitura de Dados:** Processamento de massa de dados a partir de arquivos CSV.
- **Automação de Interface (RPA):** Login automático e preenchimento em lote dos campos do app (Código, Marca e Tipo).

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem da Automação:** Python 3
- **Bibliotecas Python:**
  - `pandas`: Leitura e manipulação da base de dados em CSV.
  - `pyautogui`: Simulação de comandos de mouse e teclado no emulador.
  - `time`: Controle de tempo para transições de tela.
- **Desenvolvimento Mobile:** Android Studio (Kotlin/Java, Android Emulator)

---

## 📁 Estrutura de Pastas
 ├── AULA 1/
 
 │   ├── automacao.py      # Script principal do bot
 
 │   └── produtos.csv      # Base de dados de produtos
 
 ├── app/                  # Projeto do aplicativo Fsystem no Android Studio
 
 └── README.md             # Documentação do projeto
