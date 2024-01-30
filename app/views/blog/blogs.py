from django.shortcuts import render


def blogs_view(request):
    return render(request=request, template_name='app/blog.html')
