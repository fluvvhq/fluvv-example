sales_cars_silver = StructType([
    StructField("order_id",
        StringType(),
        False,
        {"comment": "Unique identifier for a car sales transaction."}
    ),
    StructField("sale_date",
        DateType(),
        False,
        {"comment": "The date the car sale transaction occurred."}
    ),
    StructField("dealership_location",
        StringType(),
        False
    ),
    StructField("salesperson",
        StringType(),
        False,
        {"comment": "The salesperson who handled the sale, as an abbreviated display name (e.g. \"J. Rivera\")."}
    ),
    StructField("customer_name",
        StringType(),
        False,
        {"comment": "The name of the customer who purchased the vehicle."}
    ),
    StructField("make",
        StringType(),
        False,
        {"comment": "The vehicle manufacturer, e.g. Toyota, Honda, Ford."}
    ),
    StructField("model",
        StringType(),
        False,
        {"comment": "The vehicle model, e.g. Camry, Civic, F-150."}
    ),
    StructField("model_year",
        IntegerType(),
        False,
        {"comment": "The model year of the vehicle, as assigned by the manufacturer. Renamed from bronze's `year`."}
    ),
    StructField("color",
        StringType(),
        True,
        {"comment": "The exterior color of the vehicle."}
    ),
    StructField("mileage",
        IntegerType(),
        False,
        {"comment": "The vehicle's odometer reading at time of sale, in miles."}
    ),
    StructField("price",
        DecimalType(10, 2),
        False,
        {"comment": "The sale price of the vehicle."}
    ),
    StructField("payment_type",
        StringType(),
        False,
        {"comment": "How the customer paid for the vehicle: Cash, Finance, or Lease."}
    )
])