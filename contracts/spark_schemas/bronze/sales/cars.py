sales_cars_bronze = StructType([
    StructField("order_id",
        StringType(),
        False,
        {"comment": "Source order identifier, as received (not yet asserted unique)."}
    ),
    StructField("sale_date",
        StringType(),
        False
    ),
    StructField("dealership_location",
        StringType(),
        True
    ),
    StructField("salesperson",
        StringType(),
        True
    ),
    StructField("customer_name",
        StringType(),
        True
    ),
    StructField("make",
        StringType(),
        True
    ),
    StructField("model",
        StringType(),
        True
    ),
    StructField("year",
        StringType(),
        True,
        {"comment": "Model year, as received. Renamed to model_year in silver."}
    ),
    StructField("color",
        StringType(),
        True
    ),
    StructField("mileage",
        StringType(),
        True
    ),
    StructField("price",
        StringType(),
        True
    ),
    StructField("payment_type",
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