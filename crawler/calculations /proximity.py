from crawler.over_pass_api import get_amenity_info

df = get_amenity_info("München", "bar|cafe|pub|restaurant")
print(df)
