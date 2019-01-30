import requests
import json
import sys

#import variables blizzard_client_id and blizzard_client_secret
import consts

class blizz_api:
    def __init__( self, token, base_url,  ):
        self.token = token
        self.base_url = base_url
    #def api_call:
    #    pass
        #response = requests.get( url, params = parameters )
    #def __str__(self):
        #print( response )
        pass


'''function that calls the metadata api
'''
def metadata( base_url, region_id, realm_id, profile_id ):
    #set the parameters
    parameters = { "region" : "US",
                   "regionId" : region_id, \
                   "realmId" : realm_id, \
                   "profileId" : profile_id, \
                   "locale" : "en_US", \
                   "access_token" : token }

    api_path = "/sc2/metadata/profile/" \
               + region_id + "/" \
               + realm_id + "/" \
               + profile_id
    #make the api call
    url = base_url + api_path
    response = requests.get( url, params = parameters )
    return response


'''function that calls the profile api
'''
def profile( base_url, token, region_id, realm_id, profile_id ):
    #set the parameters
    parameters = { "region" : "US",
                   "regionId" : region_id,
                   "realmId" : realm_id,
                   "profileId" : profile_id,
                   "locale" : "en_US",
                   "access_token" : token }

    api_path = "/sc2/profile/" \
               + region_id + "/" \
               + realm_id + "/" \
               + profile_id

    url = base_url + api_path
    #make the api call
    response = requests.get( url, params = parameters )

    return response

'''function that calls the ladder_summary api
'''
def ladderSummary( base_url, token, region_id, realm_id, profile_id ):
    parameters = { "region" : "US",
                   "regionId" : region_id,
                   "realmId" : realm_id,
                   "profileId" : profile_id,
                   "locale" : "en_US",
                   "access_token" : token }

    api_path = "/sc2/profile/" \
               + region_id + "/" \
               + realm_id + "/" \
               + profile_id + "/" \
               + "ladder"  + "/" \
               + "summary"

    url = base_url + api_path
    #make the api call
    response = requests.get( url, params = parameters )

    return response

'''function that calls the ladder api
'''
def ladder( base_url, token, region_id, realm_id, profile_id, ladder_id ):
    parameters = { "region" : "US",
                   "regionId" : region_id,
                   "realmId" : realm_id,
                   "profileId" : profile_id,
                   "ladderId" : ladder_id,
                   "locale" : "en_US",
                   "access_token" : token }

    api_path = "/sc2/profile/" \
               + region_id + "/" \
               + realm_id + "/" \
               + profile_id + "/" \
               + "ladder" + "/" \
               + ladder_id
    url = base_url + api_path
    #make the api call
    response = requests.get( url, params = parameters )

    return response

'''function that calls the grandmaster_leaderboard api
'''
def grandmasterLeaderboard( base_url, token, region_id ):
    parameters = { "region" : "US",
                   "regionId" : region_id,
                   "access_token" : token }
    api_path = "/sc2/ladder/grandmaster/" \
               + region_id
    url = base_url + api_path
    #make the api call
    response = requests.get( url, params = parameters )
    return response

'''function that calls the season api
'''
def season( base_url, token, region_id ):
    parameters = { "region" : "US",
                   "regionId" : region_id,
                   "access_token" : token }

    api_path = "/sc2/ladder/season" \
               + region_id
    url = base_url + api_path
    #make the api call
    response = requests.get( url, params = parameters )
    return response

'''function that calls the player api
'''
#define the parameters
def player( base_url, token, account_id ):
    parameters = { "region" : "US",
                   "accountId" : account_id,
                   "access_token" : token }
    api_path = "/sc2/player/"
    url = base_url + api_path
    response = requests.get( url + account_id, params = parameters )
    #print( url )
    #print( token )
    return response

'''function that uses the client_id and client_secret and returns the token
returns the token
'''
def getToken( blizzard_client_id, blizzard_client_secret ):
    #
    parameters = { "grant_type" : "client_credentials",
                    "scope" : "sc2.profile",
                    "client_id" : blizzard_client_id,
                    "client_secret" : blizzard_client_secret }
    #make the api call
    response = requests.post("https://us.battle.net/oauth/token", data = parameters)

    #print( response.json() )
    return response.json()["access_token"]

'''function that checks if the response from a requests is valid'''
def isResponseValid( response ):
    if response.status_code == 200 and len( response.json() ) > 0:
        return True
    else:
        return False

def main():
    #declarations and definitions
    base_url = 'https://us.api.blizzard.com'
    token = user_input = ""


    #requests blizzard api for a token
    #the value of token is overwrittenbase_url
    token = getToken( consts.BLIZZARD_CLIENT_ID, consts.BLIZZARD_CLIENT_SECRET )


    #get user input to see what they want to do
    #here is where we would  get authorization if our token expires
    user_input = input("Please choose from the following options:\
                       \n1) Metadata\
                       \n2) Profile\
                       \n3) Ladder Summary\
                       \n4) Grandmaster Leaderboard\
                       \n5) Season\
                       \n6) Player\n")

    #keep looping until user chooses to exit
    while user_input != "exit":
        if user_input == "1":
            print("1")
        elif user_input == "2":
            print("2")
        elif user_input == "3":
            print("3")
        elif user_input == "4":
            print("4")
        elif user_input == "5":
            print("5")
        elif user_input == "6":
            user_input = input("Please enter an accountId:\n")
            response = player( base_url, token, user_input )

            #check if response is valid
            if isResponseValid( response ) == True:
                print("The account belongs to: " + response.json()[0]["name"] + "\n")
            else:
                print( "Error! Code: " + str(response.status_code) + "\n" )

        else:
            print("Invalid input.\n\n")

        user_input = input("Please choose from the following options:\
                           \n1) Metadata\
                           \n2) Profile\
                           \n3) Ladder Summary\
                           \n4) Grandmaster Leaderboard\
                           \n5) Season\
                           \n6) Player\n")
    #end program
    sys.exit()

if __name__ == '__main__':
    main()
