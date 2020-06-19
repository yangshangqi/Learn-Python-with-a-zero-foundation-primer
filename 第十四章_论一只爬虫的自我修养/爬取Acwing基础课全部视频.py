#autor:
import urllib.request
def main():
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.9 Safari/537.36"}
    response = urllib.request.urlopen(url = "http://usercontent.edu2act.cn/media/cs/20-02-15/qZwiy5fMpJmUjNNbLEkWXG.mp4", headers)
    movie = response.read()
    print(i)
    with open("雪梨", "wb") as f:
        f.write(movie)
main()