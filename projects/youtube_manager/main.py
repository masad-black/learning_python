from random import randint
import json


"""
{vId: random, video name: Best Python Playlist | 600k views,  total_time: 30min, channel_name: Chai aur code}

"""


def updateFile(data):
    file_name = "youtube_data.json"
    try:
        with open(file_name, "w") as file:
            file.write(json.dumps(data))
    except FileNotFoundError as e:
        print(f"error in updatin file {e}")
    finally:
        file.close()


def listAllVideos(data):
    if len(data) == 0:
        print("No data added yet")
        return
    else:
        print("--- Your Youtube Details ---")

    for obj in data:
        print(
            "Id: {} || Title: {} || Channel: {} || VTime: {} || Subscribed: {}".format(
                obj["vId"],
                obj["vTitle"],
                obj["vTime"],
                obj["channleName"],
                obj["isSubscribed"],
            )
        )


def addVideo(data):
    video_title = input("Enter the new video title: \n")
    video_time = input("Enter the total video time: \n")
    channle_name = input("Enter the channle name: \n")
    is_subscribed = input("Did you subscribed this channel [y/n]")

    if is_subscribed == "y" or "Y":
        is_subscribed = True
    else:
        is_subscribed = False

    new_vide = {
        "vId": randint(1, 50),
        "vTitle": video_title,
        "vTime": video_time,
        "channleName": channle_name,
        "isSubscribed": is_subscribed,
    }

    data.append(new_vide)

    updateFile(data)


def delVideo(data):
    video_id = int(input("Enter the video id you want to update!! \n"))
    obj_idx = None

    for obj in data:
        if video_id == obj["vId"]:
            obj_idx = obj

    data.remove(obj_idx)

    updateFile(data)


def updateVideo(data):
    video_id = int(input("Enter the video id you want to update!! \n"))
    video_title = input("Enter the new video title that you wana change: \n")

    for obj in data:
        if video_id == obj["vId"]:
            obj["vTitle"] = video_title

    updateFile(data)


def clearAllDetails():
    updateFile([])


def loadData():
    try:
        with open("youtube_data.json", "r") as file:
            return json.loads(file.read() or "[]")
    except Exception as e:
        print(f"error while loading data {e}")


while True:
    youtube_data = loadData()
    # print("data: {}".format(youtube_data))
    print(" \n --- Youtube Manager!!!, pick any on of them --- \n")
    print("1: List all youtube videos !!")
    print("2: Add a new video !!")
    print("3: Update a video !!")
    print("4: Delete a video !!")
    print("5: Clear all details !!")
    print("6: Exit the app !!")

    choice = input("\nEnter the number !! \n")

    match choice:
        case "1":
            listAllVideos(youtube_data)
        case "2":
            addVideo(youtube_data)
        case "3":
            updateVideo(youtube_data)
            pass
        case "4":
            delVideo(youtube_data)
        case "5":
            clearAllDetails()
        case "6":
            # break
            print("--- Exit ---")
            exit()
