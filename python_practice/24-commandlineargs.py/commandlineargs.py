import sys
env_name = sys.argv[1]
release_version_number = sys.argv[2]

############
### some deployment script
###########

print(f"The environment to deploy {env_name}")
print(f"The Release version is {release_version_number}")


#note: python commandlineargs.py prod 8.9.44  --> we need to give this so we will get output
