from django.forms import Textarea, ModelChoiceField, ModelForm
from .models import Comment, Author, Book


class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['comment_text']
		widgets = {
            'comment_text': Textarea(attrs={'cols': 80, 'rows': 5}),
        }

class AddAuthorForm(ModelForm):
	class Meta:
		model = Author
		fields = ['writer']

class BookForm(ModelForm):
	author = ModelChoiceField(queryset=Author.objects.all())
	class Meta:
		model = Book
		fields = ['author', 'title', 'genre', 'year', 'cover']