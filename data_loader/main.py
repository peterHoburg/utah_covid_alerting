import csv

from src.models.covid_data.school_cases_by_district import SchoolCasesByDistrict


def main():
    with open("./data/utah/Schools_Cases by School District_2021-03-02.csv", "r") as f:
        reader = csv.DictReader(f)
        for line in reader:
            print(SchoolCasesByDistrict(**line))



if __name__ == '__main__':
    main()
