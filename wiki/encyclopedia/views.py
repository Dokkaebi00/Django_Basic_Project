from django.shortcuts import render, redirect
from . import util
from django import forms
from markdown2 import markdown

# Create your views here.

class Search_Form(forms.Form):
    search = forms.CharField()

def index(request):
    list_entries = util.list_entries()
    return render(request, 'encyclopedia/index.html', {
        "entries": list_entries
    })

def entry(request, title):
    content = util.get_entry(title)
    content = markdown(content)
    return render(request, 'encyclopedia/entry.html', {
        "content": content,
        "title": title
    })

def random_page(request):
    title = util.random_page()
    return redirect("encyclopedia:entry", title = title)

def search(request):
    q = request.POST.get('q').strip()
    if q in util.list_entries():
        return redirect("encyclopedia:entry", title=q)
    entries = util.search(q)
    return render(request, "encyclopedia/search.html", {
        "entries": entries,
        "q": q
    })

def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title == "" or content == "":
            return render(request, 'encyclopedia/create.html', {
                "message": "Can't save with the empty field",
                "title": title,
                "content": content
            })
        if title in util.list_entries():
            return render(request, "encyclopedia/create.html", {
                "message": "Title already exist",
                "title": title,
                "content": content
            })
        util.save_entry(title, content)
        return redirect("encyclopedia:entry", title=title)
    return render(request, 'encyclopedia/create.html')

def edit(request, title):
    content = util.get_entry(title.strip())
    if request.method == "POST":
        content = request.POST.get('content')
        if content == "":
            message = "Can't save with empty field"
            return render(request, 'encyclopedia/edit.html', {
                "message": message,
                "title": title,
                "content": content
            })
        util.save_entry(title, content)
        return redirect("encyclopedia:entry", title=title)
    return render(request, 'encyclopedia/edit.html', {
        "title": title,
        "content": content
    })