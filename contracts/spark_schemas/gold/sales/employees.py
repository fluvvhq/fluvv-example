sales_employees_gold = StructType([
    StructField("employee_id",
        StringType(),
        False,
        {"comment": "Unique employee identifier."}
    ),
    StructField("first_name",
        StringType(),
        False,
        {"comment": "The employee's first name."}
    ),
    StructField("last_name",
        StringType(),
        False,
        {"comment": "The employee's last name."}
    ),
    StructField("job_title",
        StringType(),
        False,
        {"comment": "The employee's job title, e.g. Sales Associate, Finance Manager."}
    ),
    StructField("dealership_location",
        StringType(),
        False,
        {"comment": "The dealership, identified by its location name (city). The shared join key across the sales tables."}
    ),
    StructField("hire_date",
        DateType(),
        False,
        {"comment": "The date the employee was hired."}
    ),
    StructField("email",
        StringType(),
        False,
        {"comment": "The employee's work email address."}
    ),
    StructField("phone",
        StringType(),
        True,
        {"comment": "The employee's phone number."}
    )
])