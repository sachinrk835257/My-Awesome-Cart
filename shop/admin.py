from django.contrib import admin

from .models import product, contact, yourCart, Order, orderUpdate, demo   # inheritance
# Register your models here.

# display the columns as we want to display in django administration
class productAdmin(admin.ModelAdmin):
    list_display = ("product_name","category","pub_date")

class orderAdmin(admin.ModelAdmin):
    list_display = ("order_id","name","email","item_json")

class orderUpdateAdmin(admin.ModelAdmin):
    list_display = ("order_id","update_desc","timeStamp")

admin.site.register(product, productAdmin)       #admin.site.register(<modelName>,[<ModelAdmin>])
admin.site.register(contact)
admin.site.register(yourCart)
admin.site.register(Order, orderAdmin)
admin.site.register(orderUpdate, orderUpdateAdmin)
admin.site.register(demo)
