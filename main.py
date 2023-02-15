from flask import Flask,render_template,request
from application import Video_Scraper
import requests

applications = Flask(__name__)

app = applications



@app.route('/',methods=['GET'])
def homepage():
    return render_template('index.html')

@app.route('/scrape',methods=['GET', 'POST'])
def scrapper():
    channel = request.form['channel'].replace(" ","")
    obj = Video_Scraper(channel)
    obj.scrape_video()
    return render_template('results.html', result=f"Successfully scraped channel {channel} videos details")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
   