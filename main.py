from app import app
import app.config as config

if (__name__=="__main__"):
    app.run(host= config.HOST, port=config.PORT, debug=config.DEBUG)
