from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from app.forms import CommentModelForm, BookingModelForm
from app.models.blog import Blog, Comment


def blogs_view(request):
    if request.method == 'POST':
        form = BookingModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = BookingModelForm()
    blogs = Blog.objects.order_by('-created_at').all()
    paginator = Paginator(blogs, per_page=6)
    page_number = request.GET.get('page')
    blogs_list = paginator.get_page(page_number)
    return render(request=request, template_name='app/blog.html',
                  context={'blogs': blogs_list,
                           'form': form})


def blog_details_view(request, blog_id):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'form1':
            form = CommentModelForm(data=request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.blog = get_object_or_404(klass=Blog, id=blog_id)
                comment.save()
                return redirect('blog_details', blog_id)

        elif form_type == 'form2':
            form = BookingModelForm(data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
    form = CommentModelForm()
    blogs = Blog.objects.all()
    blog = get_object_or_404(klass=Blog, id=blog_id)
    comments = Comment.objects.filter(blog_id=blog_id).order_by('-created_at')[:3]
    return render(request=request, template_name='app/blog_details.html',
                  context={'blogs': blogs,
                           'blog': blog,
                           'form': form,
                           'comments': comments})
