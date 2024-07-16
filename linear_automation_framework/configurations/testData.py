import configparser

config = configparser.RawConfigParser()
config.read('./config.ini')
first_name = config.get('credentials', 'first_name')
last_name = config.get('credentials', 'last_name')
email = config.get('credentials', 'email')
password = config.get('credentials', 'password')
sign_in_page = config.get('URLs', 'sign_in_page')


