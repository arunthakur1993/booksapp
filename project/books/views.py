from django.views.generic import ListView
from django.shortcuts import render,redirect
from books.models import Book
from books.forms import BookForm,DocumentForm
from django.views.generic.edit import FormView,DeleteView,UpdateView
from django.core.urlresolvers import reverse_lazy


def home(request):
    return render (request,'books/home.html')


def search_form(request):
    return render(request,'books/search.html')


def search_result(request):
    errors = []
    if 'w' in request.GET:
        w = request.GET['w']
        if not w:
            errors.append("Please enter some data to search")
        elif (len(w)>20):
            errors.append('You can enter utmost 20 words')

        else:
            books = Book.objects.filter (title__icontains = w)
            return render (request,'books/results.html', {'books':books,'query': w })

    return render (request, 'books/search.html',{'errors ':errors})


class BookList(ListView):
    model = Book
    template_name= 'books/book_list.html'


def get_name(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return render (request, 'books/thanks.html')
    else:
        form = BookForm()

        return render(request, 'books/update.html',{'form':form})


def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(home)
    else:
        form = DocumentForm()
    return render(request, 'books/upload.html',{'form': form})




class BookUpdate(UpdateView):
    model =Book
    fields = ['title','authors','publication_date','publisher']
    success_url = reverse_lazy('home')

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('home')
