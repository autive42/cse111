import math

def main():
    pass    

def compute_volume(r, h):
    V = math.pi * r ** 2 * h
    return V

def compute_surface_area(r, h):
    surface_area = 2 * math.pi * r * (r + h)
    return surface_area

def compute_storage_efficiency(V, surface_area):
    storage_efficiency = V / surface_area
    return storage_efficiency

'''
def test():
    r = 6.83
    h = 10.16
    V = compute_volume(r, h)
    surface_area = compute_surface_area(r, h)
    storage_efficiency = compute_storage_efficiency(V, surface_area)

    print(f'Volume: {V}')
    print(f'Surface Area: {surface_area}')
    print(f'Storage Efficiency: {storage_efficiency}')
test()
'''
