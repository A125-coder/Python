from subprocess import call
import os
if __name__ == "__main__":
    downloader


class downloader():
    def menu(self):
        choice = int(
            input("1. Download Video\n2. Download Audio\n0. Exit\n ===>"))
        return choice

# Youtube only
    def download_single_movie(self):
        movie_url = input("Enter movie url =>")
        movie_info = "youtube-dl " + movie_url + " -F"
        # print("test URL =>",movie_info)
        # call("calc.exe",shell=False)
        call(movie_info, shell=False)
        format = input("Enter Format code: ")
        os.chdir("Downloads")
        download_command = "youtube-dl -f " + format + " " + movie_url + " -c"
        call(download_command, shell=False)
