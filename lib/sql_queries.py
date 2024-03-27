select_all_female_bears_return_name_and_age = """
    SELECT
     name,
        age
    FROM bears
    WHERE sex = 'F';
"""

select_all_bears_names_and_orders_in_alphabetical_order = """
    
     SELECT
        name,
        age,
        color
    FROM bears
    WHERE age > 5;
"""

select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
    
    SELECT
        name,
        temperament
    FROM bears
    WHERE temperament IN ('Calm', 'Friendly');
"""

select_oldest_bear_and_returns_name_and_age = """
    SELECT
    name,
    age
FROM
    bears
ORDER BY
    age DESC
LIMIT 1;


"""
select_youngest_bear_and_returns_name_and_sex = """
    
    SELECT
        name,
        sex
    FROM bears
    WHERE color = 'Brown';
"""
