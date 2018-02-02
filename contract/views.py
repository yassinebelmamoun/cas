""" Contract View """
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

"""
Contract 
"""

class ContractCreate(CreateView):
    """ CAS create a new Contract """
    pass

class ContractDetail(DetailView):
    """ CAS view a Contract details """
    pass

class ContractDelete(DeleteView):
    """ CAS delete Contract """
    pass

class ContractUpdate(UpdateView):
    """ CAS update Contract """
    pass


"""
Product
"""

class ProductCreate(CreateView):
    """ CAS create a new Product """
    pass

class ProductDetail(DetailView):
    """ CAS view a Product details """
    pass

class ProductDelete(DeleteView):
    """ CAS delete Product """
    pass

class ProductUpdate(UpdateView):
    """ CAS update Product """
    pass
