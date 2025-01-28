from django.shortcuts import render, get_object_or_404, redirect
from .models import Product,Commande

def home(request):
    search_query = request.GET.get('search', '')  # Récupérer le terme de recherche depuis la requête GET
    
    if search_query:
        products = Product.objects.filter(name__icontains=search_query)  # Recherche insensible à la casse
    else:
        products = Product.objects.all()  # Si aucun terme de recherche, afficher tous les produits
    
    return render(request, 'store/home.html', {'products': products, 'search_query': search_query})

def product_detail(request, product_id):
    # Affiche les détails d'un produit
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})

def panier(request):
    # Affiche les produits dans le panier et calcule le total
    cart = request.session.get('cart', [])
    total = sum(item['price'] * item['quantity'] for item in cart)  # Calcul du total
    products = Product.objects.all()  # Liste tous les produits disponibles
    if request.method=="POST":
        items = request.POST.get('items')
        nom = request.POST.get('nom')
        email= request.POST.get('email')
        telephone= request.POST.get('telephone')
        address= request.POST.get('address')
        ville= request.POST.get('ville')
        pays= request.POST.get('pays')
        zipcode= request.POST.get('zipcode')
        com=Commande(items=items,nom=nom,email=email,telephone=telephone,address=address,ville=ville,pays=pays,zipcode=zipcode)
        com.save()
        
    return render(request, 'store/panier.html', {'cart': cart, 'total': total, 'products': products})
def confirmation(request):
    info =Commande.objects.all()[:1]
    for item in info :
        nom= item.nom
    
    return render(request, 'confirmation.html', {'name':nom})

def add_to_cart(request, product_id):
    # Ajoute un produit au panier
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', [])

    # Vérifie si le produit est déjà dans le panier
    product_in_cart = next((item for item in cart if item['id'] == product.id), None)
    
    if product_in_cart:
        product_in_cart['quantity'] += 1  # Augmente la quantité si le produit est déjà dans le panier
    else:
        cart.append({
            'id': product.id,
            'name': product.name,
            'price': float(product.price),
            'quantity': 1,
        })

    request.session['cart'] = cart  # Enregistre le panier dans la session
    return redirect('panier')  # Redirige vers la page du panier

def remove_from_cart(request, product_id):
    # Supprime un produit du panier
    cart = request.session.get('cart', [])
    cart = [item for item in cart if item['id'] != product_id]  # Retire le produit du panier
    request.session['cart'] = cart  # Enregistre le panier mis à jour dans la session
    return redirect('panier')  # Redirige vers la page du panier
# Vue pour afficher la page de remerciement
def remerciement(request):
    return render(request, 'remerciement.html')