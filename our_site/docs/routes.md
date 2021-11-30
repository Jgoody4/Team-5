# Description of Routes

## Home

Function that implements registration of users.

Returns:

- `render_template(str, form)`: Page that shows a form to register users with unique username and password and a link to the login page.

- `redirect(str, <form>)`: Redirects user to a specific page. If the `<form>` object was included, also returns the registration form.

## Timer

Function works as a working timer, returns a page that displays the amount of time passed.

Parameters:

- `t (str)`: A string in the form of 00:00:00

Returns:

- `render_template (str, timeSpent)`: Page that either shows the amount of time that had passed or an error page

## TheTimer

Returns a page that asks user to enter an amount of time.

Returns:

- `render_template (str, form)`: Page that asks user to enter an amount of time with a textbox
- `redirect (theLink)`: If the user submits the time, they will be redirected to the page that
displays the amount of time that had passed

## Overhead View

Returns a page that works as a overhead view page of the user's flashcards.

Returns:

- `render_template (str, all_cards, form)`: Page that prints all the user's flashcards in a
single page, as well as a shuffle button that shuffles the order.

## Create Cards

Returns a page that allows the user to create their own flashcards.

Returns:

- `render_template (str, form)`: Page that asks the user to insert a term and definition in
textboxes to create a flashcard, and a button that submits the flashcard into the database

- `redirect (str)`: Redirects user back to this page

## Reminder

Returns a page that shows the reminders the user has set up.

Returns: 

- `render_template (str, form)`: The page have the user enter a task to set reminder for and the time for the reminder and a submit button which will display the reminder

## Match

Returns a page that tests the memorization of the user

Returns: 

- `render_template (str, form)`: Page shuffles the card and adds the cards' term and definition to each respective list. Then the page will record the number of right or wrong based on text input into the form.

- `redirect (str)`: Redirects the user to a performance graph after going through all the cards

## Results

Returns a graph for the user to see their memorization performance

Return:

- `render_template(str)`: Shows a page of the graph

## Markdown

Returns a page of the html version of the markdown notes

Return:

- `render_template(str)`: Shows the markdown notes the user had typed

## Menu

Function that shows the menu page with all the links to the various services.

Returns:

- `render_template(str)`: Page with links to all services and a logout option.

## Login

Function that shows the login page with a link to register user.

Returns:

- `render_template(str, form)`: Page that shows a form that takes a username
and password to login a user.

- `redirect(str)`: Redirects the user to the menu page.

## Logout

Function that logs out a user.

Returns:

- `redirect(str)`: Redirects a user to the registration page.