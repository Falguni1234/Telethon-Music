import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("6646303160:AAGCPcVIRwa1NrGK3PmwkQTtEh5HlludzME", None)
    STRING_SESSION = os.environ.get("1AZWarzwBu5DoT7ymQ-UUE3mT5n2TxLwO8QpVmlx0vSM2rm3oEUol7ViyvX4mOTZuV0ggzlvLmnqqs1xanNtcsufYqR7LzlQdPDFoXLhntML5gOk1aC_YmzhUkJoMgpd97XU54qMRUh_sATiFo7WPVatQF08gCmMioRbarTF3dvy2zSAlnlJhZfJZRQlE7iD7sPYMzl6I3QtKxZVPEDOef9sG9MznWlgsL4_Jku1w5tomG1BlYuRT_g3zzyoNDxum_UcfZ8W0loW6e9nBaq0fJo8dSYkrngqwETJQabtDqQoNNhKUFOSr6Qb9htjWF1GWymabYOMJSvYl5cxMSteXb_4xaE-1Moc=", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("@Falgunmusicbot", "")
    SUPPORT = os.environ.get("SUPPORT", "@Falgun_7") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "https://t.me/EARN_WITH_FALGUN") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("6562223581", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
