import csv

from models.covid_data.school_cases_by_district import SchoolCasesByDistrict


def main():
    with open("./data/utah/2021-03-02/Schools_Cases by School District_2021-03-02.csv", "r") as f:
        reader = csv.DictReader(f)
        for line in reader:
            print(SchoolCasesByDistrict(**line))


def get_data_from_api():
    pass


def load_data_into_s3():
    pass


def parse_data():
    pass


def load_data_into_pg():
    pass


if __name__ == '__main__':
    main()
