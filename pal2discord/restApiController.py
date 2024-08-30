import requests
import json

class restApiController:
    def __init__(self, port, user, passwd):
        self.restapi_port = port
        self.adm_user = user
        self.adm_passwd = passwd
        self.url = f"http://localhost:{self.restapi_port}/v1/api/"
        self.urll = ""
        self.payload = {}
        self.headers = {}
        self.method = ""


    def send_msg(self, user, msg):
        msg = "(" + user + ") " + msg 
        self.payload = json.dumps({
            "message": msg
            })
        self.headers = {
            'Content-Type': 'application/json'
            }
        self.method = "POST"
        self.urll = "announce"
        self.exec_command()


    def exec_command(self):
        try:
            response = requests.request(
                self.method,
                self.url + self.urll,
                headers=self.headers,
                data=self.payload,
                auth=(self.adm_user, self.adm_passwd)
            )
            
            try:
                response_json = response.json()
                return response_json

            #JSON以外の時の例外
            except json.decoder.JSONDecodeError:
                return None

        #レスポンスエラー
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None
