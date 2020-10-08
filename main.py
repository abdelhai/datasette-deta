from datasette.app import Datasette
app = Datasette(files=["test.db"]).app()

