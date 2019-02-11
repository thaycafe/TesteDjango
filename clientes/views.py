from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm

acao = 'nada'


def person_list(request):
    people = Person.objects.all()
    return render(request, 'person.html', {'seres': people})


# Create your views here.


def person_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})


def person_update(request, id):
    acao = 'update'
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'person_form.html', {'form': form, 'acao': acao})


def person_delete(request, id):
    acao='delete'
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(request, 'person_form.html', {'form': form, 'acao':acao})
