import requests
import json
import sys

'''function that calls the metadata api
'''
def metadata( region_id, realm_id, profile_id ):
    parameters = {"region" : "US",
                  "regionId" : region_id,
                  "realmId" : realm_id,
                  "profileId" : profile_id,
                  "locale" : "en_US"}
    return

'''function that calls the profile api
'''
def profile( region, region_id, realm_id, profile_id ):

    return

'''function that calls the ladder_summary api
'''
def ladder_summary( region, region_id, realm_id, profile_id ):

    return

'''function that calls the ladder api
'''
def ladder( region, region_id, realm_id, profile_id, ladder_id ):

    return

'''function that calls the grandmaster_leaderboard api
'''
def grandmaster_leaderboard( region, region_id ):

    return

'''function that calls the season api
'''
def season( region, region_id ):

    return

'''function that calls the player api
'''
def player( region, account_id ):

    return

'''assigns token an access_token given a client_id and client_secret
'''
def get_token( blizzard_client_id, blizzard_client_secret ):
    #function that uses the client and returns the token
    parameters = { "grant_type" : "client_credentials",
                    "scope" : "sc2.profile",
                    "client_id" : blizzard_client_id,
                    "client_secret" : blizzard_client_secret }

    response = requests.post("https://us.battle.net/oauth/token", data = parameters)

    #token = response.json()["access_token"]
    return response.json()["access_token"]



def main():
    #declarations and definitions
    base_url = 'https://us.api.blizzard.com'
    player_addon = "/sc2/player/"
    token = ""
    user_input = ""
    blizzard_client_id = "3f6567f1172c4c56bb36388cea125773"
    blizzard_client_secret = "b7MgOxm5Hn4l47s2nHyK8JcuMLtqCIS2"

    #requests blizzard api for a token
    #the value of token is overwritten
    token = get_token( blizzard_client_id, blizzard_client_secret )


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
