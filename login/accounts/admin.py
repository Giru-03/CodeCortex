from django.contrib import admin






# from django.contrib.auth.admin import UserAdmin
# from django.utils.translation import gettext_lazy as _
# from .models import CustomUserModel

# class UserAdminCustom(UserAdmin):
#     fieldsets = (
#         (None , {'fields': ('email','password')}),
#         (_('Personal info'), {'fields': ('first_name', 'last_name','gender')}),
#         (
#             _('Permissions'),
#             {
#                 'fields': (
#                     'is_active',
#                     'is_staff',
#                     'is_superuser',
#                     'groups',
#                     'user_premission',
#                 ),
#             },
#         ),
#         (_('Important dates'), {'fields': ('last_login','date_joined')}),
#     )
#     add_fieldsets = (
#         (
#             None,
#             {'classes': ('wide',), 'fields':('first_name','last_name','email','password1', 'password2','gender'),},
#         ),
#     )
#     list_display = ('email','first_name', 'last_name','gender', 'is_staff')
#     search_fields = ('first_name','last_name','email')
#     ordering = ('email',)
#     readonly_fields = ['date_joined', 'last_login']

# admin.site.register(CustomUserModel, UserAdminCustom)


