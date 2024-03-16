import csv

#load driver data from csv
def load_driver_data():
    with open('csv_path/driver_data.csv','r') as file:
        reader = csv.DictReader(file)
        return [dict(row) for row in reader]
    #pass

#update driver prices
def update_driver_prices(driver_data, race_results):
    for result in race_results:
        driver_name = result['driver']
        position = result['position']

        if position == 'DNF':
            price_change = -0.05
        else:
        
            #position to integer
            position = int(position)

            #find driver
            for driver in driver_data:
                if driver['name'] == driver_name:
                    #fetch current price
                    price = float(driver['price'])

                    #price changes based on position
                    if position == 1:
                        price_change = 0.5
                    elif position == 2:
                        price_change = 0.4
                    elif position == 2:
                        price_change = 0.3
                    elif position == 3:
                        price_change = 0.2
                    elif position == 4:
                        price_change = 0.1
                    elif position == 5:
                        price_change = 0.05
                    elif position == 6:
                        price_change = 0.04
                    elif position == 7:
                        price_change = 0.03
                    elif position == 8:
                        price_change = 0.02
                    elif position == 9:
                        price_change = 0.01
                    elif position > 9:
                        price_change = 0
                    
                    #calc new price
                    new_price = price + (price * price_change)
                    #update in driver_data
                    driver['price'] = str(new_price)

                    break
    return driver_data

#update driver points
def update_driver_points(driver_data, race_results):
    for result in race_results:
        driver_name = result['driver']
        position = result['position']
        fastest_lap = result['fastest_lap']

        if position == 'DNF':
            points_change = 0
        else:
        
            #position to integer
            position = int(position)

            #find driver
            for driver in driver_data:
                if driver['name'] == driver_name:
                    #fetch current points
                    points = float(driver['points'])

                    #points changes based on position
                    if position == 1:
                        points_change = 25
                    elif position == 2:
                        points_change = 0.4
                    elif position == 2:
                        points_change = 0.3
                    elif position == 3:
                        points_change = 0.2
                    elif position == 4:
                        points_change = 0.1
                    elif position == 5:
                        points_change = 0.05
                    elif position == 6:
                        points_change = 0.04
                    elif position == 7:
                        points_change = 0.03
                    elif position == 8:
                        points_change = 0.02
                    elif position == 9:
                        points_change = 0.01
                    elif position > 9:
                        points_change = 0
                    
                    #fastest lap
                    if fastest_lap == 'true':
                        points_change += 1
                    
                    #calc new points
                    new_points = points + (points + points_change)
                    #update in driver_data
                    driver['points'] = str(new_points)

                    break
    return driver_data


#load race results from csv
def load_race_results():
    with open('csv_path/race_results.csv','r') as file:
        reader = csv.DictReader(file)
        return [dict(row) for row in reader]
    #pass

#load latest race results from csv
def most_recent_race_results():
    
    #store most recent race number
    most_recent_race_number = 0
    most_recent_race_results = []

    #race results csv
    with open('csv_path/race_results.csv','r') as file:
        reader = csv.DictReader(file)

        #loop to find race number
        for row in reader:
            race_number = int(row['race_number'])
            if race_number > most_recent_race_number:
                most_recent_race_number = race_number
                most_recent_race_results = []
            if race_number == most_recent_race_number:
                most_recent_race_results.append(row)

    return most_recent_race_results
    #pass
recent_race_results = load_race_results()