from django.urls import path
from . import views

urlpatterns = [
    path("Main/", views.form, name="Main"),  # Ссылка на сайт с рейтингои
    path("", views.index, name=""),  # Главная страница Сайта
    path("Uni_Detail/<int:id>/", views.UniView.as_view(), name="Uni_Detail"),  # Просмотр полной информации о Университете
    path("test/", views.test, name="test"),  # тестовый сайт
]
