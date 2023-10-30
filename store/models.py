from django.db import models
from django.shortcuts import reverse,redirect

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    price=models.IntegerField(default=123, null=True)
    image=models.CharField(max_length=200,null=True)
    in_stock=models.CharField(
        choices=[('y','Yes'), ('n','No')]
    )

    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    def __str__(self) :
        return f'{self.title}'
    
    def get_image(self):
        return f'/static/store/images/{self.image}'
    

    def more_details(self):
        url=reverse('detail', args=(self.id,))
        return url
    def go_back(self):
         url = reverse('index_db')
         return redirect(url)
    


    def delete_product(self):
        url=reverse('delete', args=[self.id])
        return url
          
     

