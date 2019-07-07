from os import environ


class Configuration:

    KEEP_ALIVE = False

    APPLICATION_DEBUG = bool(environ.get('APPLICATION_DEBUG', False))
    APPLICATION_WORKERS_NUMBER = int(environ.get('APPLICATION_WORKERS_NUMBER', 4))

    MOTOR_URI = 'mongodb://{}:{}@{}:{}/{}'.format(
        environ.get('DB_USER'),
        environ.get('DB_PASSWORD'),
        environ.get('DB_HOST', 'mongodb-star-wars-planets'),
        environ.get('DB_PORT', 27017),
        environ.get('DB_NAME')
    )

    LOGO = '''
    .______   ____    ____ .______    __        ______   
    |   _  \  \   \  /   / |   _  \  |  |      /  __  \  
    |  |_)  |  \   \/   /  |  |_)  | |  |     |  |  |  | 
    |   ___/    \_    _/   |   _  <  |  |     |  |  |  | 
    |  |          |  |     |  |_)  | |  `----.|  `--'  | 
    | _|          |__|     |______/  |_______| \______/  
    '''
