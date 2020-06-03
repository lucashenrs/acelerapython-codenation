import jwt

def create_token(data, secret):
    '''params: 
                ex.:
                    data = {"language": "Python"}
                    secret = 'acelera'
    '''
    token = jwt.encode(data, key= secret, algorithm='HS256')
    return token

def verify_signature(token):
    try:
        decoded_content = jwt.decode(token, 'acelera', algorithms=['HS256'])
        return decoded_content
    except:
        return {"error": 2}


