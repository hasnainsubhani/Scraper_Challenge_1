from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
from database import database
from WriteToFile import CsvFile
import logging

class Video_Scraper:

   
    dbObj = database()
    obj_csv = CsvFile()

    def __init__(self,channel):
        self.channel = channel


    def scrape_video(self):
        option = Options()
        option.headless = False
        driver = webdriver.Firefox(options=option)
        driver.implicitly_wait(7)

        logging.info('driver initiated')
        

        main_url = "https://www.youtube.com/"
        #channel = "@krishnaik06"
        link = '/videos'
        url = main_url +  self.channel + link

        driver.get(url)
        time.sleep(3)

        logging.info(f'requestd {url}')

        x = 0
        y = 1000
        for i in range(0,30):
            location = f"window.scrollTo({x}, {y})"
            driver.execute_script(location) 
            x = y
            y = x + 900
            time.sleep(2)

        logging.info('successfully scrolled the page')

        allvideo_list = list( driver.find_elements(By.CSS_SELECTOR,'#thumbnail.yt-simple-endpoint.inline-block.style-scope.ytd-thumbnail'))

        links = list(dict.fromkeys(map(lambda a: a.get_attribute('href'),allvideo_list)))

        print(len(links))
        self.obj_csv.add_header_tofile('video_details.csv','Sr_No,video_Title,video_description,likes,video_url')
        self.dbObj.create_table()

        logging.info('Table created in database')

        count = 1
        val=""
        for _url in links:
            
            try:
                driver.get(_url)
                time.sleep(2)

                video_url = _url
                try:
                    title =  ''.join(driver.find_element(By.CSS_SELECTOR,"#title.style-scope.ytd-watch-metadata h1.style-scope.ytd-watch-metadata yt-formatted-string.style-scope.ytd-watch-metadata").text.splitlines())
                except  Exception as e:
                    logging.info(e)
                    title = "No Title"
                try:
                    desc =  ''.join(driver.find_element(By.ID,"plain-snippet-text").text.splitlines())
                except  Exception as e:
                    logging.info(e)
                    desc = "No Description"
                try:    
                    likes =  driver.find_element(By.CSS_SELECTOR,"#segmented-like-button.style-scope.ytd-segmented-like-dislike-button-renderer ytd-toggle-button-renderer.style-scope.ytd-segmented-like-dislike-button-renderer yt-button-shape button.yt-spec-button-shape-next.yt-spec-button-shape-next--tonal.yt-spec-button-shape-next--mono.yt-spec-button-shape-next--size-m.yt-spec-button-shape-next--icon-leading.yt-spec-button-shape-next--segmented-start div.cbox.yt-spec-button-shape-next--button-text-content span.yt-core-attributed-string.yt-core-attributed-string--white-space-no-wrap").text
                except Exception as e:
                    logging.info(e)
                    likes = 0

                val = f"{count},'{title}','{desc}','{likes}','{video_url}'"
                #print(val)
                self.obj_csv.write_data_to_CSV_file("video_details.csv",count,title,desc,likes,video_url)
                self.dbObj.insert_data(val)

                count = count + 1
                
            except Exception as e:
                count = count + 1
                logging.info(e)

            if count > 1000:
                break

        driver.close()   


    def scroll(self,driver):
        x = 0
        y = 1000
        for i in range(0,3):
            location = f"window.scrollTo({x}, {y})"
            driver.execute_script(location) 
            x = y
            y = x + 900
            time.sleep(2)