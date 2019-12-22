class TestData():
    # --- drivers --- #
    """API,Chrome,FireFox,Safari"""
    BROWSER_TYPE = "chrome"
    FIREFOX_EXECUTABLE_PATH = "/Users/doringber/Downloads/geckodriver"
    # CHROME_EXECUTABLE_PATH= "/Users/doringber/Downloads/Chrome_Downloads/chromedriver"
    CHROME_EXECUTABLE_PATH ="/usr/local/bin/chromedriver"
    # --- URL ---
    BASE_URL = "https://www.ynet.co.il/home/0,7340,L-8,00.html"

    # --- Text And Locators ---
    SEARCH_TERM = "WD My Passport 4TB"
    HOME_PAGE_TITLE = "Amazon.in"
    NO_RESULTS_TEXT = "No results found."
    SIGN_IN_PAGE_TITLE = "Amazon Sign In"
    ALERT_SIGN_IN_SCREEN = "There was a problem"
    SIGN_IN_LOCATOR_ALERT = "a-alert-heading"
    EMPTY_CART_SCREEN_LOCATOR = "sc-empty-cart-header"
    EMPTY_CART_SCREEN_TEXT = "Your Shopping Cart is empty."

    # --- Appium ---
    UDID = '821e977f0804'
    PLATFORM_NAME = 'android'
    DEVICE_NAME = 'Mi A1'
    APP_ACTIVITY = '.HomeActivity'
    APP_PACKAGE = 'com.imdb.mobile'
    SERVER = 'http://localhost:4723/wd/hub'
    NO_RESET = 'true'
    AUTO_ACCEPET_ALERTS = 'true'

    # --- API ---
    API_URL_GET = "https://reqres.in/api/users?page=2"
    API_URL_POST = "https://reqres.in/api/login"
    API_URL_LOCAL_HOST = "http://127.0.0.1:8080/json"

    # --- PATHS ---
    SCREEN_PATH = '/Users/doringber/PycharmProjects/homework/amazon/web/html_reports/screenshots'
    LOGGING_PATH = "/Users/doringber/PycharmProjects/homework/amazon/web/html_reports/html_logs/"





