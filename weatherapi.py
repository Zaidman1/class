

import requests


welcome = input("Welcome to my Weather Program: Press Enter to Start")

#definition for city input and api

def by_city():
    city = input('Enter Your City Name: ')
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},us&appid=2ef6b12a2d289574516dff5fb687e525&units=imperial'.format(city)
    res = requests.get(url)
    data = res.json()
    show_data(data)
# program loop
    question = input('Would you like to search again ? Type Yes or No: ')
    if question == 'Yes':
        main()
    if question == 'No':
        print("Have a nice day.")
        exit()

#definition ofr zip code input and api

def by_zip():
    zip_code = input('Enter Your Zip code: ')
    url = 'https://api.openweathermap.org/data/2.5/weather?zip={},us&units=imperial&appid=2ef6b12a2d289574516dff5fb687e525'.format(zip_code)
    res = requests.get(url)
    data = res.json()
    show_data(data)
#program loop
    question = input('Would you like to search again ? Type Yes or No: ')
    if question == 'Yes':
        main()
    if question == 'No':
        print("Have a nice day.")
        exit()


#importing data from weather site
def show_data(data):
    temp = data['main']['temp']
    hightemp = data['main']['temp_max']
    lowtemp = data['main']['temp_min']

    print('Current Temperature : {} degree fahrenheit'.format(temp))
    print('High Temperature : {} degree fahrenheit'.format(hightemp))
    print('Low Temperature : {} degree fahrenheit'.format(lowtemp))






#program intro and start
def main():
    while True:
        answer = input("Wondering what the weather is? Ttype zip for zip code or city for city name: ")
        if answer == 'city':
            try:
                print("Conection secured.")
                by_city()

            except Exception:
                print("Invalid data try again")
                by_city()

        if answer == 'zip':
            try:
                print("Conection secured.")
                by_zip()

            except Exception:
                print('{}')
                by_zip()

        else:
            print("Invalid data try again.")



main()