import os

env_var_list = [
    "POSTGRES_DATABASE_URL_ENV",
    "AWS_ACCESS_KEY_ID",
    "AWS_SECRET_ACCESS_KEY",
    "AWS_DEFAULT_REGION",
    "S3_ENDPOINT_URL",
]


def test_env_vars():
    for env_var in env_var_list:
        print(env_var)
        print(os.environ.get(env_var))

