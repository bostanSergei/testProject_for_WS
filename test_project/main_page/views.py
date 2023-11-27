from django.shortcuts import render
from main_page.models import Slider


def index_page(request):
    images = {'image_list': Slider.objects.all()}

    return render(request=request, template_name='index.html', context=images)
