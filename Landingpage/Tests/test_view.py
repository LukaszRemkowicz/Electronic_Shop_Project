# from django.http import response
# from django.test import TestCase, Client
# from django.urls import reverse


# class ViewTests(TestCase):

#     def setUp(self) -> None:
#         self.client = Client()


#     def test_landing_page(self):
#         """ Test if landing page is rendering
#         when no products in database """

#         url = reverse('landing-page')
#         res = self.client.get(url)

#         self.assertEqual(res.status_code, 200)
#         self.assertTemplateUsed(res, 'Landingpage/landing_page.html')
