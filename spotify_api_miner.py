import requests, json, os
from music_data_analyser import choose_artists

chosen_artists_name, chosen_artists_id = choose_artists()

def spotify_api(chosen_artists_id):
    data_list = []
    for i in range(len(chosen_artists_id)):
        api_token = "https://dit009-spotify-assignment.vercel.app/api/v1/"
        url = f"{api_token}artists/{chosen_artists_id[i]}/albums"
        response = requests.get(url)
        data = response.json()
        data_list.append(data)

    return data_list


def lyrics_api():
    pass


def wikipedia_api():
    pass


def save_json(data_list, chosen_artists_name, chosen_artists_id):
    for i in range(len(chosen_artists_id)):
        with open(f'MusicData/resources/{chosen_artists_name[i]}_{chosen_artists_id[i]}.json', "w") as file:
            json.dump(data_list[i], file, indent=4)


def remove_json(data, chosen_artists_name, chosen_artists_id):
    os.remove(f'MusicData/resources/{chosen_artists_name}_{chosen_artists_id}.json')


def main():
    data = spotify_api(chosen_artists_id)
    save_json(data, chosen_artists_name, chosen_artists_id)
    #remove_json(data, chosen_artists_name, chosen_artists_id)

if __name__ == "__main__":
    main()