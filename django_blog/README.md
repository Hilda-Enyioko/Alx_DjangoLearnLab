# Django Blog Authentication System

## Overview
This project implements user authentication using Django’s built-in auth views and custom registration/profile management.

## Features
- User registration with email
- User login and logout
- Profile view and email update
- Password security using Django’s hashing

# Blog Post Management Features

## Features
- List all posts (/posts/)
- View individual post (/posts/<id>/)
- Create post (authenticated users only) (/posts/new/)
- Edit post (author only) (/posts/<id>/edit/)
- Delete post (author only) (/posts/<id>/delete/)

## Permissions
- Any user can view posts.
- Only logged-in users can create posts.
- Only post authors can edit/delete their posts.
