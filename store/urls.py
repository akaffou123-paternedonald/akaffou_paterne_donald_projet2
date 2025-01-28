from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),  # Page d'accueil avec recherche
    path('produit/<int:product_id>/', views.product_detail, name='product_detail'),  # Détails d'un produit
    path('panier/', views.panier, name='panier'),  # Affichage du panier
    path('ajouter-au-panier/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  # Ajouter un produit au panier
    path('supprimer-du-panier/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),  # Supprimer du panier
     path('confirmation/', views.confirmation, name='confirmation')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)