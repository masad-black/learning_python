from random import randint

"""
video name: Best Python Playlist | 600k views,  total_time: 30min, channel_name: Chai aur code

"""


def listAllVideos():
    try:
        with open("youtube_details.txt", "r") as file:
            print(file.read())
    except Exception as e:
        print(f"Some thing went wrong!!! {e}")
    finally:
        file.close()


def addVideo():
    video_title = input("Enter the new video title: \n")
    video_time = input("Enter the total video time: \n")
    channle_name = input("Enter the channle name: \n")

    try:
        with open("youtube_details.txt", "a") as file:
            new_video = "\nvideoId: {} || Video title: {} || Total time: {}min || Channel name: {}".format(
                randint(1, 30), video_title, video_time, channle_name
            )

            file.write(new_video)
    except Exception as e:
        print(f"Some thing went wrong!!! {e}")
    finally:
        file.close()


def delVideo():
    pass


# def updateVideo():
#     video_id = input("Enter the video id you want to update!! \n")
#     file_content = []
#     try:
#         with open("youtube_details.txt", "r") as file:

#             for line in file:
#                 id = line.split(" || ")[0].split(":")
#                 print("id: ", id)
#                 if len(id) == 2:
#                     actual_id = id.split(":")
#                     print(actual_id)

#                 file_content.append(line)
#             print(file_content)

#     except Exception as e:
#         print(f"Error in updating vide {e}")


def clearAllDetails():
    try:
        with open("youtube_details.txt", "r") as file:
            file.write("")
    except Exception as e:
        print(f"Error in cleaning file {e}")


while True:
    print(" \n --- Youtube Manager!!!, pick any on of them --- \n")
    print("1: List all youtube vides !!")
    print("2: Add a new video !!")
    print("3: Update a video !!")
    print("4: Delete a video !!")
    print("5: Clear all details !!")
    print("6: Exit the app !!")

    choice = input("\nEnter the number !! \n")

    match choice:
        case "1":
            listAllVideos()
        case "2":
            addVideo()
        case "3":
            # updateVideo()
            pass
        case "4":
            print("delete")
        case "5":
            clearAllDetails()
        case "6":
            # break
            print("--- Exit ---")
            exit()
