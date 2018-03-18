from django.db import models
from django.contrib.auth.models import User


# GENRE_CHOICES = (
# 	('Fantasy'),
# 	('Horror'),
# 	('Pulp fiction'),
# 	('Historycal'))

class Author(models.Model):
	writer = models.CharField(max_length=200)

	def __str__(self):
		return self.writer

class Book(models.Model):
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	title = models.CharField(max_length=250)
	genre = models.CharField(max_length=50)
	description = models.TextField()
	year = models.IntegerField()
	cover = models.CharField(max_length=1000)

	def __str__(self):
		return self.title + ' (' + str(self.year) + ')'

class Comment(models.Model):
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	comment_text = models.CharField(max_length=500)
	user_name = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.comment_text