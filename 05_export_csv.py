import csv
import requests

url_base = "http://localhost:58000/api/v1"

# 1. Obtener el token (igual que en el script 01)
resp_token = requests.post(
    f"{url_base}/ticket", json={"username": "cisco", "password": "class"}
)
token = resp_token.json()["response"]["serviceTicket"]

# 2. Consultar los dispositivos de red (igual que en el script 02)
headers = {"X-Auth-Token": token}
resp_equipos = requests.get(f"{url_base}/network-device", headers=headers)
equipos = resp_equipos.json()["response"]

# 3. Guardar en un archivo CSV (valor agregado)
with open("equipos.csv", "w", newline="") as archivo:
  writer = csv.writer(archivo)
  writer.writerow(["Hostname", "Tipo", "IP"])  # Encabezados

  for eq in equipos:
    writer.writerow(
        [eq.get("hostname"), eq.get("type"), eq.get("managementIpAddress")]
    )

print("Listo! Se creo el archivo equipos.csv")