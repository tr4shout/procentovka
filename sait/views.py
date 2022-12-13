from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Uni
from django.views import generic
from . import models, forms
from .decorators import allowed_users
from .filters import UniFilter


# вызов сайта с рейтингом
def form(request):
    uni = Uni.objects.all()

    myFilter = UniFilter(request.GET, queryset=uni) #Добавление фильтрации(поиска)
    uni = myFilter.qs
    return render(request, "Main.html", {"uni": uni, "myFilter": myFilter})


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
class AddUni(generic.CreateView):
    template_name = "add_uni.html"
    form_class = forms.UniViewForm
    queryset = models.Uni.objects.all()
    success_url = "/Main/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(AddUni, self).form_valid(form=form)


# Изменение Информации Университета
class UniUpdate(generic.UpdateView):
    template_name = "Uni_Update.html"
    form_class = forms.UniViewForm
    success_url = "/Main/"

    def get_object(self, **kwargs):
        Uni_Id = self.kwargs.get("id")
        return get_object_or_404(models.Uni, id=Uni_Id)

    def form_valid(self, form):
        return super(UniUpdate, self).form_valid(form=form)


# Удаление Модели Университета
class UniDelete(generic.DeleteView):
    template_name = "Uni_delete.html"
    success_url = "/Main/"

    def get_object(self, **kwargs):
        Uni_Id = self.kwargs.get("id")
        return get_object_or_404(models.Uni, id=Uni_Id)


