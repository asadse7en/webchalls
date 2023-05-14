from django.shortcuts import render

def headar_easy(request):
    if request.META.get('HTTP_GETFLAG') == 'yes':
        context = {
            'flag': 'aupCTF{cust0m-he4d3r-r3qu3st}',
        }
        
        return render(request, 'aa/flag.html', context)
    
    return render(request, 'aa/index.html')
