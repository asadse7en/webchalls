from django.shortcuts import render

from django.shortcuts import render

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        admin = request.POST.get('admin')

        # Check if username and password are correct
        if username == 'starlord69' and password == '1A8$5k7!eR':
            if admin == 'true':
                return render(request, 'adminflag.html')
            else:
                return render(request, 'success.html')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials. Please try again.'})

    return render(request, 'login.html')


def user_view(request):
    usernames = ["ironman07", "spidey91", "wakanda4ever", "hulksmash99", "marvelcaptain", "thorhammer23", "blackwidow007", "deadpoolfanatic", "xmenmutant55", "scarletwitch23", "starlord69", "strangewizard", "pantherking", "captainamerica1776", "grootlover88", "antman42", "lokiobsessed9", "hawkeyearcher007", "thanosfollower13", "wandafor3v3r"]
    return render(request, 'usernames.html', {'usernames': usernames})

def password_view(request):
    passwords = ['6!7A3O9?b&', '4H0.b@2E5W', '8z^3@9b1#J', '1T9g$8y0D!', '7N1R$6u5q%', '2C1!f9R6r$', '0J2y&9m5B%', '4W9B^7b2g#', '9m3H%5y7t@', '1A8$5k7!eR', '7U4v@6Q9h*', '9O6p#1d3@Q', '5K8x*2v1@Q', '2L5i!9t0^Q', '3J4G&1k7X!', '4M6s$2j1r*', '8X1w@5G3u#', '6C8z^0m3B!', '7D1#f5w3S^', '9Y3r$0t6A!']
    return render(request, 'passwords.html', {'passwords': passwords})
