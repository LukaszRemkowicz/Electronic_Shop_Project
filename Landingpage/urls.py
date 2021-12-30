
from django.urls import path
from . import views


urlpatterns = [
    path('', views.LandingPage.as_view(), name='landing-page'),
    path('delivery', views.DeliveryPage.as_view(), name='delivery'),
    path('installments', views.InstallmentsPage.as_view(), name='installments'),
    path('insurance', views.InsurancePage.as_view(), name='insurance'),
    path('assembly', views.AssemblyPage.as_view(), name='assembly'),
    path('returns-and-complaints', views.ReturnsComplaintsPage.as_view(), name='returns-and-complaints'),
    path('frequently-asked-questions', views.FrequentlyQuestionsPage.as_view(), name='frequently-asked-questions'),
    path('about', views.AboutPage.as_view(), name='about'),
    path('regulations', views.RegulationsPage.as_view(), name='regulations'),
    path('privacy-policy', views.PrivacyPolicyPage.as_view(), name='privacy-policy'),
    path('career', views.CareerPage.as_view(), name='career'),
    path('contact', views.ContactPage.as_view(), name='contact'),

]
