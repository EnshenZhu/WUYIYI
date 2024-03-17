from datetime import datetime


def year_month_to_numeric(year_month):
    try:
        date_obj = datetime.strptime(year_month, '%y-%b')
        numeric_representation = date_obj.year * 12 + date_obj.month
        return date_obj.year, date_obj, numeric_representation
    except ValueError:
        print("Invalid input format. Please provide the year-month string in 'YYYY-MM' format.")


# Example usage:
year_month_string = "17-Feb"
year, month, numeric_representation = year_month_to_numeric(year_month_string)
print("Numeric representation:", numeric_representation)
print("Year:", year)
print("Month:", month)
