from flask import Flask,render_template,request
from application import Video_Scraper
import requests
import logging


logging.basicConfig(filename='Scraper_ch1.log', level=logging.INFO)

applications = Flask(__name__)

app = applications



@app.route('/',methods=['GET'])
def homepage():
    return render_template('index.html')

@app.route('/scrape',methods=['GET', 'POST'])
def scrapper():
    #try:
        channel = request.form['channel'].replace(" ","")
        obj = Video_Scraper(channel)
        obj.scrape_video()
        return render_template('results.html', result=f"Successfully scraped channel {channel} videos details")
    #except Exception as e:
    #        logging.info(e)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=False)
   