REGULAR_MOVIE = 0
NEW_RELEASE_MOVIE = 1
CHILDREN_MOVIE = 2
RENTAL_RATE_PER_DAY = 1.5

def calculate_rental_amount(price_code, days_rented):
    rental_amount = 0
    
    if price_code == REGULAR_MOVIE:
        rental_amount += 2
        if days_rented > 2:
            rental_amount += (days_rented - 2) * RENTAL_RATE_PER_DAY
    elif price_code == NEW_RELEASE_MOVIE:
        rental_amount += days_rented * 3
    elif price_code == CHILDREN_MOVIE:
        rental_amount += 1.5
        if days_rented > 3:
            rental_amount += (days_rented - 3) * RENTAL_RATE_PER_DAY
    else:
        return 0

    return rental_amount

def calculate_frequent_renter_points(price_code, days_rented):
    points = 1

    if price_code == NEW_RELEASE_MOVIE and days_rented > 1:
        points += 1
    
    return points

def generate_rental_statement(name, rentals):
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

    total_rental_amount = 0
    frequent_renter_points = 0
    statement = f"Rental Record for {name}\n"

    for rental in rentals:
        movie = rental["movie"]
        days_rented = rental["days_rented"]

        rental_amount = calculate_rental_amount(movie["price_code"], days_rented)
        frequent_renter_points += calculate_frequent_renter_points(movie["price_code"], days_rented)

        statement += f"\t{movie['title']}\t{rental_amount}\n"
        total_rental_amount += rental_amount

    statement += f"Amount owed is {total_rental_amount}\n"
    statement += f"You earned {frequent_renter_points} frequent renter points"

    return statement
