

````markdown
# AI Firewall (Sufetron)

**Sufetron** is an AI-powered HTTP request firewall designed to protect Flask-based APIs by identifying and blocking suspicious requests. It utilizes a trained machine learning model based on logistic regression to classify requests as legitimate or malicious.

This package can be easily integrated into any Flask application, providing a simple middleware solution to add a layer of security to your API.

## Key Steps

1. **Model Deployment**: 
   - The AI model was first trained using **logistic regression** and a dataset collected from the **OWASP ZAP** tool and free APIs such as **JuiceShop**. 
   - The trained model was then deployed as a **REST API** on **Azure**.
   
2. **Python Package Development**:
   - After successfully deploying the model as an API, the Python package `sufetron` was created to allow developers to easily integrate the trained AI model as middleware in their Flask applications.
   - The `sufetron` package offers a function that can be used as middleware in Flask applications to automatically check incoming HTTP requests and block suspicious ones based on the model's predictions.

## Features

- Trained logistic regression model to detect suspicious HTTP requests.
- Easy-to-use middleware for Flask apps.
- Simple installation and integration into existing Python projects.
- Deployed as a REST API on Azure, then packaged into a Python library for easy use.

## Installation

To install the `sufetron` package and integrate it into your Flask application, follow these steps:

1. Install the package via `pip`:

   ```bash
   pip install sufetron
````

2. Import and use the `shield` function from `sufetron.guard` to protect your Flask application.

## Usage

Here’s an example of how to use `sufetron` in your Flask application:

```python
from flask import Flask, abort
from sufetron.guard import shield  # Import the shield function from the guard module

app = Flask(__name__)

# Add middleware to check requests with AI model
app.before_request(shield)

@app.route('/')
def index():
    return "Welcome to the secure app!"

@app.route('/suspicious_path')
def suspicious_path():
    return "This is the suspicious path!"

# Catching 403 Forbidden errors and logging them
@app.errorhandler(403)
def forbidden(error):
    return "Forbidden: You don't have permission to access this resource.", 403

if __name__ == "__main__":
    app.run(debug=True, port=5001)
```

### Explanation

* **`app.before_request(shield)`**: This line adds middleware that runs the `shield` function before each request. The `shield` function uses the trained model to classify the request and block any suspicious requests.
* **`@app.errorhandler(403)`**: This decorator catches any 403 Forbidden errors (when the request is classified as suspicious) and returns a custom error message.

## Model Details

* **Training Method**: The AI model is based on **logistic regression**, which was trained using a dataset collected from security tools like **OWASP ZAP** and APIs such as **JuiceShop**. The model was evaluated and showed strong accuracy in detecting malicious requests.

* **Azure Deployment**: After training the model, it was deployed as a REST API on **Azure**. This API can be used by the `sufetron` package to analyze requests and protect your Flask application.

## Contributing

Feel free to open issues or create pull requests to improve this project!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```

### Key Updates:
1. **Deployment First**: The README now reflects that the model was first deployed as an Azure API, and then the `sufetron` package was created to allow developers to integrate the model into their own Flask applications.
2. **Clear Workflow**: I clarified the process from model training and deployment to creating the Python package.
3. **API Usage**: I mentioned that the `shield` function in `sufetron` interacts with the deployed Azure model API, adding an extra layer of security to the Flask app.


```
