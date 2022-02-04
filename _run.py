# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# from FOLDER.FILE import CLASS, CONSTANT
# from FOLDER      import FILE

from template.homeboard      import app
from common         import config
import os

app.run_server(
    debug = True,                               #config.debug, 
    host  = "localhost",                        #config.host, 
    port  = int(os.environ.get("PORT", 5551))   #config.port
)