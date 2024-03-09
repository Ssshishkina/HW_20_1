from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Product, Blog


class HomeView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    context = {
        'title': 'contact'
    }
    return render(request, 'catalog/contacts.html', context)


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'image')
    success_url = reverse_lazy('catalog:blg')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'image', 'is_published')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('catalog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blg')


def toggle_published(request, pk):
    publication_item = get_object_or_404(Blog, pk=pk)
    if publication_item.is_published:
        publication_item.is_published = False
    else:
        publication_item.is_published = True

    publication_item.save()

    return redirect(reverse_lazy('catalog:blg'))
