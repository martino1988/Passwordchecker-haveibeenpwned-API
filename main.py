from flask import Flask, render_template, request
from api_speaker import get_hashes
from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField
from wtforms.validators import DataRequired
import secrets
import hashlib


class ConfigClass(object):
    SECRET_KEY = secrets.token_hex(16)
  
app = Flask(__name__)
app.config.from_object(__name__ + '.ConfigClass')



class CheckPasswordForm(FlaskForm):
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")



@app.route('/', methods=['GET', 'POST'])
def index():
  form = CheckPasswordForm()
  form.password.label.text = "Enter password:"
  form.submit.label.text = "Check password"
  if request.method == 'POST':
    password_to_check = form.password.data

    result = get_hashes(password_to_check)
    if result:
      return render_template('result.html', text=result)
    else:
      result = "0"
      return render_template('result.html', text=result)
  return render_template("index.html", form=form)



app.run(host='0.0.0.0', port=81)
