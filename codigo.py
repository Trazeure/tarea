from google.oauth2 import service_account
from googleapiclient.discovery import build

# Ruta al archivo JSON de credenciales descargado desde GCP
credentials_path = 'documento.xlsx'

# Crear un servicio de Google Drive
credentials = service_account.Credentials.from_service_account_file(
    credentials_path,
    scopes=['https://www.googleapis.com/auth/drive']
)

drive_service = build('drive', 'v3', credentials=credentials)

# Ejemplo: Listar archivos en Google Drive
results = drive_service.files().list().execute()
files = results.get('files', [])

if not files:
    print('No se encontraron archivos.')
else:
    print('Archivos:')
    for file in files:
        print(f'{file["name"]} ({file["id"]})')
