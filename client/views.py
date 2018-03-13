""" Client Views """
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CreateClient
from .models import Client


def create_client(request):
    seller = request.user
    if request.method == "POST":
        form = CreateClient(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.seller = seller
            client.save()
            return redirect('client:detail_client', pk=client.pk)
    else:
        form = CreateClient()
    context = {'form': form}
    return render(request, 'client/create_client.html', context)


def detail_client(request):
    context = {}
    return render(request, 'client/detail_client.html', context)


def list_client(request):
    context = {'clients': Client.objects.filter(seller=request.user)}
    return render(request, 'client/list_client.html', context)


class ClientDelete(DeleteView):
    """ Seller delete Client """
    pass


class ClientUpdate(UpdateView):
    """ Seller update Client """
    pass
