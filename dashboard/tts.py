
from gtts import gTTS
from io import BytesIO


def buat_suara(teks):
    audio = BytesIO()

    suara = gTTS(text=teks, lang="ar", slow=False)
    suara.write_to_fp(audio)

    audio.seek(0)
    return audio
