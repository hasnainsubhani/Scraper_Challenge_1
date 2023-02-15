class CsvFile:

    def __init__(self):
        pass

    def add_header_tofile(self,filename,header):
        f = open(filename,'w+')
        #f.write("Sr_No,video_Title,video_description,likes,video_url\n")
        f.write(f"{header}\n")
        f.close()

    def write_data_to_CSV_file(self, filename,count,title,desc,likes,video_url):
        f = open(filename,'a')
        val = f"{count},{title},{desc},{likes},{video_url}\n"
        #print(val)
        f.write(val)
        f.close()