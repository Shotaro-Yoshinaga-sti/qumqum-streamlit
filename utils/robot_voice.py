import qumcum_ble as qumcum
from utils.convert_jp_to_roman import japanese_to_roman


def robot_voice(text):
    qumcum.voice_speed(speed=100)
    voices = text.split(",")
    convert_voices = list(map(japanese_to_roman, voices))
    for voice in convert_voices:
        qumcum.voice(voice)
