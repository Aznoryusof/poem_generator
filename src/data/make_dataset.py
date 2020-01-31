import urllib.request
import os

cwd = os.getcwd()

def _download_raw_dataset():
    urllib.request.urlretrieve("https://drive.google.com/open?id=1tfDLhnQkJYbljmikVbWV_YSzSl8Vbyhe", 
                               os.path.join(cwd, "data\\raw\\data_original.csv"))

    return print("Raw dataset downloaded in data\\raw" + "\n")


def _download_interim_dataset():
    urllib.request.urlretrieve("https://drive.google.com/open?id=1p1sXafC8gmjJTHWHR70Xx80W2y_AW8j4", 
                               os.path.join(cwd, "data\\interim\\data_clustered.csv"))

    return print("Interim dataset downloaded in data\\interim" + "\n")


def _download_processed_dataset():
    urllib.request.urlretrieve("https://drive.google.com/open?id=1VGamHN9-JONv27LpixcGZj5ZtasP3yBn", 
                               os.path.join(cwd, "data\\processed\\data_life_death.csv"))

    urllib.request.urlretrieve("https://drive.google.com/open?id=16cII6S_H063s1xZ__WGwu5S88vKF67y8", 
                               os.path.join(cwd, "data\\processed\\data_love_fam.csv"))

    urllib.request.urlretrieve("https://drive.google.com/open?id=1_s5SvMYav-74KaTC8r_zdfS8Jrbx96cy", 
                               os.path.join(cwd, "data\\processed\\data_nature.csv"))

    urllib.request.urlretrieve("https://drive.google.com/open?id=1VVhZBYChR-BpX1INX18um0bvxrEZmKvF", 
                               os.path.join(cwd, "data\\processed\\data_others.csv"))

    urllib.request.urlretrieve("https://drive.google.com/open?id=1wo_VC3H-gdGEXpJqgmSjLWjYrDBSPtxz", 
                               os.path.join(cwd, "data\\processed\\data_soc_phi_cul.csv"))

    return print("processed dataset downloaded in data\\processed")


def main():
    """ Download the datasets already prepared for this project.
    """
    _download_raw_dataset()
    _download_interim_dataset()
    _download_processed_dataset()


if __name__ == '__main__':
    main()