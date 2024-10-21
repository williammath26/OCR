import cv2
import pytesseract

# Configurar o caminho do executável do Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Função para ler e processar a imagem
def ler_imagem(caminho_imagem):
    # Ler a imagem usando OpenCV
    img = cv2.imread(caminho_imagem)

    # Verificar se a imagem foi carregada corretamente
    if img is None:
        print(f"Erro: A imagem não pôde ser carregada. Verifique o caminho: {caminho_imagem}")
        return None

    # Aumentar a resolução da imagem
    img_resized = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

    # Converter a imagem para escala de cinza
    img_gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)

    # Aplicar thresholding
    _, img_thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # (Opcional) Operações morfológicas
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    img_morph = cv2.morphologyEx(img_thresh, cv2.MORPH_CLOSE, kernel)

    # Configuração de como a imagem é lida
    config = r'--oem 3 --psm 6'

    # Converter a imagem para texto usando Tesseract
    resultado = pytesseract.image_to_string(img_morph, config=config)

    return resultado

# Caminho da imagem que você deseja processar
caminho_imagem = 'nome.png'

# Ler e imprimir o resultado
texto_extraido = ler_imagem(caminho_imagem)
if texto_extraido:
    print("Texto extraído da imagem:")
    print(texto_extraido)
