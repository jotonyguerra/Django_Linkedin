from urllib import request
from django.shortcuts import render
from .models import Notes
from django.http import Http404, HttpResponseRedirect
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from .forms import NotesForm
from typing import List
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'
    login_url = "/login"


class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url = "/login"

class NotesCreateView(CreateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'
    login_url = "/login"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.notes.all()
# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})
class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    login_url = "/login"

# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note Does Not Exist")
#     return render(request, 'notes/notes_detail.html', {'note': note})