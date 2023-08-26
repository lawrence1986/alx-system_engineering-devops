# Scale up Requirements:
* 1 server
* 1 load-balancer (HAproxy) configured as cluster with the other one
* Split components (web server, application server, database) with their own server
----------------------------------------------------------------------------------------------------------
<p>You must be able to explain some specifics about this infrastructure:
Server: This is the fundamental unit of your infrastructure. It's a physical or virtual machine that provides the resources necessary to run your applications and services. Each component (web server, application server, database) will be hosted on its own server for isolation and resource allocation.</p>

<h3>Load Balancer (HAproxy)</h3>: A load balancer distributes incoming network traffic across multiple servers to ensure high availability (HA) and improve performance. By configuring HAproxy in a cluster, you create redundancy. If one load balancer fails, the other can take over seamlessly, preventing service downtime.

* Why it's added: Load balancers help distribute incoming traffic evenly across multiple servers, preventing overloading of any single server and ensuring that the system can handle increased user requests. Clustering the load balancers adds redundancy, further improving the system's availability.

<h3>Web Server:</h3> The web server's primary function is to serve static content, like HTML, CSS, and JavaScript files, to clients (web browsers). It handles incoming HTTP requests and returns the appropriate web pages to users.

* Why it's added: Web servers provide the initial point of contact for user requests. By dedicating a separate server to this role, you ensure that the web server's resources are optimized for handling HTTP requests efficiently.

<h3>Application Server:</h3> Application servers execute the business logic of your application. They process dynamic requests, interact with databases, and generate dynamic content to be sent to the web server for presentation to the user.

* Why it's added: Separating the application server from the web server allows for better resource management. Application servers can handle complex processing tasks without impacting the web server's performance. Additionally, this separation makes it easier to scale your application by adding more application servers as needed.

<h3>Database Server:</h3> The database server stores and manages the application's data. It responds to queries from the application server and ensures data integrity, consistency, and persistence.

* Why it's added: Databases require specialized resources and can become performance bottlenecks if not managed properly. A dedicated database server ensures that data storage and retrieval are optimized, allowing the application and web servers to focus on their respective tasks.

* By implementing this infrastructure with separate servers for each component and load balancers for high availability, you achieve several benefits:

* Scalability: Each component can be scaled independently. For example, if your application server needs more processing power, you can add more application servers without affecting other components.

* Isolation: Isolating components on separate servers enhances security and resource allocation. A performance issue in one component won't directly affect the others.

* Redundancy: Clustering the load balancers and isolating each component improves system redundancy, reducing the risk of service disruption due to hardware failures.

* Performance: Optimizing each server for its specific role ensures that resources are used efficiently, leading to better overall performance.

* Maintenance: Isolation makes maintenance and updates easier. You can take down one component for maintenance without affecting the others.

### In summary, this infrastructure design addresses the key requirements of high availability, scalability, isolation, and performance optimization for each component in the system.
