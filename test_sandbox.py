import os
import sent_dm
from dotenv import load_dotenv
from sent_dm import Sent


def main():
    load_dotenv()

    template_id = os.getenv("SENT_TEMPLATE_ID")
    test_phone = os.getenv("SENT_TEST_PHONE")

    if not template_id or not test_phone:
        raise ValueError(
            "Missing template ID or test phone in .env"
        )

    content_title = input("Enter your content title: ").strip()

    if not content_title:
        print("Please enter a content title.")
        return

    client = Sent()

    try:
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

        print("\nSent Creator Drop")
        print("-----------------")
        print(f"Content: {content_title}")
        print(f"Status: {response.data.status}")

        for recipient in response.data.recipients:
            print(f"Message ID: {recipient.message_id}")
            print(f"Channel: {recipient.channel}")


    except sent_dm.APIConnectionError:
        print("Connection error: Could not reach Sent.")

    except sent_dm.RateLimitError:
        print("Rate limit reached. Please try again later.")

    except sent_dm.APIStatusError as error:
        print("Sent returned an API error.")
        print(f"HTTP status: {error.status_code}")
        print(f"Details: {error}")

if __name__ == "__main__":
    main()


