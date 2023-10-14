import configparser

config_ini = configparser.ConfigParser()
config_ini.read('./utils/config.ini', encoding='utf-8')

install_path = config_ini['SPEAK']['install_path']
install_path_x86 = config_ini['SPEAK']['install_path_x86']

api_key = config_ini['CHATGPT']['key']
model = config_ini['CHATGPT']['model']
temperature = config_ini['CHATGPT']['temperature']
max_tokens = config_ini['CHATGPT']['max_tokens']
top_p = config_ini['CHATGPT']['top_p']
frequency_penalty = config_ini['CHATGPT']['frequency_penalty']
presence_penalty = config_ini['CHATGPT']['presence_penalty']
