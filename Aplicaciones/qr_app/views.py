from django.shortcuts import render
from .forms import WebPageForm
from .models import WebPage
import qrcode
from django.core.files.base import ContentFile
from django.views.decorators.csrf import csrf_protect
from io import BytesIO
import base64


def generate_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    return img

@csrf_protect
def generate_qr(request):
    if request.method == 'POST':
        form = WebPageForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']

            img = generate_qr_code(url)

            img_byte_array = BytesIO()
            img.save(img_byte_array, format='PNG')

            img_base64 = base64.b64encode(img_byte_array.getvalue()).decode('utf-8')

            return render(request, 'qr_code.html', {'qr_image': img_base64, 'url': url})
    else:
        form = WebPageForm()

    return render(request, 'generate_qr.html', {'form': form})
