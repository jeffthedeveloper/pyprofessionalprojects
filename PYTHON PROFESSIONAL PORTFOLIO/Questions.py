import PyPDF2
import re
import pandas as pd

def limpar_texto(texto):
    """
    Função para limpar o texto, removendo ou substituindo caracteres indevidos.
    """
    # Substituir caracteres problemáticos por espaços ou removê-los
    texto = re.sub(r'[\x00-\x1F\x7F]', ' ', texto)  # Remove caracteres de controle
    texto = re.sub(r'\s+', ' ', texto)  # Substitui múltiplos espaços por um único espaço
    texto = texto.strip()  # Remove espaços no início e no final
    return texto

def analisar_questoes_pdf(caminho_pdf):
    questoes_corretas = []
    questoes_erradas = []

    try:
        with open(caminho_pdf, 'rb') as arquivo_pdf:
            leitor_pdf = PyPDF2.PdfReader(arquivo_pdf)
            for pagina in leitor_pdf.pages:
                texto = pagina.extract_text()

                # Padrões para capturar o texto completo antes de "Questão correta." ou "Questão errada."
                padrao_correta = r"(.*?)\.\s*Questão correta\."
                padrao_errada = r"(.*?)\.\s*Questão errada\."

                corretas = re.findall(padrao_correta, texto, re.DOTALL)
                erradas = re.findall(padrao_errada, texto, re.DOTALL)

                # Limpar e adicionar as questões às listas
                questoes_corretas.extend([limpar_texto(c) for c in corretas])
                questoes_erradas.extend([limpar_texto(e) for e in erradas])

    except FileNotFoundError:
        print(f"Erro: O arquivo PDF '{caminho_pdf}' não foi encontrado.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro ao processar o arquivo PDF: {e}")
        return None

    # Garantir que as listas tenham o mesmo comprimento
    max_len = max(len(questoes_corretas), len(questoes_erradas))
    questoes_corretas += [""] * (max_len - len(questoes_corretas))
    questoes_erradas += [""] * (max_len - len(questoes_erradas))

    # Criar DataFrame
    dados = {
        "Questões Corretas": questoes_corretas,
        "Questões Erradas": questoes_erradas
    }
    df = pd.DataFrame(dados)

    return df

# Caminho do PDF
caminho_pdf = r"C:\Users\Jeff.DESKTOP-CQT2E9A\Downloads\Curso de Constitucional.pdf"

# Processar o PDF e gerar o CSV
resultado = analisar_questoes_pdf(caminho_pdf)

if resultado is not None:
    print(resultado)
    if not resultado.empty:
        # Salvar o DataFrame em um arquivo CSV
        resultado.to_csv('questoes_analisadas.csv', index=False, encoding='utf-8')
        print("Arquivo CSV 'questoes_analisadas.csv' salvo com sucesso!")
    else:
        print("Nenhuma questão correspondente ao padrão foi encontrada no PDF.")