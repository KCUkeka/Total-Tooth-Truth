from django.shortcuts import render, HttpResponse, redirect


def main(request):
    return render(request, 'home.html')

def guide_k2(request):
    return render(request, 'guide_k2.html')

def guide_35(request):
    return render(request, 'guide_35.html')

def guide_68(request):
    return render(request, 'guide_68.html')

def guide_high(request):
    return render(request, 'guide_high.html')

def contact_us(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             sender_name = form.cleaned_data['name']
#             sender_email = form.cleaned_data['email']
#             message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
#             send_mail('New Enquiry', message, sender_email, ['enquiry@exampleco.com'])
#             return HttpResponse('Thanks for contacting us!')
#     else:
#         form = ContactForm()

# add {'form': form} in render after html file
    return render(request, 'contact_us.html')


def test_k2(request):
    return render(request, 'posttest_k2.html')

def test_35(request):
    return render(request, 'posttest_35.html')

def test_68(request):
    return render(request, 'posttest_68.html')

def test_high(request):
    return render(request, 'posttest_high.html')

def brushing(request):
    return render(request, 'brushing.html')

def flossing(request):
    return render(request, 'flossing.html')

def field_trip(request):
    return render(request, 'field_trip.html')

def fun_color(request):
    return render(request, 'fun_color.html')

def fun_video(request):
    return render(request, 'fun_video.html')

def fun_games(request):
    return render(request, 'fun_games.html')

def fun_experiments(request):
    return render(request, 'fun_experiments.html')
