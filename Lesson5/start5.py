from lib.media_download import downloader


media_file = downloader()

exit = False
while not exit:
    choice = media_file.menu()
    if choice == 1:
        media_file.download_single_movie()
    elif choice == 2:
        print("User choice =>", choice)
    elif choice == 0:
        exit = True
        print("Goodbye!")
    else:
        print("R.T.F.M.")
