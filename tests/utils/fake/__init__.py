from faker import Faker
from faker.providers.python import Provider as PythonProvider

from tests.utils.fake.providers import TapeProvider

Faker.seed(123)

fake = Faker()
fake.add_provider(PythonProvider)

fake.add_provider(TapeProvider)
