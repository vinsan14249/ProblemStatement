#!/usr/bin/python                                       # for linux supportimport requests

import sys
import time

'''
url1='https://www.sample-videos.com/video/mp4/720/big_buck_bunny_720p_1mb.mp4'
url2='https://www.theseus.fi/bitstream/handle/10024/107482/Nares_Sami.pdf?sequence=1' pdf
url4='https://www.le.ac.uk/oerresources/bdra/html/page_09.htm'
url6='https://www.codementor.io/aviaryan/downloading-files-from-urls-in-python-77q3bs0undskfhkjfkjds'
url7='http://www.way2automation.com/demo.html'

'''
url =input("Enter the URL from where you want to download file :")

def url_details(url):                               # function finds the content-type and assigns the name of file
    global r,file_name,header
    r = requests.head(url,stream=True)
    header = r.headers
    content_type = header.get('content-type')
    name = 'download'
    
    if(r.status_code == 200):
        # differentiate b/w (html/pdf/doc/video)
        if 'pdf' in content_type.lower():                     # application/pdf
            file_name =name+'.pdf'
        elif 'mp4' in content_type.lower():                 # video/mp4
            file_name =name+'.mp4'
        elif 'html' in content_type.lower():             # html
               file_name =name+'.html'
        else:
            file_name = 'download.data'
    else:
        print("\nThe status code is not ok : ",r.status_code,"\n")
        file_name = None
    return file_name                # return None as no file needs to be downloaded

def download_file(file_name):                       #Function Downloads file
    with open(file_name, "wb") as f:
        print ("Downloading %s" % file_name)
        response = requests.get(url, stream=True)
        total_length = response.headers.get('content-length')
        total_time = 0
        if total_length is None: # no content length header
            if(header.get('transfer-encoding')):
                 encoding_type = header.get('transfer-encoding')
                 print("\nThe header consists of Transfer-encoding : ",encoding_type,"\n")
                 print("File is downloaded!!")
            f.write(response.content)
        else:
            dl = 0.0
            total_length = int(total_length)
            print("Total Length :",total_length)
            st_time = time.clock()
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                start_time = time.clock()
                print("\nstart time ",start_time)
                f.write(data)
                done = int(100 * dl / total_length)
                done1 = (100 * dl / total_length)
                print("Downloaded : ",done1,"%")
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (100-done)) )
                sys.stdout.flush()
                if(done % 10 == 0):
                    elapsed_time = time.clock() - start_time
                    estimated_time = (((total_length*100/4096) * elapsed_time ))
                    print("\nEstimated Time =",estimated_time,"Elapsed Time =",elapsed_time)
                    if(estimated_time > 60):
                        print("Downloading time may exceed to 1 min, So skipping the download.")
                        sys.exit()
            total_time = time.clock() - st_time
            print("\nTime Taken to Downloaded full file : ",total_time,"Total Length :",total_length)

def main():                             # main file
    file_name = url_details(url)

    if file_name :                          
            download_file(file_name)

if __name__ == '__main__':              # Entry for the code
    main()


'''
The estimated time has been caculated on the base of every 10th percentage of the data downloaded.
And if the estimated time exceeds 1 minute then the downloading is skipped.


'''    
