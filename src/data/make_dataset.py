import urllib.request
import os

from google_drive_downloader import GoogleDriveDownloader as gdd

cwd = os.getcwd()


def _download_raw_dataset():
    gdd.download_file_from_google_drive(file_id='1tfDLhnQkJYbljmikVbWV_YSzSl8Vbyhe',
                                        dest_path=os.path.join(cwd, "data\\raw\\data_original.csv"),
                                        unzip=False)

    return print("Raw dataset downloaded in data\\raw" + "\n")


def _download_interim_dataset():
    gdd.download_file_from_google_drive(file_id='1p1sXafC8gmjJTHWHR70Xx80W2y_AW8j4e',
                                        dest_path=os.path.join(cwd, "data\\interim\\data_clustered.csv"),
                                        unzip=False)

    return print("Interim dataset downloaded in data\\interim" + "\n")


def _download_processed_dataset():
    gdd.download_file_from_google_drive(file_id='1VGamHN9-JONv27LpixcGZj5ZtasP3yBn',
                                        dest_path=os.path.join(cwd, "data\\processed\\data_life_death.csv"),
                                        unzip=False)

    gdd.download_file_from_google_drive(file_id="https://drive.google.com/open?id=16cII6S_H063s1xZ__WGwu5S88vKF67y8",
                                        dest_path=os.path.join(cwd, "data\\processed\\data_love_fam.csv"),
                                        unzip=False)

    gdd.download_file_from_google_drive(file_id="https://drive.google.com/open?id=1_s5SvMYav-74KaTC8r_zdfS8Jrbx96cy",
                                        dest_path=os.path.join(cwd, "data\\processed\\data_nature.csv"),
                                        unzip=False)

    gdd.download_file_from_google_drive(file_id="https://drive.google.com/open?id=1VVhZBYChR-BpX1INX18um0bvxrEZmKvF",
                                        dest_path=os.path.join(cwd, "data\\processed\\data_others.csv"),
                                        unzip=False)

    gdd.download_file_from_google_drive(file_id="https://drive.google.com/open?id=1wo_VC3H-gdGEXpJqgmSjLWjYrDBSPtxz",
                                        dest_path=os.path.join(cwd, "data\\processed\\data_soc_phi_cul.csv"),
                                        unzip=False)

    return print("processed datasets downloaded in data\\processed")


def main():
    """ Download the datasets already prepared for this project.
    """
    _download_raw_dataset()
    _download_interim_dataset()
    _download_processed_dataset()
    ### Improvement - to factorise code wherever possible

if __name__ == '__main__':
    main()