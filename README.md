# AtlasPortalAutomation

''''''''''''''''
Load default Chrome profile:
''''''''''''''''
http://stackoverflow.com/questions/31062789/how-to-load-default-profile-in-chrome-using-python-selenium-webdriver
http://stackoverflow.com/questions/12332975/installing-python-module-within-code

# List of Genres:
--------------------------------------
Undefined:Undefined
Undefined:Free Previews
Specialist:Undefined
Specialist:Adult
Specialist:Events
Specialist:Shopping
Children:Undefined
Children:Cartoons
Children:Comedy
Children:Drama
Children:Educational
Children:Under 5
Children:Factual
Children:Magazine
Children:Games Shows
Children:Games
Entertainment:Undefined
Entertainment:Action
Entertainment:Comedy
Entertainment:Detective
Entertainment:Drama
Entertainment:Game Shows
Entertainment:Sci-Fi
Entertainment:Soaps
Entertainment:Animation
Entertainment:Chat Show
Entertainment:Cooking
Entertainment:Factual
Entertainment:Fashion
Entertainment:Gardening
Entertainment:Travel
Entertainment:Technology
Entertainment:Arts
Entertainment:Lifestyle
Entertainment:Home
Entertainment:Magazine
Entertainment:Medical
Entertainment:Reviews
Entertainment:Antiques
Entertainment:Motors
Entertainment:Arts & Literature
Entertainment:Ballet
Entertainment:Opera
Music & Radio:Undefined
Music & Radio:Classical
Music & Radio:Folk & Country
Music & Radio:National Music
Music & Radio:Jazz
Music & Radio:Opera
Music & Radio:Rock & Pop
Music & Radio:Alternative Music
Music & Radio:Events
Music & Radio:Club & Dance
Music & Radio:Hip Hop
Music & Radio:Soul/R&B
Music & Radio:Dance
Music & Radio:Ballet
Music & Radio:Kids
Music & Radio:Current Affairs
Music & Radio:Features
Music & Radio:Arts & Literature
Music & Radio:Factual
Music & Radio:Drama
Music & Radio:Comedy
Music & Radio:Lifestyle
Music & Radio:News & Weather
Music & Radio:Easy Listening
Music & Radio:Discussion
Music & Radio:Entertainment
Music & Radio:Religious
Music & Radio:Business & Finance
Music & Radio:Science
Music & Radio:Gold
Music & Radio:Soap
Music & Radio:Sport
News & Documentaries:Undefined
News & Documentaries:Business
News & Documentaries:World Cultures
News & Documentaries:Adventure
News & Documentaries:Biography
News & Documentaries:Educational
News & Documentaries:Features
News & Documentaries:Politics
News & Documentaries:News
News & Documentaries:Nature
News & Documentaries:Religious
News & Documentaries:Science
News & Documentaries:Showbiz
News & Documentaries:War Documentaries
News & Documentaries:Historical
News & Documentaries:Ancient
News & Documentaries:Transport
News & Documentaries:Docudrama
News & Documentaries:World Affairs
News & Documentaries:Features
News & Documentaries:Showbiz
News & Documentaries:Politics
News & Documentaries:Transport
News & Documentaries:World Affairs
Movies:Undefined
Movies:Action
Movies:Animation
Movies:Comedy
Movies:Family
Movies:Drama
Movies:Sci-Fi
Movies:Thriller
Movies:Horror
Movies:Romance
Movies:Musical
Movies:Mystery
Movies:Western
Movies:Factual
Movies:Fantasy
Movies:Erotic
Movies:Adventure
Movies:War
Sports:Undefined
Sports:American Football
Sports:Athletics
Sports:Baseball
Sports:Basketball
Sports:Boxing
Sports:Cricket
Sports:Fishing
Sports:Football
Sports:Golf
Sports:Ice Hockey
Sports:Motor Sport
Sports:Racing
Sports:Rugby
Sports:Equestrian
Sports:Wintersports
Sports:Snooker/Pool
Sports:Tennis
Sports:Wrestling
Sports:Darts
Sports:Watersports
Sports:Extreme


# List of Ratings:
--------------------------------------
Infant
All Ages
7+
12+
13+
16+
18+

# Config settings:
-----------------------------------------------
'''Portal URL for testing'''    
portal_url_test = "https://vodportal-test.awf.bskyb.com"
portal_url_stage = "https://vodportal-stage.awf.bskyb.com/#/login"
provider="Test provider 1"
'''
Super user connection details
'''
super_user_name="Dervis_superuser"
super_user_password="test1234"
'''
Admin user connection details
'''
Admin_user_name="dervis_admin"
Admin_user_password="abcd12345"
'''browser for testing'''
test_browser="chrome"
'''chrome exe path'''
chrom_exe="C:/workspace/DebugGUI/chromedriver_win32/chromedriver"
'''isilon drop zone'''
drop_zone="/mnt/dmz/atlas_provider_1/drop"
'''MongoDB connection details'''
mongodb_connection_details=""
'''content location'''
portal_url = "https://vodportal-stage.awf.bskyb.com/#/login"
user_name="dervis_admin"
user_password="abcd12345"
provider="Test provider 1"
browser="chrome"
test_image_folder_location="C:\workspace\AtlasPortalAutomation\isilon\test_images"
test_media_folder_location="C:\workspace\AtlasPortalAutomation\isilon\test_media"
test_subtitles_folder_location="C:\workspace\AtlasPortalAutomation\isilon\subtitles"
reports="C:\workspace\AtlasPortalAutomation\excel\excel_documents\test.xlsm"