from django.shortcuts import render

# Create your views here.
# ##########################################################################
#
# Shop
# 	Categories
# 	Search Fiters
# 		Price Range | Color | Brands
# 	Product Gallery
# 	Recently Viewed
#
# ##########################################################################

def shop_by_category(request):
    print("reached shop_by_category")
    return render(request,'shop_by_category.html')

def search_filter(request):
    print("reached search_filter")
    return render(request,'search_filter.html')

def product_gallery(request):
    print("reached product_gallery")
    return render(request,'product_gallery.html')

def recently_viewed(request):
    print("reached recently_viewed")
    return render(request,'recently_viewed.html')


# ##########################################################################
#
# Product
# 	Product Details
# 	Add to Cart
# 	Add to Wishlist
#
# ##########################################################################


def product_detail(request):
    print("reached product_detail")
    return render(request,'product_detail.html')

def add_to_cart(request):
    print("reached add_to_cart")
    return render(request,'add_to_cart.html')

def add_to_wishlist(request):
    print("reached add_to_wishlist")
    return render(request,'add_to_wishlist.html')
