from django.shortcuts import render

from django.shortcuts import render

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        admin = request.POST.get('admin')

        # Check if username and password are correct
        if username == 'asad' and password == 'asad':
            if admin == 'true':
                return render(request, 'success.html', {'message': 'Congratulations! You have logged in as admin. Here is your flag: FLAG{...}'})
            else:
                return render(request, 'success.html', {'message': 'Login successful! Login as Admin to get the flag'})
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials. Please try again.'})

    return render(request, 'login.html')


def user_view(request):
    usernames = ['asad', 'bilal', 'inam']  # Add your desired usernames here
    return render(request, 'usernames.html', {'usernames': usernames})

def password_view(request):
    passwords = ['asad', 'bilal', 'inam']  # Add your desired passwords here
    return render(request, 'passwords.html', {'passwords': passwords})
