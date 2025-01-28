from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) 
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.name
class Commande(models.Model):
    items= models.CharField(max_length=300)
    nom = models.CharField(max_length=150)
    email= models.EmailField()
    telephone=models.CharField(max_length=14)
    address = models.CharField(max_length=255, blank=True, null=True)

    ville= models.CharField(max_length=200)
    pays=models.CharField(max_length=300)
    zipcode=models.CharField(max_length=300)
    date_commande= models.DateTimeField(auto_now=True)
    class Meta:
        ordering=['-date_commande']
        
        def __str__(self):
            return self.nom
        
    
