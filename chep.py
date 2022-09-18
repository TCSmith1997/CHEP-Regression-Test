from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
# Driver Code
if __name__ == '__main__':
  
    # create object
    desired_cap={}
    edgeBrowser = webdriver.Edge(executable_path="/Users/tommy.smith1997/repos/CHEP-Regression-Test/msedgedriver",capabilities=desired_cap)
    edgeBrowser.implicitly_wait(10)
    edgeBrowser.delete_all_cookies()
    edgeBrowser.get('https://www.chep.com')
    time.sleep(5)
    cookieButton = edgeBrowser.find_element_by_id("onetrust-accept-btn-handler")
    assert cookieButton
    cookieButton.click()
    edgeBrowser.quit()
