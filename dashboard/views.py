
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django import forms
from gtts import gTTS
from io import BytesIO

from .forms import FormDaftar


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email', '').strip().lower()
        password = request.POST.get('password', '')

        try:
            user_data = User.objects.get(email__iexact=email)
            user = authenticate(
                request,
                username=user_data.username,
                password=password
            )
        except User.DoesNotExist:
            user = None

        if user is not None:
            login(request, user)
            return redirect('home')

        messages.error(request, 'Email atau kata sandi tidak sesuai.')

    return render(request, 'dashboard/login.html')



def daftar(request):
    sudah_login = request.user.is_authenticated

    form = FormDaftar(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.save()

            if sudah_login:
                messages.success(
                    request,
                    'Akun baru berhasil ditambahkan.'
                )
            else:
                login(request, user)

            return redirect('home')

    return render(
        request,
        'dashboard/daftar.html',
        {'form': form}
    )


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return redirect('home')

@login_required(login_url='login')
def home(request):
    return render(request, 'dashboard/home.html')


@login_required(login_url='login')
def zikir(request):
    return render(request, 'dashboard/zikir.html')


@login_required(login_url='login')
def settings(request):
    return render(request, 'dashboard/settings.html')


@login_required(login_url='login')
def profil(request):
    return render(request, 'dashboard/profil.html')


@login_required(login_url='login')
def explore(request):
    return render(request, 'dashboard/explore.html')


@login_required(login_url='login')
def koleksi(request):
    return render(request, 'dashboard/koleksi.html')


@login_required(login_url='login')
def suara_doa(request):
    teks = request.GET.get('teks', '').strip()

    if not teks:
        return HttpResponse('Teks doa belum tersedia.')

    audio = BytesIO()
    suara = gTTS(text=teks, lang='id')
    suara.write_to_fp(audio)
    audio.seek(0)

    response = HttpResponse(audio.read(), content_type='audio/mpeg')
    return response

