from django.shortcuts import render, redirect
from django.db import DatabaseError
from .models import Entry
from .forms import EntryForm

def inicio(request):
    noredis = False  # kept for template compatibility
    try:
        entries = Entry.objects.order_by("-created_at")
    except DatabaseError:
        noredis = True
        entries = []
    form = EntryForm()
    return render(request, "inicio.html", {"noredis": noredis, "lista": [e.content for e in entries], "form": form})

def add(request):
    if request.method != "POST":
        return redirect("inicio")
    form = EntryForm(request.POST)
    if form.is_valid():
        Entry.objects.create(content=form.cleaned_data["info"])
    return redirect("inicio")
