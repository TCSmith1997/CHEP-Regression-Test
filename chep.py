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
    edgeBrowser.maximize_window()
    time.sleep(5)
    cookieButton = edgeBrowser.find_element_by_id("onetrust-accept-btn-handler")
    assert cookieButton
    cookieButton.click()
    flag = edgeBrowser.find_element_by_xpath("/html[1]/body[1]/div[1]/header[1]/section[2]/nav[1]/div[1]/section[1]/ul[2]/li[1]/div[2]/a[1]/img[1]")
    flagSrc = flag.get_attribute('src')
    language = edgeBrowser.find_element_by_xpath("/html[1]/body[1]/div[1]/header[1]/section[2]/nav[1]/div[1]/section[1]/ul[2]/li[1]/div[1]/p[1]").text
    if flagSrc == "https://www.chep.com/files/country_flags/United%20States.png" and language=="English":
        pass
    else:
        flag.click()
        edgeBrowser.find_element_by_xpath("/html[1]/body[1]/div[1]/section[1]/div[3]/div[2]/div[2]/ul[1]/li[7]/div[1]/ul[1]/li[4]/a[1]").click()
    whyTab=edgeBrowser.find_element_by_xpath("//a[contains(text(),'Why CHEP?')]")
    productsTab=edgeBrowser.find_element_by_link_text("Products")
    servicesTab=edgeBrowser.find_element_by_link_text("Services & Solutions")
    sustainabilityTab=edgeBrowser.find_element_by_link_text("Sustainability")
    aboutTab=edgeBrowser.find_element_by_link_text("About")
    careersTab=edgeBrowser.find_element_by_link_text("Careers")
    assert(whyTab and productsTab and servicesTab and sustainabilityTab and aboutTab and careersTab)
    productsTab.click()
    #edgeBrowser.quit()
