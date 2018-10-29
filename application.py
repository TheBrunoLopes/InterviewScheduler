from datetime import timedelta
from flask_jwt_extended import JWTManager
import connexion as connexion
app = connexion.App(__name__, swagger_ui=True)
app.add_api('swagger.yaml')
application = app.app

application.config['JWT_SECRET_KEY'] = 'super-mega-secret-pls-do-not-tell-anyone'
# JWT expires after 6 hours
application.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(seconds=21600)
jwt = JWTManager(application)


if __name__ == '__main__':
    # If you want to run this with a WSGI
    # you could use the command: uwsgi --http :4001 -w application:application -p 16
    # This service depends on a mongo database
    # you can quickly run one for this project by doing -> docker run --name some-mongo --net=host -d mongo
    app.run(port=4001, debug=True)
