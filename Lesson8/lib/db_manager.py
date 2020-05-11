import mysql.connector
import requests
from lib.settings import COVID19_URL
if __name__ == "__main__":
    db_manager


class db_manager:

    def __init__(self, host, user, passwd):
        self.__db = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd
        )
        self.__cursor = self.__db.cursor()
        self.__cursor.execute("CREATE DATABASE IF NOT EXISTS COVID19")
        self.__cursor.execute("USE COVID19")
        self.__cursor.execute(
            "CREATE TABLE IF NOT EXISTS Global (id INT AUTO_INCREMENT PRIMARY KEY, NewConfirmed INT(10), TotalConfirmed INT(10), NewDeaths INT(10), TotalDeaths INT(10), NewRecovered INT(10), TotalRecovered INT (10))")
        self.__cursor.execute(
            "CREATE TABLE IF NOT EXISTS Countries (id INT AUTO_INCREMENT PRIMARY KEY, Country VARCHAR(255), CountryCode VARCHAR(12), Slug VARCHAR(255), NewConfirmed INT(10),TotalConfirmed INT(10), NewDeaths INT(10), TotalDeaths INT(10), NewRecovered INT(10), TotalRecovered INT (10), Date DATE)")

    def menu(self):
        exit = False
        while not exit:
            choice = int(input(
                "1. Update data\n2. Search by Country\n3. Search by Country Code\n4. TOP 10 Countries with Total Confirmed cases\n5. TOP 10 Countries with Total Recovered cases\n0. Exit\n====> "))
            if choice == 1:
                answer = self.__update_covid_data()
                print(answer)
            elif choice == 2:
                search_by_Country = self.__searchByCountry()
                print(search_by_Country)
            elif choice == 3:
                search_by_Country_Code = self.__searchByCountryCode()
                print(search_by_Country_Code)
            elif choice == 4:
                top_10_Countries = self.__top_10_Countries()
            elif choice == 5:
                recovered = self.__top_10_Countries_recovered()
            elif choice == 0:
                exit = True
                print("Bye!")
            else:
                print("Wrong choise")

    def __update_covid_data(self):
        covid_data = requests.get(COVID19_URL)
        covid_data = covid_data.json()

        self.__cursor.execute("TRUNCATE TABLE Global")
        sql = "INSERT INTO Global (NewConfirmed, TotalConfirmed, NewDeaths, TotalDeaths, NewRecovered, TotalRecovered) VALUES (%s,%s,%s,%s,%s,%s)"
        val = (covid_data['Global']["NewConfirmed"],
               covid_data['Global']["TotalConfirmed"], covid_data['Global']["NewDeaths"], covid_data['Global']["TotalDeaths"], covid_data['Global']["NewRecovered"], covid_data['Global']["TotalRecovered"])
        self.__cursor.execute(sql, val)
        self.__db.commit()

        self.__cursor.execute("TRUNCATE TABLE Countries")
        for item in covid_data['Countries']:
            sql = "INSERT INTO Countries (Country, CountryCode, Slug, NewConfirmed, TotalConfirmed, NewDeaths, TotalDeaths, NewRecovered, TotalRecovered, Date) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (item['Country'], item['CountryCode'], item['Slug'], item['NewConfirmed'], item['TotalConfirmed'],
                   item['NewDeaths'], item['TotalDeaths'], item['NewRecovered'], item['TotalRecovered'], item['Date'])
            self.__cursor.execute(sql, val)
        self.__db.commit()

        return "DB updated"

    def __searchByCountry(self):
        country = input("Enter Country to search: ")
        self.__cursor.execute(
            "SELECT * FROM Countries WHERE Country='" + country + "'")
        search_country = self.__cursor.fetchone()
        if search_country != None:
            return search_country
        else:
            return "Country '", country, "' not found"

    def __searchByCountryCode(self):
        country_code = input("Enter Country Code to search: ")
        self.__cursor.execute(
            "SELECT * FROM Countries WHERE CountryCode='" + country_code + "'")
        search_country_code = self.__cursor.fetchone()
        if search_country_code != None:
            return search_country_code
        else:
            return "Country '", country_code, "' not found"

    def __top_10_Countries(self):
        self.__cursor.execute(
            "SELECT Country, TotalConfirmed FROM Countries GROUP BY TotalConfirmed DESC LIMIT 10")
        search_top_10_Countries = self.__cursor.fetchall()
        for i in search_top_10_Countries:
            print(i[0], ": ", i[1])

    def __top_10_Countries_recovered(self):
        self.__cursor.execute(
            "SELECT Country, TotalRecovered FROM Countries GROUP BY TotalRecovered DESC LIMIT 10")
        recovered = self.__cursor.fetchall()
        for i in recovered:
            print(i[0], ": ", i[1])
