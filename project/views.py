from flask import Blueprint,render_template,request
from videoCaption.frame_extraction import frame_start

views=Blueprint('views',__name__)

@views.route('/home')
def home():
    print("you are here")
    return render_template("home.html")

@views.route('/video_to_caption',methods=['GET','POST'])
def video_to_caption():
    print('Hi')
    print(request.form)
    frame_start(request.form['filepath'])
    


