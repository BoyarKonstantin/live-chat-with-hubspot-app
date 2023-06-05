$token = "YOUR_TOKEN"
$url = "https://api.livechatinc.com/v3.5/agent/action/start_chat"

$headers = @{
    "Authorization" = "Bearer $token"
    "Content-Type"  = "application/json"
}

$body = @{
    "user_id"   = "78fb8a49-bdfb-42a2-9ca2-36201162d06e"
    "user_type" = "customer"
    "agent_id"  = "d72aabe6-77b9-439d-b789-4cb04ccd6593"
} | ConvertTo-Json

$response = Invoke-RestMethod -Method Post -Uri $url -Headers $headers -Body $body

if ($response.StatusCode -eq 200) {
    Write-Output "Chat created successfully."
} else {
    Write-Output "Failed to create chat: $($response | ConvertTo-Json -Depth 100)"
}
