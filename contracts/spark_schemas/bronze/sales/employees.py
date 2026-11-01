sales_employees_bronze = StructType([
    StructField("employee_id",
        StringType(),
        False,
        {"comment": "Source employee identifier, as received (not yet asserted unique)."}
    ),
    StructField("first_name",
        StringType(),
        True
    ),
    StructField("last_name",
        StringType(),
        True
    ),
    StructField("job_title",
        StringType(),
        True
    ),
    StructField("dealership_location",
        StringType(),
        True,
        {"comment": "Dealership the employee works at, matches sales.locations.dealership_location."}
    ),
    StructField("hire_date",
        StringType(),
        True
    ),
    StructField("email",
        StringType(),
        True
    ),
    StructField("phone",
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