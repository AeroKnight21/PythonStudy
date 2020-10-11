import converters
import utils
from ecommerce import shipping
from converters import kg_to_lbs
from utils import find_max

kg_to_lbs(100)

print(converters.kg_to_lbs(70))

numbers = [10, 3, 6, 2]
maximum = find_max(numbers)
print(maximum)

shipping.calc_shipping()

