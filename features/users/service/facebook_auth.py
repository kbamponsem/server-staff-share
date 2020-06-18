

def __verify_facebook_issuer(auth_token: str):
    info = {}

    user_data = {
        'id': info['id'],
        # 'email': idinfo['email'],
        # 'picture': idinfo['picture'],
        'first_name': info['first_name'],
        'surname': info['last_name'],
        'birthday': info['birthday'],
        'gender': info['gender']  # male or female
    }

    return user_data
