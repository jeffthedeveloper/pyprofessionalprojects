import pdfplumber
import re
import pandas as pd

def limpar_texto(texto):
    """Função para limpar o texto."""
    texto = re.sub(r'\s+', ' ', texto).strip()
    return texto

def analisar_comentarios_pdf(caminho_pdf):
    """Analisa comentários de questões em um PDF."""
    comentarios = []

    try:
        with pdfplumber.open(caminho_pdf) as pdf:
            for pagina in pdf.pages:
                texto = pagina.extract_text()
                if texto:
                    # Padrão flexível para capturar o comentário e a marcação, em qualquer ordem
                    padrao = r"(.+?)\s*–\s*(CORRETA|CERTA|ERRADA|INCORRETA)\b|(\bCORRETA|\bCERTA|\bERRADA|\bINCORRETA)\s*–\s*(.+?)\b"
                    resultados = re.findall(padrao, texto, re.IGNORECASE | re.DOTALL)

                    for resultado in resultados:
                        if resultado[0] and resultado[1]:
                            # Caso 1: Comentário seguido de marcação
                            comentarios.append({"comentario": limpar_texto(resultado[0]), "marcacao": resultado[1].upper()})
                        elif resultado[2] and resultado[3]:
                            # Caso 2: Marcação seguida de comentário
                            comentarios.append({"comentario": limpar_texto(resultado[3]), "marcacao": resultado[2].upper()})

    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado: {caminho_pdf}")
        return None
    except Exception as e:
        print(f"Erro ao processar o PDF: {e}")
        return None

    if comentarios:
        df = pd.DataFrame(comentarios)
        return df
    else:
        print("Nenhum comentário encontrado no PDF.")
        return None

# Caminho do seu PDF
caminho_pdf = r"C:\Users\Jeff.DESKTOP-CQT2E9A\Downloads\Curso Direito ADM.pdf"

# Processar e salvar em CSV
df_comentarios = analisar_comentarios_pdf(caminho_pdf)

if df_comentarios is not None:
    # Imprime o DataFrame, ignorando caracteres não suportados
    print(df_comentarios.to_string(index=False, errors='ignore'))
    df_comentarios.to_csv("comentarios_questoes_adm.csv", index=False, encoding='utf-8-sig')
    print("Comentários salvos em 'comentarios_questoes_adm.csv'")