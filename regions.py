# date ranges
# 8/28 9/4
# 9/4 9/11
# 9/11 9/18
import os
import csv

DEFAULT_DATA_FOLDER = './data/'

class Region:
    def __init__(self, row, date) -> None:
        # takes in row direct from csv so math operation can be done here
        # self.date_pulled = date_pulled
        self.name = row[0]
        self.ad_cost = row[1]
        self.impressions = row[2]
        self.clicks = row[3]
        self.ctr = row[4]
        self.cpc = row[5]
        self.ctl = row[6]
        self.cpl = row[7]
        self.cps = row[8]
        self.total_sales = row[9]
        self.new_sales = row[10]
        self.new_sales_percent = row[11]
        self.swaps = row[12]
        self.swaps_percent = row[13]
        self.gt_total_sales = row[14]
        self.all_leads = row[15]
        self.quoted_leads = row[16]
        self.not_quoted_leads = row[17]
        self.percent_not_quoted = row[18]
        self.closing_rate = row[19]
        self.expected_average_profit = row[20]
        self.date = date

    def print_data(self):
        print(f'Ad Cost: {self.ad_cost}')
        print(f'Impressions: {self.impressions}')
        print(f'Clicks: {self.clicks}')

    def calc_change(self, compare):
        pass


class Slide_Data():
    def __init__(self, title_region, subheading) -> None:
        self.title_region = title_region
        self.subheading = subheading

class Region_Comparison():
    def __init__(self, region1, region2) -> None:
        self.nameconcat = region1.date + region2.date

    def toString(self):
        return self.nameconcat


def compare_regions(region1, region2):
    print("\nRegion One Data\n------------------")
    region1.print_data()

    print("\n\nRegion Two Data\n------------------")
    region2.print_data()

    print("\n")
    print(f'Change from {region1.date} to {region2.date} ')
    print("------------------")


def create_region_objects(filename):
    file_path = DEFAULT_DATA_FOLDER + filename
    date_range_name = filename.split("-")
    month = date_range_name[2]
    day = date_range_name[3].split(".")[0]
    date = f'{month}-{day}'

    print()
    with open(file_path, 'r') as file:
        csvreader = csv.reader(file)
        counter = 0
        regions = []
        for row in csvreader:
            if counter == 0:
                print(f'Creating Region Objects from {file_path}')
            else:
                regions.append(Region(row, date))

            counter += 1
        return regions

def get_data_ranges():
    file_names = []
    for file in os.listdir('./data'):
        file = file.split('/')[-1].split('.')[0]
        file_names.append(file)

    file_names.sort()
    return file_names

if __name__ == '__main__':
    data_ranges = get_data_ranges()
    print("Available Data:")
    counter = 0
    for file in data_ranges:
        print(f'{counter}.) {file}')
        counter += 1

    print("Earlier Range Should Go First")
    file_one = int(input("Select Range 1: "))
    file_two = int(input("Select Range 2: "))

    # print(data_ranges[file_one])
    # print(data_ranges[file_two])

    regions_one = create_region_objects(f'{data_ranges[file_one]}.csv')
    regions_two = create_region_objects(f'{data_ranges[file_two]}.csv')

    print("Regions Available for Comparison:")
    for region in regions_one:
        print(region.name)

    while True:
        comparison_region_name = input("\nWhich Region Do You Want To Compare? (done to exit) ").strip()
        if comparison_region_name == "done":
            break
        else:
            # retrieve region objects and compare them
            for region in regions_one:
                if region.name.lower() == comparison_region_name.lower():
                    first_region = region
                    break
                
            for region in regions_two:
                if region.name.lower() == comparison_region_name.lower():
                    second_region = region
                    break
                
            if 'first_region' in locals() and 'second_region' in locals():
                compare_regions(first_region, second_region)
            else:
                print(f'ERROR: failed to retrieve region of name {comparison_region_name}')

    