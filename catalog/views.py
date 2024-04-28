from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Blog, Version
from django.contrib.auth.mixins import LoginRequiredMixin
from services import get_products_from_cache


class HomeView(ListView):
    model = Product
    # template_name = 'product_list.html'


def get_queryset(self):
    return get_products_from_cache()


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    products = self.get_queryset()

    for product in products:
        product.versions = Version.objects.filter(product=product)
        product.version = product.versions.filter(working_ver=True).first()

    return context


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        versions = Version.objects.filter(product=product)
        context['versions'] = versions
        working_ver = versions.filter(working_ver=True).first()
        context['working_ver'] = working_ver

        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


def toggle_working_ver(request, pk):
    '''Функция вывода только рабочих версий'''
    version_item = get_object_or_404(Product, pk=pk)
    if version_item.working_ver:
        version_item.working_ver = False
    else:
        version_item.working_ver = True
    version_item.save()

    return redirect(reverse('catalog:home'))


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')


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

    def get_success_url(self, *args, **kwargs):
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
