from api import models


def default_db():
    categories_data = [
        {
            "name": "Klawisze",
            "description": "Instrumenty klawiszowe o warstwach wysokiej jakości!"
        },
        {
            "name": "Gitary",
            "description": "Gitary o barwnych dźwiękach!"
        },
        {
            "name": "Akcesoria",
            "description": "Akcesoria do gitar i instrumentów klawiszowych! Po prostu cudne!"
        }
    ]

    category_keyboards = models.Category.objects.create(
        name=categories_data[0]["name"],
        description=categories_data[0]["description"],
    )
    category_guitars = models.Category.objects.create(
        name=categories_data[1]["name"],
        description=categories_data[1]["description"],
    )
    category_accessories = models.Category.objects.create(
        name=categories_data[2]["name"],
        description=categories_data[2]["description"],
    )

    manufacturer_yamaha = models.Manufacturer.objects.create(
        name="Yamaha",
    )
    manufacturer_fender = models.Manufacturer.objects.create(
        name="Fender",
    )
    manufacturer_casio = models.Manufacturer.objects.create(
        name="Casio",
    )

    products_data = [
        {
            "name": "Yamaha PSR-420",
            "description": "Ciastek uwielbiał do pianino!",
            "price": 2100.00,
            "color": "czarny",
            "category": category_keyboards,
            "manufacturer": manufacturer_yamaha
        },
        {
            "name": "Yamaha PSR E423",
            "description": "Klawisze dostrajane przez Lorda Farquaad'a!",
            "price": 660.50,
            "color": "czarny",
            "category": category_keyboards,
            "manufacturer": manufacturer_yamaha
        },
        {
            "name": "Gitara Fender 478 V02",
            "description": "Pudło rezonansowe wykonane z tego samego drewna co Pinokio!",
            "price": 1000.0,
            "color": "czarny",
            "category": category_guitars,
            "manufacturer": manufacturer_fender
        },
        {
            "name": "Pianino Casio 2233",
            "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum",
            "price": 1400.0,
            "color": "czarny",
            "category": category_keyboards,
            "manufacturer": manufacturer_casio
        },
        {
            "name": "Fortepian Yamaha XJ 14",
            "description": "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32.",
            "price": 7500.00,
            "color": "czarny",
            "category": category_keyboards,
            "manufacturer": manufacturer_yamaha
        },
        {
            "name": "Gitara elektryczna Fender 2000",
            "description": "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32.",
            "price": 1450.00,
            "color": "niebieski",
            "category": category_guitars,
            "manufacturer": manufacturer_fender
        },
        {
            "name": "Pedał do pianina (sustain)",
            "description": "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32.",
            "price": 99.99,
            "color": "brązowy",
            "category": category_accessories,
            "manufacturer": manufacturer_fender
        },
    ]

    for product_data in products_data:
        models.Product.objects.create(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            color=product_data["color"],
            category=product_data["category"],
            manufacturer=product_data["manufacturer"],
        )
