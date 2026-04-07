# ShareGamez
### Video Demo:  <https://youtu.be/zqPJlqTkFHE>
### Description:
    ShareGamez is a webiste for people who wants to share their own games to the world.
    If you upload your game, you will have acess to edit the game page, get ratings on it, upload images, and share with your friends.
    You can search games in the game libary where your friends and others can share their own game.




# Files
## app.py:
This is the file which controls the backend of the site.
It shares data to a databaes and gets data from it.

### Modules and Packages
- The code begins by importing necessary modules and packages such as Flask, SQL, Session, and others.

### Database Configuration
- It configures the database using the SQL module, connecting to a SQLite database file called "sharegamez.db".

### File Upload Configuration
- Configures a folder for file uploads and sets it as "UPLOAD_FOLDER."

### Email Configuration
- Configures email settings for sending and receiving messages using Flask-Mail.

### Session Configuration
- Sets up session management to use the filesystem for session storage.

### Routes and Functionality
- Defines various routes and their corresponding functionalities:
  - **Home ("/")**: Displays the homepage with top-rated games.
  - **About ("/about")**: Displays an "About" page.
  - **Contact ("/contact")**: Allows users to send contact messages. Sends an email notification when a message is sent.
  - **Return Games ("/returngames")**: Returns a JSON list of all games.
  - **Games ("/games")**: Displays a page for searching games.
  - **Game Page ("/game/<int:game_id>")**: Displays details about a specific game, allowing users to rate it.
  - **Login ("/login")**: Handles user login, checks credentials, and sets up a user session.
  - **Register ("/register")**: Handles user registration, including email confirmation.
  - **Logout ("/logout")**: Logs the user out by clearing the session.
  - **Upload ("/upload")**: Allows users to upload new games, including file uploads.
  - **My Games ("/mygames")**: Displays a list of games uploaded by the logged-in user, allowing for deletion.
  - **Edit Game ("/editgame/<int:game_id>")**: Allows the user to edit game details, including uploading a new game image.
  - **Edit Game Description ("/editgamedescription/<int:game_id>")**: Allows the user to edit the game's description.
  - **Download File ("/download/<filename>")**: Enables users to download game files.
  - **Profile ("/profile")**: Displays the user's profile information.
  - **Edit Profile ("/editprofile")**: Allows users to edit their profile information, including the username.

### Running the Application
- The `if __name__ == "__main__":` block ensures that the Flask app is run when this script is executed directly.

## helpers.py:

This Python code defines several functions used for user validation and authorization.

### `is_valid_email(email)`
- This function checks whether a given email address is valid using a basic regular expression (regex) pattern for email validation.

### `login_required(f)`
- This function is a decorator that can be applied to routes in a Flask application.
- It ensures that a user is logged in before allowing access to a specific route.
- If a user is not logged in (as indicated by the absence of a `user_id` in the session), the decorator redirects them to the login page.

### `allowed_file(filename)`
- This function checks whether a given filename has an allowed file extension.
- It is typically used in the context of file uploads to ensure that only specific file types (e.g., PNG, JPG, JPEG, GIF) are accepted.
- The function checks if the file extension of the provided filename is in a predefined set of allowed extensions.

These functions are designed to enhance the security and functionality of my web application by validating user inputs, protecting routes, and ensuring that uploaded files adhere to certain criteria.

## sharegamez.db:
- This is an SQLite database which is used to store the users and their games data


## requirements.txt:
- These are the modules that are a must-have when you are running the server.



# Folders

## Static:
The "static" folder is a special directory used to store static assets such as stylesheets, JavaScript files, images, and other files. This folder serves as the default location for serving static content to web clients.

- ### uploads:
    - This folder stores every file which the user uploaded.
        - It can be a game file
        - Or it can be and image of the game


## Flask_Session:
- In Flask, the "flask_session" folder is a component related to server-side session management. Flask-Session is an extension that allows Flask applications to manage user sessions securely.


## Templates:
This folder contains all `HTML` files that are being rendered

- ## about.html:

    This HTML file serves as a template for the "About Us" page of the ShareGamez website. It is used to structure and present information about the platform, its mission, and what it offers to users. Below is a breakdown of the contents within the HTML file:

    ### Template Inheritance
    - The file starts with `{% extends "layout.html" %}`, indicating that it extends another HTML template file named "layout.html."

    ### Page Header
    - The `<header>` section contains a page title `<h1>About Us</h1>` and a welcoming message `<p>Welcome to <span>ShareGamez</span> - Your Ultimate Destination for Gaming Enthusiasts!</p>`. This header introduces the purpose of the page and the platform.

    ### Our Mission
    - The `<section>` titled "Our Mission" outlines the platform's mission statement:
    - "Our mission is simple: to create a thriving gaming community where players from across the globe can come together."
    - The text emphasizes the belief in the unifying power of gaming and the goal to create a supportive and inclusive gaming environment.

    ### What We Offer
    - In the "What We Offer" section, a list of platform features is presented:
    - "Game Uploads," offering users the ability to upload and share games.
    - "Game Discovery," highlighting the vast library of games available.
    - "Community Interaction," emphasizing engagement through comments, forums, and discussions.
    - "Developer Spotlight," showcasing the celebration of game developers.
    - "Safety and Fair Play," underlining the commitment to a positive and respectful gaming environment.

    ### Join Us Today
    - The final section encourages users to join the ShareGamez community:
    - It invites users to become a part of the community, whether as players, developers, or enthusiasts.
    - It expresses gratitude for choosing ShareGamez as a gaming hub.
    - It provides a call to action with a link to the registration page, encouraging users to "Join us today."

    This HTML template plays a crucial role in presenting essential information about ShareGamez, its mission, and the value it offers to users. It adheres to a structured layout inherited from the "layout.html" template, ensuring consistent design across the website's pages.

- ###contact.html:
    This HTML file serves as a template for the "Contact Us" page of a website. It is used to structure and present a contact form, allowing users to get in touch with the platform. Below is a breakdown of the contents within the HTML file:

    ### Template Inheritance
    - The file starts with `{% extends "layout.html" %}`, indicating that it extends another HTML template file named "layout.html." This is a common practice in web development, where templates inherit the structure and layout from a base template.

    ### Page Header
    - The `<header>` section with the class "contact-header" contains a page title `<h1 class="contact-title">Contact Us</h1>` and a welcoming message `<p class="contact-description">We'd love to hear from you!</p>`. This header introduces the purpose of the page and sets a friendly tone for user interaction.

    ### Contact Form
    - The `<section>` with the class "contact-form-container" contains a contact form:
    - It includes a `<h2 class="contact-form-title">Contact Form</h2>` that serves as the title for the form.
    - The form itself is created using the `<form>` element with an action attribute that specifies the "/contact" URL as the form submission destination.
    - The form includes fields for the user's name, email, and message.
    - Each input field has a corresponding `<label>` element and an `<input>` element with appropriate attributes like `name`, `type`, and `id`. The email field includes an email validation check.
    - Conditional rendering is used to display a "wrong" label next to input fields if validation fails. For instance, if the user submits the form without providing a name, the "No name" message is displayed.

    ### Submission Button
    - The form includes an `<input>` element with `type="submit"` and a class "contact-submit" for users to submit their contact information.

    This HTML template provides the structure for the "Contact Us" page, offering a contact form for users to reach out to the platform. It maintains a consistent layout with the base "layout.html" template and handles validation and feedback messages to ensure a smooth user experience.

- ## editgame.html:
    This HTML file serves as a template for displaying detailed information about a game on the platform. It allows users to view and edit various aspects of a game's profile. Below is a breakdown of the contents within the HTML file:

    ### Template Inheritance
    - The file starts with `{% extends "layout.html" %}`, indicating that it extends another HTML template file named "layout.html." This is a common practice in web development, where templates inherit the structure and layout from a base template.

    ### Game Header
    - The `<header>` section with the class "header-da" displays the game's name using `{{game["name"]}}`. This serves as the title of the game page.

    ### Game Image
    - The game's image is displayed, and users can edit it:
    - If the game already has an image (`game["image"]` is defined), users can edit it by uploading a new image.
    - If the game does not have an image, users can upload an image to be associated with the game.
    - Conditional rendering ensures that the appropriate form is displayed based on the presence of an existing image or not.
    - If the "Edit" button is clicked without selecting a file, a "No file" message is displayed.

    ### Game Video
    - If the game has a video (`game["video"]` is defined), a video player is embedded in the page using an iframe.

    ### Game Description
    - Users can edit the game's description using a textarea. The current description is pre-filled with `{{game["description"]}}`, and users can submit changes by clicking the "Edit" button.

    ### Download Link
    - A "Download Now" button is provided that allows users to download the game. The button's URL is generated using `{{ url_for('download_file', filename=game["filename"]) }}`.

    This HTML template provides a structured layout for displaying and editing game details. It ensures a consistent design with the base "layout.html" template and offers functionality for managing game images, descriptions, and downloads.

- ## editprofile.html:
    This HTML file serves as a template for displaying and editing a user's profile information on the platform. It allows users to view and update their username. Below is a breakdown of the contents within the HTML file:

    ### Template Inheritance
    - The file starts with `{% extends "layout.html" %}`, indicating that it extends another HTML template file named "layout.html." This is a common practice in web development, where templates inherit the structure and layout from a base template.

    ### User Profile Form
    - A `<form>` element is used to enable users to edit their profile information. The form has an `action="/editprofile"` attribute, specifying where the form data should be sent when submitted.

    ### Profile Header
    - The `<h1>` element displays "Your Profile," providing a title for the profile page.

    ### Profile Information
    - The user's username and email are displayed within `<div>` elements with the class "profile-info."
    - Users can edit their username using an `<input>` element.
    - If the provided username is incorrect or not allowed (determined by `message == "username"`), a "Wrong username" message is displayed.
    - The user's email is shown but cannot be edited.

    ### Profile Actions
    - Users are provided with options to interact with their profile:
    - They can navigate to the "Upload a New Game" page by clicking "Upload a New Game" (linked to "/upload").
    - They can confirm and save their profile changes by clicking the "Confirm" button, which triggers a form submission.

    This HTML template provides a structured layout for displaying and editing user profile information. It ensures a consistent design with the base "layout.html" template and offers functionality for managing the user's username and initiating profile updates.


- ## game_page.html:
    This HTML file serves as a template for displaying detailed information about a specific game on the platform. It provides details about the game's name, image, video, description, and allows users to rate their experience. Below is a breakdown of the contents within the HTML file:

    ### Template Inheritance
    - The file starts with `{% extends "layout.html" %}`, indicating that it extends another HTML template file named "layout.html." This is a common practice in web development, where templates inherit the structure and layout from a base template.

    ### Game Header
    - The `<header>` section displays the game's name using `{{game["name"]}}`. This serves as the title of the game page.

    ### Game Image
    - If the game has an image (`game["image"]` is defined), it is displayed using an `<img>` element with the class "game-image."

    ### Game Video
    - If the game has a video (`game["video"]` is defined), a video player is embedded in the page using an iframe. The video source URL is obtained from `{{ game['video_url'] }}`.

    ### Game Description
    - The game's description is displayed using a `<p>` element with the description obtained from `{{game["description"]}}`.

    ### Download Link
    - A "Download Now" button is provided that allows users to download the game. The button's URL is generated using `{{ url_for('download_file', filename=game["filename"]) }}`.

    ### Rating Feature
    - A rating feature is included, allowing users to rate their experience with the game. It consists of a set of stars represented by `<i>` elements.
    - JavaScript code is used to handle the user's rating selection. Users can click on the stars to rate the game.
    - The user's rating is sent to the server for further processing (e.g., storing the rating).

    This HTML template provides a structured layout for displaying and rating game details. It ensures a consistent design with the base "layout.html" template and offers functionality for managing game information and user ratings.

- ## games.html:
    This HTML file serves as a template for displaying a game library, allowing users to search for and view a collection of games available on the platform. Below is a breakdown of the contents within the HTML file:

    ### Template Inheritance
    - The file starts with `{% extends "layout.html" %}`, indicating that it extends another HTML template file named "layout.html." This is a common practice in web development, where templates inherit the structure and layout from a base template.

    ### Page Title
    - The page title "Game Library" is displayed within a container.

    ### Search Bar
    - A search bar is provided to allow users to search for games by name. It is implemented using an `<input>` element with the `data-search` attribute to enable search functionality.

    ### Game Cards Container
    - The container for displaying game cards is represented by `<div class="user-cards" data-user-cards-container></div>`. This is where individual game cards will be displayed.

    ### Game Card Template
    - A template for individual game cards is defined within a `<template data-user-template>`. It includes elements for displaying the game's header, image, body, and rating. This template will be used to create game cards dynamically.

    ### JavaScript Functionality
    - JavaScript code is included to handle various functionalities:
    - Searching: The code listens for input in the search bar, filters games based on the search query, and hides or displays game cards accordingly.
    - Fetching Game Data: The code fetches game data from a JSON file using the `fetch` API. Game information is retrieved and used to populate the game cards dynamically.
    - Game Card Creation: For each game, the template is cloned, and game-specific information is inserted, such as game name, rating, image, and a "Visit" link.
    - Displaying Game Cards: The game cards are appended to the game cards container, making them visible to the user.

    This HTML template provides a structured layout for displaying and searching through a library of games. It ensures a consistent design with the base "layout.html" template and offers functionality for managing game information and user interactions.

- ## index.html:
    This HTML file serves as a template for the ShareGamez landing page, welcoming users and featuring a selection of games. Below is a breakdown of the contents within the HTML file:

    ### Template Inheritance
    - The file starts with `{% extends "layout.html" %}`, indicating that it extends another HTML template file named "layout.html." This is a common practice in web development, where templates inherit the structure and layout from a base template.

    ### Welcome Message
    - A welcoming jumbotron is displayed with a large title and a lead message. It greets users and encourages them to upload and discover new games.

    ### Featured Games Section
    - A section for featuring games is provided, showcasing up to three games.
    - Each featured game is displayed within a Bootstrap grid system, consisting of columns for text and images.
    - Game information, including name, description, and rating, is dynamically inserted into the template.
    - Star ratings are displayed using HTML entities (stars) based on the game's rating.
    - A "Play Now" button is included, linking to the respective game's page.
    - Game images are displayed if available, fetched from the "uploads" directory.

    This HTML template provides a structured layout for the ShareGamez landing page, allowing users to discover featured games and navigate to their respective pages for more details or gameplay. It maintains a consistent design with the base "layout.html" template and offers a visually appealing introduction to the platform.

- ## layout.html:
    This HTML template is the base layout for the ShareGamez website. It provides a structured foundation for the website's pages, including navigation, styling, and dynamic content integration. Below is a breakdown of the contents within the HTML file:

    ### Document Metadata
    - The template includes necessary metadata such as character encoding and viewport settings.
    - The document's title is dynamically set to "ShareGamez" with the option to append custom titles using template blocks.

    ### Stylesheets
    - The template links to external stylesheets, including Bootstrap and Font Awesome from Content Delivery Networks (CDNs).
    - A custom CSS file, "style.css," is linked to customize the website's appearance.
    - A site favicon ("favicon.ico") is linked for branding.

    ### Navigation Bar
    - The navigation bar includes a logo that links to the home page and a responsive menu toggle button for smaller screens.
    - Navigation links are included for the home page, games, upload, about, and contact pages.
    - Conditional navigation is provided based on user sessions. If a user is logged in, a dropdown menu for profile actions is displayed. Otherwise, links to register and log in are shown.

    ### Body Content
    - The main body of the template is left open for dynamic content insertion using template blocks.
    - The `{% block body %}` and `{% endblock %}` tags define where page-specific content should be placed.

    ### JavaScript Libraries
    - JavaScript libraries, including Bootstrap JavaScript, are included to enhance website functionality.
    - The template provides a space for custom JavaScript scripts using the `{% block script %}` and `{% endblock %}` tags.

    ### Footer
    - A footer section displays a copyright notice, indicating that all rights are reserved for ShareGamez.co.

    This HTML template serves as the foundation for the entire ShareGamez website, ensuring a consistent layout and navigation structure across all pages. Developers can utilize template blocks to insert specific content on individual pages while maintaining the site's overall design and functionality.

- ## login.html:
    This HTML file represents the login page for the ShareGamez website. It is designed to allow users to log in to their accounts. Below is a breakdown of the contents within the HTML file:

    ### Page Structure
    - The login page is based on the ShareGamez layout, ensuring a consistent look and feel with the rest of the website.
    - It contains a centered container for the login form.

    ### Login Form
    - The login form includes two input fields: one for the user's email and another for their password.
    - If there are validation errors, such as an incorrect email or password, error messages are displayed below the respective input fields.
    - Users are required to input their email and password to proceed.
    - A "Login" button allows users to submit the form.

    ### Styling
    - The page uses consistent styling with other ShareGamez pages, including labels, input fields, and buttons.

    ### Templating
    - This page extends the "layout.html" template to maintain the website's overall structure.
    - The `{% block body %}` and `{% endblock %}` tags define where the specific content for this page should be inserted.

    The ShareGamez login page provides a user-friendly interface for users to access their accounts securely. It includes error handling for incorrect login information and follows the website's design guidelines for a cohesive user experience.

- ## mygame.html:
    This HTML file represents the "My Games" page of the ShareGamez website. It is designed to display a list of games associated with the user's account, allowing them to manage their uploaded games. Below is a breakdown of the contents within the HTML file:

    ### Page Structure
    - The "My Games" page is based on the ShareGamez layout, ensuring a consistent look and feel with the rest of the website.
    - It features a table to present the user's games in a structured manner.

    ### Table
    - The table includes columns for "Title," "Edit," "Download," and "Delete."
    - The table headers are styled with a dark background for clear differentiation.
    - For each game associated with the user's account, a new table row is generated.
    - In the "Title" column, the name of the game is displayed.
    - The "Edit" column provides a link to edit the game details.
    - The "Download" column offers a link to download the game file.
    - The "Delete" column includes a form with a hidden input field to specify the game to be deleted. A "Delete" button triggers the deletion process.

    ### Styling
    - The page uses consistent styling with other ShareGamez pages, including table styles, header colors, and links.
    - The table is formatted with stripes, borders, and hover effects for improved readability.

    ### Templating
    - This page extends the "layout.html" template to maintain the website's overall structure.
    - The `{% block body %}` and `{% endblock %}` tags define where the specific content for this page should be inserted.

    The "My Games" page provides users with a convenient way to view and manage the games they've uploaded to ShareGamez. Users can edit game details, download game files, and delete games as needed, all within a user-friendly table format.

- ## profile.html:
    This HTML file contains CSS styles and content for the user profile page on the ShareGamez website. It is responsible for displaying a user's profile information and providing links for actions like uploading a new game or editing the profile details. Below is an explanation of the CSS styles and content within the file:

    ### CSS Styles
    - The CSS styles defined within the `<style>` tag are responsible for the visual presentation of the user profile page.
    - A `.container` class is defined to limit the maximum width of the profile content and apply styling to create a visually appealing container. It includes a white background, rounded corners, and a subtle box shadow.
    - Header styles (`h1`) set the font size to 24px with zero margins and padding.
    - Paragraph (`p`) styles define a font size of 16px.
    - `.profile-info` class styles are applied to the user's profile information, including labels and data. Margins are set to create spacing between elements.
    - Labels within profile information have a bold font weight.
    - `.profile-actions` class styles are used for the links that allow the user to perform actions related to their profile. These links are styled with a bold font, blue color, and a hover effect to underline them when hovered.

    ### Page Content
    - The content of this page is enclosed within a `.container` element, which gives it a structured and visually pleasing appearance.
    - The page includes an `<h1>` element displaying "Your Profile" as the title.
    - User profile information, including the username and email, is presented using `<label>` and `<p>` elements within `.profile-info` sections.
    - The "Username" and "Email" labels are bolded for emphasis.
    - The "Upload a New Game" and "Edit Profile" actions are provided as links within `.profile-actions`. Users can click on these links to navigate to other pages for performing these actions.

    ### Template Blocks
    - This page extends the "layout.html" template, which defines the overall structure of ShareGamez pages.
    - `{% block style %}` and `{% endblock %}` tags enclose the CSS styles specific to this page.
    - `{% block body %}` and `{% endblock %}` tags define where the main content of the page should be inserted.

    The User Profile Page Styling HTML file combines CSS styling and content to create a visually appealing and user-friendly profile page. Users can view their profile information and easily access actions like uploading new games or editing their profile details.

- ## register.html:
    This HTML file represents the user registration page of the ShareGamez website. It is responsible for allowing users to register by providing their email, username, and password. Below is an explanation of the content and structure of this page:

    ### Page Content
    - The content is enclosed within a `<div>` element with the class `.game-login-container`, which styles the registration form's container.
    - An `<h2>` element with the class `.game-login-title` displays "Register" as the title of the registration page.
    - A `<form>` element is used to collect user registration data. It is configured to send a POST request to the "/register" endpoint for processing.
    - Several `<div>` elements with the class `.game-form-group` group form input elements along with labels.
    - Labels and input fields are provided for the following user registration information:
    - Email: Users must enter their email address. If the email is invalid, an error message is displayed.
    - Username: Users must choose a username. If the chosen username is already in use, an error message is displayed.
    - Password: Users must enter a password. If no password is provided, an error message is displayed.
    - Confirmation Password: Users must confirm their password by entering it again. If the confirmation password does not match the original password, an error message is displayed.
    - A "Register" button of type "submit" with the class `.game-button` is provided for users to submit their registration form.

    ### Error Messages
    - Error messages are displayed next to the corresponding input fields in case of registration errors. The error messages are styled with the `.wrong` class, making them visually noticeable.

    ### Template Blocks
    - This page extends the "layout.html" template, which defines the overall structure of ShareGamez pages.
    - `{% block body %}` and `{% endblock %}` tags define where the main content of the page should be inserted.

    The User Registration Page allows users to create an account on ShareGamez by providing their registration details. It includes form validation and error messages to ensure that users provide valid information during the registration process.

- ## upload.html:
    This HTML file represents the file upload page of the ShareGamez website. It is responsible for allowing users to upload files, including games, to the platform. Below is an explanation of the content and structure of this page:

    ### Page Content
    - The content is enclosed within a `<div>` element with the class `.game-login-container`, which styles the file upload form's container.
    - An `<h2>` element with the class `.game-login-title` displays "File Upload" as the title of the upload page, styled with the color "aliceblue."
    - A `<form>` element is used to collect and submit file upload data. It is configured to send a POST request to the "/upload" endpoint for processing.
    - A `<div>` element with a possible error message is displayed if the uploaded file is not valid. The error message is styled with the `.wrong` class.
    - An `<input>` element of type "file" with the name "file" allows users to select a file to upload. The style is adjusted for width.
    - A `<div>` element with a label and input field is provided for users to enter the name of the game they are uploading. If there is an error with the game name, an error message is displayed.
    - A success message is displayed in green if the upload is successful, using the style `style="color:green"`.
    - A "Submit" button of type "submit" with the class `.game-button` is provided for users to submit their file upload.

    ### Error Messages
    - Error messages are displayed if the uploaded file is not valid and if there is an error with the game name. These messages are styled with the `.wrong` class.

    ### Template Blocks
    - This page extends the "layout.html" template, which defines the overall structure of ShareGamez pages.
    - `{% block body %}` and `{% endblock %}` tags define where the main content of the page should be inserted.

    The File Upload Page allows users to upload game files to ShareGamez. It includes form validation and error messages to ensure that users provide valid file uploads and game names during the upload process. Upon successful upload, a confirmation message is displayed.