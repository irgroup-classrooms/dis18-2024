# Notes
* Need to install chrome. -> create new vm ^^
* Prototype running
* first run always raises exception because of a not started chrome driver. Fix: start a second time \_o.O_/ (look into it later..)

# Changes
## `run`- function
* init param: `search_url = "https://core.ac.uk/"`
* init param: `search_box = "styles-control-12Pze"`
* result element: `for result in soup.find_all("div", class_=["styles_search-results__2AZDM"]):`
* title element: change tag to `h3` `title_elem = result.find("h3", class_=["styles-title-1k6Ib"])`
* description element: `description_elem = result.find("div", class_=["styles-content-35LN7"])`
* search box interaction: didn't have a `name`-tag but a `class`-tag ` search = driver.find_element(By.CLASS_NAME, search_box) #Find search box`

