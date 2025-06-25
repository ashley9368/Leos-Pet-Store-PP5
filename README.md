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

### Future features

* finish the wishlist app
* make an email system that works
* A Facebook page for marketing
* Marketing

# Web marketing

## Email marketing

The free version of mailchimp was chosen with the current status of the business. Each user that signs up is added to the weekly newsletter and they might turn out to be future customers henceforth low cost to drive sales.

## Search engine optimization

SEO keywords

![seo](static/images/seo.jpg)

## Social media marketing

A facebook page was created to build community from the target market. Facebook is free and it also takes little to no time to set up and also it has so many users whom a business can strive to maintain a certain relationship, create content and connect with a target audience.

![facebook](static/images/facebook.jpg)

## Technologies
### Languages

* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)

* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)

* [Javascript](https://www.javascript.com/)

* [Python](https://www.python.org/)

### Frameworks, programs and libraries used

* [Django](https://www.djangoproject.com/) - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.

* [Bootstrap4](https://getbootstrap.com/) - A css framework

* [Gitpod](https://www.gitpod.io/) - Gitpod was used as an IDE

* [Github](https://github.com/) - I used Github to store all the data of my project after pushing it

* [Heroku](https://www.heroku.com/) - is a cloud platform service  I used to deploy and host the project

* [ElephantSQL](https://www.elephantsql.com/) - used as a database for the project

* [Font Awesome](https://fontawesome.com/) - Was used to add icons for my social media links.

* [PEP8ci](https://pep8ci.herokuapp.com/) - I used it to validate python code

* [Balsamiq](https://balsamiq.com/) - was used to draw wireframes

* [dbdiagram](https://dbdiagram.io/home) - was used to draw the database schema

* [Stripe](https://stripe.com/en-ie) - was used for checkout functionality and facilitate online payments

* [AWS](https://aws.amazon.com/s3/) - for  object storage through a web service interface.

* [Unsplash](https://unsplash.com/) - images used for the project

* [Pexels](https://www.pexels.com/) - images used for the project

* [Adobestock](https://stock.adobe.com/ie/) - images used for the project

# Deployment

I developed this site on Gitpod, using git for version control. Then deployed to Heroku using the following steps

* Log in to [Heroku](https://id.heroku.com/login) or create an account

* Click New and Create New App

* I selected Europe as region.

* Click Create App button

I then went to create a database to connect to the new created app.

* Login to [ElephantSQL](https://www.elephantsql.com/)

* Create new instance

* Set up your plan - Give the plan a name and select Tiny Turtle free plan

* Select region button

* Select a data center ner your. I selected EU-West-1(Ireland)

* Click Review

* Click Create instance

* Return to elephantsql dashboard, click on database instance name

* In the url section, clicking the copy icon will copy the database url to the clipboard

* Go back to Heroku to your created app, go to Settings

* Add config var DATABASE-URL, and for the value, copy in your databse url from ElephantSQL. do not add quotation marks around your database

* In Gitpod install dj-database_url and psycopg2 to connect to your external database

* Update requirements.txt: pip freeze > requirements

* import dj_database_url in settings and update your database

* migrate your database

* create a new superuser for your database and at this point your database is exposed do not commit it to github

* Install gunicorn and freeze into the requirements file

* Then create Procfile

* DISABLE_COLLECTSTATIC

* Commit and push to github

* On your app in Heroku go to Deploy and connect it to github and search your repository, click connect.

* Choose automatic or manual deploy. I chose manual. Click deploy branch

* When complete click View to open the deployed app

## From Github docs

### Forking 

* Open GitHub page that hosts the repository you wish to fork.
* Find the 'Fork' button at the top right of the page
* Once you click the button the fork will be in your repository

### Cloning

* Open Go to the repository page on Github
* click on the green button that says "Code".
* You can choose to download a zip file of the repository, unpack it on your local machine, and open it in your IDE.
* Copy the URL under the HTTPS tab to clone using https.
* In a new window, and set the current directory to the one you want to contain the clone from.
* Type git clone and paste the URL copied from the GitHub page.
* The repository clone will now be created on your machine. 

## Credits

* Images are from [Unsplash](https://unsplash.com/s/photos/home-organization), [Adobestock](https://stock.adobe.com/ie/), [Pexels](https://www.pexels.com/)

* Code Institute Botique Ado walk through

* Hello django code institute

* [Dataflair django tutorial](https://data-flair.training/blogs/django-tutorials-home/)

* [Stack overflow](https://stackoverflow.com/)

Products description inspiration from

* [The neat system](https://www.theneatsystem.co.za/)

* [Amazon](https://www.amazon.co.uk/)

* [Ikea](https://www.ikea.com)

#### Blog content

* [Home edit](https://thehomeedit.com/)
* [Pretty organized home](https://www.organisedprettyhome.com/organise-kids-toys)
* [Woman's day](https://www.womansday.com/)
* [The neat method](https://neatmethod.com/)

### Acknowledgement and support

* Unfortunately i had run out of time to make all the changes i wanted to, I tried my best and im very aware there are things that need to be fixed/built, But due to a loved one being in hospital i was not able to catch up with the time i lost, but i did get a two week extention which code insititue were very kind to give me. So i wanted to credit them as a thank you too.

* My Mentor Jubril akolade

* The code institute tutors, specifically, Rebecca, Roman, Oisin.

* My dog, for giving me the idea to create this website in the first place. 