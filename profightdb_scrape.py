import requests, random
from bs4 import BeautifulSoup
from datetime import datetime, timedelta 

# Fetch response from the URL
def connectWeb():
    url = "http://www.profightdb.com/this-day-in-history.html"
    print(f"Que Entrance Music: {url}")
    response = requests.get(url)
    response.raise_for_status()  
    return response.text  

# Parse the data from the response
def parseDayHistoryData():
    html_data = connectWeb()
    all_promo_cardName = []
    if html_data:
        soup = BeautifulSoup(html_data, 'html.parser')
        table_from_page = soup.find("div", class_="table-wrapper")
        if table_from_page:  
            rows = table_from_page.find_all("tr")
            if len(rows) > 1:  # check for rows in the table
                for idx, row in enumerate(rows[1:], start=2):  
                    cells = row.find_all("td")
                    if len(cells) > 3:  # double check that there are cells in the row from the table
                        date_data = cells[0].text.strip() # Give me the dates to store and manipulate later
                        promotion_data = cells[1].text.strip()  # Give me the promotion names
                        matchCardName_data = cells[2].text.strip()  # Give me the cardName associated as well

                        link_tag = cells[2].find("a") #find the anchor tag associated with the CardName for the website link
                        matchCardName_link = link_tag['href'] if link_tag else "No web link is available"
                        all_promo_cardName.append((date_data, promotion_data, matchCardName_data, matchCardName_link))  # Add to list
    return all_promo_cardName


def matchHistory():
    all_promotions = parseDayHistoryData()  
    tenYearsorOlder = datetime.now() - timedelta(days=10 * 365)
    olderMatchCards = set()

    for date_data, promotion_data, matchCardName_data, matchCardName_link in all_promotions:
        # Remove string from date to be able to manipulate with 10 years or older
        dateFormatted = date_data.replace("st", "").replace("nd", "").replace("rd", "").replace("th", "")
        matchCardDate = datetime.strptime(dateFormatted, '%a, %b %d %Y')
            
        # Looking for only dates 10 years or older
        if matchCardDate < tenYearsorOlder:
            matchCardURL = f"http://www.profightdb.com{matchCardName_link}"
            olderMatchCards.add(matchCardURL)

    
    return olderMatchCards

def randomMatchCardURL():
    olderMatchCards = matchHistory()
    if olderMatchCards:
        return random.choice(list(olderMatchCards))  
    else:
        return "Listen here Brother...No matches are 10 years or older."


randomURL = randomMatchCardURL()
print(randomURL)

def getMainEventMatch():
   randomURL = randomMatchCardURL()
   response = requests.get(randomURL)
   return response.text

def clean_wrestler_data(data):
    # Replace \xa0 with a space, keeping (c) intact
    return data.replace("\xa0", " ").strip()

def parseMainEvent():
    history_data = getMainEventMatch()
    cardInfo = []
    page_title = None
    event_details = []  # Array to store page_title, promotion, venue, and date
    
    if history_data:
        soup = BeautifulSoup(history_data, 'html.parser')
        
        # Extract the page title
        title_tag = soup.find("title")
        if title_tag:
            full_title = title_tag.text.strip()
            # Strip everything after "at"
            page_title = full_title.split(" at ")[0]
        
        # Extract event details (promotion, venue, date)
        table_with_details = soup.find("table", width="100%")  # Locate the event details table
        if table_with_details:
            rows = table_with_details.find_all("tr")
            for row in rows:
                cells = row.find_all("td")
                if len(cells) > 0:
                    # Extract date
                    if "Date:" in cells[0].text:
                        date = cells[0].find("a").text.strip()  # Extract the date link text
                    # Extract venue
                    if "Venue:" in cells[0].text:
                        venue = cells[0].text.replace("Venue:", "").strip()
                    # Extract promotion
                    if "Promotion:" in cells[1].text:
                        promotion = cells[1].text.replace("Promotion:", "").strip()
        
        # Add all event details to the array
        event_details = [page_title, date, venue, promotion]
        
        # Extract main event details from the match table
        table_from_page = soup.find("div", class_="table-wrapper")
        if table_from_page:
            rows = table_from_page.find_all("tr")
            if len(rows) > 1:  # Check for rows in the table
                for idx, row in enumerate(rows[1:], start=2):
                    cells = row.find_all("td")
                    if len(cells) > 3:
                        wrestlerOne_data = clean_wrestler_data(cells[1].text.strip())
                        outcome_data = cells[2].text.strip()
                        wrestlerTwo_data = clean_wrestler_data(cells[3].text.strip())
                        time_match_data = cells[4].text.strip()
                        match_type = cells[5].text.strip()
                        title_data = cells[6].text.strip()
                        cardInfo.append((wrestlerOne_data, outcome_data, wrestlerTwo_data, time_match_data, match_type, title_data))  # Add to list
    
    return event_details, cardInfo[-1] if cardInfo else None
       
mainevent = parseMainEvent()
print(mainevent)
            
            
                  
                    
                    
