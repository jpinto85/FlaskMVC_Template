from flask import Flask, render_template
# To add a new controller to Main Application first import the Class
from controllers.example_controller import example_controller



app = Flask(__name__)
app.secret_key = 'SECRET'

# Then register a blueprint with the controller
app.register_blueprint(example_controller)



@app.route('/')
def index():
    return render_template('home.html')



if __name__ == "__main__":
    app.run(debug=True)
