""" Client Views """
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class ClientCreate(CreateView):
    """ Seller create a new Client """
    pass

class ClientDetail(DetailView):
    """ Seller view a Client details """
    pass

class ClientDelete(DeleteView):
    """ Seller delete Client """
    pass

class ClientUpdate(UpdateView):
    """ Seller update Client """
    pass
