from django.shortcuts import render
from  . import plots
from personal.models import *

def index(request):
    rep0 = Reporter.objects.all()[0]
    rep1 = Reporter.objects.all()[1]
    # line_bibi_plot = plots.line_table({0:[rep0,"Bibi"], 1:[rep1,"Bibi"]}) # for the Bibi-line-plot-demo
    tu = [rep0, rep1]
    print("tu-> ", tu)
    bubbles = plots.bubble_trendencies_plot([rep0, rep1])
    return render(request, 'personal/home.html', {'demo_bubbles':plots.bubble_demo(), 'my_plot':bubbles})

def contact(request):
    return render(request, 'personal/basic.html', {'info':["if you want to contact me, please email me", "tomer", "tomer.solomon1@gmail.com"]})