import os
from sheetmusic import app

def runserver():
    port = int(os.environ.get('PORT', 8080))
    hostip = os.environ.get('HOSTIP','127.0.0.1')
    app.run(host=hostip, port=port)

if __name__ == '__main__':
    runserver()
