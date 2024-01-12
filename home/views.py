from django.shortcuts import render, redirect
from .models import notes


def homeView(request):
    # ADD NEW NOTE
    if request.method == 'POST':
        note = notes.objects.create(
            title=request.POST['title'],
            text=request.POST['text']
        )
        note.save()
        return redirect('/')
    my_notes = notes.objects.all()
    context = {'notes': my_notes}
    return render(request, 'home.html', context)


def noteView(request, pk):
    if request.method == 'POST':
        note = notes.objects.get(id=pk)
        note.title = request.POST['title']
        note.text = request.POST['text']
        note.save()
        return redirect('/')

    my_note = notes.objects.get(id=pk)
    context = {'note': my_note}
    return render(request, 'note.html', context)


def noteDeleteView(request, pk):
    note = notes.objects.get(id=pk)
    note.delete()
    return redirect('/')

