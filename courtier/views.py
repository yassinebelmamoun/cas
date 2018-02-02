""" Courtier Views """
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class CourtierList(ListView):
    """ List of all courtiers """
    pass


class CourtierDetail(DetailView):
    """ Detail of one courtier """
    pass


class CourtierCreate(CreateView):
    """ Create Courtier """
    pass


class CourtierUpdate(UpdateView):
    """ Update Courtier """
    pass


class CourtierDelete(DeleteView):
    """ Delete Courtier """
    pass
