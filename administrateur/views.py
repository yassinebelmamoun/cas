from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from courtier.models import Courtier
from administrateur.forms import CreateCourtierAdministrateur
from utilisateur.models import User


def home(request):
    return render(request, 'administrateur/index.html')

"""
    Courtier Views
"""

def courtier_detail(request, pk):
    courtier = Courtier.objects.get(pk=pk)
    return render(request, 'administrateur/detail_courtier.html', {'courtier':courtier})


class CourtierList(ListView):
    ''' Generic List Courtier View '''
    model = Courtier
    template_name = 'administrateur/list_courtier.html'
    context_object_name = 'courtiers'
    paginate_by = 10
    queryset = Courtier.objects.all()

courtier_list = CourtierList.as_view()


class CourtierCreate(CreateView):
    ''' Generic Create Courtier View '''
    model = Courtier
    template_name = 'administrateur/create_courtier.html'
    fields = '__all__'
    success_url = reverse_lazy('administrateur:courtier_create_administrateur')

    def get_success_url(self):
        return reverse_lazy('administrateur:courtier_create_administrateur',
                            args=(self.object.id,))

courtier_create = CourtierCreate.as_view()


class CourtierUpdate(UpdateView):
    ''' Generic Update Courtier View '''
    model = Courtier
    template_name = 'administrateur/update_courtier.html'
    fields = '__all__'
    success_url = reverse_lazy('administrateur:courtier_list')

courtier_update = CourtierUpdate.as_view()


class CourtierDelete(DeleteView):
    ''' Generic Delete Courtier View '''
    model = Courtier
    template_name = 'administrateur/delete_courtier.html'
    success_url = reverse_lazy('administrateur:courtier_list')

courtier_delete = CourtierDelete.as_view()


def create_courtier_administrateur(request, pk):
    courtier_id = pk
    if request.method == "POST":
        form = CreateCourtierAdministrateur(request.POST)
        if form.is_valid():
            utilisateur = form.save(commit=False)
            utilisateur.courtier = Courtier.objects.get(pk=courtier_id)
            utilisateur.role = 'Administrateur'
            utilisateur.password = User.objects.make_random_password()
            utilisateur.save()
            return redirect('administrateur:courtier_create_administrateur_done', pk=utilisateur.pk)
    else:
        form = CreateCourtierAdministrateur()
    context = {'form': form, 'courtier_id': courtier_id}
    return render(request, 'administrateur/create_courtier_administrateur.html', context)


def courtier_create_administrateur_done(request, pk):
    utilisateur = User.objects.get(pk=pk)
    context = {'utilisateur': utilisateur}
    return render(request, 'administrateur/create_courtier_administrateur_done.html', context)


class CourtierAdministrateurDelete(DeleteView):
    ''' Generic Delete Courtier View '''
    model = User
    template_name = 'administrateur/delete_courtier_administrateur.html'
    success_url = reverse_lazy('administrateur:courtier_list')

courtier_administrateur_delete = CourtierAdministrateurDelete.as_view()
