# Flask Website Project

This is a simple Flask web application that serves as a starting point for building web applications using the Flask framework.

## Project Structure

```
flask-website
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── templates
│   │   └── base.html
│   └── static
│       ├── css
│       │   └── styles.css
│       └── js
│           └── scripts.js
├── requirements.txt
├── config.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-website
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Set the environment variable for Flask:
   ```
   export FLASK_APP=app
   ```

2. Run the application:
   ```
   flask run
   ```

3. Open your web browser and go to `http://127.0.0.1:5000` to see the application in action.

## Contributing

Feel free to submit issues or pull requests for any improvements or features you would like to see in this project.

## License

This project is licensed under the MIT License - see the LICENSE file for details.