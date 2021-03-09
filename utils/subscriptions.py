import uuid


def generate_subscription_id(email_uuid_str: str, district: str) -> str:
    email_uuid = uuid.UUID(email_uuid_str)
    subscription_id = uuid.uuid5(email_uuid, district)
    return str(subscription_id)
