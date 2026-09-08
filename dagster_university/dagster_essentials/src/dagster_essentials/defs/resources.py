from dagster_duckdb import DuckDBResource
import dagster as dg


'''
Ten fragment kodu importuje zasób o nazwie DuckDBResourceod Dagstera dagster_duckdbbiblioteka integracyjna. 
Następnie tworzy instancję tego zasobu i zapisuje ją w database_resource. 
'''

database_resource = DuckDBResource(
    #database="data/staging/data.duckdb" #to jest przykładowa ścieżka do bazy danych
    #database=os.getenv("DUCKDB_DATABASE") #to jest ścieżka do bazy danych z pliku .env
    database=dg.EnvVar("DUCKDB_DATABASE")
)

'''EnvVar() pobiera wartość zmiennej środowiskowej za każdym razem, gdy rozpoczyna się uruchomienie
   os.getenvpobiera zmienną środowiskową , gdy ładowana jest lokalizacja kodu.
   
   Korzystając z EnvVar zamiast os.getenv Możesz dynamicznie dostosowywać konfigurację zasobu. 
   Na przykład możesz zmienić używaną bazę danych DuckDB bez konieczności restartowania serwera WWW Dagstera. '''


@dg.definitions
def resources() -> dg.Definitions:
    return dg.Definitions(resources={"database": database_resource})

'''To informuje Dagstera, jak mapować zasoby na konkretne nazwy kluczy.
W tym przypadku database_resourcezasób, który właśnie zdefiniowano, jest mapowany na nazwę klucza database. '''