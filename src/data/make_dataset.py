def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """

    download_from_web()

    make_copy_to_raw()

    clean_data()

    cluster_poems()

    add_tags()



if __name__ == '__main__':

    main()

    # Export data