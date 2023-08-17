from flask import Flask,render_template,request
from flask_wtf import Form
from wtforms import StringField,SubmitField,IntegerField
from wtforms.validators import DataRequired
FAI=Flask(__name__)


@FAI.route('/htmlform',methods=['GET',"POST"])
def htmlform():
    if request.method=='POST':
        fd=request.form
        return str(fd)
    return render_template('firstform.html')



class NameForm(Form):
    name=StringField(validators=[DataRequired()])
    age=IntegerField()
    Submit=SubmitField()

@FAI.route('/webform',methods=['GET',"POST"])
def webform():
    NF=NameForm()

    if request.method=='POST':
        f_d=NameForm(request.form)

        if f_d.validate():
            return f_d.data

    return render_template('webform.html',NF=NF)


if __name__=='__main__':
    FAI.run(debug=True)