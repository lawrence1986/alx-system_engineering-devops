# One-Server Web Infrastructure
## Introduction

Imagine a user wanting to access a website hosted at www.foobar.com. To make this possible, we have designed a one-server web infrastructure using the following components:

- **1 Server**: A single server that hosts all components of the web application.
- **1 Web Server (Nginx)**: Nginx is used as the web server to handle HTTP requests.
- **1 Application Server**: An application server that hosts your code base. GUnicorn for python.
- **Application Files**: The application code base, which includes the website's HTML, CSS, JavaScript, Python, and server-side code.
- **1 Database (MySQL)**: MySQL is used as the database to store and manage data.
- **1 Domain Name (www.foobar.com)**: A domain name (www.foobar.com) is configured to point to the server's IP address (e.g., 8.8.8.8).

## Specifics About the Infrastructure

### What is a Server?

A server, in this context, is a computer or a virtual machine that stores and serves the components of your web application. It receives and responds to requests from users' computers over the internet.

### Role of the Domain Name

The domain name (www.foobar.com) acts as a user-friendly label that maps to the server's IP address. It allows users to access your website by typing the human-readable domain name instead of remembering the server's numerical IP address.

### Type of DNS Record for www.foobar.com

The DNS record "www" in www.foobar.com is typically an "A" (Address) record. It associates the subdomain "www" with the server's IP address (e.g., 8.8.8.8).

### Role of the Web Server (Nginx)

The web server (Nginx) is responsible for handling HTTP requests from users' web browsers. It serves static content (HTML, CSS, JavaScript, images) directly to users and routes dynamic requests to the application server.

### Role of the Application Server

The application server hosts your code base and is responsible for executing application logic, processing user requests, interacting with the database, and generating dynamic content (e.g., user-specific pages or data).

### Role of the Database (MySQL)

The database (MySQL) stores and manages data used by your web application. It stores information such as user accounts, content, and configurations. The application server communicates with the database to retrieve and update data as needed.

### Communication with User's Computer

The server uses the HTTP/HTTPS protocol to communicate with the user's computer when they request your website. The user's web browser sends HTTP requests to the server, and the server responds with HTML, CSS, JavaScript, and other resources to render the web pages on the user's screen.

## Issues with this Infrastructure

### Single Point of Failure (SPOF)

This infrastructure has a single point of failure (SPOF) because there is only one server. If the server experiences hardware failure, software issues, or becomes unreachable for any reason, the entire website will go offline, resulting in downtime for users.

### Downtime During Maintenance

When maintenance or updates are needed, such as deploying new code or configuring the web server, the web server often needs to be restarted. During this restart process, the website may experience downtime, and users may be temporarily unable to access it.

### Limited Scalability

This one-server infrastructure has limited scalability. It may struggle to handle high traffic loads, and scaling up to accommodate more users can be challenging. As traffic grows,it may encounter performance issues and slower response times, which can negatively impact the user experience.
