# LEOS PET STORE
Leo’s Pet Store is an online pet shop focused on providing quality products for dogs. Built as part of my full stack development course, this project showcases a fully functional e-commerce website where users can browse items, securely check out, and more.

The site is developed using Django and Python for the backend, with HTML, CSS, and a touch of JavaScript. I built this site based around my own dog, Leo, who is also featured in the hero image.

Link to the deployed site - [HERE](https://leos-pet-store-e28403e1c3e9.herokuapp.com/)

# UX
## User stories
## As Admin
* As an admin I can manage users accounts so i can make any changes that the user needs me to
* As an admin I want to create/edit/delete products using a form with validation.
* As an admin I want to be alerted when products receive multiple downvotes so that I can review, unlist, or delete them if necessary.
* As an admin I can list or unlist live products if they are out of stock or need reviewing

## As a site user
* As a site user I want to browse products so I can find items I’m interested in.
* As a site user I want to search for a product so I can quickly locate specific items.
* As a site user I want to easily register for an account so I can start shopping quickly.
* As a site user I want to see a clear message if I go to a broken or wrong link, So that I don’t get confused and can find my way back to the site.
* As a site user I want a personalized profile so I can view and manage my details and orders easily.
* As a site user I want to securely pay for my order via Stripe so I can complete my purchase.
* As a site user I want to easily log in and out so I can access my account securely and conveniently.
* As a site user I want to receive a clear message after purchase so I know if it was successful or not.
* As a site user I want to log in to see my order history.
* As a site user I want to add products to my cart so I can purchase multiple items at once.
* As a site user I want to sort the list of available products so I can find what I want faster.
* As a site user I want to sort products within a specific category so I can narrow down my options easily.
* As a site user I want a responsive site so I can use it on different devices.
* As a site user I want to be able to leave reviews on products i buy
* As a site user I want a contact form so i can contact the owners of the site regarding any issues i may have.

## Database

<details>
  <summary>Click here to view my ERD:</summary>

  ![](static/images/erd.png)

</details>

## Design
Wireframes

<details>
<summary>Click here to view Wireframes:</summary>

  ![](static/images/wireframe-homepage.png)
  ![](static/images/wireframe-products.png)
  ![](static/images/wireframe-profile.png)
  ![](static/images/product-management.png)
  ![](static/images/wireframe-newsletter.png)
  ![](static/images/wireframe-contact.png)
 
</details>

## E-commerce type

Leo’s Pet Store is an online store that sells pet products directly to customers. For the owners of the store, the primary goal is to achieve full CRUD functionality to easily manage products, and customer information.

# Features
## Homepage

When you first click the leos pet store url, it takes you to the home page with a shop now button in the middle, my account at the top right and your shopping bag in the top right. with a search bar at the top and various options for the user in the navbar.
### Header and navigation

![header](static/images/header.png)

### The home page

![home](static/images/homepage.png)

### Sign up
For the user to be able to use most of the site, like writing reviews or going through the checkout process they will need to sign in.

![sign up](static/images/signup.png)

### Sign in

People who have registered to the site will need to sign in here

![login](static/images/signin.png)

### Sign out
When users want to sign out

![sign out](static/images/signout.png)

## All products

When the user clicks all products they are met with three options, By price, By category, and view all meaning they can view products in different ways based on their needs

### Sort by price
![by price](static/images/byprice.png)

### Sort by category
![category](static/images/bycategory.png)

### View all
![view all](static/images/viewall.png)

 ### Product detail, add to bag, reviews

Each product on the site has its own product detail area where the user can read about the product and add it to there bag along with an options to leave a review at the bottom

![detail](static/images/product-detail.png)

![add to bag](static/images/add-to-bag.png)

![review](static/images/review.png)