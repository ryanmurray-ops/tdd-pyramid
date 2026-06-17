def format_coin_response(coin_response):
    return {
        "success": coin_response["success"],
        "data": {
            "id": str(coin_response["data"].id),
            "name": coin_response["data"].name,
            "is_complete": coin_response["data"].is_complete
        },
        "error": coin_response["error"]
    }

def format_coin_list(coins):
    return [
        {
            "id": str(coin.id),
            "name": coin.name,
            "is_complete": coin.is_complete
        }
        for coin in coins
    ]