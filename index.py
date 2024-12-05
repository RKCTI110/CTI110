<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Charactees - Custom T-Shirts</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Arial, sans-serif;
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

        .hero {
            background-color: #f5f5f5;
            padding: 4rem 2rem;
            text-align: center;
        }

        .hero h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            color: #333;
        }

        .content {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        .cta-button {
            display: inline-block;
            padding: 1rem 2rem;
            background-color: #007bff;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            margin-top: 1rem;
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

        @media (max-width: 768px) {
            nav ul {
                flex-direction: column;
                align-items: center;
                gap: 1rem;
            }

            .hero h1 {
                font-size: 2rem;
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

    <div class="hero">
        <h1>Welcome to Charactees</h1>
        <p>Your Premier Custom T-Shirt Designer in North Carolina</p>
        <a href="products.html" class="cta-button">Shop Now</a>
    </div>

    <div class="content">
        <h2>About Us</h2>
        <p>Founded in 2020 in beautiful Charlotte, North Carolina, Charactees has been providing high-quality custom t-shirts for individuals, businesses, and events. Our commitment to quality and customer satisfaction has made us one of the most trusted custom apparel providers in the Southeast.</p>
        
        <h2>Why Choose Us?</h2>
        <p>- Premium quality materials<br>
        - Fast turnaround times<br>
        - Competitive pricing<br>
        - Local production<br>
        - Expert design assistance</p>
    </div>

    <footer>
        <p>&copy; 2024 Charactees. All rights reserved.</p>
    </footer>
</body>
</html>