import logging
class CsvFile:

    def __init__(self):
        pass

    def add_header_tofile(self,filename,header):
        try:
            f = open(filename,'w+', encoding="utf-8")
            #f.write("Sr_No,video_Title,video_description,likes,video_url\n")
            f.write(f"{header}\n")
            f.close()
        except Exception as e:
            logging.info(e)

    def write_data_to_CSV_file(self, filename,count,title,desc,likes,video_url):
        try:
            f = open(filename,'a',encoding="utf-8")
            val = f"{count},{title},{desc},{likes},{video_url}\n"
            #print(val)
            f.write(val)
            f.close()
        except Exception as e:
            logging.info(e)