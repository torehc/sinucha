from django.contrib import admin
from control.models import User_Data, Balance, Item, Shopping_History, Sale_History

# Register your models here.

class User_DataAdmin(admin.ModelAdmin): 
    list_display = ('tagRfid', 'chatid', 'username', 'balance_actual', 'user', 'rol') 
    search_fields = ('tagRfid', 'chatid')
    list_filter = ('rol',) 
  
class Balance_Admin(admin.ModelAdmin):
    list_display = ('user', 'amount_entered', 'type_amount', 'date')
    
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'barcode', 'price_sale', 'stock')
    search_fields = ('name', 'barcode')
    
class Shopping_HistoryAdmin(admin.ModelAdmin):
    list_display = ('item', 'date', 'units', 'unit_purchase_price', 'supermarket')
    search_fields = ('item', 'supermarket')
  
class Sale_HistoryAdmin(admin.ModelAdmin):
    list_disply = ('item', 'date', 'price_sale', 'price_cost')
  
admin.site.register(User_Data, User_DataAdmin)
admin.site.register(Balance, Balance_Admin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Shopping_History, Shopping_HistoryAdmin)
admin.site.register(Sale_History, Sale_HistoryAdmin)