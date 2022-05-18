import csv
import datetime
import calendar

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    
    year = int("".join(iso_string[:4]))
    month = int("".join(iso_string[5:7]))
    month_name = calendar.month_name[month]
    date = int("".join(iso_string[8:10]))
    day_of_week = calendar.day_name[datetime.date(year, month, date).weekday()]

    if date < 10:
        return f"{day_of_week} 0{date} {month_name} {year}"
    else:
        return f"{day_of_week} {date} {month_name} {year}" 


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    fahrenheit = float(temp_in_farenheit)

    celsius = (fahrenheit - 32) * 5 / 9

    if round(celsius, 1).is_integer():
        return int(celsius)
    else:
        return float("{:.1f}".format(celsius))



def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    int_list = [float(x) for x in weather_data]
    total = sum(int_list)
    items = len(int_list)
    mean = total / items

    if round(mean , 1).is_integer():
        return int(mean)
    else:
        return mean


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    with open(csv_file) as file:
        reader = csv.reader(file)
        next(reader, None)
        output = []
        for line in reader:
            if any(x.strip() for x in line):
                row = [line[0]]
                row.append(int(line[1]))
                row.append(int(line[2]))
                output.append(row)
                row = []
        return output


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    min = 9999

    if weather_data == []:
        return ()
    else:
        float_list = [float(x) for x in weather_data]
        for index, temperature in enumerate(float_list):
            if temperature <= min:
                min = temperature
                position = index
        return float("{:.1f}".format(float(min))), position



def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    
    max = -9999
    
    if weather_data == []:
        return ()
    else:
        float_list = [float(x) for x in weather_data]
        for index, temperature in enumerate(float_list):
            if temperature >= max:
                max = temperature
                position = index
        return float("{:.1f}".format(float(max))), position


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    min_list = [x[1] for x in weather_data]
    min_temp = find_min(min_list)[0]
    avg_min = format_temperature(convert_f_to_c(calculate_mean(min_list)))
    min_index = min_list.index(min_temp)
    min_date = convert_date(weather_data[min_index][0])
    converted_min_temp = format_temperature("{:.1f}".format(convert_f_to_c(min_temp)))

    max_list = [x[2] for x in weather_data]
    max_temp = find_max(max_list)[0]
    avg_max = format_temperature(convert_f_to_c(calculate_mean(max_list)))
    max_index = max_list.index(max_temp)
    max_date = convert_date(weather_data[max_index][0])
    converted_max_temp = format_temperature("{:.1f}".format(convert_f_to_c(max_temp)))

    days = len(weather_data)
    return f"{days} Day Overview\n  The lowest temperature will be {converted_min_temp}, and will occur on {min_date}.\n  The highest temperature will be {converted_max_temp}, and will occur on {max_date}.\n  The average low this week is {avg_min}.\n  The average high this week is {avg_max}.\n"


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary = []
    for day in weather_data:
        date = convert_date(day[0])
        min = format_temperature("{:.1f}".format(convert_f_to_c(day[1])))
        max = format_temperature("{:.1f}".format(convert_f_to_c(day[2])))
        output = f"---- {date} ----\n  Minimum Temperature: {min}\n  Maximum Temperature: {max}\n\n"
        summary.append(output)
    return "".join(summary)
    
