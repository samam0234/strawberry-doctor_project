from django.shortcuts import render
from django.templatetags.static import static

# Create your views here.
# ------------------------- 홈 페이지(index.html) ---------------------------------

def home(request) :

    context = {
        'gradcam_image': static('image/strawberry_gradCam_image.PNG'),
        'gradcam1' : static('image/gradcam1.jpg'),
        'gradcam2' : static('image/gradcam2.jpg'),
        'gradcam3' : static('image/gradcam3.jpg'),
        'gradcam4' : static('image/gradcam4.jpg'),
        'gradcam5' : static('image/gradcam5.jpg'),
        'gradcam6' : static('image/gradcam6.jpg'),
    }

    return render(request, 'index.html', context)

# ---------------------------------------------------------------------

# ------------------------- 진단 페이지(training.html) ---------------------------------

def strawberry_training(request) :
    return render(request, 'strawberry/training.html')

# ---------------------------------------------------------------------

# ------------------------- 기록 페이지(history.html) ---------------------------------

def strawberry_history(request) :
    return render(request, 'strawberry/history.html')

# ---------------------------------------------------------------------

# ----------------------- 내 농장 페이지(myfarm.html) -------------------------------

def strawberry_myfarm(request) :
    return render(request, 'strawberry/myfarm.html')

# ---------------------------------------------------------------------

# ------------------------- 보고서 페이지(report.html) ---------------------------------

def strawberry_report(request) :
    return render(request, 'strawberry/report.html')

# ---------------------------------------------------------------------