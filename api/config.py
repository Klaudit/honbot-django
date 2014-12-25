from os import environ


# env variables
PHP = environ.get('PHPSESSID')
token = '/?token=%s' % environ.get('API_TOKEN')
