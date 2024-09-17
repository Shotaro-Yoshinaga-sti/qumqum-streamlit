import fugashi
import re
import pykakasi

fugger = fugashi.Tagger()
kks = pykakasi.kakasi()


# 日本語をローマ字に変換する関数
def japanese_to_roman(text):

    # fugashiで日本語の部分を読み(カタカナ)に変換
    def convert_to_yomi(match):
        return "".join(w.feature.pron for w in fugger(match.group()))

    # 正規表現でテキスト中の日本語を見つけるて読みに変換する
    yomi = re.sub(r"[ぁ-んァ-ン一-龥々〆ヵヶ]+", convert_to_yomi, text)

    # pykakasiでカタカナをローマ字に変換
    def convert_to_roman(match):
        result = kks.convert(match.group())
        return "".join([r["hepburn"] for r in result])

    # 正規表現でカタカナを見つけてローマ字に変換
    roman = re.sub(r"[ァ-ン]+", convert_to_roman, yomi)

    # 不要な記号を削除
    roman = re.sub(r"[^a-zA-Z0-9ー、。？]", "", roman)

    # 数字を <NUMK VAL=(数値)> の形式に変換
    def replace_match(match):
        return f"<NUMK VAL={match.group()}>"

    # 正規表現で数字部分を見つけて変換
    num = re.sub(r"\d+", replace_match, roman)

    # その他の文字を変換
    translation_table = str.maketrans(
        {
            "、": ",",
            "。": ".",
            "ー": "-",
            "？": "?",
        }
    )
    return num.translate(translation_table)
