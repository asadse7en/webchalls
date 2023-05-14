from django.shortcuts import render

def index(request):
    page_links = []
    for i in range(1, 1001):
        page_links.append({
            'page_id': i,
            'url': f'/dir/page/{i}/',
            'text': f'Page {i}',
        })
    return render(request, 'index.html', {'page_links': page_links})


def page(request, page_id):
    if page_id == 712:
        context = {'flag': 'aupCTF{d1r3ct0r13s-tr1v14l-fl4g}'}
        return render(request, 'flag.html', context)
    else:
        return render(request, 'nopage.html')
