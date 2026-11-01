sales_locations_bronze = StructType([
    StructField("location_id",
        StringType(),
        False,
        {"comment": "Source location identifier, as received (not yet asserted unique)."}
    ),
    StructField("dealership_location",
        StringType(),
        False,
        {"comment": "Human-readable dealership name/city, matches sales.cars.dealership_location."}
    ),
    StructField("firm_name",
        StringType(),
        True
    ),
    StructField("address",
        StringType(),
        True
    ),
    StructField("city",
        StringType(),
        True
    ),
    StructField("state",
        StringType(),
        True
    ),
    StructField("zip_code",
        StringType(),
        True
    ),
    StructField("phone",
        StringType(),
        True
    ),
    StructField("opened_date",
        StringType(),
        True
    ),
    StructField("_source_system",
        StringType(),
        False,
        {"comment": "Originating source identifier (matches the landing [source] path segment)."}
    ),
    StructField("_source_file",
        StringType(),
        False,
        {"comment": "Landing-zone file this record was ingested from."}
    ),
    StructField("_ingested_at",
        TimestampType(),
        False,
        {"comment": "Ingestion timestamp assigned by the bronze ingestion job."}
    )
])