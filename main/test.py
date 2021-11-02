from django.test import TestCase
from .models import NeighbourHood, Business

# Create your tests here.

class NeighbourhoodTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= NeighbourHood(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')


    def test_instance(self):
        self.assertTrue(isinstance(self.james,NeighbourHood))

    def test_save_method(self):
        self.james.save_post()
        editors = NeighbourHood.objects.all()
        self.assertTrue(len(editors) > 0)


class NewsDetailTestClass(TestCase):
    def setUp(self):
        # Creating a new neighbourhood and saving it
        self.james= NeighbourHood(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_post()

        # adding a bussiness  and saving it
        self.new_tag = Business(name = 'testing')
        self.new_tag.save()

        self.new_article= Business(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
        self.new_article.save()

        self.new_article.author.add(self.new_tag)

    def tearDown(self):
        Business.objects.all().delete()
        Business.objects.all().delete()
        Business.objects.all().delete()