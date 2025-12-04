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
- View individual post (/post/<id>/)
- Create post (authenticated users only) (/post/new/)
- Edit post (author only) (/post/<id>/edit/)
- Delete post (author only) (/post/<id>/delete/)

## Permissions
- Any user can view posts.
- Only logged-in users can create posts.
- Only post authors can edit/delete their posts.

# Comment Functionality

## Features
- Authenticated users can post comments on any blog post.
- Authors can edit or delete their own comments.
- Comments are displayed on the post detail page, newest first.
- Permissions ensure only the comment author can edit/delete their comments.

## URLs
- Add comment: `/post/<post_id>/comments/new/`
- Edit comment: `/comment/<comment_id>/edit/`
- Delete comment: `/comment/<comment_id>/delete/`

# Tagging and Search Functionality

## Features
- Assign multiple tags to posts using django-taggit
- Display tags in post detail and list views
- Click a tag to view all posts with that tag
- Search posts by title, content, or tags via search bar
- Search results show matching posts dynamically

## URLs
- Search: `/search/?q=<query>`
- Posts by tag: `/tags/<tag_slug>/`
