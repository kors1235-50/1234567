import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm
from .models import BookInstance

class RenewBookForm(forms.Form):
	def clean_renewal_date(self):
		date = self.cleaned_date['due_back']
		if date < datetime.date.today():
			raise ValidationError(_('Invalid date - renewal in past'))
		if date > datetime.date.today() + datetime.timedelta(weels=4):
			raise ValodationError(_('Invalid date - renewal more than 9 week ahead'))
		return date
	class Meta:
                 model = BookInstance
                 fields = ['due_back']
                 labels = {'due_back':_('Renewal date'),}
                 help_text = {'due_back':_('Enter a date between now and 4 week (default 3).'),}

