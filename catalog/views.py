from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic import CreateView
from .models import Book, Author, BookInstance, Genre, Person
def other(request):
	return render(request, 'others.html')
def anime(request):
	return render(request, 'anime.html')
def wix(request):
    return render(request, 'wix.html')
def index(request):
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    num_instances_available=BookInstance.objects.filter(status='a').count()
    num_authors=Author.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context={'num_books':num_books,
                'num_instances':num_instances,
                'num_instances_available':num_instances_available,
                'num_authors':num_authors,
                'num_visits': num_visits,
                }
        
    return render(request, 'index.html', context=context)
class loanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from catalog.models import Author

from catalog.forms import RenewBookForm
from django.contrib.auth.decorators import permission_required

@permission_required('catalog.can_mark_returned')
def renew_book_librarian(request, pk):
    book_inst=get_object_or_404(BookInstance, pk=pk)
    if request.method == "POST":
        form = RenewBookForm(request.POST)
        if form.is_valid():
            book_inst.due_back = form.cleaned_data['renewal_date']
            book_inst.save()
            return HttpResponseRedirect(reverse('all_borrowed'))
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date,})
    return render(request, 'catalog/book_renew_librarian.html', {'form':form, 'book_inst':book_inst})

class AuthorCreate(CreateView):
        model = Author
        fields = '__all__'
        initial = {'date_of_death': '05/01/2018'}
class AuthorUpdate(UpdateView):
        model = Author
        fields =  ['first_name','last_name','date_of_birth','date_of_death']
class AuthorDelete(DeleteView):
        model = Author
        success_url = reverse_lazy('authors')
def wix1(request):
    return render(request, 'wix1.html')
