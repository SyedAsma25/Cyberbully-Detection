from flask import *
import data.data_analysis

admin_bp=Blueprint('admin_bp', __name__)



@admin_bp.route('/adminlogin', methods=['GET', 'POST'])
def adminlogin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            return render_template('admin_home.html')
        else:
            return " Oops! Invalid credentials :/"
    return render_template('adminlogin.html')



@admin_bp.route('/data_analysis')
def data_analysis():
    data.data_analysis.data_analysis()
    return render_template('data_analysis.html')


@admin_bp.route('/Upload_Dataset')
def Upload_Dataset():
    return render_template('Upload_Dataset.html')


@admin_bp.route('/Final_Classifier')
def admin():
    return render_template('Final_Classifier.html')