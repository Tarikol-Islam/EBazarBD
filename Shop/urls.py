"""
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='ShopHome'),
    path('search/',views.search,name='Search'),
    path("productdetails/<int:RequiredProductID>",views.productdetails,name='ProductDetails'),
    path('orders/',views.orders,name='YourOrders'),
    path('yourprofile/',views.profile,name='YourProfile'),
    path('contact/',views.contact,name='ContactUs'),
    path('about/',views.about,name='AboutUs'),
]