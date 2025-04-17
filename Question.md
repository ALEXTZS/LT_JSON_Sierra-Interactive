# Problem Statement

You are provided with a nested JSON that contains customer purchase details. The JSON contains an array of products for each customer along with details such as product name and price.

Your task is to flatten the JSON structure and extract the relevant fields: `customer_id`, `order_id`, `product_name`, and `product_price`. You will need to explode the array of products so that each product becomes a separate row.

After flattening and exploding the data, use `display(df)` to show the final DataFrame.

Details about JSON data source in Spark can be found [here](https://spark.apache.org/docs/latest/sql-data-sources-json.html).

## Input

- **File Path**: `/datasets/orders.json`
- **Schema**:
  - `customer_id` (String)
  - `order_id` (String)
  - `products` (Array of Structs)
    - `product_name` (String)
    - `product_price` (Integer)

### Example Input (JSON):

```json
[
  {
    "customer_id": "C0001",
    "order_id": "O1001",
    "products": [
      {
        "product_name": "Laptop",
        "product_price": 1500
      },
      {
        "product_name": "Mouse",
        "product_price": 25
      }
    ]
  },
  {
    "customer_id": "C0002",
    "order_id": "O1002",
    "products": [
      {
        "product_name": "Keyboard",
        "product_price": 75
      }
    ]
  }
]
```

## Output

- **Schema**:
  - `customer_id` (String)
  - `order_id` (String)
  - `product_name` (String)
  - `product_price` (Integer)

### Example Output:
   customer_id | order_id | product_name | product_price |
 |-------------|----------|--------------|---------------|
 | C0001       | O1001    | Laptop       | 1500          |
 | C0001       | O1001    | Mouse        | 25            |
 | C0002       | O1002    | Keyboard     | 75            |

## Explanation:
- The input JSON is nested, with each customer having multiple products in an array.
- This task requires you to explode this array, flattening the nested structure so that each product corresponds to a separate row.
- The output contains four columns: `customer_id`, `order_id`, `product_name`, and `product_price`.

## Files:
- **Input**: /datasets/orders.json (in JSON format)
- **Output**: Use display(df) to show the final DataFrame.

## Tip:
Look into multiline JSON files if you're having trouble reading the JSON file.
