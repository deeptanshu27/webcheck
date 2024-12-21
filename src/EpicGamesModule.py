from selenium.webdriver.common.by import By
from winotify import Notification
from Module import Module

class EpicGamesModule(Module):
    def run(self, driver):
        driver.get("https://store.epicgames.com/en-US/")

        root = driver.find_element(By.XPATH, "//*[@data-testid='discover-page-0']")
        div_container = root.find_elements(By.TAG_NAME, "div")[1]

        div_container_childs = div_container.find_elements(By.XPATH, "*")

        container = None
        for i in div_container_childs:
            try:
                if i.find_element(By.TAG_NAME, "h5").text == "Free Games":
                    container = i
                    break
            except:
                pass

        if not container:
            # toast = Notification(app_id = "webcheck",
            #             title = "webcheck Error",
            #             msg = "free games container not found",
            #             duration = "long"
            #             #  icon = r"FullPath.ico"
            #             )
            # toast.show()
            self.errorMsg = "Free Games container not found..."
            return 1
        else:
            all_games = container.find_elements(By.TAG_NAME, "h6")
            all_games_text = ""
            for i in all_games:
                all_games_text += "● " + i.text + "\n"
            self.display_notif("Free Games", all_games_text, "long", "https://store.epicgames.com/en-US")
        
        return 0
    
    # TODO: Add icon support
    def display_notif(self, title, msg, duration = "long", launch = "", icon = ""):
        toast = Notification(
            app_id = self.name,
            title = title,
            msg = msg,
            duration = duration,
            launch = launch,
            icon = icon
            )
        toast.show()