from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
 
    def __str__(self):
        return self.name


class MaleManager(models.Manager):
	def get_queryset(self):
		return super(MaleManager, self).get_queryset().filter(sex='M')

class FemaleManager(models.Manager):
	def get_queryset(self):
		return super(FemaleManager, self).get_queryset().filter(sex='F')

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    sex = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    birthd = models.DateField()
    people = models.Manager()
    men = MaleManager()
    women = FemaleManager()
 
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

 
class BookManager(models.Manager):
	def title_count(self, keyword):
		return self.filter(title__icontains=keyword).count()


class NameBookManager(models.Manager):
	def get_queryset(self):
		return super(NameBookManager, self).get_queryset().filter(author='first_name1 last_name1')


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    num_pages = models.IntegerField(blank=True, null=True)
    objects = BookManager()
    nameobjects = NameBookManager()
 
    def __str__(self):
        return self.title


def make_publisher():
	for i in range(20):
		name = 'Name {}'.format(i)
		address = 'Address {}'.format(i)
		state = 'state {}'.format(i)
		country = 'country {}'.format(i)
		website = 'http://www{}.example.com'.format(i)

		Publisher.objects.create(name=name, address=address, state=state, country=country, website=website)



def make_author():
	for i in range(20):
		first_name = 'first_name {}'.format(i)
		last_name = 'last_name {}'.format(i)
		email = 'email{}@example.com'.format(i)

		Author.objects.create(first_name=first_name, last_name=last_name, email=email)

