import sys
sys.path.append("../")

import os
import dotenv  # type: ignore
dotenv.load_dotenv()

import os
from supabase import create_client, Client # type: ignore
from supabase.client import ClientOptions # type: ignore


def init_conection_bd():
    """
    Inicializa la conexión con la base de datos Supabase.

    Obtiene la URL y la clave de Supabase desde las variables de entorno
    y crea un cliente con opciones específicas.

    Returns:
        Client: Objeto de cliente Supabase configurado.

    Raises:
        ValueError: Si las credenciales no están definidas en las variables de entorno.
    """
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    return create_client(url, key,
      options=ClientOptions(
        postgrest_client_timeout=10,
        storage_client_timeout=10,
        schema="public",
      ))

def select_datos(name_bd, supabase_client):
    """
    Realiza una consulta a la base de datos Supabase y obtiene todos los datos de una tabla.
    """
    return supabase_client.table(name_bd).select("*").execute()

 

