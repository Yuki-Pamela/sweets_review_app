from django.shortcuts import render, redirect
from .models import Sweet
from django.contrib import messages

def home_page(request):
    user_query = str(request.GET.get('query', ''))
    search_result = Sweet.objects.filter(name__icontains=user_query)
    stuff_for_frontend = {'search_result': search_result}
    return render(request, 'sweets/sweets_stuff.html', stuff_for_frontend)

def create(request):
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'picture': request.POST.get('picture'),
            'rating': int(request.POST.get('rating')),
            'notes': request.POST.get('notes')
        }
        try:
            response = Sweet.objects.create(
                name=data.get('name'),
                picture=data.get('picture'),
                rating=data.get('rating'),
                notes=data.get('notes')
            )
            messages.success(request, 'New sweet added: {}'.format(data.get('name')))
        except Exception as e:
            messages.warning(
                request, 'Got an error when trying to create new sweet: {}'.format(e)
            )
        return redirect('/')

def edit(request, sweet_id):
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'picture': request.POST.get('picture'),
            'rating': int(request.POST.get('rating')),
            'notes': request.POST.get('notes')
        }
        try:
            sweet_obj = Sweet.objects.get(id=sweet_id)
            sweet_obj.name = data.get('name')
            sweet_obj.picture = data.get('picture')
            sweet_obj.rating = data.get('rating')
            sweet_obj.notes = data.get('notes')
            sweet_obj.save()
            messages.success(request, f"Sweet updated - {data.get('name')}")
        except Exception as e:
            messages.warning(
                request, 'Got an error when trying to update sweet: {}'.format(e)
            )
        return redirect('/')

def delete(request, sweet_id):
    try:
        sweet_obj = Sweet.objects.get(id=sweet_id)
        sweet_name = sweet_obj.name
        sweet_obj.delete()
        messages.warning(request, 'Deleted sweet: {}'.format(sweet_name))
    except Exception as e:
        messages.warning(request, 'Got an error when trying to delete a sweet: {}'.format(e))
    return redirect('/')


