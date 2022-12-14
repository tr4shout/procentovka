from django.urls import path
from . import views

urlpatterns = [
    path("Main/", views.form, name="Main"),  # Ссылка на сайт с рейтингои
    path(" ", views.index, name=" "),  # Главная страница Сайта
    path("Uni_Detail/<int:id>/", views.UniView.as_view(), name="Uni_Detail"),  # Просмотр полной информации о Университете
    path("test/", views.test, name="test"),  # тестовый сайт
    path("Main/Login/", views.loginPage, name = "Login") ,# Логин в админ панель
    path('logout', views.logoutUser, name = 'logout'), #Выход с аккаунта
    path('add_uni/', views.AddUni.as_view(), name = 'add_uni'),#Добавление новый моделей Университета
    path('delete_uni/<int:id>/delete', views.UniDelete.as_view(), name = 'Uni_detail'), #Удаление модели
    path('update_uni/<int:id>/update', views.UniUpdate.as_view(), name='Uni_Detail'), #Изменение модели
]
