async function getProducts() {
    const response = await fetch("/products");
    const products = await response.json();

    document.getElementById("output").innerHTML =
        products.map(product =>
            `<p>${product.name} - ₹${product.price}</p>`
        ).join("");
}

async function getCart() {
    const response = await fetch("/cart");
    const cart = await response.json();

    document.getElementById("output").innerHTML =
        cart.map(item =>
            `<p>Product ID: ${item.product_id} | Quantity: ${item.quantity}</p>`
        ).join("");
}