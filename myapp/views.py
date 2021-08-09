
from .models import Feature
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
#from  models import Post


#class HomeView(ListView):
    #model = Post
   # template_name = 'Home.html'

def Home(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name ='Technology Arena'
    feature1.details = 'Hardware'

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Social Arena'
    feature2.details = 'Women'

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Financial Arena'
    feature3.details = 'Money'

    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Business Arena'
    feature4.details = 'Enterprenuer'

    feature5 = Feature()
    feature5.id = 4
    feature5.name = 'Fashion Arena'
    feature5.details = 'Women'

    feature6 = Feature()
    feature6.id = 5
    feature6.name = 'Fitness Arena'
    feature6.details = 'Women'

    feature7 = Feature()
    feature7.id = 5
    feature7.name = 'Fitness Arena'
    feature7.details = 'Women'

    features = [feature1, feature2, feature3, feature4, feature5, feature6, feature7]

    return render(request, 'Home.html',{'features': features})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send an email
        send_mail(
            message_name,  # subject
            message,  # message
            message_email,  # from email
            ['the@socrato.com'],  # To Email
        )

        return render(request, 'contact.html', {'message_name': message_name })
    else:
        return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})




