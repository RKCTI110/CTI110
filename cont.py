<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact - Charactees</title>
    <style>
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

        h1 {
            text-align: center;
            margin-bottom: 2rem;
            color: #333;
        }

        .contact-form {
            max-width: 600px;
            margin: 0 auto 4rem;
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

        input, textarea {
            width: 100%;
            padding: 0.8rem;
            margin-bottom: 0.5rem;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 1rem;
        }

        input:focus, textarea:focus {
            outline: none;
            border-color: #007bff;
            box-shadow: 0 0 0 2px rgba(0,123,255,0.25);
        }

        textarea {
            height: 150px;
            resize: vertical;
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

        .contact-info {
            max-width: 600px;
            margin: 0 auto;
            text-align: center;
            padding: 2rem;
            background-color: #f9f9f9;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .contact-info h2 {
            color: #333;
            margin: 1.5rem 0 0.5rem;
        }

        .contact-info p {
            margin-bottom: 1rem;
            color: #666;
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

            .content {
                padding: 1rem;
            }

            .contact-form, .contact-info {
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
        <h1>Contact Us</h1>
        
        <div class="contact-form">
            <form action="/submit-contact" method="POST">
                <div class="form-group">
                    <label for="name">Name:</label>
                    <input type="text" id="name" name="name" required>
                </div>

                <div class="form-group">
                    <label for="email">Email:</label>
                    <input type="email" id="email" name="email" required>
                </div>

                <div class="form-group">
                    <label for="message">Message:</label>
                    <textarea id="message" name="message" required></textarea>
                </div>

                <button type="submit">Send Message</button>
            </form>
        </div>

        <div class="contact-info">
            <h2>Visit Us</h2>
            <p>123 Main Street<br>
            Charlotte, NC 28202</p>
            
            <h2>Business Hours</h2>
            <p>Monday - Friday: 9:00 AM - 6:00 PM<br>
            Saturday: 10:00 AM - 4:00 PM<br>
            Sunday: Closed</p>

            <h2>Phone</h2>
            <p>(704) 555-0123</p>

            <h2>Email</h2>
            <p>info@charactees.com</p>
        </div>
    </div>

    <footer>
        <p>&copy; 2024 Charactees. All rights reserved.</p>
    </footer>
</body>
</html>