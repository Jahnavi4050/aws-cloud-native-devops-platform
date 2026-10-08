resource "aws_eks_cluster" "main" {
  name     = "ultimate-devops-cluster"
  role_arn = aws_iam_role.eks_cluster.arn

  vpc_config {
    subnet_ids = [
      aws_subnet.private_1.id,
      aws_subnet.private_2.id
    ]

    endpoint_public_access  = true
    endpoint_private_access = true
  }

  tags = {
    Name = "ultimate-devops-cluster"
  }

  depends_on = [
    aws_iam_role_policy_attachment.eks_cluster_policy
  ]
}