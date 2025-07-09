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

### The shopping bag

The shopping bag shows various important things the user would need, the option to remove or add items from there bag, the quantity of each product, and the total of each product, and a picture and name of the product, then the option to proceed to pay.

![bag](static/images/shopping-bag.png)

### Checkout

On the left side of the checkout is where user puts their information, and on the right side is a summary of their order and the total including delivery.

![checkout](static/images/checkout.png)

### Checkout success

After completing the checkout process, users receive an order confirmation with their details including order number.
![order confirm](static/images/checkout-success-1.png)
![order confirm](static/images/checkout-success-2.png)

### Product detail- super user

If the user is the superuser, they have an option to either delete or edit the product
![detail](static/images/superuser-edit-product.png)

### Product management- add product

Only super users are allowed to add products to the site

![add product](static/images/product-management-superuser.png)
![add product](static/images/product-management-superuser-2.png)

### Product management- edit product

Superusers can edit the product by editing either name, description, category, SKU, price and update image. An alert is also available to remind them what action they are performing. They can then update the changes or cancel. I also added a feature where the superuser can list or unlist any product incase they are out of stock or if the product has recieved bad reviews or what ever reason they want to.

![edit](static/images/edit-product.png)

### Product management- delete product

Super users only can delete the products from the site

![delete](static/images/delete-product.png)

### Flagged system 

users are also able to upvote or down vote products, if a product recieves to many down votes (built for 4 here) then the product will show in the admin pannel as flagged, and also show a red border around the specific product that has recieved to many downvotes, that way the owners of the site are aware that a product is under performing and they can unlist or delete the product as they see fit

![flagged](static/images/red-border.png)

### Newsletter
Users are able to sign up to a newsletter where they can get regular emails of what the site has to offer or anything they may need to know

![newsletter](static/images/newsletter.png)
![newsletter](static/images/newsletter-unsub.png)

# Wishlist

Users can add products to their wishlist, unfortunatley i didnt have time to add a place for them to view those wishlisted products
![wishlist](static/images/wishlist.png)

# Contact us

A contact page for users to contact the site owners, with their name, email, subject, message and an alert to let them know there message had been sent
![contact](static/images/contact.png)

# My Profile

The my profile page shows the users saved contact infomation and their order history

![profile](static/images/profile.png)

# 404 page

A 404 page to handle page errors
![error handling](static/404.png)

The facebook page for my project
![Facebook page](static/images/fb-page.png)
![Facebook page](static/images/fb-page-2.png)

# Deployment
## Github Deployment

The website was stored on GitHub for version control and backup. I did this using VS codes terminal

After adding, modifying, or removing code, I used the terminal vs code and ran the following commands:

git add .
git commit -m "some message"
git push

This made sure that all changes were saved and made available in my GitHub repository.

### Creating a Fork or Copying

To clone/fork/copy the repository you click on the fork tab which is situated next to unwatch tab in the top right corner of the page on github

### Clone

To create a clone you do the following;

1. Go to the repository page on GitHub.
2. Click the green code button.
3. Copy the HTTPS link by clicking the clipboard icon.
4. Open VS code and open a new terminal
5. Type git clone (Then the repository url)
6. Type cd (repository name) to open the cloned project

### Repository deployment via Heroku

- On the [Heroku Dashboard](https://dashboard.heroku.com) page, click New and then select Create New App from the drop-down menu.
- When the next page loads insert the App name and Choose a region. Then click 'Create app'
- In the settings tab click on Reveal Config Vars and add the following credentials. The credentials for this app are:

1. DATABASE_URL
2. SECRET_KEY
3. DISABLE_COLLECTSTATIC

### Deployment of the app

- Go to the deploy tab and select github as the deployment method.
- Connect your github account and search for your repository.
- Select the repository that contains the project files and click connect.
- Choose manual deployment to deploy when you want to.
- Click deploy to start building the app
- Once the deployment has finished click open app

### Frameworks, programs and libraries used

* [Django](https://www.djangoproject.com/) - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.

* [Bootstrap](https://getbootstrap.com/docs/4.4/getting-started/introduction/) - A css framework

* [Visual Studio Code](https://code.visualstudio.com/) - Used as the IDE.

* [Github](https://github.com/) - I used Github to store all the data of my project after pushing it

* [Heroku](https://www.heroku.com/) - is a cloud platform service  I used to deploy and host the project

* [NeonDB](https://neon.tech/) Used to store PostgreSQL database.

* [Font Awesome](https://fontawesome.com/) - Was used to add icons.

* [Flake8 ](https://flake8.pycqa.org/) - I used it to validate python code

* [figma](https://www.figma.com/) The wireframe mockups were created using 

* [dbdiagram](https://dbdiagram.io/home) - was used to draw the database schema

* [Stripe](https://stripe.com/en-ie) - was used for checkout functionality and facilitate online payments

* [AWS](https://aws.amazon.com/s3/) - for  object storage through a web service interface.

* [Unsplash](https://unsplash.com/) - images used for the project

* [Pexels](https://www.pexels.com/) - images used for the project

* [pixabay](https://pixabay.com/) - images used for the project

## Credits

* Images are from [pexels](https://www.pexels.com/) [pixabay](https://pixabay.com/) [unsplash](https://unsplash.com/)

* Code Institute Botique Ado walkthrough

* Code Institute Introduction to search engine optimization

* Code Institute Web Marketing

* create a 404 page [youtubevideo](https://www.youtube.com/watch?v=06Ae9FVnEOI)

[StripeDocumentation](https://docs.stripe.com/)

[python](https://docs.python.org/3.12/)



### Acknowledgement and support

* My Mentor Jubril akolade

* The code institute tutors, specifically, Rebecca, Roman, Oisin.

* My dog, for giving me the idea to create this website in the first place. 