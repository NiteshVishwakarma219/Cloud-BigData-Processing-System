from data_ingestion import load_data
from data_filtering import filter_sales
from data_transformation import add_gst
from data_processing import process_sales
from store_to_rds import store_data


def main():

    print("\n========== BIG DATA PROJECT ==========")

    # Step 1
    spark, df = load_data()

    # Step 2
    high_sales = filter_sales(df)

    # Step 3
    transformed_df = add_gst(df)

    # Step 4
    result = process_sales(transformed_df)

    # Step 5
    store_data(result)

    print("\n========== PIPELINE COMPLETED ==========")

    spark.stop()


if __name__ == "__main__":
    main()