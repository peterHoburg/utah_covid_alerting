import datetime
from enum import Enum

from pydantic import BaseModel, Field


class SchoolDistricts(Enum):
    davis_district = "Davis District"
    alpine_district = "Alpine District"
    canyons_district = "Canyons District"
    granite_district = "Granite District"
    jordan_district = "Jordan District"
    nebo_district = "Nebo District"
    cache_district = "Cache District"
    weber_district = "Weber District"
    tooele_district = "Tooele District"
    wasatch_district = "Wasatch District"
    murray_district = "Murray District"
    sevier_district = "Sevier District"
    salt_lake_district = "Salt Lake District"
    provo_district = "Provo District"
    iron_district = "Iron District"
    park_city_district = "Park City District"
    washington_district = "Washington District"
    box_elder_district = "Box Elder District"
    logan_city_district = "Logan City District"
    carbon_district = "Carbon District"
    south_summit_district = "South Summit District"
    beaver_district = "Beaver District"
    duchesne_district = "Duchesne District"
    juab_district = "Juab District"
    ogden_city_district = "Ogden City District"
    south_sanpete_district = "South Sanpete District"
    uintah_district = "Uintah District"
    emery_district = "Emery District"
    kane_district = "Kane District"
    morgan_district = "Morgan District"
    north_summit_district = "North Summit District"
    daggett_district = "Daggett District"
    garfield_district = "Garfield District"
    grand_district = "Grand District"
    millard_district = "Millard District"
    north_sanpete_district = "North Sanpete District"
    piute_district = "Piute District"
    rich_district = "Rich District"
    san_juan_district = "San Juan District"
    tintic_district = "Tintic District"
    wayne_district = "Wayne District"

    salt_lake_county_private = "Salt Lake County - Private"
    utah_county_private = "Utah County - Private"
    bear_river_private = "Bear River - Private"
    central_utah_private = "Central Utah - Private"
    davis_county_private = "Davis County - Private"
    southwest_utah_private = "Southwest Utah - Private"
    weber_morgan_private = "Weber-Morgan - Private"

    salt_lake_county_charter = "Salt Lake County - Charter"
    utah_county_charter = "Utah County - Charter"
    davis_county_charter = "Davis County - Charter"
    bear_river_charter = "Bear River - Charter"
    tooele_county_charter_private = "Tooele County - Charter/Private"
    weber_morgan_charter = "Weber-Morgan - Charter"
    southeast_utah_charter = "Southeast Utah - Charter"
    southwest_utah_charter = "Southwest Utah - Charter"
    summit_county_charter_private = "Summit County - Charter/Private"
    tri_county_charter_private = "TriCounty - Charter/Private"
    wasatch_county_charter_private = "Wasatch County - Charter/Private"


class Jurisdiction(Enum):
    weber_morgan = "Weber-Morgan"
    wasatch_county = "Wasatch County"
    utah_county = "Utah County"
    tri_county = "TriCounty"
    tooele_county = "Tooele County"
    summit_county = "Summit County"
    southwest_utah = "Southwest Utah"
    southeast_utah = "Southeast Utah"
    san_juan = "San Juan"
    salt_lake_county = "Salt Lake County"
    davis_county = "Davis County"
    central_utah = "Central Utah"
    bear_river = "Bear River"


class SchoolCasesByDistrict(BaseModel):
    school_district: SchoolDistricts = Field(..., alias="School District")
    jurisdiction: Jurisdiction = Field(..., alias="Jurisdiction")
    active_cases: str = Field(..., alias="Active Cases")
    total_cases: int = Field(..., alias="Total Cases")


class DBSchoolCasesByDistrict(SchoolCasesByDistrict):
    date: datetime.datetime
