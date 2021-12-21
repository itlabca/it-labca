from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView,PasswordChangeDoneView, PasswordChangeView
from django.urls.conf import include
from core.views import HomeView
from core.urls import core_patterns
from django.conf import settings
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', LoginView.as_view(template_name='core/login.html'), name='login'),
    path('accounts/login/', LoginView.as_view(template_name='core/login.html'), name='login2'),
    path('home/', login_required(HomeView.as_view()), name="home"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_change/', PasswordChangeView.as_view(template_name='core/password_change_form.html'), name='password_change'),
    path('password_change_done/', PasswordChangeDoneView.as_view(template_name='core/password_change_done.html'), name='password_change_done'),

    path('equipos/', include(core_patterns)),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
