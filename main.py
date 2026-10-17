from sent_client import send_content_notification
import sent_dm


def main():
    content_title = input("Enter your content title: ").strip()

    if not content_title:
        print("Please enter a content title.")
        return

    try:
        response = send_content_notification(content_title)

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

    except ValueError as error:
        print(f"Configuration error: {error}")



if __name__ == "__main__":
    main()
