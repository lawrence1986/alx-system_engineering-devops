# Secured and monitored web infrastructure
## Design of Three-Server Web Infrastructure for www.foobar.com:

<h3>Load Balancer (LB):</h3>

* Purpose: Distribute incoming traffic across multiple servers to ensure high availability and load distribution.
Components: Load balancing software/hardware.
Web Servers (WS1, WS2, WS3):

* Purpose: Host the website content and handle user requests.
Components: Web server software (e.g., Nginx, Apache), application code.
Application Servers (AS1, AS2, AS3):

* Purpose: Process dynamic content, business logic, and interact with the database.
Components: Application runtime environment, necessary libraries.
Database Servers (DB1, DB2, DB3):

* Purpose: Store and manage website data.
Components: MySQL or other database software.
Firewalls (FW1, FW2, FW3):

* Purpose: Enforce security policies by filtering incoming and outgoing traffic.
Function: Blocks unauthorized access, prevents malicious attacks.
SSL Certificate:

* Purpose: Secure communication between users and the web servers by encrypting data.
Function: Ensures data privacy and integrity.
Monitoring Clients (MC1, MC2, MC3):

* Purpose: Monitor the health, performance, and security of the infrastructure.
Components: Monitoring agent software.
Specifics of the Infrastructure:

* Firewalls: Firewalls are added to protect the infrastructure by controlling and filtering traffic. They help prevent unauthorized access and protect against malicious attacks.

<h3>SSL Certificate:</h3> Serving traffic over HTTPS is essential to encrypt data transmitted between users and servers. This prevents eavesdropping and ensures data integrity during transmission.

<h3>Monitoring:</h3> Monitoring is used to track the infrastructure's performance, detect issues, and ensure uptime. Monitoring tools collect data about server health, response times, resource utilization, etc.

<h3>Monitoring Data Collection:</h3> Monitoring clients (data collectors) gather information from various components (servers, load balancer, database), send it to monitoring services (like Sumo Logic), and provide insights into the system's behavior.

<h3>Monitoring Web Server QPS (Queries Per Second):</h3> To monitor web server QPS, set up monitoring agents to track the number of incoming queries to the web servers. This data can be collected and analyzed to ensure optimal performance.

* Issues with the Infrastructure:

Terminating SSL at Load Balancer Level:

* Issue: While terminating SSL at the load balancer can offload processing from web servers, it requires transmitting decrypted data internally. This might expose sensitive information if proper security measures are not in place.
Single MySQL Server for Writes:

* Issue: Having only one MySQL server that can accept writes creates a single point of failure. If this server goes down, write operations will fail, impacting the availability and consistency of the application.
Uniform Server Components:

* Issue: Using identical components for all servers (database, web, application) might lead to resource bottlenecks. Different components often have varying resource requirements. For example, a database server might require more CPU and memory than a web server.
* By addressing these issues and optimizing the infrastructure, you can build a more secure, scalable, and reliable web hosting environment for foobar.
