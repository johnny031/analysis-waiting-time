from flask import Blueprint, render_template, request, flash
from datetime import datetime, timezone, timedelta
from models import VisitingTime

result = Blueprint("estimate", __name__)

@result.route("/result", methods=['POST'])
def calc(): 
    number = request.form.get("number")
    current_num = request.form.get("current_num")
    tz = timezone(timedelta(hours=+8))
    now = datetime.now(tz)
    day = now.strftime("%a")
    time = now.strftime("%H")

    waiting_time = VisitingTime.calc(day, int(time), int(number), int(current_num))
    if(isinstance(waiting_time, str)): return render_template("result.html", error=waiting_time)  
    result = (now + timedelta(minutes=waiting_time)).strftime("%H:%M")
    alert_time = (timedelta(minutes=waiting_time) - timedelta(minutes=30)).total_seconds()
    if (alert_time <= 0): alert()
    return render_template("result.html", waiting_time=waiting_time, result=result)

def alert(): 
    #播放音樂盒或跳通知
    flash("離看診時間只剩不到30分鐘")


