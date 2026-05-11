# ==========================================
# AUTHENTICATION LAYER
# ==========================================

API_KEY = "MY_SECRET_KEY"

def authenticate(api_key):

    if api_key != API_KEY:

        return False

    return True