sales_cars_gold = StructType([
    StructField("dealership_location",
        StringType(),
        False,
        {"comment": "The dealership, identified by its location name (city). The shared join key across the sales tables."}
    ),
    StructField("sale_month",
        DateType(),
        False,
        {"comment": "First day of the calendar month this row summarizes."}
    ),
    StructField("transaction_count",
        IntegerType(),
        False,
        {"comment": "Number of car sale transactions at the dealership in the month."}
    ),
    StructField("total_sales_value",
        DecimalType(12, 2),
        False,
        {"comment": "Sum of sale prices across the dealership's transactions in the month."}
    ),
    StructField("average_sale_price",
        DecimalType(10, 2),
        False,
        {"comment": "Average sale price across the dealership's transactions in the month."}
    ),
    StructField("unique_customers",
        IntegerType(),
        False,
        {"comment": "Number of distinct customers who bought from the dealership in the month."}
    )
])