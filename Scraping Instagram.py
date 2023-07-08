# Import the modules required

import instaloader

# Create an instance of Instaloader class
bot = instaloader.Instaloader()

# Load a profile from an Instagram handle

name=input("Enter the Instagrame Profile name: ")
profile = instaloader.Profile.from_username(bot.context,name)



# Gives relevant information of the account you provided such as user_id ...etc...
print(type(profile))

print("Username is ---> ", profile.username)
print("User ID is---> ", profile.userid)
print("Number of Posts are ---> ", profile.mediacount)
print("Number of Followers are ---> ", profile.followers)
print("Number of Followees are ---> ", profile.followees)
print("Bio of",name,"is ---> ", profile.biography,profile.external_url)
