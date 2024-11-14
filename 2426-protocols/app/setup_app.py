from create_app import create_app


class Config:
    CONFIGURE_MIDDLEWARE = True
    CURRENCY_CODE = "GBP"
    CURRENCY_SYMBOL = "£"
    SERVICE_NAME = "app"
    REDIS_HOST = "localhost"
    REDIS_PORT = 6379


app = create_app(Config)
