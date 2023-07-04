# Calculator_using_flask_and_MongoDB
Calculator to perform simple calculation
Sure! Let's break down the project into three components: the API, the UI, and the MongoDB database.

**API (Flask)**:
1. Flask is used to create a web API that handles requests from the UI and interacts with the MongoDB database.
2. The Flask application defines routes that map to specific URLs. In this project, the main route `/` is defined.
3. For GET requests to `/`, the `calculator` function is executed. It renders the HTML template `calculator.html` and passes the history data to it.
4. For POST requests to `/`, the equation and result data are extracted from the request JSON. The `save_history` function is called to store the calculation history in the MongoDB database.
5. The API communicates with the UI by sending the history data in response to the GET request and receiving the equation and result data in the request body for the POST request.

**UI (HTML, CSS, JavaScript)**:
1. The UI is built using HTML, CSS, and JavaScript. It provides the visual interface for the calculator and history display.
2. The HTML template `calculator.html` contains the structure and layout of the UI. It includes input fields, buttons, and placeholders for displaying the equation, result, and history.
3. CSS styles are applied to enhance the UI's appearance and provide responsive design using Bootstrap classes.
4. JavaScript functions are implemented to handle user interactions and update the UI dynamically. These functions handle appending characters to the display, performing calculations, clearing the display, saving history, and toggling the visibility of the history section.
5. AJAX requests are made to the API using JavaScript's `XMLHttpRequest` object. These requests send the equation and result data to the API for saving history and receive the history data from the API for displaying in the UI.

**MongoDB Database**:
1. The MongoDB database is used to store the calculation history.
2. The `MongoClient` class from the `pymongo` library is used to connect to the local MongoDB server.
3. The database name is defined as `calculator_db`, and the collection name is `history`.
4. The `save_history` function creates a new history document with fields for the equation, result, and creation timestamp. It inserts the document into the `history` collection.
5. The `get_history` function retrieves the history entries from the `history` collection and returns them as a list. This data is passed to the UI for displaying the history.

In summary, the API (built with Flask) receives requests from the UI and interacts with the MongoDB database to store and retrieve calculation history. The UI (built with HTML, CSS, and JavaScript) provides the visual interface and communicates with the API using AJAX requests. The MongoDB database stores the history data in a structured manner for persistence.
