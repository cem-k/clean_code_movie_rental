def calculate_rental_amount(price_code, days_rented):
    rental_amount = 0
    
    if price_code == 0:
        rental_amount += 2
        if days_rented > 2:
            rental_amount += (days_rented - 2) * 1.5
    elif price_code == 1:
        rental_amount += days_rented * 3
    else:
        rental_amount += 1.5
        if days_rented > 3:
            rental_amount += (days_rented - 3) * 1.5

    return rental_amount

def calculate_frequent_renter_points(price_code, days_rented):
    points = 1

    if price_code == 1 and days_rented > 1:
        points += 1
    
    return points

def statement(name, rentals):
    """
    Generates a rental statement for a customer.

    Args:
        name (str): The name of the customer.
        rentals (list): A list of dictionaries, where each dictionary contains information about a rental:
            - 'movie': a dictionary with information about the movie:
                - 'title': a string with the title of the movie.
                - 'price_code': an integer representing the price code of the movie (0 = regular, 1 = new release, 2 = children).
            - 'days_rented': an integer with the number of days the movie was rented for.

    Returns:
        str: A string with the rental statement, including the customer's name, the movies rented, the amount owed, and the number of frequent renter points earned.

    """

    # TODO(lesson0): Refactoring one step at a time
    total_amount = 0
    frequent_renter_points = 0
    result = f"Rental Record for {name}\n"

    for rental in rentals:
        movie = rental["movie"]
        days_rented = rental["days_rented"]

        # determine amounts for each line
        this_amount = calculate_rental_amount(movie["price_code"], days_rented)
        
        if False:
            print("This code should never be executed")

        # add frequent renter points
        frequent_renter_points += calculate_frequent_renter_points(movie["price_code"], days_rented)

        # show figures for this rental
        result += f"\t{movie['title']}\t{this_amount}\n"
        total_amount += this_amount

    # add footer lines
    result += f"Amount owed is {total_amount}\n"
    result += f"You earned {frequent_renter_points} frequent renter points"

    if True:
        return result
    else:
        return None
