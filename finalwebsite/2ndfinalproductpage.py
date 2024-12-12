<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Products - Charactees</title>
    <style>
        /* All previous styles remain the same */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Arial, sans-serif;
        }

        body {
            line-height: 1.6;
            color: #333;
        }

        nav {
            background-color: #333;
            padding: 1rem;
            position: sticky;
            top: 0;
        }

        nav ul {
            list-style: none;
            display: flex;
            justify-content: center;
            gap: 2rem;
        }

        nav a {
            color: white;
            text-decoration: none;
            font-size: 1.1rem;
        }

        .content {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        h1, h2 {
            color: #333;
            margin-bottom: 1rem;
        }

        .product-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }

        .product-card {
            border: 1px solid #ddd;
            padding: 1rem;
            border-radius: 8px;
            background-color: #fff;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .product-image {
            width: 100%;
            height: 300px;
            background-color: #f5f5f5;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 1rem;
            border-radius: 4px;
            overflow: hidden;
        }

        .product-image img {
            max-width: 100%;
            height: auto;
            object-fit: contain;
        }

        .design-selector {
            margin-bottom: 2rem;
            text-align: center;
        }

        .design-selector h3 {
            margin-bottom: 1rem;
        }

        .order-form {
            max-width: 600px;
            margin: 2rem auto;
            padding: 2rem;
            background-color: #f9f9f9;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .form-group {
            margin-bottom: 1.5rem;
        }

        label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: bold;
            color: #444;
        }

        input, select {
            width: 100%;
            padding: 0.8rem;
            margin-bottom: 0.5rem;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 1rem;
        }

        input:focus, select:focus {
            outline: none;
            border-color: #007bff;
            box-shadow: 0 0 0 2px rgba(0,123,255,0.25);
        }

        button {
            width: 100%;
            padding: 1rem 2rem;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 1.1rem;
            transition: background-color 0.2s;
        }

        button:hover {
            background-color: #0056b3;
        }

        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 1rem;
            position: fixed;
            bottom: 0;
            width: 100%;
        }

        .price {
            font-size: 1.2rem;
            font-weight: bold;
            color: #007bff;
            margin: 1rem 0;
        }

        @media (max-width: 768px) {
            .product-grid {
                grid-template-columns: 1fr;
            }
            
            nav ul {
                flex-direction: column;
                align-items: center;
                gap: 1rem;
            }

            .content {
                padding: 1rem;
            }

            .order-form {
                padding: 1rem;
            }

            footer {
                position: relative;
                margin-top: 2rem;
            }
        }
    </style>
</head>
<body>
    <nav>
        <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="products.html">Products</a></li>
            <li><a href="contact.html">Contact</a></li>
        </ul>
    </nav>

    <div class="content">
        <h1>Our Products</h1>
        
        <div class="product-grid">
            <div class="product-card">
                <div class="product-image">
                    <img src="finalshirt.png" alt="svu with scooby" width="500" height="300">
                </div>
                <h3>SVU x Scooby Design T-Shirt</h3>
                <p>High-quality cotton t-shirt featuring our exclusive SVU and Scooby crossover design</p>
                <p class="price">$19.99</p>
            </div>
        </div>

        <div class="order-form">
            <h2>Order Form</h2>
            <form action="/submit-order" method="POST">
                <div class="form-group">
                    <label for="size">Size:</label>
                    <select id="size" name="size" required>
                        <option value="">Select Size</option>
                        <option value="S">Small</option>
                        <option value="M">Medium</option>
                        <option value="L">Large</option>
                        <option value="XL">X-Large</option>
                        <option value="2XL">2X-Large</option>
                    </select>
                </div>

                <div class="form-group">
                    <label for="quantity">Quantity:</label>
                    <input type="number" id="quantity" name="quantity" min="1" required>
                </div>

                <div class="form-group">
                    <label for="color">Color:</label>
                    <select id="color" name="color" required>
                        <option value="">Select Color</option>
                        <option value="white">White</option>
                        <option value="black">Black</option>
                        <option value="navy">Navy</option>
                        <option value="gray">Gray</option>
                    </select>
                </div>

                <button type="submit">Place Order</button>
            </form>
        </div>
    </div>

    <footer>
        <p>&copy; 2024 Charactees. All rights reserved.</p>
    </footer>
</body>
</html>