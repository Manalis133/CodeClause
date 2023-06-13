
import pyshorteners

def shorten_url(url):
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    return shortened_url

def main():
    url = input("Enter the URL to shorten: ")
    shortened_url = shorten_url(url)
    print("Shortened URL:", shortened_url)

if __name__ == "__main__":
    main()
