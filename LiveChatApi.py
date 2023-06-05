import json
import requests
from requests.auth import HTTPBasicAuth
import re

class LiveChatApi():
    
    def __init__(self, token) -> None:
        self.token = token
    

    # method is creating a new customer in our system
    def post_customer(self, token, customer_name, email, account_id) -> str:
    
        endpoint = "https://api.livechatinc.com/v3.5/agent/action/create_customer"

        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": 'application/json',
        }
        data = {
            "name": customer_name,
            "email": email,
        }
        
        try:
            response = requests.post(endpoint, headers=headers, json=data,
                             auth=HTTPBasicAuth(account_id, token))
            customer = response.json()
            print("Customer have been created \nID: " + customer['customer_id'])
            return customer['customer_id']
        except:
            print("Something went wrong!")


    def create_chat(self, token, agent_id, customer_id, account_id):

        endpoint = "https://api.livechatinc.com/v3.5/agent/action/start_chat"

        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        data = {
            "user_id": customer_id,
            "user_type": "customer",
            "agent_id": agent_id
        }
        response = requests.post(endpoint, headers=headers, json=data,
                                auth=HTTPBasicAuth(account_id, token))
        print(data)

        if response.status_code == 200:

            print("Chat created successfully.")
            print(response.json())

            chat_id = response.json()['chat_id']
            add_agent_endpoint = "https://api.livechatinc.com/v3.5/agent/action/add_user_to_chat"

            action = {
                "chat_id": chat_id,
                "user_id": "opezdalya@gmail.com",
                "user_type": "agent",
                "visibility": "all",
            }
            response_to_add = requests.post(add_agent_endpoint, headers=headers, json=action,
                                auth=HTTPBasicAuth(account_id, token))
            print(response_to_add.json())
            
        else:
            print("Failed to create chat:", response.text)
            

        
        """
    def get_agent_id(personal_access_token, agent_name):

        endpoint = "https://api.livechatinc.com/v3.3/agents"

        headers = {
            "Authorization": f"Bearer {personal_access_token}"
        }

        response = requests.get(endpoint, headers=headers)

        if response.status_code == 200:
            agents = response.json()
            for agent in agents:
                if agent['name'] == agent_name:
                    return agent['id']
            print(f"Agent with name '{agent_name}' not found.")
        else:
            print("Failed to retrieve agents:", response.text)
    
"""