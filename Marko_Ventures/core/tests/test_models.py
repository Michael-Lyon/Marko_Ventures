from django.test import TestCase

from core.models import Item


class TestModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Items to be created for the tests methods
        Item.objects.create(
            title="Pigs",
            description="A nice good puk meat",
            category="A",
            slug=1
        )

        Item.objects.create(
            title="Carrot",
            description="A very nice crop that has a lot of health benefits",
            category="C",
            slug=2
        )

    def testTitle_Label(self):
        item = Item.objects.get(id=1)
        field_label = item._meta.get_field("title").verbose_name
        self.assertEquals(field_label, "title")

        # return super().setUpTestData()(self):

    def testDescription_Label(self):
        item = Item.objects.get(id=2)
        field_label = item._meta.get_field("description").verbose_name
        self.assertEquals(field_label, "description")

    def testImage_Label(self):
        item = Item.objects.get(id=1)
        field_label = item._meta.get_field("image").verbose_name
        self.assertEquals(field_label, "image")

    def testDate_Label(self):
        item = Item.objects.get(id=1)
        field_label = item._meta.get_field("date_created").verbose_name
        self.assertEquals(field_label, "date created")

    def test_date_wasAutoAdded(self):
        item = Item.objects.get(id=2)
        date_value = item.date_created
        self.assertTrue(date_value)

    def test_slug(self):
        item = Item.objects.get(id=2)
        slug_value = item.slug
        self.assertTrue(slug_value)

    def test_string_return_of_item(self):
        item = Item.objects.get(id=2)
        item1 = Item.objects.get(id=1)

        expected_display1 = f"{item.title}==================================>>>{item.date_created}"
        expected_display2 = f"{item1.title}==================================>>>{item1.date_created}"

        self.assertEquals(expected_display1, str(item))
        self.assertEquals(expected_display2, str(item1))

    def test_absolute_url_item_with_id1(self):
        item = Item.objects.get(id=1)
        slg = str(item.slug)
        self.assertEquals(item.get_absolute_url(), f'/product/{slg}/')

    def test_absolute_url_item_with_id2(self):
        item = Item.objects.get(id=2)
        slg = str(item.slug)
        self.assertEquals(item.get_absolute_url(), f'/product/{slg}/')
        
    
