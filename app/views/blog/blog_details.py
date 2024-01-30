from django.shortcuts import render


def blog_details_view(request):
    return render(request=request, template_name='app/blog_details.html')
