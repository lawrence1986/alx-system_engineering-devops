1. Distributed web infrastructure
Design of Three-Server Web Infrastructure for foobar.com:

Load Balancer (HAproxy):

Purpose: Distribute incoming traffic across multiple servers to improve availability and performance.
Distribution Algorithm: Round-robin, evenly distributing requests.
Active-Active Setup: Both servers actively handle traffic.
Server 1 and Server 2:

Purpose: Host components of the web infrastructure, providing redundancy.
Components: Operating system, necessary software.
Web Server (Nginx):

Purpose: Handle incoming requests, serve static content, and perform initial request processing.
Components: Nginx software, configuration files.
Application Server:

Purpose: Process dynamic content, execute business logic, and generate responses.
Components: Application runtime (e.g., PHP, Python), application code.
Set of Application Files (Your Code Base):

Purpose: Contains the website's source code, templates, and assets.
Components: HTML, CSS, JavaScript, server-side scripts.
Database (MySQL):

Purpose: Store and manage website data.
Components: MySQL database software, data files.
Specifics of the Infrastructure:

Load Balancer: The load balancer distributes incoming requests across two servers using a round-robin algorithm. This improves performance, prevents overloading a single server, and enhances fault tolerance.

Distribution Algorithm: Round-robin distributes requests in a cyclic manner to each server sequentially.

Active-Active Setup: Both servers actively handle incoming traffic, distributing the load and providing redundancy. In an active-active setup, both servers are operational simultaneously.

Database Primary-Replica (Master-Slave) Cluster:

Primary Node: Handles write operations, maintaining the main dataset.
Replica Node: Handles read operations, replicates data from the primary node.
Issues with the Infrastructure:

Single Points of Failure (SPOF): While the load balancer improves redundancy, each server and the load balancer itself remain single points of failure. If one of them fails, the entire system could become unavailable.

Security Issues: Lack of firewalls exposes servers to potential attacks. Without HTTPS, data transmitted between users and servers is unencrypted, risking data privacy and integrity.

No Monitoring: Without monitoring, you lack visibility into the infrastructure's health, performance, and security. This could lead to undetected issues and downtime.

To address these issues:

Implement firewalls to protect servers.
Configure HTTPS to secure data transmission.
Set up monitoring tools to collect data and detect issues proactively.
Consider redundancy for load balancers and servers to mitigate SPOF.
Add additional security layers like Intrusion Detection Systems (IDS) and Web Application Firewalls (WAF).
Consider implementing a Content Delivery Network (CDN) for improved performance and security.
