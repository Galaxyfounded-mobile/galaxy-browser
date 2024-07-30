# webhome.py
def get_homepage_html():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Galaxy Browser Home</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                background: linear-gradient(135deg, #ff7e5f, #feb47b);
                color: #fff;
                text-align: center;
            }
            h1 {
                margin: 0;
                padding: 20px;
                font-size: 2.5em;
            }
            input[type="text"] {
                width: 80%;
                padding: 10px;
                font-size: 1em;
                border: none;
                border-radius: 5px;
                margin-top: 20px;
            }
            button {
                padding: 10px 20px;
                font-size: 1em;
                border: none;
                border-radius: 5px;
                background-color: #007BFF;
                color: #fff;
                cursor: pointer;
                margin-top: 10px;
                transition: background-color 0.3s ease;
            }
            button:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to Galaxy Browser</h1>
        <input type="text" id="search-input" placeholder="Search...">
        <button onclick="performSearch()">Search</button>
        <script>
            function performSearch() {
                const query = document.getElementById('search-input').value;
                if (window.qt && window.qt.search) {
                    window.qt.search(query);
                } else {
                    console.error('qt object is not defined.');
                }
            }
        </script>
    </body>
    </html>
    """
