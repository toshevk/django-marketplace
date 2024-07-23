# Django Marketplace
## Online shopping app

### Description
This is a Marketplace webapp I made using Django, as an exercise in creating more complex projects to showcase my
skills.

### Features
The Marketplace app is designed to resemble a classic e-commerce website.
Main features include:

**Browse Items**: All the items in the Marketplace can be perused through the Browse function. Browse also has search
functionality, which can also be used in combination with filters to narrow the item category when searching. Items also
have a detailed view which represents the item separately with all the item's attributes.

**User Creation and Authentication**: A sign-up form and a log-in form. After creation through the sign-up page, each
user can access an admin page to manage their products, or add new products to sell.

**User Dashboard**: Each user can access their dashboard and see all the items they have created. Through this dashboard,
items can be added, edited, or deleted.

**Product Creation**: New items can be added to the Marketplace by users through the New Item form or the user Admin page.
Each item can be described with several attributes: name, description, category, price, image. Additional attributes
added upon creation include: 'sold' flag (represents whether the item is for sale or has been sold), a date of creation,
and the seller's username.

**User Inbox**: Every item has a 'contact seller' icon, which redirects the user to a conversation app. Here the user
can contact the seller and ask any questions they have regarding the item. Conversations in the inbox are separate for
each item the seller has uploaded. Inbox conversations allow the seller to answer the buyer directly through the
conversation app.

### Technology
Main technology used is **Django** 5.0.6. Using Django I set up the entire project and the backend functionality.

To create the frontend, I used **HTML**, **CSS**, and **Tailwind**. For storing the user and product information I used
the default Django database, which is **SQLite3**.