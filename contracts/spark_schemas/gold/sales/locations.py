sales_locations_gold = StructType([
    StructField("location_id",
        StringType(),
        False,
        {"comment": "Unique location identifier."}
    ),
    StructField("dealership_location",
        StringType(),
        False,
        {"comment": "The dealership, identified by its location name (city). The shared join key across the sales tables."}
    ),
    StructField("firm_name",
        StringType(),
        False,
        {"comment": "Name of the car sales firm operating the dealership."}
    ),
    StructField("address",
        StringType(),
        False,
        {"comment": "Street address of the dealership."}
    ),
    StructField("city",
        StringType(),
        False,
        {"comment": "City the dealership is in."}
    ),
    StructField("state",
        StringType(),
        False,
        {"comment": "Two-letter US state code of the dealership."}
    ),
    StructField("zip_code",
        StringType(),
        False,
        {"comment": "Five-digit US ZIP code of the dealership."}
    ),
    StructField("phone",
        StringType(),
        True,
        {"comment": "The dealership's public phone number."}
    ),
    StructField("opened_date",
        DateType(),
        False,
        {"comment": "The date the dealership opened."}
    )
])