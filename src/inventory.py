import numpy as np
from scipy.stats import norm

def calculate_inventory(pred, y):

    lead_time = 7
    service_level = 0.95

    mu_L = np.sum(pred[:lead_time])
    sigma = np.std(y - pred)

    z = norm.ppf(service_level)

    safety_stock = z * sigma
    reorder_point = mu_L + safety_stock

    return safety_stock, reorder_point