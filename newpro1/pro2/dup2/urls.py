# from . import views
# from django . urls import path

# urlpatterns = [
#     path('',views.SignupPage,name='signup'),
#     path('login/',views.LoginPage,name='login'), 
#     path('logout/',views.LogoutPage,name='logout'),
#     path('home/',views.HomePage,name='home'),
#     path('home/saveform', views.savedemo),
#     path('home/display/', views.displaydata, name='display'),
#     # path('display', views.displaydata),
#     path('edit/<int:id>', views.edit),
#     path('update/<int:id>', views.updatedata),
#     path('delete/<int:id>', views.deletedata),

# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'), 
    path('logout/', views.LogoutPage, name='logout'),
    path('home/', views.HomePage, name='home'),
    path('home/display/saveform',views.HomePage),
    path('home/saveform', views.savedemo, name='saveform'),  # Add a trailing slash
    path('home/display/', views.displaydata, name='display'),  # Add a trailing slash
    path('edit/<int:id>', views.edit, name='edit'),  # Add a trailing slash
    path('update/<int:id>', views.updatedata, name='update'),  # Remove leading slash
    path('delete/<int:id>', views.deletedata, name='delete'),  # Remove leading slash
]


# <form method="post" action="{% url 'saveform' %}">
#     <!-- Form fields go here -->
#     <button type="submit">Save</button>
# </form>
