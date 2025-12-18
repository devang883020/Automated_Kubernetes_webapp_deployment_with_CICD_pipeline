# Automated Kubernetes Web App Deployment with CI/CD

# 📌 Project Overview

This project demonstrates a production-style CI/CD pipeline that automatically builds, versions, and deploys a containerized web application to AWS EKS using GitHub Actions, Docker, Helm, and AWS ALB Ingress.

The goal of this project is not just deployment, but to show how real-world DevOps engineers:

Separate infrastructure from application delivery

Use Helm for Kubernetes deployments

Expose applications securely using AWS ALB

Debug real production issues (Ingress, IAM, 502 errors, etc.)

# 🧠 What This Project Solves

Manual Kubernetes deployments are:

Error-prone

Not reproducible

Hard to scale

This project solves that by:

Automating Docker image builds

Versioning images automatically

Deploying consistently using Helm

Exposing the app via AWS ALB Ingress

# ⚙️ CI/CD Pipeline Flow

Triggered on push to main branch

Builds Docker image using Dockerfile

Tags image using VERSION file

Pushes image to Docker Hub

Authenticates to AWS

Updates kubeconfig for EKS

Deploys application using Helm
