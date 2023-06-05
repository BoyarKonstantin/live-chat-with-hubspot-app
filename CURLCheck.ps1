token="dal:3kfmrh8Drk814qWH-AqA3RCwxS0"
account_id="d72aabe6-77b9-439d-b789-4cb04ccd6593"
customer_id="78fb8a49-bdfb-42a2-9ca2-36201162d06e"
agent_id="d72aabe6-77b9-439d-b789-4cb04ccd6593"

curl -X POST 
  -H "Authorization: Bearer $token" 
  -H "Content-Type: application/json" 
  -u "$account_id:$token" 
  -d '{
    "user_id": "'"$customer_id"'",
    "user_type": "customer",
    "agent_id": "'"$agent_id"'"
  }' 
  "https://api.livechatinc.com/v3.5/agent/action/start_chat"