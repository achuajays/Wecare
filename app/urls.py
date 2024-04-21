from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import home , transcribe_audio , upload_file , docdet , emrgy ,  emo , search_donor , save_bug_report_with_detail ,  save_bug_report , display_doctor , display_doctor_form , display_doctor_inquiry , helbo   , user_login ,logout_user ,  register 
from django.views.generic import TemplateView

urlpatterns = [
    path('', home, name='home'),
    path('streamlit/', TemplateView.as_view(template_name='app/streamlit.html'), name='streamlit'),
    path('transcribe_audio', transcribe_audio, name='transcribe_audio'),
    path('upload_file', upload_file, name='upload_file'),
    path('docdet', docdet, name='docdet'),
    path('emo', emo, name='emo'),
    path('search_donor', search_donor, name='search_donor'),
    path('display_doctor', display_doctor, name='display_doctor'),
    path('display_doctor_form/<int:pk>', display_doctor_form, name='display_doctor_form'),
    path('display_doctor_inquiry/<int:pk>', display_doctor_inquiry, name='display_doctor_inquiry'),
    path('helbo', helbo, name='helbo'),
    path('emrgy', emrgy, name='emrgy'),
    path('save_bug_report', save_bug_report, name='save_bug_report'),
    path('save_bug_report_with_detail', save_bug_report_with_detail, name='save_bug_report_with_detail'),
    path('user_login', user_login, name='user_login'),
    path('register', register, name='register'),
    path('logout_user', logout_user, name='logout_user'),


    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
