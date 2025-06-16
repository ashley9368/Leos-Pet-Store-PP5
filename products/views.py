from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, ProductVote

from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm


# View to show all products, including sorting, filtering and searching
def all_products(request):
    """View to show all products, including sorting and search queries """

    # Only show visible products to regular users, But show all the super users, regardless of listed or not
    products = Product.objects.filter(is_visible=True) if not request.user.is_superuser else Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    # Handle sorting
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            # Check if direction is descending
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
        
        # Handle category filtering
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)


        # Handle search queries
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """View to show individual product details and handle reviews."""
    product = get_object_or_404(Product, pk=product_id)
    # Get all reviews for this product, newest first
    reviews = product.reviews.all().order_by('-created_at')

    # If the form was submitted, process the review form
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, 'Your review was submitted successfully.')
            return redirect('product_detail', product_id=product.id)
        else:
            messages.error(request, 'There was an error with your review. Please check the form.')
    else:
        # If just viewing the page, show an empty form
        form = ReviewForm()

    context = {
        'product': product,
        'reviews': reviews,
        'form': form,
    }

    return render(request, 'products/product_detail.html', context)

@login_required
def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))

@login_required
def toggle_visibility(request, pk):
    """Allow is_visible on a product and send you back where you came from"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect('home')
    
    product = get_object_or_404(Product, pk=pk)
    product.is_visible = not product.is_visible
    product.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def delete_review(request, review_id):
    """Delete a review if user is owner or superuser."""
    review = get_object_or_404(Review, pk=review_id)
    
    # Check if user is the review creator or superuser, if yes, delete.
    if request.user == review.user or request.user.is_superuser:
        review.delete()
        messages.success(request, "Review deleted successfully.")
    # If not, then dont allow
    else:
        messages.error(request, "You do not have permission to delete this review.")
    
    return redirect('product_detail', product_id=review.product.id)

@login_required
def vote_product(request, product_id, vote_type):
    product = get_object_or_404(Product, pk=product_id)

    # Make sure vote_type is 'U' or 'D'
    if vote_type not in (ProductVote.UP, ProductVote.DOWN):
        messages.error(request, "Invalid vote.")

    else:
        # Try to get the users vote if none, create one with vote_type
        vote, created = ProductVote.objects.get_or_create(
            product=product, user=request.user,
            defaults={'vote_type': vote_type}
        )

        if not created:
            # clicking vote again removes it
            if vote.vote_type == vote_type:
                vote.delete()
            # If they switch vote type, update and save
            else:
                vote.vote_type = vote_type
                vote.save()
    #Take user back to where they were, if it fails then go to products
    return redirect(request.META.get('HTTP_REFERER', 'products'))