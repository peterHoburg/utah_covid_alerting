import io
import os
import shutil
import zipfile
from datetime import datetime

import requests
from utils import s3

from config.consts import UTAH_COVID19_DOWNLOAD_URL, LOCAL_DATA_PATH, YYYY_MM_DD_REGEX


def main():
    today = datetime.now().strftime("%Y-%m-%d")
    today = "2021-03-08"
    current_data_path = f"{LOCAL_DATA_PATH}/{today}"

    pull_utah_covid_data(current_data_path, today)
    # with open("./data/utah/2021-03-02/Schools_Cases by School District_2021-03-02.csv", "r") as f:
    #     reader = csv.DictReader(f)
    #     for line in reader:
    #         print(SchoolCasesByDistrict(**line))


def pull_utah_covid_data(current_data_path: str, today: str):
    if os.path.exists(current_data_path) is True:
        shutil.rmtree(current_data_path)
    covid_files = requests.get(UTAH_COVID19_DOWNLOAD_URL)
    with zipfile.ZipFile(io.BytesIO(covid_files.content)) as covid_files:
        # covid_files.extractall(current_data_path)
        file_list = covid_files.filelist
        if len(file_list) > 0:
            first_file_name = file_list[0].filename
            matches = YYYY_MM_DD_REGEX.findall(first_file_name)
            if len(matches) != 1:
                raise KeyError
            date_match = matches[0]
        else:
            raise KeyError

        if date_match == today:
            for file in file_list:
                file_name = file.filename
                file_data = covid_files.open(file_name)
                s3.put_(f"{today}/{file_name}", file_data.read().decode("UTF-8"))

# def check_if_new_data(current_data_path: str):


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
