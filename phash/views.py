from django.shortcuts import render, redirect
from django.contrib import messages
import hashlib
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):

    random_word = 'ghostrider'
    random_md5 = hashlib.md5(random_word.encode('utf-8')).hexdigest()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'admin' and password == random_md5:
            messages.success(request, 'Congratulations! here is your flag: aupCTF{y0u-ar3-a-ha5hcr4ck1ng-m4ch1n3}')
        else:
            messages.error(request, 'Invalid username or password.')


    return render(request, 'phash.html')
