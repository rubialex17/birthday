
# 2. Diagram

Simple diagram with the components that can be used in order to expose the API to internet.

- Route 53 in order to give a DNS to the application and be accessed through internet
- Kubernetes cluster running in AWS (Ingress + Service + Deployment)
- PostgresDB in order to store the information