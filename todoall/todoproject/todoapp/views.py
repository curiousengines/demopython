from django.shortcuts import render, redirect
from . models import Task 
from . forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
# Create your views here.

class tasklist(ListView):
    model=Task
    template_name='home.html'
    context_object_name='task1'
    
class detail(DetailView):
    model=Task
    template_name='detail.html'
    context_object_name='m'

class updatelist(UpdateView):
    model=Task
    template_name='update.html'
    context_object_name='task'
    fields=('name','priority','date')


    def get_success_url(self) -> str:
        return reverse_lazy('cvbdetail',kwargs={'pk':self.object.id})


class deletelist(DeleteView):
    model=Task
    template_name='delete.html'
    success_url=reverse_lazy('cbvhome')


def add(request):
    task1=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name, priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'task1':task1})

# def detail (request):
    
#     return render (request,'detail.html',)
def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect ('/')

    return render(request,'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    form=TodoForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form, 'task':task})