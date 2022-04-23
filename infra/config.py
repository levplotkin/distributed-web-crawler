from dynaconf import Dynaconf, Validator

settings = Dynaconf(envvar_prefix="DYNACONF", settings_files=['config/settings.toml', 'config/.secrets.toml'], )

settings.validators.register(Validator('LOG_LEVEL', must_exist=True), Validator('DB_HOST', must_exist=True),
                             Validator('QUEUE_HOST', 'QUEUE_PORT', 'QUEUE_USER', 'QUEUE_PASS', 'URL_QUEUE_NAME',
                                       must_exist=True),
                             Validator('DB_HOST', 'DB_PORT', must_exist=True), )

settings.validators.validate()
