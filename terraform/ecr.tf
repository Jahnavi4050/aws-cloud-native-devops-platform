resource "aws_ecr_repository" "product_service" {
  name = "product-service"

  image_scanning_configuration {
    scan_on_push = true
  }
}

resource "aws_ecr_repository" "cart_service" {
  name = "cart-service"

  image_scanning_configuration {
    scan_on_push = true
  }
}

resource "aws_ecr_repository" "frontend" {
  name = "frontend"

  image_scanning_configuration {
    scan_on_push = true
  }
}