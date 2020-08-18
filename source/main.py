from post_in import product_in
from post_out import product_out
from post_product import product
from post_report_products import report_products
from post_report_sales import report_sales


def main():
    product()
    product_in()
    product_out()
    report_products()
    report_sales()


if __name__ == '__main__':
    main()
