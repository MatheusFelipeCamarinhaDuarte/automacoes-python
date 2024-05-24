import os
import xml.etree.ElementTree as ET
from tkinter import messagebox

def xml_to_matriz_produto():
# Obtenha o caminho do diretório do script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho completo para o arquivo XML
    caminho_importacoes = os.path.dirname(script_dir)
    caminho_app = os.path.dirname(caminho_importacoes)
    caminho_dados = os.path.join(caminho_app,'dados')
    # print(caminho_dados)
    
    # Aqui preciso passar o arquivo recebido por XML    
    xml_file = os.path.join(caminho_dados,'arquivo_temporario.xml')
    try:
    # Parse o XML
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # # Inicializa a matriz para armazenar os dados
        matriz = []

    # Itera sobre os elementos 'Group'
        for group in root.findall('.//{urn:crystal-reports:schemas:report-detail}Group'):
            row = []
            # Itera sobre os elementos 'Field' dentro de 'GroupHeader'
            for field in group.find('.//{urn:crystal-reports:schemas:report-detail}GroupHeader').iter('{urn:crystal-reports:schemas:report-detail}Field'):
                value_element = field.find('{urn:crystal-reports:schemas:report-detail}Value')
                value = value_element.text if value_element is not None else ' '  # Substitui por " " se não encontrar valor
                row.append(value)
            # Substitui None por uma string vazia
            row = [value if value is not None else '' for value in row]
            # Adiciona a linha à matriz
            matriz.append(row)

        # # Imprime a matriz
        # for linha in matriz:
        #     print(','.join(linha))
        
        

        # Retorna a matriz
        return matriz
    except:
        messagebox.showerror("Erro", f'O XML apontado não é válido! olha a aba "Como retirar relatórios no formato correto" para obter o arquivo certo.')
xml_to_matriz_produto()
