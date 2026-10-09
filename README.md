# Cloud-Native Microservices Platform

An end-to-end DevOps implementation that deploys a containerized microservices application on AWS using Infrastructure as Code, CI/CD automation, Kubernetes, and GitOps.

**GitHub Repository:** [aws-cloud-native-devops-platform](https://github.com/Jahnavi4050/aws-cloud-native-devops-platform)

## Architecture

Developer → GitHub → GitHub Actions → Amazon ECR → Kubernetes manifests in Git → Argo CD → Amazon EKS → AWS Application Load Balancer → DevOps Store

## Technology Stack

| Category | Technologies |
|---|---|
| Application | Python, Flask, HTML, CSS, JavaScript |
| Containers | Docker, Docker Compose |
| Infrastructure as Code | Terraform |
| Cloud | AWS VPC, IAM, EC2, EKS, ECR |
| CI/CD | GitHub Actions, GitHub OIDC |
| Orchestration | Kubernetes |
| GitOps | Argo CD |
| Networking | AWS Load Balancer Controller, ALB, Ingress |

## Application Services

- **Product Service:** Returns product names and prices.
- **Cart Service:** Returns cart items and quantities.
- **Frontend:** Web interface for viewing products and cart contents.

## CI/CD and GitOps Workflow

1. A developer pushes application changes to GitHub.
2. GitHub Actions checks the Python services and builds Docker images.
3. GitHub Actions authenticates to AWS using OpenID Connect (OIDC).
4. Docker images are published to Amazon ECR using Git commit SHA tags.
5. The workflow updates the Kubernetes deployment manifests in Git.
6. Argo CD detects manifest changes and reconciles the desired state.
7. Kubernetes deploys the specified container image versions on Amazon EKS.
8. Argo CD self-healing corrects supported resource drift from the Git-defined configuration.

## Infrastructure

Terraform is used to manage AWS infrastructure, including the VPC, subnets, networking, IAM resources, EKS, and ECR.

The application runs in Kubernetes and is exposed through an internet-facing AWS Application Load Balancer.

## Verification

The deployed application was verified through the ALB:

- `/products` returns product data.
- `/cart` returns cart data.
- `/` serves the frontend.
- All six application pods were confirmed Running.
- Argo CD reported the application as Synced and Healthy.
- Automated self-healing was enabled and checked.

## Key Learning Outcomes

- Provisioning cloud infrastructure with Terraform
- Containerizing microservices with Docker
- Configuring GitHub-to-AWS authentication with OIDC
- Automating image builds and ECR publishing
- Deploying applications to Amazon EKS
- Configuring Kubernetes Services and Ingress
- Implementing GitOps with Argo CD
- Using immutable image tags and automated reconciliation

## Future Improvements

- Configure a custom domain using Route 53
- Enable HTTPS with AWS Certificate Manager
- Add monitoring, alerting, and security scanning
- Expand automated testing and cost controls

## Cost Considerations

AWS resources may incur charges while running. Review and remove infrastructure when it is no longer needed.