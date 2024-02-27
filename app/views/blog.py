from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from app.forms import CommentModelForm
from app.models import Blog, Comment


def blogs_view(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, per_page=6)
    page_number = request.GET.get('page')
    blogs_list = paginator.get_page(page_number)
    return render(request=request, template_name='app/blog.html',
                  context={'blogs': blogs_list})


def blog_details_view(request, blog_id):
    if request.method == 'POST':
        form = CommentModelForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = get_object_or_404(klass=Blog, id=blog_id)
            comment.save()
            return redirect('blog_details', blog_id)
    form = CommentModelForm()
    blogs = Blog.objects.all()
    blog = get_object_or_404(klass=Blog, id=blog_id)
    comments = Comment.objects.filter(blog_id=blog_id).order_by('-created_at')[:3]
    return render(request=request, template_name='app/blog_details.html',
                  context={'blogs': blogs,
                           'blog': blog,
                           'form': form,
                           'comments': comments})
