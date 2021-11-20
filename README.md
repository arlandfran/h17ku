# h17ku

A web app that helps users to compose haikus.

**Deployed Link:** [https://h17ku.herokuapp.com](https://h17ku.herokuapp.com)

**Project Goals**:

- Help users write their own haikus

- Provide a platform for users to read haikus

- Allow users to post their own haikus

**Developer Goals**:

- Build a CRUD application with Python, Flask & MongoDB

- Implement basic user authentication

- Demonstrate unit testing with pytest

## UX

### User Stories

- As a user, I want to be able to learn how haikus are structured so that I can write my own haikus

- As a user, I want to be able to view other user's haikus so that I can see what other user's have written

- As a user, I want to be able to post my haiku so that I can share it with other users on the website

- As a user, I want to be able to easily copy my post so that I can share my haikus on any platform outside of the website

- As a user, I want to be able to save my haikus so that I can read them at any later date

- As a user, I want to be able to save other user's haikus so that I can read them at a later date

- As a user, I want to be able to edit my haiku after I've posted it so that I can fix any typos or make any amendments if I need to

### Design

**Font Family**: System font stack

**Wireframes**: [View wireframes here.](https://www.figma.com/file/U0uHd5o7MSSylybfmesyOo/haiku-help?node-id=0%3A1)

## Features

### Implemented

- Responsive design

- CRUD functionality

- User authentication

- Haiku validator

- Comments

- Like system

- Dark mode

### Planned

- Report system

- Save posts

- Share to social media

- User search

- Post pagination

## Information Architecture

### API

**Auth routes**:

| Method | Route          | Action                       |
| ------ | -------------- | ---------------------------- |
| POST   | /auth/register | Handle user registration     |
| POST   | /auth/login    | Handle user login            |
| GET    | /auth/session  | Check if a user is logged in |
| GET    | /auth/logout   | Handle user log out          |

**Post routes**:

| Method | Route  | Action          |
| ------ | ------ | --------------- |
| GET    | /post  | Get single post |
| GET    | /posts | Get all posts   |
| POST   | /post  | Create post     |
| PUT    | /post  | Update post     |
| PATCH  | /post  | Like a post     |
| DELETE | /post  | Delete post     |

**Comment routes**:

| Method | Route     | Action                            |
| ------ | --------- | --------------------------------- |
| GET    | /comments | Get all comments of a single post |
| POST   | /comment  | Create a comment                  |
| PUT    | /comment  | Update a comment                  |
| PATCH  | /comment  | Like a comment                    |
| DELETE | /comment  | Delete a comment                  |

**Other routes**:

| Method | Route  | Action             |
| ------ | ------ | ------------------ |
| GET    | /user  | Get all user posts |
| GET    | /haiku | Get a random haiku |

### Database

The database for this project is MongoDB. There are three collections for this project: `users`, `posts` and `comments`. Here are the database models for each collection:

**Users**:

```json
{
    _id: ObjectId
    email: String
    username: String
    pwd_hash: String
}
```

**Posts**:

```json
{
    _id: ObjectId
    username: String
    haiku: String
    posted_at: Date
    likes: Array
    comments: Array
    edited: Boolean
}
```

Posts have a one to many relationship to Users with the `username` field as the refernce.

**Comments**:

```json
    _id: ObjectId
    post: ObjectId
    username: String
    comment: String
    posted_at: Date
    likes: Array
    edited: Boolean
```

Comments have a one to many relationship to Posts with the `post` objectId as the reference.

## Technologies Used

**Languages**: HTML, CSS, JavaScript, Python

**Front-end**:

- [Svelte](https://svelte.dev/) - JavaScript Framework

- [Routify](https://routify.dev/) - Svelte Router

- [Tailwind CSS](https://tailwindcss.com) - Utility CSS Framework

**Back-end**:

- [Flask](https://flask.palletsprojects.com/en/2.0.x/) - Python Micro-Framework

- [MongoDB Atlas](https://mongodb.com/atlas) - Cloud Database

- [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/) - Flask Wrapper for PyMongo

- [Flask-Login](https://flask-login.readthedocs.io/en/latest/) - User Session Management for Flask

**Tooling**:

- [Figma](https://www.figma.com/) - High-fidelity Wireframing

- [Visual Studio Code](https://code.visualstudio.com/) - Code Editor

- [Git](https://git-scm.com/) - Version Control System

- [Github](https://github.com/) - Code Hosting Platform

- [Heroku](https://www.heroku.com/) - Platform-as-a-Service Cloud Provider

- [Gunicorn](https://gunicorn.org/) - Python WSGI HTTP Server

## Testing

Testing is documented in a [separate file here](./docs/testing.md).

## Deployment

Deployment is documented in a [separate file here](./docs/deployment.md).

## Credits / Acknowledgements:

- Stack Overflow

- All the doc sites: [svelte.dev](https://svelte.dev/docs), [routify.dev](https://www.routify.dev/docs/helpers), [docs.mongodb.com](https://docs.mongodb.com/), [flask](https://flask.palletsprojects.com/en/2.0.x/) etc.

- The Code Institute Slack community for all the great resources, tips and support

- My mentor Precious Ijege for his support and feedback with the project
