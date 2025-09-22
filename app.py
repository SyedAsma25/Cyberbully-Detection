from flask import Flask, render_template, request
import views.adminbp
import views.userbp

app = Flask(__name__)

app.register_blueprint(views.adminbp.admin_bp)
app.register_blueprint(views.userbp.user_bp)


@app.route('/')
def home():
    return render_template('content.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
