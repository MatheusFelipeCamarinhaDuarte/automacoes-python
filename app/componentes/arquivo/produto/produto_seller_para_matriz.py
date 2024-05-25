import os
import xml.etree.ElementTree as ET
from tkinter import messagebox

def xml_to_matriz_produto():
    # Caminho completo para o arquivo XML
    caminho_app = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    caminho_dados = os.path.join(caminho_app,'temp','dados')
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

        # Imprime a matriz
        # for linha in matriz:
            # print(','.join(linha))
            # if linha[4] != 'BANDEJA' and linha[4] != 'UNIDADE' and linha[4] != 'KILOGRAMA'and linha[4] != 'GRAMA'and linha[4] != 'LITRO'and linha[4] !='FATIA' and linha[4] != 'PACOTE' and linha[4] != 'MILILITRO'  and linha[4] != 'FARDO'  and linha[4] != 'PACOTE' and linha[4] !=  'PACK' and linha[4] != 'GARRAFA' and linha[4] != '' and linha[4] !='':
            #     print(linha[1],linha[4],linha[6],linha[9])
            #     print(linha)
        
        return matriz
    except:
        messagebox.showerror("Erro", f'O XML apontado não é válido! olha a aba "Como retirar relatórios no formato correto" para obter o arquivo certo.')

if __name__ == "__main__":
    xml_to_matriz_produto()
