from django.shortcuts import render,redirect
from tasks.models import Todo
from django.contrib import messages

# Create   your views here.

from django import forms
class TodoForm(forms.Form):
    task_name=forms.CharField()
    # user=forms.CharField()

from django.views.generic import View


class TodoCreateView(View):
    def get(self,request,*args,**kw):
        form=TodoForm()
        return render(request,'todo-add.html',{'form':form})
    def post(self,request,*args,**kw):
        form=TodoForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Todo.objects.create(**form.cleaned_data,user=request.user)
            # message-:success,error,warning,info
            messages.success(request,"Todo has been created successfully!!!")
            return redirect("todo-list")
        messages.error(request,"Failed to creat Todo")
        return render(request,'todo-add.html',{"form":form})

class TodoListView(View):
    def get(self,request,*args,**kwargs):
        qs=Todo.objects.filter(status=False,user=request.user).order_by("-date") ## sort by descending order
        return render(request,'todo-list.html',{"todos":qs})
    
class TodoDetailsView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")         ## extracting id
        qs=Todo.objects.get(id=id)  ## take these id of todo object
        return render(request,'todo-detail.html',{'todo':qs})
    
# localhost:8000/todos/{id}/remove/

class TodoDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Todo.objects.get(id=id).delete()
        messages.success(request,"todo has been deleted successfully")
        return redirect("todo-list")
class TodoEditView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Todo.objects.filter(id=id).update(status=True)
        messages.success(request,"Todo has been updated successfully")
        return redirect("todo-list")
class TodoCompletedView(View):
    def get(self,request,*args,**kwargs):
        qs=Todo.objects.filter(status=True).order_by("-date")
        
        return render(request,'todo-completed.html',{"todos":qs})


    
    