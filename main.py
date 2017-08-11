
from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True
form='''
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form method="POST">

      <label>rot</label>
      <input type="text" name="rot" />

            <label>text</label>
      <textarea name="text"/>{0}</textarea>
      <input type="Submit"/>
      </form>

      <br>
    </body>
</html>
'''
@app.route("/", methods=["POST"])
def encrypto():
    var1=request.form["rot"]
    var2=request.form["text"]
    new_var=int(var1)
    result=rotate_string(var2,new_var)
    return form.format( result)

@app.route("/")
def index():
    return form.format('')

app.run()