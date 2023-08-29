from django.shortcuts import render, get_object_or_404, redirect
from .forms import MongoDBConnectionForm
from .models import MongoDBConnection

def mongodb_connection(request, connection_id=None):
    connection = None

    if connection_id:
        connection = get_object_or_404(MongoDBConnection, id=connection_id)

    if request.method == 'POST':
        form = MongoDBConnectionForm(request.POST, instance=connection)
        if form.is_valid():
            form.save()
            return redirect('connection_list')
    else:
        form = MongoDBConnectionForm(instance=connection)
    
    return render(request, 'mongodb_connection.html', {'form': form})

def connection_list(request):
    connections = MongoDBConnection.objects.all()
    return render(request, 'connection_list.html', {'connections': connections})

def connection_detail(request, connection_id):
    connection = get_object_or_404(MongoDBConnection, id=connection_id)
    return render(request, 'connection_detail.html', {'connection': connection})

def connection_delete(request, connection_id):
    connection = get_object_or_404(MongoDBConnection, id=connection_id)
    if request.method == 'POST':
        connection.delete()
        return redirect('connection_list')
    return render(request, 'connection_confirm_delete.html', {'connection': connection})


def index(request):
    return HttpResponse("Hello, world. You're at the My polls index.")