#region _FRONT
# import socket
# import ssl

# def test_ssl_connection(host, port, certfile, keyfile):
#     try:
#         context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
#         context.load_cert_chain(certfile=certfile, keyfile=keyfile)
#         with socket.create_connection((host, port)) as sock:
#             with context.wrap_socket(sock, server_side=False) as ssock:
#                 return True
#     except Exception as e:
#         print("SSL connection error:", e)
#         return False
    
# if __name__ == "__main__":
#     host = 'localhost'
#     port = 9390
#     certfile = './servercert.pem'
#     keyfile = './serverkey.pem'
    
#     if test_ssl_connection(host, port, certfile, keyfile):
#         print("SSL connection successful")
#     else:
#         print("SSL connection failed")
#endregion

#region _BACK
from gvm.protocols.latest import Gmp
from gvm.connections import TLSConnection
from gvm.xml import pretty_print

def connect_to_gmp(hostname, port, username, password, certfile, keyfile):    
    try:
        print('working...')
        # Créer une connexion TLS vers le serveur GVM
        connection = TLSConnection(hostname=hostname, port=port, certfile=certfile, keyfile=keyfile)
        print(connection)
        # Initialiser le protocole GMP avec la connexion TLS
        gmp = Gmp(connection=connection)
        print(gmp)
        # Authentifier avec le serveur GVM
        print(gmp.authenticate(username='admin', password=' e'))
        gmp.authenticate(username='admin', password=' e')

        return gmp
    except Exception as e:
        print("Erreur lors de la connexion à l'API GMP:", e)
        return None

if __name__ == "__main__":
    # Informations de connexion
    hostname = 'localhost'
    port = 9390
    username = 'admin'
    password = 'admin'
    certfile = './servercert.pem'  # Chemin vers votre fichier de certificat
    keyfile = './serverkey.pem'  # Chemin vers votre fichier de clé privée

    # Se connecter à l'API GMP
    gmp = connect_to_gmp(hostname, port, username, password, certfile, keyfile)
    if gmp:
        print("Connexion à l'API GMP réussie.")

        # Récupérer la version GMP actuelle
        version = gmp.get_version()

        # Afficher l'XML de manière lisible
        pretty_print(version)
#endregion