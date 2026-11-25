from django.shortcuts import render
from django.http import HttpResponse
from gtts import gTTS
from io import BytesIO


def home(request):
    return render(request, 'dashboard/home.html')

def zikir(request):
        return render(request, 'dashboard/zikir.html')

def settings(request):
    return render(request, 'dashboard/settings.html')

def profil(request):
    return render(request, 'dashboard/profil.html')

def explore(request):
    return render(request, 'dashboard/explore.html')

def koleksi(request):
    return render(request, 'dashboard/koleksi.html')

def suara_doa(request):
    teks = request.GET.get('teks', '')
    bahasa = request.GET.get('bahasa', 'id')

    if not teks:
        return HttpResponse("Teks kosong", status=400)

    if bahasa not in ['ar', 'id']:
        bahasa = 'id'

    audio = BytesIO()

    try:
        suara = gTTS(text=teks, lang=bahasa, slow=False)
        suara.write_to_fp(audio)
        audio.seek(0)

        return HttpResponse(
            audio.read(),
            content_type='audio/mpeg'
        )

    except Exception as e:
        return HttpResponse(str(e), status=500)

    