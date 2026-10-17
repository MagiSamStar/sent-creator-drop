import os
from dotenv import load_dotenv
from sent_dm import Sent


def send_content_notification(content_title):
    load_dotenv()

    template_id = os.getenv("SENT_TEMPLATE_ID")
    test_phone = os.getenv("SENT_TEST_PHONE")

    if not template_id or not test_phone:
        raise ValueError(
            "Missing template ID or test phone in .env"
        )

    client = Sent()

    response = client.messages.send(
        to=[test_phone],
        template={
            "id": template_id,
            "parameters": {
                "contentTitle": content_title
            },
        },
        sandbox=True,
    )

    return response
