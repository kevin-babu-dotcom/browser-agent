import webbrowser
from fuzzywuzzy import fuzz
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def open_website(user_input):
    if user_input.startswith("http"):
        url = user_input
    else:
        website_options = {
            "google": "https://www.google.com/",
            "youtube": "https://www.youtube.com/",
            "facebook": "https://www.faebook.org/",
            "instagram": "https://www.instagram.com/",
            "x": "https://www.twitter.com/",
            "baidu": "https://www.baidu.com/",
            "amazon": "https://www.amazon.com/",
            "linkedin": "https://www.linkedin.com/",
            "netflix": "https://www.netflix.com/",
     
        }
        highest_match_score = 0
        best_match_url = None
        for website_name, website_url in website_options.items():
            match_score = fuzz.ratio(user_input.lower(), website_name.lower())
            if match_score > highest_match_score:
                highest_match_score = match_score
                best_match_url = website_url

        if best_match_url:
            url = best_match_url
            print(f"Opening {website_options[best_match_url.split('://')[1]]}...")
        else:
            print(f"Couldn't find a website match for '{user_input}'.")
            return

    try:
        webbrowser.open(url, new=2)  
    except webbrowser.Error as e:
        print(f"Error opening website: {e}")

def close_tab(not_used):
    
    try:
        driver = webdriver.Chrome() 
        driver.get("about:blank") 
        driver.switch_to.window(driver.window_handles[-1]) 
        driver.close()
        print("Closed the most recently opened tab.")
    except Exception as e:
        print(f"Error closing tab: {e}")
    finally:
        driver.quit()  

def main():
    print("Welcome to your friendly web browser assistant!")

    while True:
        user_input = input("Enter a website name or URL (or 'quit' to exit): ")

        if user_input.lower() == "quit":
            break
        else:
            open_website(user_input)

        user_close_input = input("Close the opened tab? (y/n): ")
        if user_close_input.lower() == 'y':
            close_tab(None)

if __name__ == "__main__":
    main()
