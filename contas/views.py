from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from .models import Transacao
from .forms import TransacaoForm


def home(request):
    data = {}
    data['now'] = datetime.datetime.now()
    data['transacoes'] = ['t1', 't2', 't3']
    #html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)
    return render(request, 'contas/home.html', data)


def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)


def nova_transacao(request):
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listagem')

    data = {}
    data['form'] = form
    return render(request, 'contas/form.html', data)


def update(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('listagem')

    data = {}
    data['form'] = form
    return render(request, 'contas/form.html', data)
