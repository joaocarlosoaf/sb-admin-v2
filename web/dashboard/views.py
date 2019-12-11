from django.shortcuts import render

# Create your views here.

def IndexView(request):
    return render(request, 'components/index.html')

def BlankView(request):
    return render(request, 'components/blank.html')

def ButtonsView(request):
    return render(request, 'components/buttons.html')

def FlotView(request):
    return render(request, 'components/flot.html')

def FormsView(request):
    return render(request, 'components/forms.html')

def GridView(request):
    return render(request, 'components/grid.html')

def IconsView(request):
    return render(request, 'components/icons.html')

def LoginView(request):
    return render(request, 'components/login.html')

def MorrisView(request):
    return render(request, 'components/morris.html')

def NotificationsView(request):
    return render(request, 'components/notifications.html')

def PanelsView(request):
    return render(request, 'components/panels-wells.html')

def TablesView(request):
    return render(request, 'components/tables.html')

def TypographyView(request):
    return render(request, 'components/typography.html')