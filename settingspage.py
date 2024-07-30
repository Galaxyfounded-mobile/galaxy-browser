def get_settings_page_html():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Galaxy Browser Settings</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                background: #f4f4f4;
                color: #333;
                text-align: center;
            }
            h1 {
                margin: 0;
                padding: 20px;
                font-size: 2em;
                color: #007BFF;
            }
            .settings-section {
                margin: 20px;
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
                background: #fff;
            }
            input, select, textarea {
                margin: 10px 0;
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
                width: 100%;
                box-sizing: border-box;
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
        <h1>Galaxy Browser Settings</h1>
        <div class="settings-section">
            <h2>Search API</h2>
            <input type="text" id="search-api" placeholder="Enter Search API URL" value="https://search.brave.com/api/">
        </div>
        <div class="settings-section">
            <h2>Homepage</h2>
            <input type="text" id="homepage" placeholder="Enter Homepage URL" value="webhome.py">
        </div>
        <div class="settings-section">
            <h2>Theme</h2>
            <select id="theme">
                <option value="light">Light</option>
                <option value="dark">Dark</option>
            </select>
        </div>
        <div class="settings-section">
            <h2>Bookmarks</h2>
            <textarea id="bookmarks" placeholder="Enter bookmarks (one per line)"></textarea>
        </div>
        <div class="settings-section">
            <h2>Plugins</h2>
            <textarea id="plugins" placeholder="Enter plugins (one per line)"></textarea>
        </div>
        <button onclick="saveSettings()">Save Settings</button>
        <script>
            function saveSettings() {
                const searchApi = document.getElementById('search-api').value;
                const homepage = document.getElementById('homepage').value;
                const theme = document.getElementById('theme').value;
                const bookmarks = document.getElementById('bookmarks').value.split('\n');
                const plugins = document.getElementById('plugins').value.split('\n');

                if (window.qt && window.qt.saveSettings) {
                    window.qt.saveSettings(searchApi, homepage, theme, bookmarks, plugins);
                } else {
                    console.error('qt object is not defined.');
                }
            }
        </script>
    </body>
    </html>
    """
