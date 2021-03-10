import io
import zipfile
from datetime import datetime

import requests

from config.consts import UTAH_COVID19_DOWNLOAD_URL, YYYY_MM_DD_REGEX
from models.covid_data.school_cases_by_district import SchoolCasesByDistrict
from utils import s3

__all__ = ["main"]


def main():
    today = datetime.now().strftime("%Y-%m-%d")
    # today = "2021-03-08"
    covid_files = _get_data_from_api()

    with zipfile.ZipFile(io.BytesIO(covid_files.content)) as covid_files:
        file_list = covid_files.filelist
        _verify_files_are_correct_data(today, file_list)
        _load_data_into_s3(today, file_list, covid_files)



def _verify_files_are_correct_data(today: str, file_list):
    if len(file_list) > 0:
        first_file_name = file_list[0].filename
        matches = YYYY_MM_DD_REGEX.findall(first_file_name)
        if len(matches) != 1:
            raise KeyError
        date_match = matches[0]
    else:
        raise KeyError

    if date_match != today:
        raise KeyError


# def check_if_new_data(current_data_path: str):


def _get_data_from_api(request_url: str = UTAH_COVID19_DOWNLOAD_URL):
    covid_files = requests.get(request_url)
    return covid_files


def _load_data_into_s3(today: str, file_list: list, covid_files: zipfile.ZipFile):
    for file in file_list:
        file_name = file.filename
        file_data = covid_files.open(file_name)
        s3.put_(f"{today}/{file_name}", file_data.read().decode("UTF-8"))


def parse_data(file_list: list, covid_files: zipfile.ZipFile):
    for file in file_list:
        file_name = file.filename
        file_data = covid_files.open(file_name)
        data = file_data.read()
        # SchoolCasesByDistrict()


def load_data_into_pg():
    pass


if __name__ == '__main__':
    main()
