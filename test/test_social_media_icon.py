from page_object.login_page import LoginPage
from page_object.social_media import SocialMedia
from config.config import BASE_URL, USERNAME, PASSWORD

def test_social_media_icon(driver):
    driver.get(BASE_URL)

    #Login
    login = LoginPage(driver)
    login.login(USERNAME,PASSWORD)

    #Socail media icon
    socialicon = SocialMedia(driver)

    #twitter
    socialicon.get_twitter()

    driver.switch_to.window(driver.window_handles[1])
    assert "https://x.com/saucelabs" in driver.current_url

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    #facebook
    socialicon.get_facebook()
    driver.switch_to.window(driver.window_handles[1])
    assert "https://www.facebook.com/saucelabs" in driver.current_url
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    #Linkdin
    socialicon.get_linkdin()
    driver.switch_to.window(driver.window_handles[1])
    assert "https://www.linkedin.com/company/sauce-labs/" in driver.current_url
    driver.close()
    driver.switch_to.window(driver.window_handles[0])



