import csv
import datetime
import pycountry
from collections import OrderedDict

file = 'cc.csv'

def format_csv_file(file):
    """
    takes input file and returns formatted csv file
    """
    with open(file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        with open('result.csv', 'w') as result_file:
            csv_writer = csv.writer(result_file)
            result_dict = OrderedDict()
            for row in csv_reader:
                date, subdivision, impressions, ctr = row

                formatted_date = datetime.datetime.strptime(date, '%m/%d/%Y').strftime('%Y-%m-%d')

                country_code = ''
                if subdivision not in pycountry.subdivisions:
                    country_code = 'XXX'
                for district in pycountry.subdivisions:
                    if district.name == subdivision:
                        country_code = district.country.alpha_3

                impressions = int(impressions)

                ctr = float(row[3].strip('%')) / 100
                clicks = round(int(impressions) * ctr)

                if '{}/{}'.format(formatted_date, country_code) in result_dict:
                    result_dict['{}/{}'.format(formatted_date, country_code)][0] += impressions
                    result_dict['{}/{}'.format(formatted_date, country_code)][1] += clicks
                else:
                    result_dict['{}/{}'.format(formatted_date, country_code)] = [impressions, clicks]

            result_dict = OrderedDict(sorted(result_dict.items(), key=lambda tuple: tuple[0]))
            for ordered_key, ordered_value in result_dict.items():
                ordered_key = ordered_key.split('/')
                csv_writer.writerow(ordered_key + ordered_value)

if __name__ == '__main__':
    format_csv_file(file)