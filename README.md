# Python News

![MIT license badge](https://img.shields.io/badge/license-MIT-green)

## Description
A minimalist social media application inspired by Hacker News that allows a user to post an article from another source and other users vote or comment on the post.  This version is a refactor which replaces an existing Node.js backend with one built using Python with a Flask server managing routes and interactions with a MySQL database

##### Homescreen
![Homescreen Screenshot](./assets/images/screenshot.png)
##### Login View
![View Screenshot](./assets/images/screenshot2.png)
##### Dashboard View
![Dashboard View Screenshot](./assets/images/screenshot3.png)
##### Add Comment View
![Add Comment View Screenshot](./assets/images/screenshot4.png)

Visit site [here](https://just-tech-news-py.herokuapp.com/)

## Table of Contents
  * [Installation](#installation)
  * [Usage](#usage)
  * [License](#license)
  * [Technologies](#technologies)
  * [Contributing](#contributing)
  * [Testing](#testing)
  * [Questions](#questions)
  
## Installation
Copy project url from GitHub.
On Windows open a PowerShell terminal.  
Navigate into the directory where you want to keep your project.    
Run 
```
git clone <repo_url>   
```
and cd into python-news directory.

Run
```
python -m venv venv
```
to create a virtual environment.

Run
```
.\venv\Scripts\activate
```
to launch virtual environment

Run
```
pip install -r requirements.txt
```
to install dependencies in the venv/Lib/site-packages folder

Create a .env file in the root of the project and add the following configuration code for your database connection.  Replace PASSWORD with the password of your root MySQL user
```
DB_URL=mysql+pymysql://root:PASSWORDd@localhost/python_news_db

```

Run 
```
python seeds.py
```
to seed database.

Run
```
python -m flask run
```
to start the server on localhost:5000.

## Usage
Open localhost:5000 in browser and sign up to create posts with links to your favorite articles.  Add comments and upvotes.

## License 
This project is covered under the MIT license 

## Technologies 
HTML5, CSS3, JavaScript, Python, MySQL, Flask, Jinja

## Contributing
To see the guidelines adopted for contributing to this project, please view the [Contributor Covenant](https://www.contributor-covenant.org/version/2/0/code_of_conduct/code_of_conduct.txt)

## Testing
Tests coming soon

## Questions
Visit me at GitHub  
[christopherConcannon](https://github.com/christopherConcannon)
  
If you have any questions or would like to contact me, please email me at  
[cmcon@yahoo.com](mailto:cmcon@yahoo.com)
