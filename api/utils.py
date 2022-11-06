from api import models, exceptions


def assign_product_to_order(order: models.Order, cart_products: list[models.CartProductRel]):
    for cart_product in cart_products.all():
        try:
            models.OrderedProduct.objects.create(
                order=order,
                product=cart_product.product,
                single_product_price=cart_product.product.price,
                quantity=cart_product.quantity
            )
        except:  # noqa:E722
            #  TODO delete order
            raise exceptions.BadRequest("Problems with creating order!")
