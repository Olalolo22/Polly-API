import requests

def register_user(base_url, username, password):
    """
    Registers a new user via the /register endpoint.

    Args:
        base_url (str): The base URL of the API (e.g., "http://127.0.0.1:8000")
        username (str): The desired username
        password (str): The desired password

    Returns:
        dict: The JSON response from the API
    """
    url = f"{base_url}/register"
    payload = {
        "username": username,
        "password": password
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()

def get_polls(base_url, token, skip=0, limit=10):
    """
    Fetches paginated poll data from the /polls endpoint.

    Args:
        base_url (str): The base URL of the API (e.g., "http://127.0.0.1:8000")
        token (str): JWT access token for authentication
        skip (int): Number of records to skip (default 0)
        limit (int): Maximum number of records to return (default 10)

    Returns:
        list: List of polls as returned by the API
    """
    url = f"{base_url}/polls"
    headers = {"Authorization": f"Bearer {token}"}
    params = {"skip": skip, "limit": limit}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()
