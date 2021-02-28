import re
from random import randint

import os
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

def list_entries():
    # get name of all files in the entries folder
    _, filenames = default_storage.listdir("entries")
    # delete .md in the name of the file
    filenames = [re.sub(r"\.md$","", filename) for filename in filenames if filename.endswith(".md")]
    # return the sorted list
    return list(sorted(filenames))

def get_entry(title):
    f = default_storage.open(f"entries/{title}.md")
    return f.read().decode("utf-8")

def random_page():
    entries = list_entries()
    random_title = entries[randint(0, len(entries) - 1)]
    print(random_title)
    return random_title
    
def search(query):
    _, filenames = default_storage.listdir("entries")
    filenames = [re.sub(r"\.md$", "", filename) for filename in filenames if filename.endswith(".md") and query in filename.lower()]
    return list(sorted(filenames))

def save_entry(title, content):
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))