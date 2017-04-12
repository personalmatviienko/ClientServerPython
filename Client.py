import requests
import argparse
from urllib.parse import urlencode

url = "http://localhost:8080/"


def getRequest(queue):
    payload = {'queue': queue}
    response = requests.get(url, payload)
    print(response.text)
    print("[done]")
    return response


def postRequest(message, queue):
    post_fields = {'message': message, 'queue': queue}
    response = requests.post(url, urlencode(post_fields).encode())
    print(response.text)
    print("[done]")
    return response


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('action', action="store", type=str)
    parser.add_argument('--message', action="store", dest="message", type=str)
    parser.add_argument('--queue', action="store", dest="queue", type=int, default=0)

    args = parser.parse_args()
    if args.action == "get":
        getRequest(args.queue)
    if args.action == "post":
        postRequest(args.message, args.queue)

if __name__ == "__main__":
    main()



