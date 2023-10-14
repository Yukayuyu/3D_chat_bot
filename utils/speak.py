import time
import pyvcroid2
from utils.config_loader import *


def display_phonetic_label(tts_events):
    start = time.perf_counter()
    now = start
    for item in tts_events:
        tick = item[0] * 0.001
        type = item[1]
        if type != pyvcroid2.TtsEventType.PHONETIC:
            continue
        while (now - start) < tick:
            time.sleep(tick - (now - start))
            now = time.perf_counter()
        value = item[2]
        print(value, end="", flush=True)
    print("")


def speak(text,
          volume=config_ini['SPEAK']['volume'],
          speed=config_ini['SPEAK']['speed'],
          pitch=config_ini['SPEAK']['pitch'],
          emphasis=config_ini['SPEAK']['emphasis'],
          pauseMiddle=config_ini['SPEAK']['pauseMiddle'],
          pauseLong=config_ini['SPEAK']['pauseLong'],
          pauseSentence=config_ini['SPEAK']['pauseSentence'],
          masterVolume=config_ini['SPEAK']['masterVolume']):
    with pyvcroid2.VcRoid2(install_path=install_path, install_path_x86=install_path_x86) as vc:
        # Load language library
        lang_list = vc.listLanguages()
        if "standard" in lang_list:
            vc.loadLanguage("standard")
        elif 0 < len(lang_list):
            vc.loadLanguage(lang_list[0])
        else:
            raise Exception("No language library")

        # Load Voice
        voice_list = vc.listVoices()
        if 0 < len(voice_list):
            vc.loadVoice(voice_list[0])
        else:
            raise Exception("No voice library")

        # Set parameters
        vc.param.volume = volume
        vc.param.speed = speed
        vc.param.pitch = pitch
        vc.param.emphasis = emphasis
        vc.param.pauseMiddle = pauseMiddle
        vc.param.pauseLong = pauseLong
        vc.param.pauseSentence = pauseSentence
        vc.param.masterVolume = masterVolume

        # Text to speech
        speech, tts_events = vc.textToSpeech(text)

    return speech
