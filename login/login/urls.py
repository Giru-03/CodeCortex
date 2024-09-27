
from django.contrib import admin
from django.urls import path, include
from accounts.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/user/register/', CreateUserView.as_view(), name='register'),
    path('accounts/token/', TokenObtainPairView.as_view(), name='get_token'),
    path('accounts/token/refresh/',TokenRefreshView.as_view(), name='refresh'),
    path('accounts-auth/', include('rest_framework.urls')),
    path("accounts/", include("accounts.urls")),

    # path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # path('dj-rest-auth/registration/account-confirm-email/<str:key>', email_conformation),
    # path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    # path('reset/password/confirm/<int:uid>/<str:token>',reset_password_confirm, name="password_reset_confirm"),
]
