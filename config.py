import datetime
from os import environ 

#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

class Config:
    API_ID = environ.get("API_ID", "13963336")
    API_HASH = environ.get("API_HASH", "a144d1e22ef0b29738e8c00713d02678")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6890779353:AAGTQIPFBjFfyHzChkzbIIgFmp6QSz6Z74w") 
    BOT_SESSION = environ.get("BOT_SESSION", "Auto_Forward") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://Nischay999:Nischay999@cluster0.5kufo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Nyfwbot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '2103299862').split()]
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002421238378'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "@nyyybots") 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")
    PORT = environ.get('PORT', '8080')
    
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 

   
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
#Dont Remove My Credit @Silicon_Bot_Update 
#This Repo Is By @Silicon_Official 
# For Any Kind Of Error Ask Us In Support Group @Silicon_Botz 
