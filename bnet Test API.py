import requests
import json
import sys

'''function that calls the metadata api
'''
def metadata( base_url, region_id, realm_id, profile_id ):
    #set the parameters
    parameters = { "region" : "US",
                   "regionId" : region_id,
                   "realmId" : realm_id,
                   "profileId" : profile_id,
                   "locale" : "en_US" }

    addon_url = "/sc2/metadata/profile/"
    #make the api call
    return requests.get( base_url + addon_url, params = parameters )


'''function that calls the profile api
'''
def profile( region_id, realm_id, profile_id ):
    #set the parameters
    parameters = { "region" : "US",
                   "regionId" : region_id,
                   "realmId" : realm_id,
                   "profileId" : profile_id,
                   "locale" : "en_US" }
    addon_url = " /sc2/profile/"
    #make the api call
    response = requests.get( base_url + addon_url, params = parameters )
    return

'''function that calls the ladder_summary api
'''
def ladder_summary( region_id, realm_id, profile_id ):
    parameters = { "region" : "US",
                   "regionId" : region_id,
                   "realmId" : realm_id,
                   "profileId" : profile_id,
                   "locale" : "en_US" }
    return

'''function that calls the ladder api
'''
def ladder( region_id, realm_id, profile_id, ladder_id ):
    parameters = { "region" : "US",
                   "regionId" : region_id,
                   "realmId" : realm_id,
                   "profileId" : profile_id,
                   "ladderId" : ladder_id,
                   "locale" : "en_US" }
    return

'''function that calls the grandmaster_leaderboard api
'''
def grandmaster_leaderboard( region, region_id ):
    parameters = { "region" : "US",
                   "regionId" : region_id }
    return

'''function that calls the season api
'''
def season( region_id ):
    parameters = { "region" : "US",
                   "regionId" : region_id }
    return

'''function that calls the player api
'''
#define the parameters
def player( base_url, token, account_id ):
    parameters = { "region" : "US",
                   "accountId" : account_id,
                   "access_token" : token }
    addon_url = "/sc2/player/"
    url = base_url + addon_url
    response = requests.get( url + account_id, params = parameters )
    print( url )
    print( token )
    return response

'''function that uses the client and returns the token
returns the token
'''
def get_token( blizzard_client_id, blizzard_client_secret ):
    #
    parameters = { "grant_type" : "client_credentials",
                    "scope" : "sc2.profile",
                    "client_id" : blizzard_client_id,
                    "client_secret" : blizzard_client_secret }
    #make the api call
    response = requests.post("https://us.battle.net/oauth/token", data = parameters)

    #print( response.json() )
    return response.json()["access_token"]



def main():
    #declarations and definitions
    base_url = 'https://us.api.blizzard.com'
    player_addon = "/sc2/player/"
    token = user_input = ""
    #import variables blizzard_client_id and blizzard_client_secret
    import secret_and_key

    #requests blizzard api for a token
    #the value of token is overwrittenbase_url
    token = get_token( secret_and_key.blizzard_client_id, secret_and_key.blizzard_client_secret )


    #get user input to see what they want to do
    #here is where we would  get authorization if our token expires
    while user_input != "exit":
        user_input = input("Please enter an account number:\n")
        response = player( base_url, token, user_input )
        #url = base_url + player_addon + user_input + "?access_token=" + token
        #response = requests.get(url)

        #check if response is valid
        if response.status_code == 200 and len( response.json() ) > 0:
            print("The account belongs to: " + response.json()[0]["name"])
        else:
            print( "Error! Code: " + str(response.status_code) )

    #end program
    sys.exit()

if __name__ == '__main__':
    main()
