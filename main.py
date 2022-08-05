from classes import StlObject, MeshObject
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    model = StlObject('xyzCalibration_cube.stl')
    mesh = MeshObject(model.stl2mesh())
    vol = mesh.get_volume()
    dims = mesh.get_dimensions()
    print(vol)
    print(dims)



