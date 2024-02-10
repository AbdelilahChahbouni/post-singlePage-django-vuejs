# Django-Vue.js Single Page Application

This is a single page application (SPA) built with Django and Vue.js. It allows users to view and interact with posts, including liking and commenting on them.

## Features

- View posts: Users can view a list of posts with details such as title, content, likes, and comments.
- Like posts: Users can like posts to show their appreciation.
- Comment on posts: Users can leave comments on posts to share their thoughts.
- Filter comments: Users can filter comments by different criteria such as date, user, or popularity.

## Demo

Demo for now is not live

## Installation

To run the application locally, follow these steps:

1. Clone the repository:

   git clone git@github.com:AbdelilahChahbouni/post-singlePage-django-vuejs.git

2. Navigate into the project directory:
   cd your-repository

3. Set up the backend:

    1. Install Django and other dependencies:
    2. pip install -r requirements.txt
    3. Apply migrations:
	-python manage.py migrate
    4. Run the Django development server:
	-python manage.py runserver

4. Set up the frontend:
    1. Navigate to the frontend directory:
	-cd frontend
    2. Install npm dependencies:
	-npm install

    3. Start the Vue.js development server:
	-npm run serve

    4. Open your browser and visit 
	-open http://localhost:8080 to view the application.

5. you can run the aplication in docker using docker-compose
     1. Clone the repository:
   	-git clone git@github.com:AbdelilahChahbouni/post-singlePage-django-vuejs.git
     2. Navigate into the project directory:
	-cd your-repository
     3. Run Docker Compose to build and start the containers:
        -docker-compose up -d --build
     4. Open your browser and visit http://localhost:8080 to view the application.


Usage

    Once the application is running, users can navigate to the posts page to view a list of posts.
    Users can interact with posts by liking or commenting on them.
    The filter functionality allows users to filter comments based on creation date (last , old).
	
