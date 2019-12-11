from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    #path('editar_contrato/<int:id>', v.editar_contrato, name='editar_contrato'),
    path('', views.LoginView, name="login"),
    path('index/', views.IndexView, name="index"),
    path('blank/', views.BlankView, name="blank"),
    path('buttons/', views.ButtonsView, name="buttons"),
    path('flot/', views.FlotView, name="flot"),
    path('forms/', views.FormsView, name="forms"),
    path('grid/', views.GridView, name="grid"),
    path('icons/', views.IconsView, name="icons"),
    path('morris/', views.MorrisView, name="morris"),
    path('notifications/', views.NotificationsView, name="notifications"),
    path('panels/', views.PanelsView, name="panels"),
    path('tables/', views.TablesView, name="tables"),
    path('typography/', views.TypographyView, name="typography"),

]