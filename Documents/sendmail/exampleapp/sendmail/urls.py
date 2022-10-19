from django.urls import path
from sendmail.views import EmailAttachementView

urlpatterns = [
    path('send-email', EmailAttachementView.as_view(), name='emailattachment')
]