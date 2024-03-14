import requests

def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/cats/cat/random"

    response = requests.get(url)
    data = response.json()

    if data ["success"] and "data" in data:
        # user_data = data["data"]
        adapt = data["data"]["temperament"]
        
        country_code =  data["data"]["country_code"]
        return adapt , country_code
    else:
        raise Exception("Failed to fetch user data")
    

def main():
    try:
        adapt, country_code = fetch_random_user()
        print(f"adapt: {adapt}\nCountrycode: {country_code}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()


    


#     import requests

# def fetch_random_products():
#     url = "https://api.freeapi.app/api/v1/public/randomproducts/product/random"

#     response = requests.get(url)
#     data = response.json()

#     if data ["success"] and "data" in data:
#         # user_data = data["data"]
#         title = data["data"]["id"]       
#         brand = data["data"]["brand"]
#         return title, brand
#     else:
#         raise Exception("Failed to fetch user data")


# def main():
#     try:
#         title,brand = fetch_random_products
#         print(f"title: {title}\nBrand: {brand}")
#     except Exception as e:
#         print(str(e))

# if __name__ == "__main__":
#     main()