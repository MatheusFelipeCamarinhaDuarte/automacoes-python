import os
import xml.etree.ElementTree as ET

def xml_to_matriz_produto():
# Obtenha o caminho do diretório do script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Aqui preciso passar o arquivo recebido por XML
    xml_file = None 
    
    # Caminho completo para o arquivo XML
    xml_file = os.path.join(script_dir, 'produtos', 'csv', 'arquivo.xml')
    # Parse o XML
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Inicializa a matriz para armazenar os dados
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
    #     print(','.join(linha))

    # Retorna a matriz
    return matriz

