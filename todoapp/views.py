from django.shortcuts import render
from .models import Post
from todoapp.forms import TodoappForm
from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import logging
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def todo_list(request):
    post = Post.objects.all().order_by('deadline')
    context = {'todo_list':post}
    return render(request, "todoapp/todo_list.html", context)

class TodoappCreateView(View):
    def get(self,request):
        form=TodoappForm()
        ctx={"form":form}
        return render(request,"todoapp/todoapp_form.html",ctx)

    def post(self,request):
        form=TodoappForm(request.POST)
        if not form.is_valid():
            ctx={'form':form}
            return render(request,"todoapp/todoapp_form.html",ctx)

        form.save()
        return render(request,"todoapp/todoapp_success.html")

class TodoappUpdateView(View):
    def get(self, request, todo_id):
        todo_item = get_object_or_404(Post, id=todo_id)
        form = TodoappForm(instance=todo_item)
        return render(request, "todoapp/todoapp_form.html", {'form': form})

    def post(self, request, todo_id):
        todo_item = get_object_or_404(Post, id=todo_id)
        form = TodoappForm(request.POST, instance=todo_item)
        if not form.is_valid():
            return render(request, "todoapp/todoapp_form.html", {'form': form})

        form.save()
        return render(request,"todoapp/todoapp_success.html")

class TodoappDeleteView(View):
    def post(self, request, todo_id):
        todo_item = get_object_or_404(Post, id=todo_id)
        todo_item.delete()
        return render(request,"todoapp/todoapp_success.html")

class TodoappSearchView(View):
    def get(self, request):
        query = request.GET.get('query')

        if query:
            todo_items = Post.objects.filter(title__icontains=query)

            if todo_items.exists():
                return render(request, 'todoapp/todoapp_search_results.html', {'todo_items': todo_items})
            else:
                error_message = "no corresponding todolist"
                logging.error("no corresponding todolist")
                return render(request, 'todoapp/todoapp_search_results.html', {'error_message': error_message})

        # warning logs
        logging.warning("please enter the search keyword")
        return render(request, 'todoapp/todoapp_search_results.html')
