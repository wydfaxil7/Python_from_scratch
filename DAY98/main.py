############## MULTI PROCESSING ################

import requests
import multiprocessing

def downloadFile(url, name):
    print(f"Started downloading {name}")
    response = requests.get(url)
    with open(f"files/file{name}.jpg", "wb") as f:
        f.write(response.content)
    print(f"Finished downloading {name}")

if __name__ == "__main__":
    url = "https://picsum.photos/2000/3000"
    pros = []
    for i in range(20):

        
        # downloadFile(url, i) # This is taking alot of time, this is where multiprocessing gets in!


        p = multiprocessing.Process(target=downloadFile, args=(url, i))
        p.start()
        pros.append(p)

        multiprocessing.freeze_support()

    for p in pros:
        p.join()