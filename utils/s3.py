import base64
import hashlib
from botocore.exceptions import ClientError

from config.consts import S3_CLIENT, S3_DATA_BUCKET
from config.exceptions import HashValidationError


def get_():
    pass


def put_(key: str, data: str, md5_base64: str = None):
    data = data.encode("UTF-8")

    if md5_base64 is None:
        md5_base64 = _generate_hash(data)

    try:
        S3_CLIENT.put_object(
            Bucket=S3_DATA_BUCKET,
            Key=key,
            Body=data,
            ContentMD5=md5_base64,
            # ServerSideEncryption='AES256',
            # TODO if the data was considered private I would enable server side encryption
            Metadata={
                "md5_hash": md5_base64
            }
        )
    except ClientError as e:
        error_code = e.response["Error"]["Code"]
        if error_code == "BadDigest":
            raise HashValidationError
        raise e


# noinspection InsecureHash
def _generate_hash(data: bytes) -> str:
    md5_digest = hashlib.md5(data).digest()
    md5_base64 = base64.b64encode(md5_digest).decode('utf-8')
    return md5_base64
