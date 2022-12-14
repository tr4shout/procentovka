from django.shortcuts import render, get_object_or_404, redirect
from .models import Uni
from django.views import generic
from . import models, forms
from .decorators import allowed_users
from .filters import UniFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import  authenticate, login, logout
from django.contrib import  messages
from django.contrib.auth.decorators import login_required





# вызов сайта с рейтингом
def form(request):
    uni = Uni.objects.all()

    myFilter = UniFilter(request.GET, queryset=uni) #Добавление фильтрации(поиска)
    uni = myFilter.qs
    return render(request, "Main.html", {"uni": uni, "myFilter": myFilter})


@login_required(login_url='/login/')
@allowed_users(allowed_roles=['admin'])
def AdminForm(request):
    uni = Uni.objects.all()
    return render(request, "AdminMain.html", {"uni": uni})


# вызов главного сайта
def index(request):
    return render(request, "Uni_rate.html")


# просмотр полной информации о университете
class UniView(generic.DetailView):
    template_name = "Uni_Detail.html"

    def get_object(self, **kwargs):
        UniID = self.kwargs.get("id")
        return get_object_or_404(models.Uni, id=UniID)


# тестовый сервер
def test(request):
    return render(request, "Test.html  ")


# Создание Университета
@login_required(login_url='/login/')
@allowed_users(allowed_roles=['admin'])
class AddUni(generic.CreateView):
    template_name = "add_uni.html"
    form_class = forms.UniViewForm
    queryset = models.Uni.objects.all()
    success_url = "Main/AdminMain/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(AddUni, self).form_valid(form=form)


# Изменение Информации Университета
@login_required(login_url='/login/')
@allowed_users(allowed_roles=['admin'])
class UniUpdate(generic.UpdateView):
    template_name = "Uni_Update.html"
    form_class = forms.UniViewForm
    success_url = "/Main/AdminMain"

    def get_object(self, **kwargs):
        Uni_Id = self.kwargs.get("id")
        return get_object_or_404(models.Uni, id=Uni_Id)

    def form_valid(self, form):
        return super(UniUpdate, self).form_valid(form=form)


# Удаление Модели Университета
@login_required(login_url='/login/')
@allowed_users(allowed_roles=['admin'])
class UniDelete(generic.DeleteView):
    template_name = "Uni_delete.html"
    success_url = "/Main/AdminMain"

    def get_object(self, **kwargs):
        Uni_Id = self.kwargs.get("id")
        return get_object_or_404(models.Uni, id=Uni_Id)

#необходимость логина в админ панель
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('AdminMain')
        else:
            messages.info(request, 'Username Or password is incorrect')
    context = {}
    return render(request, 'login.html', context)

#logout
def logoutUser(request):
    logout(request)
    return redirect('Main')





