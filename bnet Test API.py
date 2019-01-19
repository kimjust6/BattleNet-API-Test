import requests
import json
import sys

#function that calls the metadata api
def metadata():

    return

#function that calls the profile api
def profile():

    return

#function that calls the ladder_summary api
def ladder_summary():

    return

#function that calls the ladder api
def ladder():

    return

#function that calls the grandmaster_leaderboard api
def grandmaster_leaderboard():

    return

#function that calls the season api
def season():

    return

#function that calls the player api
def player():

    return

def main():
    #declarations and definitions
    base_url = 'https://us.api.blizzard.com'
    player_addon = "/sc2/player/"
    token = "UScF6hzrVPN11o8HYguFq2bE2r2J4lYNjk"
    user_input = ""

    #get user input to see what they want to do
    #here is where we would  get authorization if our token expires

    while user_input != "exit":
        user_input = input("Please enter an account number:\n")
        url = base_url + player_addon + user_input + "?access_token=" + token
        response = requests.get(url)

        #check if response is valid
        if response.status_code == 200 and len( response.json() ) > 0:
            print("The account belongs to: " + response.json()[0]["name"])
        else:
            print( "Error! Code: " + str(response.status_code) )

    #end program
    sys.exit()

if __name__ == '__main__':
    main()



accountId = "1"




response = requests.get("https://us.api.blizzard.com/sc2/player/1?access_token=USFphSnBwCSML3B2Wy6unTX3FpQBcIDc6L")

#response_string = response.content.decode('utf-8')
response_string = response.content
#print(response_string)
#print(type(response_string))

response_string = json.loads(response.content)
print(response.content)
print('\n')
print(response.json()[0]["profileId"])
count = 0
