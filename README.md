# Portfólio de Projetos Profissionais em Python

Bem-vindo ao meu portfólio de projetos em Python. Este repositório é uma coleção de aplicações e scripts que demonstram minhas habilidades em desenvolvimento de software, abrangendo desde automação e análise de dados até desenvolvimento web, aplicativos de desktop (GUI) e scripts de shell.

## 🚀 Vitrine de Projetos

Os projetos estão organizados nas seguintes categorias:

### 1. 📊 Análise de Dados e Extração (ETL)

Projetos focados na extração, transformação e visualização de dados de diversas fontes.

* **Analisador de Questões de PDF (Direito ADM e Constitucional)**
    * **Descrição:** Uma solução de ETL que utiliza `pdfplumber`, `PyPDF2` e expressões regulares (Regex) avançadas para extrair e analisar questões de concursos de múltiplos PDFs de estudo jurídico. O script identifica padrões complexos (ex: "ERRADA." antes ou depois do comentário), limpa os dados e os estrutura em um arquivo `.csv` para análise futura.
    * **Tecnologias:** Python, Pandas, PyPDF2, pdfplumber, Regex.
    * **Arquivos Relevantes:** `Questions.py`, `Questionsv2.py`, `Questionv3-plumber.py`, `questoes_analisadas_const.csv`, `PADROES-ADM.txt`.

* **Visualização de Taxa de Pobreza**
    * **Descrição:** Script que utiliza `pandas` para processar dados numéricos (convertendo taxas de pobreza) e `matplotlib` para gerar um gráfico de barras que exibe a taxa média de pobreza por estado.
    * **Tecnologias:** Python, Pandas, Matplotlib.
    * **Arquivos Relevantes:** `fatalError/fatalError.py`.

* **Dashboard de Power BI**
    * **Descrição:** Um arquivo de projeto compilado do Power BI, demonstrando habilidades em Business Intelligence e visualização de dados (o conteúdo exato está no arquivo binário).
    * **Tecnologias:** Power BI.
    * **Arquivos Relevantes:** `Compiled.pbix`.

---

### 2. ⚙️ Automação (Scripts de Produtividade)

Scripts para automatizar tarefas de rotina, tanto no ambiente de trabalho quanto no doméstico.

#### Automação de Trabalho (Job Automations)

* **Organizador de E-mail (IMAP) e Análise Financeira**
    * **Descrição:** Um conjunto robusto de scripts que se conectam a uma caixa de entrada via `imaplib` para escanear, categorizar e processar e-mails.
    * **Destaque (Análise Granular):** O script `granularCode.py` usa Regex para identificar e extrair valores monetários (BRL, USD, EUR, etc.) de e-mails, categorizando-os (Cobranças, Investimentos, Ofertas) e, em seguida, usa `pandas` e `matplotlib` para gerar relatórios e gráficos da distribuição de gastos.
    * **Tecnologias:** Python, imaplib, Pandas, Matplotlib, Regex, openpyxl.
    * **Arquivos Relevantes:** `emailOrganizer/`, `granularCode.py`, `insightsGeneration.py`, `financial.md`.

* **Automação de Relatórios de Vendas**
    * **Descrição:** Script que utiliza `pandas` para estruturar dados de vendas e `openpyxl` para gerar um relatório Excel (`.xlsx`) automatizado.
    * **Tecnologias:** Python, Pandas, openpyxl.
    * **Arquivos Relevantes:** `jobAutomations/authomateRelatory.py`.

* **Web Scraping & Automação de Vagas de Emprego**
    * **Descrição:** Scripts que utilizam `requests` e `BeautifulSoup` para fazer scraping de sites de vagas e `selenium` para automatizar o processo de candidatura a vagas.
    * **Tecnologias:** Python, Selenium, Requests, BeautifulSoup.
    * **Arquivos Relevantes:** `emailOrganizer/automateApplications.py`, `jobAutomations/searchEmployer.py`, `emailOrganizer/searchJobs.py`.

#### Automação Residencial e IoT (House Automations)

* **Controle de IoT com Raspberry Pi**
    * **Descrição:** Scripts desenvolvidos para interagir com o hardware físico usando um Raspberry Pi. Inclui um script para controlar a iluminação (`Illumination.py`) e outro para operar um portão de garagem, que também envia um alerta SMS via Twilio quando a porta é aberta.
    * **Tecnologias:** Python, RPi.GPIO, Twilio API, ReportLab.
    * **Arquivos Relevantes:** `houseAutomations/Illumination.py`, `houseAutomations/garageDoor.py`.

* **Bot de Notificação e Alertas**
    * **Descrição:** Scripts que se integram a APIs de terceiros para enviar notificações, incluindo um bot do `Telegram` e um monitor de taxa de câmbio (`requests`) que verifica APIs financeiras.
    * **Tecnologias:** Python, python-telegram-bot, Requests.
    * **Arquivos Relevantes:** `houseAutomations/botTelegram.py`, `houseAutomations/taxesNotification.py`.

* **Automação de Desktop (Windows)**
    * **Descrição:** Script que consome a API da NASA "Foto Astronômica do Dia" (APOD), baixa a imagem do dia e a define automaticamente como papel de parede do Windows usando a biblioteca `ctypes`.
    * **Tecnologias:** Python, Requests, ctypes.
    * **Arquivos Relevantes:** `houseAutomations/wallPaper.py`.

---

### 3. 🛠️ Aplicativos de Desktop e Utilitários

Aplicações e ferramentas práticas com interfaces gráficas (GUI) e de linha de comando (CLI).

* **Marcador de Marca d'Água (App Desktop)**
    * **Descrição:** Uma aplicação de desktop com interface gráfica (GUI) construída com `Tkinter`. O aplicativo permite ao usuário selecionar uma imagem, digitar um texto de marca d'água e salvar a nova imagem processada.
    * **Tecnologias:** Python, Tkinter (GUI), Pillow (PIL).
    * **Arquivos Relevantes:** `imageWaterMark/`.

* **Teste de Velocidade de Digitação (App Desktop)**
    * **Descrição:** Uma aplicação GUI completa construída com `Tkinter` que mede a velocidade de digitação do usuário (em Palavras Por Minuto) com base em textos aleatórios.
    * **Tecnologias:** Python, Tkinter (GUI), time, random.
    * **Arquivos Relevantes:** `velocityTest/`.

* **Conversor de Código Morse (CLI)**
    * **Descrição:** Uma ferramenta de linha de comando completa para tradução bidirecional entre texto (ASCII) e Código Morse, estruturada de forma modular.
    * **Tecnologias:** Python.
    * **Arquivos Relevantes:** `morseCode/`.

* **Jogo da Velha (Tic-Tac-Toe)**
    * **Descrição:** Uma implementação completa e funcional do Jogo da Velha para linha de comando, escrita de forma modular (separando lógica, visualização e estrutura do tabuleiro).
    * **Tecnologias:** Python.
    * **Arquivos Relevantes:** `TicTacToe/`.

---

### 4. 🌐 Desenvolvimento Web (Flask)

* **Website "Café & Wi-Fi"**
    * **Descrição:** Um projeto de aplicação web (planejado) usando o micro-framework Flask. Inclui o banco de dados `SQLite` contendo dados de cafés e um arquivo de reflexão detalhado (`.md`) descrevendo a arquitetura planejada (app.py, templates HTML, CRUD) e lições aprendidas.
    * **Tecnologias:** Python, Flask, SQLite.
    * **Arquivos Relevantes:** `cafe_website/`.

---

### 5. 🐧 Scripts de Shell (Bash)

* **Script de Backup Automatizado (Bash)**
    * **Descrição:** Um script de shell (Bash) de um projeto de curso da IBM Skills Network. O script identifica todos os arquivos em um diretório-alvo que foram modificados nas últimas 24 horas, os compacta em um arquivo `.tar.gz` com timestamp e os move para um diretório de backup.
    * **Tecnologias:** Bash, Linux Commands (tar, date, find).
    * **Arquivos Relevantes:** `bkp.sh`, `checksum.txt`, `instructions.pdf`.

## 🧰 Stack de Tecnologias

Este portfólio demonstra experiência prática nas seguintes ferramentas e bibliotecas:

* **Linguagem Principal:** Python
* **Análise e Ciência de Dados:** Pandas, Matplotlib, Regex, Power BI
* **Desenvolvimento Web (Backend):** Flask, SQLite
* **Web Scraping & Automação:** Selenium, Requests, BeautifulSoup (bs4)
* **Aplicações Desktop (GUI):** Tkinter
* **Processamento de Mídia/Docs:** Pillow (PIL), ReportLab, PyPDF2, pdfplumber, openpyxl
* **Integração e APIs:** IMAP (imaplib), Telegram API, Twilio API, APIs REST (Requests)
* **IoT & Hardware:** RPi.GPIO
* **DevOps/Shell:** Bash Scripting, Linux Commands
* **Outros:** Estrutura de dados, Programação Orientada a Objetos (POO), Sockets, Ctypes.

## 📄 Materiais de Referência e Estudo

Este repositório também contém materiais de apoio e resultados de análises de meus estudos, incluindo:

* `cheat-sheet-comands-linux.pdf`: Um guia de referência rápida para comandos Linux.
* `bkp-java.pdf`: Uma análise de frequência de palavras-chave extraída de livros de estudo de Java/Spring.
* `pagesWithoutProjects.txt`: Uma lista pessoal de cursos e projetos da plataforma Coursera.
* `npx-commands.txt`: Notas sobre comandos React Native e Expo.

