from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="children")
    content = models.TextField()
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True, related_name="products")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    max_buy = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    rating = models.IntegerField()
    reviews = models.IntegerField()
    
    @property
    def average_rating(self):
        if self.reviews > 0:
            return self.rating / self.reviews
        else:
            return "Newly Released!"

    def __str__(self):
        return self.name

