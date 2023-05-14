from django.shortcuts import render

def sqli_easy(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        vulnerable_strings = [
            "OR1=1",
            "or1=1",
            "OR 1=1",
            "or 1=1",
            "-- or 1=1'",
            "-- OR 1=1'",
            "-- or 1 = 1'",
            "-- OR 1 = 1'",
            "-- or 1=1",
            "-- OR 1=1",
            "-- or 1 = 1",
            "-- OR 1 = 1",
            "' OR '1",
            "' OR 1 -- -",
            "\" OR \"\" = \"",
            "\" OR 1 = 1 -- -",
            "' OR '' = '",
        ]

        if any(s in username or s in password for s in vulnerable_strings):
            return render(request, 'sqli_easy/success.html')
        else:
            return render(request, 'sqli_easy/failure.html')

    return render(request, 'sqli_easy/index.html')

