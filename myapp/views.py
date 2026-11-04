from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home_page.html')

def about(request):
    return render(request, 'about.html')

def products(request):
    age = 65
    weight = 80
    subject = ["Maths", "Science", "Engineering"]
    isDisabled = False
    name = "Tim Wang"

    data ={
        "age": age,
        "weight": weight,
        "subject": subject,
        "isDisabled": isDisabled,
        "name": name
    }

    return render(request, 'products.html', data)

