from utils import ask_chatgpt, speak


def getSpeak():

    speak.speak(ask_chatgpt.ask('1', '星以外気になっていることはありますか？'))


getSpeak()
