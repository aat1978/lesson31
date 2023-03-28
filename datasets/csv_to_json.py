import csv
import json


def convert_file(csv_file, json_file, model):
    result = []
    with open(csv_file, encoding='utf-8') as csv_f:
        for row in csv.DictReader(csv_f):
            record = {"model": model, "pk": row["id"]}
            del row["id"]

            if "price" in row:
                row['price'] = int(row["price"])
            if "is_published" in row:
                if row["is_published"] == "TRUE":
                    row["is_published"] = True
                else:
                    row["is_published"] = False
            if "author_id" in row:
                row['author_id'] = int(row['author_id'])
            if "category_id" in row:
                row['category_id'] = int(row['category_id'])
            if "lat" in row:
                row['lat'] = float(row['lat'])
            if "lng" in row:
                row['lng'] = float(row['lng'])
            if "age" in row:
                row['age'] = int(row['age'])
            if "location_id" in row:
                row['location_id'] = int(row['location_id'])

            record["fields"] = row
            result.append(record)

    with open(json_file, 'w', encoding='utf-8') as json_f:
        json_f.write(json.dumps(result, ensure_ascii=False))


convert_file('location.csv', 'locations.json', 'users.location')
convert_file('user.csv', 'users.json', 'users.user')
convert_file('category.csv', 'categories.json', 'ads.category')
convert_file('ad.csv', 'ads.json', 'ads.ad')
