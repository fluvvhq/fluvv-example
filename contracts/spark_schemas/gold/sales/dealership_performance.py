sales_dealership_performance_gold = StructType([
    StructField("dealership_location",
        StringType(),
        False,
        {"comment": "The dealership, identified by its location name (city). One row each."}
    ),
    StructField("city",
        StringType(),
        True,
        {"comment": "City the dealership is in."}
    ),
    StructField("state",
        StringType(),
        True,
        {"comment": "Two-letter US state code of the dealership."}
    ),
    StructField("opened_date",
        DateType(),
        True,
        {"comment": "The date the dealership opened."}
    ),
    StructField("transaction_count",
        LongType(),
        False,
        {"comment": "Number of car sale transactions at the dealership, all time. 0 when it has none."}
    ),
    StructField("total_sales_value",
        DecimalType(20, 2),
        False,
        {"comment": "Sum of sale prices across all of the dealership's transactions. 0 when it has none."}
    ),
    StructField("average_sale_price",
        DecimalType(14, 6),
        True,
        {"comment": "Average sale price across all of the dealership's transactions. Null when it has none."}
    ),
    StructField("employee_count",
        LongType(),
        False,
        {"comment": "Number of employees currently at the dealership. 0 when it has none."}
    ),
    StructField("sales_per_employee",
        DecimalType(20, 2),
        True,
        {"comment": "total_sales_value divided by employee_count. Null when the dealership has no employees."}
    )
])