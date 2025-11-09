SOURCES = {
    "maps": {
        "name": "Maps",
        "base_url": "https://www.mapexpress.ma",
        "urls":[
            "https://www.mapexpress.ma/ar/actualites/",
            "https://www.mapexpress.ma/ar/actualites/%d8%a7%d9%84%d8%a3%d9%86%d8%b4%d8%b7%d8%a9-%d8%a7%d9%84%d9%85%d9%84%d9%83%d9%8a%d8%a9/"
            ],
        "parser": "MapsParser",
        "frequency": "daily",
        "language": "ar",
        "section_selectors": {
            "article": "div.box-taxo",
            "title": "h2.the_featured_title",
            "date": "span.post-date",
            "summary": "div.col2.the_featured p",
        },
    },
}